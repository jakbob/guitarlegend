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

from __future__ import with_statement

import error
import options

import time

######################
# Required libraries #
######################
import pyglet
from pyglet.gl import *
from pyglet.graphics import vertex_list

import pyaudio

import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg

import pylab


######################
#    Game modules    #
######################
from options import kb

import tab
import graphics

from manager import game_manager

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

    def debug_draw(self, window):
        """Draws the debug view of the scene."""
        glClear(GL_COLOR_BUFFER_BIT)       # We are not bound to a window, all the functions and methods are
                                           # merely abstractions for lower level GL calls. If I understand
                                           # correctly, the window just swaps the GL context, or whatever the
                                           # lingo is. Anyways. No window. No clear(). If, however, a window
                                           # is passed using a lambda, we may use it.

    def game_draw(self, window):
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
        pyglet.window.Window.on_key_press(window, symbol, modifiers)

class TestScene(Scene):
    def __init__(self):
        self.name = "Test scene"
        self.time = "0"

    def debug_draw(self, window):
        """Draws the debug view of the scene."""
        glClear(GL_COLOR_BUFFER_BIT)       # We are not bound to a window, all the functions and methods are
                                           # merely abstractions for lower level GL calls. If I understand
                                           # correctly, the window just swaps the GL context, or whatever the
                                           # lingo is. Anyways. No window. No clear(). If, however, a window
                                           # is passed using a lambda, we may use it.
    
        label = pyglet.text.Label("Debug " + self.name, 
                                  x=window.width//2, y=window.height//2, 
                                  font_name="Times New Roman", font_size=46, 
                                  anchor_x="center", anchor_y="center")
    
        label.draw()

    def game_draw(self, window):
        """Draws the game view of the scene."""
        glClear(GL_COLOR_BUFFER_BIT)

        helptext = "<font face='Times New Roman' size='46'>Controls:<br><br><i>s</i>: SoundTestScene<br><i>t</i>: TestinNotes<br><i>m</i>: MainTestScene<br><i>u</i>: Pop scene</font>"
        #helptext = "Hej"
        #document = pyglet.text.decode_html(helptext)
        #label = pyglet.text.HTMLLabel(helptext)#,
        label = pyglet.text.HTMLLabel('<b>Hello</b>, <i>world</i>',
                                      x=10, y=10)
        #x=window.width//2, y=window.height//2, 
        #                              #font_name="Times New Roman", #font_size=46, 
        #                              anchor_x="center", anchor_y="center")

        label.draw()

    def on_key_press(self, window, symbol, modifiers):
        
        """Handles keyboard input. The keys are defined in options.py and are
        sorted according to namespaces. See that file for further information.

        Arguments:
        window -- the window that recieved the keypress
        symbol -- the key that was pressed
        modifiers -- the modifiers (ctrl, alt, etc.) that were down 
                     when the keypress occurred

        """
        
        if symbol == kb.test.exit:
            window.close()
        elif symbol == kb.test.soundtest:
            game_manager.push(SoundTestScene())
        elif symbol == kb.test.tabtest:
            game_manager.push(TestinNotes("data/pokemon-melody.mid"))
        elif symbol == kb.test.maintest:
            game_manager.push(MainTestScene())
        elif symbol == kb.test.up:
            game_manager.pop()
        else:
            print "Recieved keypress:", symbol, "\t\tModifiers:", modifiers

class MainTestScene(TestScene):
    """Defines an isolated environment for a specific scene, 
    providing methods for handling of input, logic and rendering
    of the scene."""
    def __init__(self):
        self.name = "Test scene"
        self.time = "0"

    def debug_draw(self, window):
        """Draws the debug view of the scene."""
        glClear(GL_COLOR_BUFFER_BIT)       # We are not bound to a window, all the functions and methods are
                                           # merely abstractions for lower level GL calls. If I understand
                                           # correctly, the window just swaps the GL context, or whatever the
                                           # lingo is. Anyways. No window. No clear(). If, however, a window
                                           # is passed using a lambda, we may use it.
    
        label = pyglet.text.Label("Debug " + self.name, 
                                  x=window.width//2, y=window.height//2, 
                                  font_name="Times New Roman", font_size=46, 
                                  anchor_x="center", anchor_y="center")
    
        label2 = pyglet.text.Label("dt = " + self.time,
                                   x=100, y=window.height//2 - 100, 
                                   anchor_x="left", anchor_y="top",
                                   font_name="Times New Roman", font_size=36)
        label.draw()
        label2.draw()

    def game_draw(self, window):
        """Draws the game view of the scene."""
        glClear(GL_COLOR_BUFFER_BIT)

        label = pyglet.text.Label("Game " + self.name, 
                                  x=window.width//2, y=window.height//2, 
                                  font_name="Times New Roman", font_size=46, 
                                  anchor_x="center", anchor_y="center")

        label.draw()

    def do_logic(self, dt):

        """Handles the scene's logic."""
        
        self.time = str(dt)

class SoundTestScene(TestScene):
    
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
        pylab.ion()  # Makes pylab interactive. Plotting does not blockthe application.

        # The figure lets us define the physical size of the plot, so that we can create a texture from it
        self.graph_dpi = 50
        self.graph_width = 4
        self.graph_height = 4

        self.fig = pylab.figure(figsize=[self.graph_width, self.graph_height], # Inches
                                dpi=self.graph_dpi,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                                )
        
        # Set up the axes for plotting
        self.time_plane = pylab.subplot(211)
        self.freq_plane = pylab.subplot(212)
        
        self.fig.add_axes(self.time_plane)
        self.fig.add_axes(self.freq_plane)

        # Do not change the scale to match the graph
        self.time_plane.set_autoscale_on(False) 
        self.freq_plane.set_autoscale_on(False)
        
        # Set the scales of the plot. TODO They use magic numbers. Fix this.
        self.time_plane.set_xlim(xmin=-10, xmax=options.INPUT_CHUNK_SIZE + 10)
        self.time_plane.set_ylim((0, 20000))
        
        self.freq_plane.set_xlim(xmin=-100, xmax=options.INPUT_CHUNK_SIZE-10000)
        self.freq_plane.set_ylim((0, 100000))
        
        time_x = range(options.INPUT_CHUNK_SIZE)
        freq_x = pylab.arange(0, options.INPUT_RATE, step=float(options.INPUT_RATE)/options.INPUT_CHUNK_SIZE)
        
        # Set up initial data, so that we get instances of the plots' data,
        # that we can edit
        self.time_data, = self.time_plane.plot(time_x, [0]*options.INPUT_CHUNK_SIZE)
        self.freq_data, = self.freq_plane.plot(freq_x, [0]*options.INPUT_CHUNK_SIZE)
        
        self.pyglet_plot_1 = pyglet.image.create(self.graph_dpi * self.graph_width, 
                                               self.graph_dpi * self.graph_width)
        self.pyglet_plot_2 = pyglet.image.create(self.graph_dpi * self.graph_width, 
                                               self.graph_dpi * self.graph_width)

        self.graph_updated = True

        #pyglet.clock.schedule_interval(self.update_plot, 1) # Still too slow...
        import threading
        self.update_plot_thread = threading.Thread(target=self.update_plot)
        self.plot_lock = threading.RLock()
        self.quit = False
        self.update_plot_thread.start()


    def __del__(self):
        #pyglet.clock.unschedule(self.update_plot)
        self.quit = True
        self.update_plot_thread.join()
        
    def update_plot(self):
        while not self.quit:
            print "bojs"
            canvas = agg.FigureCanvasAgg(self.fig)
            canvas.draw()
            renderer = canvas.get_renderer()
            self.raw_data = renderer.tostring_argb() # Why isn't rgb and pitch=-3*400 below working?

            raw_pyglet_image = self.pyglet_plot_1.get_image_data()
            #print id(raw_pyglet_image)
            #print id(self.pyglet_plot_1)
            #print "hoj"
            self.plot_lock.acquire()
            #print "setting"
            #print "2 = ", id(self.pyglet_plot_2)
            #print "1 = ", id(self.pyglet_plot_1)
            #temporary = self.pyglet_plot_2
            #self.pyglet_plot_2 = self.pyglet_plot_1
            #self.pyglet_plot_1 = temporary
            raw_pyglet_image.set_data("ARGB", -4*(self.graph_width*self.graph_dpi),
                                      self.raw_data)
            self.plot_lock.release()

            time.sleep(0.1)

    def debug_draw(self, window):
        #ax = fig.gca()
        #ax.plot(y)
        # Update the data
        window.clear()
        # Platt
        #with self.plot_lock:
        self.plot_lock.acquire()
        print "plotting"
        print "2 = ", id(self.pyglet_plot_2)
        print "1 = ", id(self.pyglet_plot_1)
        self.pyglet_plot_1.blit(0,0)
        self.plot_lock.release()

    def do_logic(self, dt):
        pass

class ErrorScene(Scene):
    """Defines an isolated environment for a specific scene, 
    providing methods for handling of input, logic and rendering
    of the scene."""
    def __init__(self):
        self.name = "Error scene"

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

class TestinNotes(TestScene): #a NoteTestScene 
    def __init__(self, midifile):
        self.name = "Note test"
        self.tab = tab.Tab(midifile)
        self.note_batch = pyglet.graphics.Batch()

        #begin speed and memory unoptimized code
        self.death_notes = []
        for note in self.tab.all_notes:
            bolle = graphics.DeathNote(note,self.tab.ticksPerQuarter,self.note_batch)
            bolle.sprite.x = bolle.note.start
            bolle.sprite.y = bolle.note.string * 50
            self.death_notes.append(bolle)
    def game_draw(self, window):
        window.clear()
        self.note_batch.draw()
    def do_logic(self,dt):
        for olle in self.death_notes:
            olle.sprite.x -= 500*dt
            

            


