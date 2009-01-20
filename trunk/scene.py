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

import pyglet
from pyglet.gl import *
from pyglet.graphics import vertex_list

import error
import options

class Scene(object):
    """Defines an isolated environment for a specific scene, 
    providing methods for handling of input, logic and rendering
    of the scene."""
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

    @staticmethod
    def do_logic(scene):
        """Handles the scene's logic."""
        pass

class TestScene(object):
    """Defines an isolated environment for a specific scene, 
    providing methods for handling of input, logic and rendering
    of the scene."""
    def __init__(self):
        self.name = "Test scene"

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

        label.draw()

    @staticmethod
    def game_draw(scene, window):
        """Draws the game view of the scene."""
        glClear(GL_COLOR_BUFFER_BIT)

        label = pyglet.text.Label("Game " + scene.name, 
                                  x=window.width//2, y=window.height//2, 
                                  font_name="Times New Roman", font_size=46, 
                                  anchor_x="center", anchor_y="center")

        label.draw()

    @staticmethod
    def do_logic(scene):
        """Handles the scene's logic."""
        pass

class ErrorScene(object):
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
    
    @staticmethod
    def do_logic(scene):
        """Handles the scene's logic."""
        pass
