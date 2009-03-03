#!/usr/bin/env python
# Tune guitar
# (c) Jonne Mickelin 2008-2009
# -*- coding: utf-8 -*-

import wonderful
import pylab

SAMPLE_RATE = 44100
N = 8192
MAG_THRESHOLD = 100

def main():
    # Open the interface to the Mic
    wonderful.init(SAMPLE_RATE, N)

    # Make matplotlib interactive. It says "interactive", at least, but I don't see
    # any buttons. This makes a window appear without blocking the application
    # (which pylab.show() would have done).
    pylab.ion()

    # Set up the two subplots and make their scales fixed
    ax = pylab.subplot(111)
    ax.set_autoscale_on(False)
    ax.set_xlim(xmin=-10, xmax=SAMPLE_RATE+10)   # We pad the graph on the sides so we can
                                       # see better
    ax.set_ylim((0, 10*MAG_THRESHOLD))
    ax.set_xlabel("Hz")

    # Plot some bogus data, so that we may use set_ydata for animation later
    d = [0]*N
    n = pylab.arange(0, SAMPLE_RATE, step=float(SAMPLE_RATE)/N)
    line, = ax.plot(n, d) #http://www.scipy.org/Cookbook/Matplotlib/Animations

    while True:
        try:
            d = wonderful.munch()
            if d is not None:
                line.set_ydata(d)          # Update the plots
                pylab.draw()                # Draw it, and then repeat
            
        except KeyboardInterrupt:
            print "C-c was pressed. Exiting."
            break

    wonderful.terminate()

if __name__ == "__main__":
    main()

