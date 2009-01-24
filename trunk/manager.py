# -*- coding: utf-8 -*-
#
# manager.py
#
# Provides the GameManager class, which handles multiple
# windows and scene transitions.
#
# (c) Jonne Mickelin 2009

import pyglet
from pyglet.gl import *

import scene as game_scenes

class BasicWindow(pyglet.window.Window):
    
    """Basic window type to be used with scenes and 
    a GameManager. Draws the scene to the screen in 
    a manner pre-defined by a method within the scene.
    """
    
    def __init__(self, *args, **kwargs):
        pyglet.window.Window.__init__(self, *args, **kwargs)
        self.scene = None # Which scene the window is currently looking at

    def change_scene(self, scene, method):

        """Change the scene to draw.

        Arguments:
        scene -- the scene to switch to
        method -- the scene's method for drawing that will be used by this window
        """

        # Well... Magic/more magic. This exact function did not work
        # when it was run directly within GameManager.change_scene. 
        # The lambda made the two window's functions point to the
        # "method" provided by the last window (provided it didn't
        # just point to the clear method).

        # Every window is associated with 
        # a rendering method in the scene
        # which defines how to draw to the
        # window.
        
        # TODO: Method and stuff should probably also be refactored here

        if hasattr(scene, method):                       # The method is optional.
            m = getattr(scene, method)
            self.on_draw = (lambda: m(scene, self))      # Lambda, because the window does not
                                                         # accept any arguments.
        else:
            self.on_draw = self.clear                    # If there is no such method, just clear the window

        self.scene = scene

class MainWindow(BasicWindow):
    
    """A window that exits the program when it is closed."""

    def on_close(self):
        pyglet.app.exit()
                 
class GameManager(object):

    """Handles the scenes of the game. Runs the logic and controls
    the windows. The game is divided into a number of scenes, which
    might be viewed as different states of the game (i.e. menu, game,
    etc.). The scenes contain information about a) the flow of the 
    game and the controlling of it's data (in other words the logic) 
    and b) how the data is represented on the multiple windows. The 
    former is done by calling the scene's do_logic method, which 
    alters the scene object, and the latter is done by the two methods
    debug_draw and game_draw (currently there are just these two windows, 
    but there is support for more).
    The widows provide a context for rendering the scenes to the screen, 
    as defined by the scene itself. The windows do not contain information
    about the game or it's objects. They do, however, store a reference
    to the scene's drawing methods. Multiple windows should be able
    to render the same content. Because of this, the scene's drawing methods
    _cannot_ alter the state of the scene, for apparent reasons.
    """
    
    def __init__(self):
        self.windows = []                            # Contains pairs of (window instances, rendering method in the scene)
        self.scenes = []
        self.current_scene = None

        # Handle the scene's logic at a fixed interval
        pyglet.clock.schedule_interval(self.handle_scene_logic, 1/30.0) 

    def handle_scene_logic(self, dt):
        
        """This function is scheduled to run periodically,
        updating the current scene by calling it's do_logic
        method.
        """

        self.current_scene.do_logic(dt)

    def add_window(self, window, method):

        """Add a window to control. 

        Arguments:
        window -- the window instance to render to
        method -- the name (as a string) of the method that 
                  defines how and what should be drawn to the 
                  window, as a string.
        
        Returns: The current number of windows bound to the application
        """

        self.windows.append((window, method))
        
        return len(self.windows)

    def push(self, scene):
        
        """Add a scene on top of the stack, and switch to it.
        The scene starts running when the logic-function of
        the current scene exits.
        
        Arguments:
        scene -- the scene to push to the stack
        
        Returns: Number of scenes on the stack.
        """

        self.scenes.append(scene)
        self.change_scene(scene)

        return len(self.scenes)

    def pop(self):
        
        """Pop the current scene from the top of the stack
        and switch to the scene under it. That scene is then
        started once the previous scene's logic function 
        exits.

        Returns: The popped scene.
        """
        
        scene = self.scenes.pop()
        
        try:
            self.change_scene(self.scenes[-1])
        except IndexError, err:                         # Print an error if the scene is empty
            self.change_scene(game_scenes.ErrorScene())

        return scene

    def change_scene(self, scene):
        
        """Direct all windows and the manager to use the provided
        scene as the current one. Intended for internal use. This 
        method is available to the users, but using the stack is 
        recommended.

        Arguments:
        scene -- scene to change to
        """

        for window, method in self.windows:
            window.change_scene(scene, method)
        self.current_scene = scene
        
    def swap_top(self):

        """Swaps the two scenes at the top so that the topmost
        scene ends up second top, and vice versa.

        Returns: The scene that was on top previously.
        """

        top = self.pop()
        secondtop = self.pop()
        
        self.push(top)
        self.push(secondtop)
        
        return top

    def run(self):

        """Hand control over to the manager."""
        
        pyglet.app.run()

# Singleton instance of the game. Use this instead of
# initializing a new instance.
game_manager = GameManager()
