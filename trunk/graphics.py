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
    def __init__(self, note, ticksPerQuarter,x=0,y=0, batch=None):
        self.note = note
        quarters = float(note.stop-note.start)/ticksPerQuarter
        width = int(quarters*quarterlen)
        image=self._get_texture(width)
        self.sprite = pyglet.sprite.Sprite(image,x=x,y=y,batch=batch)   
        self.sprite.color = (40*self.note.string+12*self.note.fret,30*self.note.string+15*self.note.fret,35*self.note.string+17*self.note.fret) #mer jobb här...
        self.label = pyglet.text.Label(str(self.note.fret),font_size=30,color=(0,0,0,220),x=self.sprite.x+30,y=self.sprite.y+self.sprite.height/2,anchor_x="center",anchor_y="center",batch=batch)
	self.played = False #this note haven't been played
	self.failed = False #player haven't missed this note (yet)
    
    def _get_texture(self, width):
        img = pyglet.image.Texture.create(width, start_circle.height)
        img.blit_into(end_circle, width-end_circle.width,0,0)
        img.blit_into(start_circle, 0,0,0)
        
        if width>=2*start_circle.width: 
            for x in xrange((width-2*start_circle.width)/straight.width):
                img.blit_into(straight, start_circle.width+x*straight.width,0,0)
            #det h�r �r under *host* konstruktion
            rest = width-(2*start_circle.width+(x+1)*straight.width)
            if rest>0:
                img.blit_into(straight.get_region(0,0,rest,straight.height), start_circle.width+(x+1)*straight.width,0,0)
        return img
    
    def update(self, dx=0):
        #if self.sprite.image: #ser till att det inte krachar när spriten är död. kommer inte på nån snyggare lösning för tillfllet
        self.sprite.x += dx
        self.label.x = self.sprite.x+30
                
    def die(self):
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
