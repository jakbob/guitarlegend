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
import heapq
import os

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
import wonderful

import graphics
import particlesystem
from manager import game_manager

the_danger_point = 100 #the point where the notes should be played

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

    def __init__(self, soundfile, midifile):

        self.name = "Ingame"
        self._setup_graphics()

        self._load_file(soundfile, midifile)
        self.particles = particlesystem.ParticleSystem(velfactor=50)

    def end(self):
        if self.music.playing:
            self.music.stop()
        print "in end, yo"
        #wonderful.terminate()

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
        glTranslatef(0, 0, 1.0)
        # The labels are also drawn rotated, which makes them less readable. 
        # I'll work on improving this, when I have time.
        self.label_batch.draw()
        glTranslatef(0, 0, 1.0)
        self.deathbar.draw()
        glDisable(GL_DEPTH_TEST)

        # Try to uncomment this and see why it is commented out.
        # There is something wrong with the particles, and I don't have
        # the orc to find out what. particlesystem.py is like an italian
        # restaurant.
        #glLoadIdentity()
        #glEnable(GL_DEPTH_TEST)
        #glTranslatef(-window.width/2.0 + 100, 
        #              -self.guitar_neck.height/2.0, 
        #              -880.0)  # Ugly magic number.
        #self.particles.draw()

        #glDisable(GL_DEPTH_TEST)
        glPopMatrix()

    def do_logic(self, dt):

        # The progress of the notes is synchronized with the background song.
        t = self.music.time
        self._check_tempochange(t)
        #let's see if it works
        if t == self.lasttime:
            delta_time = self.offsync = dt/2 #move a little
        else:
            delta_time = t - self.lasttime - self.offsync
            self.offsync = 0
        try:
            self._update_notes(delta_time)
        except IndexError:
            pass
        self.particles.update(t - self.lasttime)
        self.lasttime = t
        
        #sound = self._get_sound_input()
        #if sound:
        #    print sound
        freqs = wonderful.munch()
        if freqs is not None:
            lowest_hearable = int(20*options.DFT_SIZE/float(options.SAMPLE_RATE))
            relevant_freqs = freqs[lowest_hearable:options.DFT_SIZE/2]
            largest = heapq.nlargest(6, enumerate(relevant_freqs), key=(lambda (num, amp): amp))
            hertz_freqs = [(p + lowest_hearable) * float(options.SAMPLE_RATE) / options.DFT_SIZE
                             for (p, mag) in largest 
                            if mag > options.FREQ_THRESHOLD]
            print [midify(f) for f in  hertz_freqs]
        # Here we should check if the song has ended
        # Might I suggest that there is a pause between 
        # that and the showing of the score or whatever
        # happens next?

    def _setup_graphics(self):

        glClearColor(0x4b/255.0, 0x4b/255.0, 0x4b/255.0, 0)

        glClearDepth(1.0)               # Prepare for 3d. Actually, this might as well 
                                        # be in on_resize, no? Or maybe not. I don't know.

        glDepthFunc(GL_LEQUAL)          # Change the z-priority or whatever one should call it

        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    
    def _load_file(self, soundfile, midifile):
        
        self.tab = tab.Tab(midifile)
        self.note_batch = pyglet.graphics.Batch()
        self.label_batch = pyglet.graphics.Batch()
        self.guitar_neck = graphics.create_guitar_texture(3000)
        self.deathbar = pyglet.sprite.Sprite(
           pyglet.image.load(
           os.path.join(options.data_dir, "thingy.png")),
           the_danger_point, 0)
    
        # Create the textures for all the notes
        self.death_notes = []            # Graphics for all notes, active or inactive
        for note in self.tab.all_notes:
            x = the_danger_point + (note.start) * graphics.quarterlen / self.tab.ticksPerQuarter
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
        
        self.the_edge = [] #notes that are to be played

        self.temponr = 0
        self.tempo = self.tab.tempo[self.temponr][1] #välj första tempot

        music = pyglet.media.load(soundfile)
        self.music = pyglet.media.StaticSource(music).play()
        self.lasttime = self.music.time    # The position in the song in the last frame
        self.offsync = 0
        self.music._old_eos = self.music._on_eos
        def on_music_eos():
            self.music._old_eos()
            game_manager.pop()
        self.music._on_eos = on_music_eos #misstänker bugg i pyglet
    
    def _check_tempochange(self, t):

        """Check if there are more changes in tempo and if 
        it is time for such a change. In that case, do the change."""

        # Tempo change position is in microseconds
        if len(self.tab.tempo) - 1 < self.temponr \
                and self.tab.tempo[self.temponr + 1][0] <= t*1000000:
            self.temponr += 1
            self.tempo = self.tab.tempo[self.temponr][1]

    def _update_notes(self, dt):
        """Make sure there are notes to update, and update them"""
        if self.active_sprites:
            self._update_active_notes(dt)
            if self.notecounter < len(self.death_notes):
                self._set_active_notes(dt)
            self.check_whos_playing([]) #såhär nånting?

    def _update_active_notes(self, dt):
        self.the_edge = [] #
        # Update only active notes
        for note in self.active_sprites:
            # Movement during one second
            #vel = graphics.quarterlen * 1000000 / float(self.tempo) # Tempo is in microseconds
            note.update(dt, self.tempo)#(time - self.lasttime))
            if note.sprite.x < the_danger_point and \
               note.sprite.x + note.sprite.width > the_danger_point:
                self.the_edge.append(note)
            
    def _set_active_notes(self, dt):
        # Kill the notes that have travelled far enough. This distance 
        # used to be the screen width, but this does not apply when it's tilted
        if (self.active_sprites[0].sprite.x \
                + self.active_sprites[0].sprite.width) < -100: # A little bit of margin
            self.active_sprites[0].die()
            self.active_sprites.pop(0)
                    
        # At the same time, we add new notes at the end once the last 
        # currently active note is supposed to appear on screen.
        # Again, this is not the same anymore.
        if self.active_sprites[-1].sprite.x < (options.window_width + 500): 

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

    def _get_sound_input(self):

        freqs = wonderful.munch()
        if freqs is not None:
            lowest_hearable = int(20*options.DFT_SIZE/float(options.SAMPLE_RATE))
            relevant_freqs = freqs[lowest_hearable:options.DFT_SIZE/2]
            largest = heapq.nlargest(6, enumerate(relevant_freqs), key=(lambda (num, amp): amp))
            hertz_freqs = [(p + lowest_hearable) * float(options.SAMPLE_RATE) / options.DFT_SIZE
                             for (p, mag) in largest 
                            if mag > options.FREQ_THRESHOLD]
            return [midify(f) for f in  hertz_freqs]
    
    def check_whos_playing(self, notes_played):
        for note in self.the_edge:
            if note.note.pitch in notes_played:
                note.is_played()
                #give points
                self.points += 1 # This sounds bad
                print self.points
                self.particles.explode(pos=(note.sprite.x,
                                            note.sprite.y, 0))
            else:
                note.missed()
