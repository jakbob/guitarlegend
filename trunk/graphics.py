# -*- coding: utf-8 -*-
#
# Module for graphic primitives and the setting up
# thereof.
#
# (c) Jonne Mickelin & Jakob Florell 2008-09

import pyglet
import os

import error
import options

quarterlen = 100 # The lenght (in pixels) of a quarter note

start_circle = pyglet.image.load("data/circle1.png") # Well, fuck Windows! At least, fuck them until we fix this. Which will be soon.
end_circle = pyglet.image.load("data/circle2.png")
straight = pyglet.image.load("data/straight.png")

normal_guitar = pyglet.image.load("data/guitar.png")
guitar_fret = pyglet.image.load("data/guitarfret.png")

class DeathNote:

    """A deadly combination of a note and sprite"""

    def __init__(self, note, ticksPerQuarter, x=0, y=0, batch=None):

        self.note = note
        num_quarters = float(note.stop - note.start) / ticksPerQuarter
        note_width = int(num_quarters * quarterlen)

        # Prepare an image texture that we can blit to the screen(s)
        image = self._get_texture(note_width)

        # Then make a sprite of it
        self.sprite = pyglet.sprite.Sprite(image, x=x, y=y, batch=batch)

        self.set_color()

        self.label = pyglet.text.Label(str(self.note.fret),
                                       font_size=options.note_label_size, color=options.note_label_color,
                                       x=self.sprite.x+30, y=self.sprite.y + self.sprite.height/2,
                                       anchor_x="center", anchor_y="center", 
                                       batch=batch)

	self.played = False #this note haven't been played
	self.failed = False #player haven't missed this note (yet)
    
    def _get_texture(self, width):

        """Create a texture based on note data"""

        img = pyglet.image.Texture.create(width, start_circle.height)
        
        if width > end_circle.width: #temp, måste komma på bättre sätt
            img.blit_into(end_circle, width - end_circle.width, 0, 0) # Put in the caps of the note first
        img.blit_into(start_circle, 0, 0, 0)
        
        if width >= 2 * start_circle.width: # If the note is longer than that
            for offset in xrange(start_circle.width, 
                                 width - start_circle.width, 
                                 straight.width):
                img.blit_into(straight, 
                              offset,
                              0, 0)

            # Fill in the missing space between the last straight piece and the end cap
            rest = width - (2 * start_circle.width + (offset + 1) * straight.width)
            if rest > 0:
                region = straight.get_region(0, 0, rest, straight.height)
                img.blit_into(region, start_circle.width + (offset + 1)*straight.width, 0, 0)

        return img

    def set_color(self):

        """Set the color, based on what string and fret the note symbolizes"""
        
        def hex_to_rgb_list(hexcolor):
            
            """Mask out the rgb parts of a 6-digit hexadecimal number."""
            
            b = hexcolor & 0xFF
            g = (hexcolor >> 8) & 0xFF
            r = (hexcolor >> 16) & 0xFF
            
            return [r, g, b]

        base_color = options.string_base_colors[self.note.string-1] + options.string_brightness
        hex_color = base_color + options.string_color_step[self.note.string-1] * self.note.fret

        self.sprite.color = hex_to_rgb_list(hex_color)

    def update(self, dt, tempo):

        """Update the on-screen position of the note."""

        dx = -quarterlen * (1000000.0/float(tempo)) # Tempo is in microseconds

        self.sprite.x += dx*dt
        self.label.x = self.sprite.x + 30
                
    def die(self):

        """Deallocate the note."""

        self.sprite.delete()
        self.label.delete()
        del self # Does not seem to do much
        
    def is_played(self):
        self.played = True
        self.sprite.color = options.played_note_color
    
    def missed(self):
        self.played = False
        self.sprite.color = options.dead_note_color

def create_guitar_texture(length):
    
    retimg = pyglet.image.Texture.create(length, guitar_fret.height)

    if length < guitar_fret.width:
        region = guitar_fret.get_region(0, 0, length, guitar_fret.height)
        retimg.blit_into(region, 0, 0, 0)
    else:
        retimg.blit_into(guitar_fret, 0, 0, 0)
    
    offset = guitar_fret.width
    for offset in xrange(guitar_fret.width, length, normal_guitar.width):
        retimg.blit_into(normal_guitar, offset, 0, 0)

    return retimg
