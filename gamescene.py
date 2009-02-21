# -*- coding: utf-8 -*-
#
# gamescene.py
# Defines the behaviour of the actual game scene
# 
# (c) Jakob Florell and Jonne Mickelin 2009

import error

####################
# Standard library #
####################

import math

####################
# Required Modules #
####################
import pyglet
from pyglet.gl import *
from pyglet.graphics import vertex_list

####################
#   Game modules   #
####################
import scene

import options
import tab

import graphics
import particlesystem

def midify(f):                       
    """                              
    Returns the midi keycode for given frequency.
    Could probably be more optimized but this will have to do
    for now.
    """
    n = round(69.0 + 12.0 * math.log(f / 440.0, 2))
    return int(n)


class GameScene(scene.TestScene):
    """In this scene we test things. Mostly notes"""

    def __init__(self, midifile):

        self.name = "Note test"

        self.tab = tab.Tab(midifile)

        self.note_batch = pyglet.graphics.Batch()
        self.label_batch = pyglet.graphics.Batch()
        self.guitar_neck = graphics.create_guitar_texture(3000)

        self.particles = particlesystem.ParticleSystem(velfactor=50)

        # Create the textures for all the notes
        self.death_notes = []            # Graphics for all notes, active or inactive
        for note in self.tab.all_notes:
            x = note.start * graphics.quarterlen / self.tab.ticksPerQuarter
            y = (6 - note.string) / 6.0 * self.guitar_neck.height + 3.5 # 2 is calibration

            notegraphic = graphics.DeathNote(note, self.tab.ticksPerQuarter,
                                       x=x, y=y, batch=None)
            self.death_notes.append(notegraphic)

        # Only a fixed number of notes are moved across the screen at once, to 
        # improve performance
        self.notecounter = 20 # Number of notes that will be active
        self.active_sprites = self.death_notes[:self.notecounter]

        for note in self.active_sprites: 
            note.sprite.batch = self.note_batch

            note.label.begin_update()
            note.label.batch = self.label_batch
            note.label.end_update()

        self.temponr = 0
        self.tempo = self.tab.tempo[self.temponr][1] #välj första tempot

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
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
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
        glTranslatef(-window.width/2.0 + 100, 
                      -self.guitar_neck.height/2.0, 
                      -900.0)  # Ugly magic number.

        # Draw the notes rotated, as per the user's preferences
        glRotatef(options.notes_x_rot, 1.0, 0.0, 0.0)
        glRotatef(options.notes_y_rot, 0.0, 1.0, 0.0)
        glRotatef(options.notes_z_rot, 0.0, 0.0, 1.0)

        # Graphics of guitar neck in background?
        self.guitar_neck.blit(0, 0)
        glTranslatef(0, 0, 1.0)
        self.note_batch.draw()
        self.particles.draw()
        glTranslatef(0, 5, 1.0)
        # The labels are also drawn like that, which makes them less readable. I'll work on improving this, when I have time.
        self.label_batch.draw()
        
        glDisable(GL_DEPTH_TEST)

        glPopMatrix()

    def do_logic(self,dt):
 
        # Check if there are more changes in tempo and if it is time for such a change.
        # In that case, do the change.
        if len(self.tab.tempo)-1 < self.temponr \
                and self.tab.tempo[self.temponr + 1][0] <= self.music.time*1000000:
                      #self.music.time är i microsekunder
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
                    self.particles.explode(pos=(note.sprite.x,
                       note.sprite.y, 0))
                else:
                    note.failed = True
                    note.sprite.color = options.dead_note_color
                    #probably temp
                    self.particles.explode(pos=(note.sprite.x,
                       note.sprite.y, 0))
        #update particlesystem
        self.particles.update(time-self.lasttime)
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
                and self.active_sprites[-1].sprite.x < (options.window_width + 500) \
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
 
