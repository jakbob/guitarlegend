# -*- coding: utf-8 -*-
#
# scene.py
#
# Defines the Scene class, which provides an isolated 
# environment for different scenes of the game. The 
# environment provides methods for handling input, 
# logic and rendering of the scene.
#
# (c) Jonne Mickelin 2009

######################
# Required libraries #
######################
import pyglet
from pyglet.gl import *
from pyglet.graphics import vertex_list

import pyaudio
import pylab # strange bug! from pylab import plot DOES NOT WORK. X yells and screams and hates.

######################
#    Game modules    #
######################
import error
import options
from options import kb
#from manager import game_manager

class Scene(object):
    """Defines an isolated environment for a specific scene, 
    providing methods for handling of input, logic and rendering
    of the scene.

    To define a new scene, derive this class and overload the
    methods debug_draw, game_draw and logic. You may also create other
    drawing functions, depending on what the game's windows expect
    (see manager.py for details on defining windows). The drawing 
    functions _should only_ define objects that they themselves 
    are supposed to use for drawing, and _may not_ change the
    state of the scene. The state is updated using the do_logic()
    method, which is run at a specific interval by the scene
    manager. 

    To add a scene, initialize it, and pass it to the (singleton) 
    scene manager, using scene_manager.push(scene). To end a scene,
    call the scene's end() method, which takes care of removing it
    from the scene manager.
    """

    def __init__(self):
        self.name = "Abstract scene"

    @staticmethod
    def debug_draw(scene, window):
        """Draws the debug view of the scene."""
        glClear(GL_COLOR_BUFFER_BIT)       # We are not bound to a window, all the functions and methods are
                                           # merely abstractions for lower level GL calls. If I understand
                                           # correctly, the window just swaps the GL context, or whatever the
                                           # lingo is. Anyways. No window. No clear(). If, however, a window
                                           # is passed using a lambda, we may use it.

    @staticmethod
    def game_draw(scene, window):
        """Draws the game view of the scene."""
        glClear(GL_COLOR_BUFFER_BIT)

    def do_logic(self, dt):
        """Handles the scene's logic."""
        pass

    def end(self):
        topscene = scene_manager.pop()
        if topscene != self:
            scene_manager.push(topscene)
        else:
            del topscene

    def on_key_press(self, window, symbol, modifiers):
        
        """Handles keyboard input. The keys are defined in options.py and are
        sorted according to namespaces. See that file for further information.

        Arguments:
        window -- the window that recieved the keypress
        symbol -- the key that was pressed
        modifiers -- the modifiers (ctrl, alt, etc.) that were down 
                     when the keypress occurred
        """
        
        if (symbol & kb.test.exit) == symbol:
            window.close()

class TestScene(Scene):
    """Defines an isolated environment for a specific scene, 
    providing methods for handling of input, logic and rendering
    of the scene."""
    def __init__(self):
        self.name = "Test scene"
        self.time = "0"

    @staticmethod
    def debug_draw(scene, window):
        """Draws the debug view of the scene."""
        glClear(GL_COLOR_BUFFER_BIT)       # We are not bound to a window, all the functions and methods are
                                           # merely abstractions for lower level GL calls. If I understand
                                           # correctly, the window just swaps the GL context, or whatever the
                                           # lingo is. Anyways. No window. No clear(). If, however, a window
                                           # is passed using a lambda, we may use it.
    
        label = pyglet.text.Label("Debug " + scene.name, 
                                  x=window.width//2, y=window.height//2, 
                                  font_name="Times New Roman", font_size=46, 
                                  anchor_x="center", anchor_y="center")
    
        label2 = pyglet.text.Label("dt = " + scene.time,
                                   x=100, y=window.height//2 - 100, 
                                   anchor_x="left", anchor_y="top",
                                   font_name="Times New Roman", font_size=36)
        label.draw()
        label2.draw()

    @staticmethod
    def game_draw(scene, window):
        """Draws the game view of the scene."""
        glClear(GL_COLOR_BUFFER_BIT)

        label = pyglet.text.Label("Game " + scene.name, 
                                  x=window.width//2, y=window.height//2, 
                                  font_name="Times New Roman", font_size=46, 
                                  anchor_x="center", anchor_y="center")

        label.draw()

    def do_logic(self, dt):

        """Handles the scene's logic."""
        
        self.time = str(dt)

    def on_key_press(self, window, symbol, modifiers):
        
        """Handles keyboard input. The keys are defined in options.py and are
        sorted according to namespaces. See that file for further information.

        Arguments:
        window -- the window that recieved the keypress
        symbol -- the key that was pressed
        modifiers -- the modifiers (ctrl, alt, etc.) that were down 
                     when the keypress occurred

        """
        
        if (symbol & kb.test.exit) == symbol:
            window.close()
        elif (symbol & kb.test.soundtest) == symbol:
            game_manager.push(SoundTestScene())
        else:
            print "Recieved keypress:", symbol, "\t\tModifiers:", modifiers

# class SoundTestScene(Scene):
    
#     """Get sound input and display the time and frequency graphs
#     in real-time.
#     """

#     def __init__(self, 
#                  format=options.INPUT_FORMAT, 
#                  channels=options.INPUT_CHANNELS, 
#                  rate=options.INPUT_RATE, 
#                  frames_per_buffer=options.INPUT_CHUNK_SIZE):

#         p = pyaudio.PyAudio()
#         self.instream = p.open(format=format,
#                                channels=channels,
#                                rate=rate,
#                                input=True,             # It is, indeed, an input stream
#                                frames_per_buffer=frames_per_buffer)
#         pylab.ion()  # Makes pylab interactive. Plotting does not blockthe application.
        
#         # Set up the axes for plotting
#         self.time_plane = pylab.subplot(211)
#         self.freq_plane = pylab.subplot(212)

#         self.time_plane.set_autoscale_on(False) # Do not change the scale to match the graph
#         self.freq_plane.set_autoscale_on(False)
        
#         # Set the scales of the plot. TODO They use magic numbers. Fix this.
#         self.time_plane.set_xlim(xmin=-10, xmax=options.INPUT_CHUNK_SIZE + 10)
#         self.time_plane.set_ylim((0, 20000))

#         self.freq_plane.set_xlim(xmin=-100, xmax=options.INPUT_CHUNK_SIZE-10000)
#         self.freq_plane.set_ylim((0, 100000))

#         time_x = range(options.INPUT_CHUNK_SIZE)
#         freq_x = pylab.arange(0, options.INPUT_RATE, step=float(options.INPUT_RATE)/options.INPUT_CHUNK_SIZE)

#         # Set up initial data, so that we get instances of the plots' data,
#         # that we can edit
#         self.time_data, = self.time_plane.plot(time_x, [0]*options.INPUT_CHUNK_SIZE)
#         self.freq_data, = self.freq_plane.plot(freq_x, [0]*options.INPUT_CHUNK_SIZE)

class ErrorScene(Scene):
    """Defines an isolated environment for a specific scene, 
    providing methods for handling of input, logic and rendering
    of the scene."""
    def __init__(self):
        self.name = "Error scene"

    @staticmethod
    def debug_draw(scene, window):
        """Draws the debug view of the scene."""
        glClearColor(174/255.0, 23/255.0, 23/255.0, 0)
        glClear(GL_COLOR_BUFFER_BIT)       # We are not bound to a window, all the functions and methods are
                                           # merely abstractions for lower level GL calls. If I understand
                                           # correctly, the window just swaps the GL context, or whatever the
                                           # lingo is. Anyways. No window. No clear(). If, however, a window
                                           # is passed using a lambda, we may use it.

        label = pyglet.text.Label("Error", 
                                  x=window.width//2, y=window.height//2, 
                                  font_name="Times New Roman", font_size=46, 
                                  anchor_x="center", anchor_y="center")

        label.draw()

    game_draw = debug_draw
    
    def do_logic(self, dt):
        """Handles the scene's logic."""
        pass
