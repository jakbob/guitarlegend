#!/usr/bin/env python
# Tune guitar
# -*- coding: utf-8 -*-

import math
import pyaudio
import struct
import time
#import matplotlib.pyplot as plt
import pylab

import fft.pydft as dft

notes = [ u"C",
          u"C\u266f",
          u"D", 
          u"D\u266f",
          u"E", 
          u"F",
          u"F\u266f",
          u"G", 
          u"G\u266f",
          u"A", 
          u"G\u266f",
          u"H", 
          u"c", 
          u"c\u266f",
          u"d", 
          u"d\u266f",
          u"e", 
          u"f", 
          u"f\u266f",
          u"g", 
          u"g\u266f",
          u"a", 
          u"a\u266f",
          u"h" ]

chunk = 1024 # samples per buffer, i.e. number of samples to fetch every time read is called
FORMAT = pyaudio.paInt16 # 16 bits per sample
struct_format = "1h" # same as above
CHANNELS = 1 # mono
RATE = 44100 # Hz, samples per second
#RECORD_SECONDS = 5

def tone_freq(num):
    """Return the frequency for the tone number num, where 0 is the middle A (440 Hz)"""
    
    return 2**(num/12.0) * 440.0

# def dft(vals):
#     N = len(vals)
#     freqs = []
#     for i in xrange(N):
#         R = 0
#         I = 0
#         for j in xrange(N):
#             R += vals[j]*math.cos(-2*math.pi*i*j/N)
#             I -= vals[j]*math.sin(-2*math.pi*i*j/N)
#         freqs.append((R, I))

#     return freqs

def disect(data):
    size = struct.calcsize(struct_format)
    datas = []
    for i in xrange(chunk):
        datas.append(struct.unpack(struct_format, data[i:i+size])[0])
    return datas

def maxindex(vals):
    i = 0
    max = 0
    for num, val in enumerate(vals):
        if val > max:
            max = val
            i = num

    return i

def f_filter(data):
    #data[512] = 0
    #data[0] = 0
    return data

def freq(data):
    disected = disect(data)
    freqs = dft.DFT(disected)
    #return maxindex(freqs)
    return freqs

def main():
    for num, name in enumerate(notes):
        print "%s\t: %.2f Hz" % (name, tone_freq(num-len(notes)+3))
 
    p = pyaudio.PyAudio()
    
    instream = p.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      input=True, # It is, indeed, an input stream
                      frames_per_buffer=chunk)

    
    #data = instream.read(chunk*5) # Read some data and throw it away. Not sure this is necessary
    data = instream.read(chunk)
    f = freq(data)

    pylab.ion()
    n = range(len(f))
    pylab.subplot(211)
    line, = pylab.plot(n, disect(data)) #http://www.scipy.org/Cookbook/Matplotlib/Animations
    pylab.subplot(212)
    line2, = pylab.plot(n, f_filter(f)) 

    while True:
        tstart = time.time()
        data = instream.read(chunk)
        d = disect(data)
        f = dft.DFT(d)
        line.set_ydata(d)
        line2.set_ydata(f_filter(f))
        pylab.draw()
        #time.sleep(0.1)

if __name__ == "__main__":
    main()

