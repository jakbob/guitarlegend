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

def uniq(iterable):
    N = options.DFT_SIZE
    SAMPLE_RATE = options.SAMPLE_RATE
    rets = {}
    for (num, amp) in iterable:
        try:
            p = midify(num * float(SAMPLE_RATE)/N)
            if p < 0:
                raise OverflowError("Bajs")
        except OverflowError:
            continue

        if p in rets:
            if rets[p] < amp:
                rets[p] = amp
        else:
            rets[p] = amp
    return rets

def get_note_numbers(mag_list):
    N = options.DFT_SIZE
    MAG_THRESHOLD = options.MAG_THRESHOLD
    
    if mag_list is not None:
        assert mag_list[:N/2][0] == mag_list[0]
        note_numbers = uniq(enumerate(mag_list[:N/2]))
        return [p for p in get_largest(note_numbers) if note_numbers[p] > MAG_THRESHOLD]
    else:
        return None

def get_largest(l):
    largest = heapq.nlargest(6, l, key=(lambda key: l[key]))
    return largest

def get_sound():
    mag_list = wonderful.munch()
    return get_note_numbers(mag_list)

#try:
#    while True:
#        t = time.clock()
#        s = get_sound()
#        if s is not None:
#            print s, "\t\tin", t-lasttime, "seconds"
#        lasttime = t
#
#except KeyboardInterrupt:
#    pass
    
class GameScene(scene.TestScene):
    """In this scene we test things. Mostly notes"""

    def __init__(self, soundfile, midifile):

        self.name = "Ingame"
        self._setup_graphics()

        self._load_file(soundfile, midifile)
        self.particles = particlesystem.ParticleSystem(velfactor=50)
    
    def end(self):
        try:
            self.music.stop()
        except ValueError:
            pass #det blir knas ibland när låten stoppas 2 ggr
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
        #self.camera.focus(width, height)

    def game_draw(self, window):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # We need to set a default scene clearcolor. 
                                                           # How about on_switch_to and on_witch_from functions?
        glPushMatrix()
        glLoadIdentity()

        glEnable(GL_DEPTH_TEST)

        #glTranslatef(0,0,-10.0)
        #self.pointmeter.draw()   
    
        glTranslatef(-window.width/2.0 + 100, 
                      -self.guitar_neck.height/2.0, 
                      -900.0)# Ugly magic number.
        self.pointmeter.draw()

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

        #Try to uncomment this and see why it is commented out.
        #There is something wrong with the particles, and I don't have
        #the orc to find out what. particlesystem.py is like an italian
        #restaurant.
        #glLoadIdentity()
        #glEnable(GL_DEPTH_TEST)
        #glTranslatef(-window.width/2.0 + 100, 
                     #-self.guitar_neck.height/2.0, 
                     #-880.0)  # Ugly magic number.
        #self.particles.draw()

        glDisable(GL_DEPTH_TEST)
        glPopMatrix()
        #self.camera.hud_mode(window.width, window.height)

    def do_logic(self, dt):

        # The progress of the notes is synchronized with the background song.
        t = self.music.time
        self._check_tempochange(t)
        #let's see if it works
        if t == self.lasttime: 
            delta_time = self.lastdelta #move a little
            self.offsync += self.lastdelta
        else:
            delta_time = t - self.lasttime
        if self.offsync > delta_time / 3:
            delta_time -= self.offsync / 3
            self.offsync -= self.offsync / 3
        else:
            delta_time -= self.offsync
            self.offsync = 0.0
        try:
            self._update_notes(delta_time)
        except IndexError:
            pass
        self.particles.update(delta_time)
        self.lasttime = t
        self.lastdelta = delta_time
        
        in_notes = get_sound()
        print in_notes
        self._compare_notes(in_notes)
        
    def _setup_graphics(self):
        #äcklig grå färg
        #glClearColor(0x4b/255.0, 0x4b/255.0, 0x4b/255.0, 0)
        #svart:
        glClearColor(0,0,0,0)

        glClearDepth(1.0)               # Prepare for 3d. Actually, this might as well 
                                        # be in on_resize, no? Or maybe not. I don't know.

        glDepthFunc(GL_LEQUAL)          # Change the z-priority or whatever one should call it

        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    
    def _load_file(self, soundfile, midifile):
        print "Loading File. Please wait."
        self.tab = tab.Tab(midifile)
        self.note_batch = pyglet.graphics.Batch()
        self.label_batch = pyglet.graphics.Batch()
        self.guitar_neck = graphics.create_guitar_texture(3000)
        img = pyglet.image.load(
           os.path.join(options.data_dir, "thingy.png"))
        self.deathbar = pyglet.sprite.Sprite(img, 
           the_danger_point + img.width / 2, 0)
        self.points = 0
        self.pointmeter = pyglet.text.Label(str(self.points), font_size = 20,
           bold = True, anchor_x = "right", anchor_y = "top", 
           color = (200, 200, 20, 255),
           x = 560, y = 270) #äckliga magiska konstanter men jag pallarnte
           #x = self.camera.x, y = self.camera.y)
    
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
        self.lastdelta = 0 #holds the last delta_time, used for smooth movement
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
            #self.check_whos_playing([]) #såhär nånting?

    def _update_active_notes(self, dt):
        self.the_edge = [] #
        # Update only active notes
        for note in self.active_sprites:
            # Movement during one second
            #vel = graphics.quarterlen * 1000000 / float(self.tempo) # Tempo is in microseconds
            note.update(dt, self.tempo)
            if note.sprite.x < the_danger_point + 10 and \
               note.sprite.x + note.sprite.width > the_danger_point - 10:
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

    def _compare_notes(self, notes_played):
        if notes_played is None:
            return
        for note in self.the_edge:
            if note.note.pitch in notes_played:
                note.is_played()
                #give points
                self.points += 1 # This sounds bad
                self.pointmeter.text = str(self.points)
                self.particles.explode(pos=(note.sprite.x,
                                            note.sprite.y, 0))
            else:
                note.missed()
