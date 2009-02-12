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
import tilt #tempy
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

class TestinNotes(TestScene): #a NoteTestScene
    """In this scene we test things. Mostly notes"""

    def __init__(self, midifile):
        self.name = "Note test"
        self.tab = tab.Tab(midifile)
        self.note_batch = pyglet.graphics.Batch()
        self.label_batch = pyglet.graphics.Batch()
        #för att labels ska ritas sist, enkla sättet

        self.death_notes = []
        for note in self.tab.all_notes:
            x = note.start*graphics.quarterlen/self.tab.ticksPerQuarter
            y = (7 - note.string) * options.window_height / 10

            bolle = graphics.DeathNote(note, self.tab.ticksPerQuarter,
                                       x=x, y=y, batch=None)
            self.death_notes.append(bolle)

        self.notecounter = 20 #number of notes that will be active
        self.active_sprites = self.death_notes[:self.notecounter] 
            #holds active notes
        for thing in self.active_sprites: 
          #kan säkert göras snyggare, men jag pallarnte
            thing.sprite.batch = self.note_batch
            thing.label.begin_update()
            thing.label.batch = self.label_batch
            thing.label.end_update()

        self.temponr = 0
        self.tempo = self.tab.tempo[self.temponr][1] #välj första tempot

        self.timepast = 0 #hur lång tid som gått sedan starten

        music = pyglet.resource.media('pokemon.ogg')
        self.music = music.play()  # It should be called "player", because it is one, but what the hell. I'll change my code instead
        self.music.on_eos = self.nuedetslut #det borde funka, men det verkar inte så
        self.lasttime = self.music.time    
        print "All done!"
        
    def nuedetslut(self):
        print "Hur dödar man den här och kommer tillbaka till menyn?"
    def end(self):
        self.music.stop()

    def game_draw(self, window):
        glClearColor(0x4b/255.0, 0x4b/255.0, 0x4b/255.0, 0)
        glClear(GL_COLOR_BUFFER_BIT)
        #window.clear()
        self.note_batch.draw()
        self.label_batch.draw()
        tilt.tilt()

    def do_logic(self,dt):
        #kontrollera 1 om det finns fler tempoväxlingar, 2 om det är dax för tempoväxling
        if len(self.tab.tempo)-1 < self.temponr \
                and self.tab.tempo[self.temponr+1][0] <= self.timepast:
            self.temponr += 1
            self.tempo = self.tab.tempo[self.temponr][1]

        time = self.music.time
        
        #update only active notes
        for olle in self.active_sprites:
            #vi borde spara konstanter centralt
            #förflyttning på en sekund:
            vel = graphics.quarterlen * 1000000 / float(self.tempo) #funkarej #tempo är i microsek
            olle.update(dx = -vel * (time - self.lasttime))
            #tinta grått när det blir fel
            if not olle.failed and olle.sprite.x < 0:#self.win_width/10
                if olle.played:
                    self.points += 1
                    print self.points
                else:
                    olle.failed = True
                    olle.sprite.color = options.dead_note_color
        self.lasttime = time
        
        
        #om den första noten har kommit utanför skärmen, döda så gott det går
        if (self.active_sprites[0].sprite.x +\
                self.active_sprites[0].sprite.width) < -100:#lite marginal
            self.active_sprites[0].die()
            self.active_sprites.pop(0)
        
        #om den sista noten är nästan inne på skärmen, lägg en ny not sist
        if self.active_sprites \
                and self.active_sprites[-1].sprite.x < (options.window_width \
                + 200) and len(self.death_notes) > self.notecounter: 
              #eventuellt borde man spara längden på den längsta noten
              #det kan bugga om den sista noten är längre än win_width + 200
            kalle = self.death_notes[self.notecounter]
            kalle.sprite.x = self.active_sprites[-1].sprite.x + \
                (kalle.note.start - self.active_sprites[-1].note.start) \
                * graphics.quarterlen / self.tab.ticksPerQuarter
            kalle.sprite.batch = self.note_batch

            kalle.label.begin_update()
            kalle.label.batch = self.label_batch
            kalle.label.end_update()

            self.active_sprites.append(kalle)
            self.notecounter += 1 #ticka upp
        #här kolla om låten är slut, temp
        # Men den ska väl inte dö när låten slutar?
        
           
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
