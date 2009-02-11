# -*- coding: utf-8 -*-
#
# Module for handling graphic operations.
# As it is, it depends on Pyglet, but it should
# be easily exchanged for other libraries.
#
# (c) Jonne Mickelin & Jakob Florell 2008-09

import pyglet

import error
import options

quarterlen = 200 #The lenght (in pixels) of a quarter note

start_circle = pyglet.image.load("data/circle1.png") #ja, det �r ett hack, jag pallarnte
end_circle = pyglet.image.load("data/circle2.png")
straight = pyglet.image.load("data/straight.png")


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

        self.set_color() #lite hackigt men jag bryrmejnte

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

        img.blit_into(end_circle, width - end_circle.width, 0, 0) # Put in the caps of the note first
        img.blit_into(start_circle, 0, 0, 0)
        
        if width >= 2 * start_circle.width: # If the note is longer than that

            for offset in xrange((width - 2 * start_circle.width) / straight.width): # Attention! xrange does not support floating numbers!
                img.blit_into(straight, 
                              start_circle.width + offset*straight.width,
                              0, 0)

            # Fill in the missing space between the last straight piece and the end cap
            rest = width - (2 * start_circle.width + (offset + 1) * straight.width)
            if rest > 0:
                region = straight.get_region(0, 0, rest, straight.height)
                img.blit_into(region, start_circle.width + (offset + 1)*straight.width, 0, 0)

        return img

    @staticmethod
    def hex_to_rgb_list(hexcolor):

        """Mask out the rgb parts of a 6-digit hexadecimal number."""

        b = hexcolor & 0xFF
        g = (hexcolor >> 8) & 0xFF
        r = (hexcolor >> 16) & 0xFF

        return [r, g, b]

    def set_color(self):

        """Set the color, based on what string and fret the note symbolizes"""

        base_color = options.string_base_colors[self.note.string-1] + options.string_brightness
        hex_color = base_color + options.string_color_step[self.note.string-1] * self.note.fret

        self.sprite.color = self.hex_to_rgb_list(hex_color)

    def update(self, dx=0):
        """Update the on-screen position of the note."""
        ##if self.sprite.image: #ser till att det inte krachar när spriten är död. kommer inte på nån snyggare lösning för tillfllet

        self.sprite.x += dx
        self.label.x = self.sprite.x + 30
                
    def die(self):
        """Deallocate the note."""
        self.sprite.delete()
        self.label.delete()
        del self #verkar inte göra så mycket

if __name__ == "__main__":
    import tab
    window = pyglet.window.Window()
    tab = tab.Tab("data/pokemon-melody.mid")
    olle = DeathNote(tab.string[2][10], tab.ticksPerQuarter)

    @window.event
    def on_draw():
        window.clear()
        olle.sprite.draw()
        olle.label.draw()

    pyglet.app.run()
