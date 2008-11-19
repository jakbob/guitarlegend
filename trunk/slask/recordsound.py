#!/usr/bin/env python
# Copied from the example on this page: http://people.csail.mit.edu/hubert/pyaudio/#docs
# Requires PyAudio (http://people.csail.mit.edu/hubert/pyaudio/)

# I made this to clear up some terminology and test the library, thus the redundant comments.

# Jonne Mickelin 19 Nov 2008

import wave
import pyaudio

chunk = 1024 # samples per buffer, i.e. number of samples to fetch every time read is called
FORMAT = pyaudio.paInt16 # 16 bits per sample
CHANNELS = 1 # mono
RATE = 44100 # Hz, samples per second
RECORD_SECONDS = 5

WAVE_OUTPUT_FILENAME= "output.wav"

p = pyaudio.PyAudio()

instream = p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True, # It is, indeed, an input stream
                  frames_per_buffer=chunk)

print "* recording"

frames = []
for i in range(0, RATE / chunk * RECORD_SECONDS): # (sample/s)/(sample/call)*s = calls to read
    # Total number of samples = chunk*RATE/chunk * RECORD_SECONDS = 215*1024
    data = instream.read(chunk)
    frames.append(data)

print "* done recording"

instream.close()

wavdata = "".join(frames) # frames is currently a list of 16-bit values represented by strings
wf = wave.open(WAVE_OUTPUT_FILENAME, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(wavdata)
wf.close()
