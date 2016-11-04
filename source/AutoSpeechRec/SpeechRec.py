"""Sample that streams audio to the Google Cloud Speech API via GRPC."""

from __future__ import division

import contextlib
import re
import signal
import sys
import threading

from google.cloud import credentials
from google.cloud.speech.v1beta1 import cloud_speech_pb2 as cloud_speech
from google.rpc import code_pb2
from grpc.beta import implementations
from grpc.framework.interfaces.face import face
import pyaudio
from six.moves import queue

print("This is working!")
