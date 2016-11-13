"""Sample that streams audio to the Google Cloud Speech API via GRPC."""

from __future__ import division

import contextlib
import functools
import re
import signal
import sys

from datetime import datetime
from google.cloud import credentials
from google.cloud.speech.v1beta1 import cloud_speech_pb2 as cloud_speech
from google.rpc import code_pb2
from grpc.beta import implementations
from grpc.framework.interfaces.face import face
import pyaudio
from six.moves import queue

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

DEADLINE_SECS = 60 * 3 + 5
SPEECH_SCOPE = 'https://www.googleapis.com/auth/cloud-platform'

TEXT = []
BREAK = False

def make_channel(host, port):
    """Creates an SSL channel with auth credentials from the environment."""
    ssl_channel = implementations.ssl_channel_credentials(None, None, None)

    creds = credentials.get_credentials().create_scoped([SPEECH_SCOPE])
    auth_header = (
        'Authorization',
        'Bearer ' + creds.get_access_token().access_token)
    auth_plugin = implementations.metadata_call_credentials(
        lambda _, cb: cb([auth_header], None),
        name='application_default_credentials')

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
    """ Continously read audio and add to the buffer.
        Start recording if the audio stream is not silent, stop recording
        if the audio stream is silent for
    """
    #print("fill buffer started")
    buff.put(in_data)
    return None, pyaudio.paContinue

# [START audio_stream]
@contextlib.contextmanager
def record_audio(rate, chunk):
    """Opens a recording stream in a context manager."""
    # Create a thread-safe buffer of audio data
    buff = queue.Queue()

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
    # Signal the _audio_data_generator to finish
    buff.put(None)
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
    recognition_config = cloud_speech.RecognitionConfig(
        encoding='LINEAR16',  # raw 16-bit signed LE samples
        sample_rate=rate,  # the rate in hertz
        # See http://g.co/cloud/speech/docs/languages
        # for a list of supported languages.
        language_code='en-US',  # a BCP-47 language tag
    )
    streaming_config = cloud_speech.StreamingRecognitionConfig(
        interim_results=interim_results,
        config=recognition_config,
    )

    yield cloud_speech.StreamingRecognizeRequest(
        streaming_config=streaming_config)

    for data in data_stream:
        # Subsequent requests can all just have the content
        yield cloud_speech.StreamingRecognizeRequest(audio_content=data)


def listen_print_loop(recognize_stream, sentence):
    """Iterates through server responses and prints them.

    The recognize_stream passed is a generator that will block until a response
    is provided by the server. When the transcription response comes, print it.

    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    t1 = datetime.now()
    word_count = 0
    global TEXT

    signal.signal(signal.SIGALRM, returnText)
    signal.alarm(6)

    for resp in recognize_stream:
        print("Inside record")

        if resp.error.code != code_pb2.OK:
            raise RuntimeError('Server error: ' + resp.error.message)

        if not resp.results:
            continue

        # Display the top transcription
        result = resp.results[0]
        sentence.append(result.alternatives[0].transcript)
        TEXT = sentence
        word_count = word_count + 1

def getSpeechText():
    with cloud_speech.beta_create_Speech_stub(
            make_channel('speech.googleapis.com', 443)) as service:
        with record_audio(RATE, CHUNK) as buffered_audio_data:
            requests = request_stream(buffered_audio_data, RATE)
            recognize_stream = service.StreamingRecognize(
                requests, DEADLINE_SECS)

            # Exit things cleanly on interrupt
            signal.signal(signal.SIGINT, lambda *_: recognize_stream.cancel())

            # Now, put the transcription responses to use.
            try:
                sentence = []
                listen_print_loop(recognize_stream, sentence)
                recognize_stream.cancel()
            except Exception:
                return ''.join(TEXT)

def returnText(signum, stack):
    raise Exception

if __name__ == '__main__':
    print(getSpeechText())
