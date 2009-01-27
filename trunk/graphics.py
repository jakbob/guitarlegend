# -*- coding: utf-8 -*-
#
# Module for handling graphic operations.
# As it is, it depends on Pyglet, but it should
# be easily exchanged for other libraries.
#
# (c) Jonne Mickelin & Jakob Florell 2008-09

import pyglet

import error

quarterlen = 400 #The lenght (in pixels) of a quarter note

start_circle = pyglet.image.load("data/circle1.bmp") #ja, det �r ett hack, jag pallarnte
end_circle = pyglet.image.load("data/circle2.bmp")
straight = pyglet.image.load("data/straight.bmp")


class DeathNote:
    def __init__(self, note, ticksPerQuarter):
        self.note = note
        quarters = float(note.stop-note.start)/ticksPerQuarter
        width = int(quarters*quarterlen) #magiskt nummer... jag pallarinte. L�ngden p� en fj�rdedelsnot
        img = pyglet.image.Texture.create(width, start_circle.height)


        img.blit_into(end_circle, width-end_circle.width,0,0)
        img.blit_into(start_circle, 0,0,0)
        
        if width>=2*start_circle.width: #80=40*2 jag borde verkligen sluta med det h�r.
            for x in xrange((width-2*start_circle.width)/straight.width):
                img.blit_into(straight, start_circle.width+x*straight.width,0,0)
            #det h�r �r under *host* konstruktion
            rest = width-(2*start_circle.width+(x+1)*straight.width)
            if rest>0:
                img.blit_into(straight.get_region(0,0,rest,straight.height), start_circle.width+(x+1)*straight.width,0,0)
        self.sprite = pyglet.sprite.Sprite(img)	
        
        self.sprite.color = (40*self.note.string,30*self.note.string,35*self.note.string)
    
if __name__ == "__main__":
    import tab
    window = pyglet.window.Window()
    tab = tab.Tab("data/pokemon-melody.mid")
    olle = DeathNote(tab.string[2][10], tab.ticksPerQuarter)

    @window.event
    def on_draw():
        window.clear()
        olle.sprite.draw()

    pyglet.app.run()
