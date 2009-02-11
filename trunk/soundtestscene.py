####################
# Standard library #
####################
from __future__ import with_statement

#import threading
try:
    import multiprocessing
except ImportError, err:
    try:
        import pyprocessing as multiprocessing
    except ImportError:
        message = "You appear to be using Python 2.5 or older,\
and do not appear to have pyprocessing installed. Either update to\
Python 2.6 or install pyprocessing from http://pyprocessing.berlios.de/"
        error.critical(message)
        error.bail_out(err)

import time
import struct

####################
# Required modules #
####################
import pyglet
import pyaudio

import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg

import pylab

####################
#   Game modules   #
####################
import scene
import options
import fft

class SoundBarfingProcess(multiprocessing.Process):
    def __init__(self, 
                 quit_pipe,
                 format=options.INPUT_FORMAT, 
                 channels=options.INPUT_CHANNELS, 
                 rate=options.INPUT_RATE, 
                 frames_per_buffer=options.INPUT_CHUNK_SIZE):

        multiprocessing.Process.__init__(self)
        
        self.name = "Sound test"

        # We put everything that has to do with pyaudio in it's
        # own thread to avoid undefined behaviour.
        p = pyaudio.PyAudio()
        self.instream = p.open(format=format,
                               channels=channels,
                               rate=rate,
                               input=True,      # It is, indeed, an input stream
                               frames_per_buffer=frames_per_buffer)
        self.quit = False
        self.quit_pipe = quit_pipe

        self.chunk_size = frames_per_buffer

    def disect(self, data):
        """Return an array of Python values, by unpacking the given C-data 
        using the global variable struct_format as a format identifier."""
        
        size = struct.calcsize(options.STRUCT_INPUT_FORMAT)
        datas = []
        for i in xrange(self.chunk_size):
            datas.append(struct.unpack(options.STRUCT_INPUT_FORMAT, data[i:i+size])[0])
        return datas
 
    def run(self):
        while not self.quit:
            if self.quit_pipe.poll():
                self.quit = self.quit_pipe.recv()
                print "Recieved quit instruction. Value:", self.quit
            else:
                raw_data = self.instream.read(self.chunk_size)
                disected = self.disect(raw_data)
                freqs = fft.FFT(disected)
                print freqs

class SoundTestScene(scene.TestScene):
    
    """Get sound input and display the time and frequency graphs
    in real-time.
    """
    
    def __init__(self, 
                 format=options.INPUT_FORMAT, 
                 channels=options.INPUT_CHANNELS, 
                 rate=options.INPUT_RATE, 
                 frames_per_buffer=options.INPUT_CHUNK_SIZE):

        # Use this to communicate quit events
        self.quit_pipe, child_quit_pipe = multiprocessing.Pipe()

        self.soundthread = SoundBarfingProcess(child_quit_pipe, 
                                               format, channels, 
                                               rate, frames_per_buffer)

        self.name = "Sound test"
        
        self.soundthread.start()

    def end(self):
         self.quit_pipe.send(True)
         self.soundthread.join()

    def debug_draw(self, window):
        window.clear()

    def do_logic(self, dt):
        pass
