#!/usr/bin/env python
# Tune guitar
# (c) Jonne Mickelin 2008
# -*- coding: utf-8 -*-

import math
import pyaudio
import struct
import time

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

chunk = 4000               # samples per buffer, i.e. number of samples to fetch every time read is called
FORMAT = pyaudio.paInt16   # 16 bits per sample
struct_format = "1h"       # same as above
CHANNELS = 1               # mono
RATE = 22050               # Hz, samples per second
#RECORD_SECONDS = 5

def tone_freq(num):
    """Return the frequency for the tone number num, where 0 is the middle A (440 Hz)"""
    
    return 2**(num/12.0) * 440.0

def freq_tone(freq):
    return log(f/440.0)/log(2) * 12

def disect(data):
    """Return an array of Python values, by unpacking the given C-data 
    using the global variable struct_format as a format identifier."""

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

def t_filter(data, N=512):
    """Filter out noise in the time domain. Argument is the frequency of 
    the noise."""

    def hejsum(d, a, b):
        if a < 0:
            a = 0
        return sum(d[a:b])

    filtered = []

    if N == 0:
        return data

    #for i in xrange(len(data)): # Recursive definition. Broken.
    #    if i-f < 0: rem = 0
    #    else: rem = data[i-f]
    #    if i < 1: last = 0
    #    else: last = filtered[i-1]
    #    
    #    w = last - (rem + data[i])
    #    filtered.append(w)
    
    i = 0
    while i < len(data):
        a = hejsum(data, i-N, i)
        filtered.append(a/(N+1))
        i += 1

    # for i in range(len(data)):
    #         b = 0
    #         for j in range(i-f, i):
    #             try: 
    #                 b += data[j]
    #             except IndexError:
    #                 pass
    #         filtered.append(b/f)
        
    #     print "kuk"
    
    return filtered

#     filtered = [] 

#     if f == 0:
#         return data

#     # We use a recursice moving average filter
#     for i in xrange(len(data)):
#         #try:
#         if i-f < 0:
#             rem = 0
#         else:
#             rem = data[i-f]
            
#         if i is 0:
#             last = 0
#         else:
#             last = filtered[i-1]
            
#         filtered.append(last + float(data[i])/f - float(rem)/f)   # Last value, off with the value f steps ago, 
#                                                                    # on with a new value.
#         #except IndexError:
#         #    print i, f
#         #    filtered.append(data[i]/f)   # Now, this is probably wrong
#                                          # What we do is we set the filtered data to be 
#                                          # equal to the unfiltered data for the first f
#                                          # samples.
#     return filtered
    


def freq(data):
    """Deprecated. Convert data to python objects, then perform 
    the DFT. It also returned the index of the frequency with the 
    highest amplitude at some point."""
    disected = disect(data)
    freqs = dft.DFT(disected)
    #return maxindex(freqs)
    return freqs

def average(l1, l2):
    """Return a list that is the average of the two lists l1 
    and l2 elementwise."""
    if len(l1) != len(l2):
        raise ValueError, "List sizes not equal!"

    r = [(a + b)/2 for a, b in zip(l1, l2)]
    
    return r

def multiply(data, fun):
    for i in range(len(data)):
        data[i] *= fun(i)
    return data

def hamming(n):
    return 0.53836 - 0.46164*math.cos(2*math.pi*n/(chunk-1))

def highpass(i, n):
    if i < n:
        return 0
    else: 
        return 1

def bandpass(i, a, b):
    if a <= i <= b:
        return 1
    else:
        return 0

def make_highpass(n):
    return lambda n: highpass(n, n)

def make_bandpass(a, b):
    return lambda n: bandpass(n, a, b)

def main():
    for num, name in enumerate(notes):
        print "%s\t: %.2f Hz" % (name, tone_freq(num-len(notes)+3))
 
    # Open the interface to the Mic
    p = pyaudio.PyAudio()
    instream = p.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      input=True,             # It is, indeed, an input stream
                      frames_per_buffer=chunk)

    # Make matplotlib interactive. It says "interactive", at least, but I don't see
    # any buttons. This makes a window appear without blocking the application
    # (which pylab.show() would have done).
    pylab.ion()

    # Read data one time first
    data = instream.read(chunk)
    d = disect(data)
    #d = t_filter(d)
    f1 = dft.DFT(d)

    # Set up the two subplots and make their scales fixed
    ax1 = pylab.subplot(211)
    ax1.set_autoscale_on(False)
    ax1.set_xlim(xmin=-10, xmax=len(d)+10)  # We pad the graph on the sides so we can
                                            # see better
    ax1.set_ylim((-30000, 30000))             # Starts out with just noise, hopefully. 
                                            # This should be set manually to match the 
                                            # expectedmaximum amplitude, but I'm not 
                                            # sure what level that is.
                                            #The noise seems to be around 70000

    ax2 = pylab.subplot(212)
    ax2.set_autoscale_on(False)
    ax2.set_xlim(xmin=-100, xmax=RATE+100)
    ax2.set_ylim((0, max(f1)/100))
    ax2.set_xlabel("Hz")

    # Plot the preliminary data, so that we may use set_ydata for animation later
    n = range(len(d))
    n2 = pylab.arange(0, RATE, float(RATE)/chunk)
    line1, = ax1.plot(n, d) #http://www.scipy.org/Cookbook/Matplotlib/Animations
    line2, = ax2.plot(n2, f1) 

    while True:
        try:
            data = instream.read(chunk) # Read data from the mic
            d = disect(data)            # Convert this data to values that python can understand
            d = t_filter(d, 52)        # Filter data in the time domain to remove noise

            #f2 = dft.DFT(d)             # Perform the DFT on the filtered data
            f2 = pylab.fft(d)
            #f2 = multiply(f2, make_bandpass(20.0/RATE, 20000.0/RATE))

            #f2 = average(f2, f1)        # Okay, I don't know if this is an established 
                                        # method, but it's an attempt att reducing fluctuations
                                        # by averaging with the last spectrum. Pretty slow, I guess (O(n)).
            #f1 = f2

            line1.set_ydata(d)          # Update the plots
            line2.set_ydata(f2)
            pylab.draw()                # Draw it, and then repeat

        except KeyboardInterrupt:
            print "C-c was pressed. Exiting."
            break

if __name__ == "__main__":
    main()

