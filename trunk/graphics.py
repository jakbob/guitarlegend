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
    def __init__(self, note, ticksPerQuarter, batch=None):
        self.note = note
        quarters = float(note.stop-note.start)/ticksPerQuarter
        self.width = int(quarters*quarterlen) #bättre lösning här?
        self.sprite = None
        self.label = None
        self.batch = batch
        self.textured = False #this note haven't been given a texture yet
    
    def _get_texture(self, width):
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
        self.sprite = pyglet.sprite.Sprite(img, x=self.x, y=self.y, batch=self.batch)   
        self.sprite.color = (40*self.note.string+12*self.note.fret,30*self.note.string+15*self.note.fret,35*self.note.string+17*self.note.fret)
        self.label = pyglet.text.Label(str(self.note.fret),font_size=30,color=(0,0,0,220),x=self.x,y=self.y,anchor_x="center",anchor_y="center",batch=self.batch)
        self.textured = True
    
    def update(self):
        if self.textured:
            self.sprite.x = self.x
            self.label.x = self.x+30
            self.sprite.y = self.y
            self.label.y = self.y+self.sprite.height/2
        if self.x < 640*2 and not self.textured: #hur kommer man åt window.heigth härifrån?
            self._get_texture(self.width)
        if self.x < -640 and self.textured:
            self.sprite.delete() #för säkerhets skull
            del self.sprite #eventuellt döda hela objektet?
            del self.label
            self.textured = False
            print "nu e den död"
        
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
