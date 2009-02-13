# -*- coding: utf-8 -*-
#
# scene.py
#
# Defines the Scene class, which provides an isolated 
# environment for different scenes of the game. The 
# environment provides methods for handling input, 
# logic and rendering of the scene.
#
# (c) Jonne Mickelin, Jakob Florell 2009

import error
import options

######################
# Required libraries #
######################
import pyglet
from pyglet.gl import *
from pyglet.graphics import vertex_list

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
        #game_manager.pop()
        #if topscene != self:
        #    scene_manager.push(topscene)
        #else:
        #    del topscene
        pass

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

    def on_resize(self, width, height):
        # Pyglet default
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(GL_MODELVIEW)

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
    
        helptext = "<font face='Times New Roman' size='7' color='white'>Controls:<br><br><i>s</i>: SoundTestScene<br><i>t</i>: TestinNotes<br><i>m</i>: MainTestScene<br><i>u</i>: Pop scene</font>"

        label = pyglet.text.HTMLLabel(helptext,
                                      x=window.width//2, y=window.height//2, 
                                      anchor_x="center", anchor_y="center",
                                      multiline=True, width=500)
        label.draw()

    def game_draw(self, window):
        """Draws the game view of the scene."""
        glClear(GL_COLOR_BUFFER_BIT)

        helptext = "<font face='Times New Roman' size='7' color='white'>Controls:<br><br><i>s</i>: ThreadedScene<br><i>t</i>: TestinNotes<br><i>m</i>: MainTestScene<br><i>u</i>: Pop scene</font>"

        label = pyglet.text.HTMLLabel(helptext,
                                      x=window.width//2, y=window.height//2, 
                                      anchor_x="center", anchor_y="center",
                                      multiline=True, width=500)

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
        elif symbol == kb.test.threadtest:
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

class TestinNotes(TestScene):
    """In this scene we test things. Mostly notes"""

    def __init__(self, midifile):

        self.name = "Note test"

        self.tab = tab.Tab(midifile)

        self.note_batch = pyglet.graphics.Batch()
        self.label_batch = pyglet.graphics.Batch()

        # Create the textures for all the notes
        self.death_notes = []            # Graphics for all notes, active or inactive
        for note in self.tab.all_notes:
            x = note.start * graphics.quarterlen / self.tab.ticksPerQuarter
            y = (7 - note.string) * options.window_height / 10

            notegraphic = graphics.DeathNote(note, self.tab.ticksPerQuarter,
                                       x=x, y=y, batch=None)
            self.death_notes.append(notegraphic)

        # Only a fixed number of notes are moved across the screen at once, to 
        # improve performance
        self.notecounter = 200 # Number of notes that will be active
        self.active_sprites = self.death_notes[:self.notecounter]

        for note in self.active_sprites: 
            note.sprite.batch = self.note_batch

            note.label.begin_update()
            note.label.batch = self.label_batch
            note.label.end_update()

        self.temponr = 0
        self.tempo = self.tab.tempo[self.temponr][1] #välj första tempot

        self.timepast = 0 # hur lång tid som gått sedan starten,   ########DEPRECATED?#########

        music = pyglet.resource.media('pokemon.ogg') # GAAAAAAAAAAH! HISSMUSIK!
        self.music = music.play()
        #self.music.on_eos =  #det borde funka, men det verkar inte så
        self.lasttime = self.music.time    # The position in the song in the last frame

        # Set up the graphics
        glClearColor(0x4b/255.0, 0x4b/255.0, 0x4b/255.0, 0)

        glClearDepth(1.0)               # Prepare for 3d. Actually, this might as well 
                                        # be in on_resize, no? Or maybe not. I don't know.

        glDepthFunc(GL_LEQUAL)          # Change the z-priority or whatever one should call it

        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) # Too slow, for some cards, maybe. It does not 
                                                          # give much of a performance gain for me.

    def end(self):

        self.music.stop() # Should check if music is still playing. Stopping twice seems to hang the program.

    def on_resize(self, width, height):

        # Perspective
        glViewport(0, 0, width, height)

        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()
        ## glOrtho(-width/2., width/2., -height/2., height/2., 0, 1000) # I should save this snippet somewhere else
        gluPerspective(30, width / float(height), .1, 10000)

        glMatrixMode(GL_MODELVIEW)

    def game_draw(self, window):
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # We need to set a default scene clearcolor. 
                                                           # How about on_switch_to and on_witch_from functions?
        glPushMatrix()
        
        glLoadIdentity()
        
        glEnable(GL_DEPTH_TEST)
        glTranslatef(0, 0, -900.0)  # Ugly magic number. More translation might be needed.

        # Draw the notes rotated, as per the user's preferences
        glRotatef(options.notes_x_rot, 1.0, 0.0, 0.0)
        glRotatef(options.notes_y_rot, 0.0, 1.0, 0.0)
        glRotatef(options.notes_z_rot, 0.0, 0.0, 1.0)

        # Graphics of guitar neck in background?

        self.note_batch.draw()
        
        # The labels are also drawn like that, which makes them less readable. I'll work on improving this, when I have time.
        self.label_batch.draw()
        
        glDisable(GL_DEPTH_TEST)

        glPopMatrix()

    def do_logic(self,dt):
 
        # Check if there are more changes in tempo and if it is time for such a change.
        # In that case, do the change.
        if len(self.tab.tempo)-1 < self.temponr \
                and self.tab.tempo[self.temponr + 1][0] <= self.timepast:
            self.temponr += 1
            self.tempo = self.tab.tempo[self.temponr][1]

        # The progress of the notes is synchronized with the background song.
        time = self.music.time
        
        # Update only active notes
        for note in self.active_sprites:
            # We should store the constants centrally [why? Jonnes anm.]

            # Movement during one second
            vel = graphics.quarterlen * 1000000 / float(self.tempo) # Tempo is in microseconds
            note.update(dx = -vel * (time - self.lasttime))

            # Change the colour of missed notes
            if not note.failed and note.sprite.x < 0:
                if note.played:
                    self.points += 1
                    print self.points
                else:
                    note.failed = True
                    note.sprite.color = options.dead_note_color

        self.lasttime = time
        
        # Kill the notes that have travelled far enough. This distance 
        # used to be the screen width, but this does not apply when it's tilted
        if (self.active_sprites[0].sprite.x \
                + self.active_sprites[0].sprite.width) < -100: # A little bit of margin
            self.active_sprites[0].die()
            self.active_sprites.pop(0)
        
        # At the same time, we add new notes at the end once the last 
        # currently active note is supposed to appear on screen.
        # Again, this is not the same anymore.
        if self.active_sprites \
                and self.active_sprites[-1].sprite.x < (options.window_width + 200) \
                and len(self.death_notes) > self.notecounter: 

            # Alternatively, one should store the length of the longest notes
            # This could cause bugs if the last note is longer than window_width + 200

            # Recall that self.notecounter is the index of the next note currently not on screen.
            note = self.death_notes[self.notecounter]

            # Put it at the correct distance behind the last note
            note.sprite.x = self.active_sprites[-1].sprite.x \
                + (note.note.start - self.active_sprites[-1].note.start) \
                * graphics.quarterlen / self.tab.ticksPerQuarter
            
            # Add the note and it's label to the batches
            note.sprite.batch = self.note_batch
            note.label.begin_update()
            note.label.batch = self.label_batch
            note.label.end_update()
            
            self.active_sprites.append(note)
            self.notecounter += 1

        # Here we should check if the song has ended
        # Might I suggest that there is a pause between 
        # that and the showing of the score or whatever
        # happens next?
        
           
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

from soundtestscene import SoundTestScene
#from threadedscene import ThreadedScene
