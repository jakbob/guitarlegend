# -*- coding: utf-8 -*-
#
# Module for handling graphic operations.
# As it is, it depends on Pyglet, but it should
# be easily exchanged for other libraries.
#
# (c) Jonne Mickelin & Jakob Florell 2008-09

import pyglet

import error

circle = pyglet.imgage.load("data/circle.bmp") #ja, det är ett hack, jag pallarnte
straight = pyglet.imgage.load("data/straight.bmp")


class DeathNote:
	def __init__(self, note, ticksPerQuarter):
		quarters = float(note.stop-note.start)/ticksPerQuarter
		width = int(quarters*40) #magiskt nummer... jag pallarinte. Längden på en fjärdedelsnot
		img = pyglet.image.AbstractImage(width, circle.height)
		img.blit_into(circle, 0,0,0)
		if width>=80: #80=40*2 jag borde verkligen sluta med det här.
			for x in xrange((width-80)/straight.width):
				img.blit_into(straight, x*straight.width,0,0)
			img.blit_into(circle, width-circle.width,0,0)#det här är under *host* konstruktion
			
			
		

