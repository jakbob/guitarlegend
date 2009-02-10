####################
# Standard library #
####################
from __future__ import with_statement

#import threading
import multiprocessing
import time

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

plot_lock = multiprocessing.RLock()

# def begin_plotting(scene):
#     setup_plot(scene)
#     update_plot(scene)

# def setup_plot(thescene):
#     pylab.ion()  # Makes pylab interactive. Plotting does not blockthe application.
    
#     # The figure lets us define the physical size of the plot, so that we can create a texture from it
#     thescene.graph_dpi = 50
#     thescene.graph_width = 4
#     thescene.graph_height = 4
    
#     thescene.fig = pylab.figure(figsize=[thescene.graph_width, thescene.graph_height], # Inches
#                                 dpi=thescene.graph_dpi,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
#                                 )
    
#     # Set up the axes for plotting
#     thescene.time_plane = pylab.subplot(211)
#     thescene.freq_plane = pylab.subplot(212)
    
#     thescene.fig.add_axes(thescene.time_plane)
#     thescene.fig.add_axes(thescene.freq_plane)
    
#     # Do not change the scale to match the graph
#     thescene.time_plane.set_autoscale_on(False) 
#     thescene.freq_plane.set_autoscale_on(False)
    
#     # Set the scales of the plot. TODO They use magic numbers. Fix this.
#     thescene.time_plane.set_xlim(xmin=-10, xmax=options.INPUT_CHUNK_SIZE + 10)
#     thescene.time_plane.set_ylim((0, 20000))
    
#     thescene.freq_plane.set_xlim(xmin=-100, xmax=options.INPUT_CHUNK_SIZE-10000)
#     thescene.freq_plane.set_ylim((0, 100000))
    
#     time_x = range(options.INPUT_CHUNK_SIZE)
#     freq_x = pylab.arange(0, options.INPUT_RATE, step=float(options.INPUT_RATE)/options.INPUT_CHUNK_SIZE)
    
#     # Set up initial data, so that we get instances of the plots' data,
#     # that we can edit
#     thescene.time_data, = thescene.time_plane.plot(time_x, [0]*options.INPUT_CHUNK_SIZE)
#     thescene.freq_data, = thescene.freq_plane.plot(freq_x, [0]*options.INPUT_CHUNK_SIZE)
    
#     thescene.pyglet_plot = pyglet.image.create(thescene.graph_dpi * thescene.graph_width, 
#                                                thescene.graph_dpi * thescene.graph_width)

# def update_plot(scene):
#         while not scene.quit:
#             canvas = agg.FigureCanvasAgg(scene.fig)
#             canvas.draw()
#             renderer = canvas.get_renderer()
#             scene.raw_data = renderer.tostring_argb() # Why isn't rgb and pitch=-3*400 below working?

#             raw_pyglet_image = scene.pyglet_plot.get_image_data()

#             print "Setting"
#             with plot_lock:
#                 raw_pyglet_image.set_data("ARGB", -4*(scene.graph_width*scene.graph_dpi),
#                                           scene.raw_data)
        
#             time.sleep(0.1)


class SoundTestScene(scene.TestScene):
    
    """Get sound input and display the time and frequency graphs
    in real-time.
    """
    
    def __init__(self, 
                 format=options.INPUT_FORMAT, 
                 channels=options.INPUT_CHANNELS, 
                 rate=options.INPUT_RATE, 
                 frames_per_buffer=options.INPUT_CHUNK_SIZE):
        
        self.name = "Sound test"

        p = pyaudio.PyAudio()
        self.instream = p.open(format=format,
                               channels=channels,
                               rate=rate,
                               input=True,             # It is, indeed, an input stream
                               frames_per_buffer=frames_per_buffer)
        #self._setup_plot()

        #def _setup_plot(self):
        #setup_plot(self)
        #self.update_plot_thread = threading.Thread(target=self.update_plot)
        #self.update_plot_thread = multiprocessing.Process(target=begin_plotting, args=(self,))
        self.quit = False
        #self.update_plot_thread.start()
        #self.update_plot()

        #pyglet.clock.schedule_interval(self.update_plot, 1) # Still too slow...

    def __del__(self):
        #pyglet.clock.unschedule(self.update_plot)
        self.quit = True
        self.update_plot_thread.join()

    def debug_draw(self, window):
        #ax = fig.gca()
        #ax.plot(y)
        # Update the data
        window.clear()
        # Platt
        #with self.plot_lock:
        #with plot_lock:
        #self.pyglet_plot.blit(0,0)

    def do_logic(self, dt):
        pass
