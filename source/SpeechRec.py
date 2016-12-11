"""Sample that streams audio to the Google Cloud Speech API via GRPC."""
# to do list:-
# 1. make init function and move service and cloud context object there.

from __future__ import division

import contextlib
import functools
import re
import signal
import sys

from google.cloud import credentials
from google.cloud.speech.v1beta1 import cloud_speech_pb2 as cloud_speech
from google.rpc import code_pb2
from grpc.beta import implementations
from oauth2client.client import GoogleCredentials
import pyaudio
from six.moves import queue

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms
DEADLINE_SECS = 60 * 3 + 5

# google speech recongition parameters.
ALTERNATIVES = 10

def make_channel(host, port):
    """Creates an SSL channel with auth credentials from the environment."""
    # In order to make an https call, use an ssl channel with defaults
    ssl_channel = implementations.ssl_channel_credentials(None, None, None)

    creds = GoogleCredentials.get_application_default()

    auth_header = (
        'Authorization',
        'Bearer ' + creds.get_access_token().access_token)

    auth_plugin = implementations.metadata_call_credentials(
        lambda _, cb: cb([auth_header], None),
        name='google-speech-creds')

    # compose the two together for both ssl and google auth
    composite_channel = implementations.composite_channel_credentials(
        ssl_channel, auth_plugin)

    return implementations.secure_channel(host, port, composite_channel)


def _audio_data_generator(buff):
    """A generator that yields all available data in the given buffer.

    Args:
        buff - a Queue object, where each element is a chunk of data.
    Yields:
        A chunk of data that is the aggregate of all chunks of data in `buff`.
        The function will block until at least one data chunk is available.
    """
    stop = False
    while not stop:
        # Use a blocking get() to ensure there's at least one chunk of data.
        data = [buff.get()]

        # Now consume whatever other data's still buffered.
        while True:
            try:
                data.append(buff.get(block=False))
            except queue.Empty:
                break

        # `None` in the buffer signals that the audio stream is closed. Yield
        # the final bit of the buffer and exit the loop.
        if None in data:
            stop = True
            data.remove(None)

        yield b''.join(data)


def _fill_buffer(buff, in_data, frame_count, time_info, status_flags):
    """Continuously collect data from the audio stream, into the buffer."""
    buff.put(in_data)
    return None, pyaudio.paContinue


# [START audio_stream]
@contextlib.contextmanager
def record_audio(rate, chunk, buff):
    """Opens a recording stream in a context manager."""
    audio_interface = pyaudio.PyAudio()
    audio_stream = audio_interface.open(
        format=pyaudio.paInt16,
        channels=1, rate=rate,
        input=True, frames_per_buffer=chunk,
        stream_callback=functools.partial(_fill_buffer, buff),
    )

    yield _audio_data_generator(buff)

    audio_stream.stop_stream()
    audio_stream.close()

    audio_interface.terminate()
# [END audio_stream]


def request_stream(data_stream, rate, interim_results=False):
    """Yields `StreamingRecognizeRequest`s constructed from a recording audio
    stream.

    Args:
        data_stream: A generator that yields raw audio data to send.
        rate: The sampling rate in hertz.
        interim_results: Whether to return intermediate results, before the
            transcription is finalized.
    """
    # first send the config request.
    # adding context hints.
    phrases = {"pick", "up", "key", "sword", "hammer", "lamp", "lantern", "light",
                "get the key", "take the key", "drop the sword", "kill the dragon"}
    context = cloud_speech.SpeechContext()
    print("type of context phrases is ", context.phrases)

    for item in phrases:
        context.phrases.append(item)
    print("type of context phrases is ", context.phrases)

    recognition_config = cloud_speech.RecognitionConfig(
        encoding='LINEAR16',  # raw 16-bit signed LE samples
        sample_rate=rate,  # the rate in hertz
        language_code='en-US',  # a BCP-47 language tag
        max_alternatives=ALTERNATIVES,
        speech_context=context,
    )
    streaming_config = cloud_speech.StreamingRecognitionConfig(
        interim_results=interim_results,
        single_utterance=True,
        config=recognition_config,
    )

    yield cloud_speech.StreamingRecognizeRequest(
        streaming_config=streaming_config)

    for data in data_stream:
        yield cloud_speech.StreamingRecognizeRequest(audio_content=data)


def process_transcript(recognize_stream, buff):
    """Iterates through server responses and prints them.

    The recognize_stream passed is a generator that will block until a response
    is provided by the server. When the transcription response comes, print it.
    """
    end_of_utterance = False

    for resp in recognize_stream:
        if resp.error.code != code_pb2.OK:
            raise RuntimeError('Server error: ' + resp.error.message)

        if resp.endpointer_type == resp.START_OF_SPEECH:
            print("start of speech recording")

        if not resp.results:
            if resp.endpointer_type == resp.END_OF_UTTERANCE:
                end_of_utterance = True
            continue

        # Display the top transcription
        print("before result")

        result = resp.results[0]
        i = 0
        for res in result.alternatives:
            print(i,". text is", res.transcript, end=",")
            print("confidence is", res.confidence)
            i = i + 1

        if end_of_utterance:
            buff.put(None)
            break;

def main():
    service = cloud_speech.beta_create_Speech_stub(
                make_channel('speech.googleapis.com', 443))
    buff = queue.Queue()
    with record_audio(RATE, CHUNK, buff) as buffered_audio_data:
        requests = request_stream(buffered_audio_data, RATE)
        recognize_stream = service.StreamingRecognize(
            requests, DEADLINE_SECS)

        # Exit things cleanly on interrupt
        signal.signal(signal.SIGINT, lambda *_: recognize_stream.cancel())

        # Now, put the transcription responses to use.
        try:
            process_transcript(recognize_stream, buff)
            recognize_stream.cancel()
        except Exception as err:
            recognize_stream.cancel()
            print("Error occured!".format(err))
            pass

if __name__ == '__main__':
    main()
