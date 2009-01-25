import pyglet
import random

class Particle:
	def __init__(self, active, life, fadetime, pos, vel):
		self.active = active
		self.life = life
		self.fade = fadetime
		self.pos = pos
		self.vel = vel
		
		self.gravity = (0,0,0) #to be implemented

class ParticleSystem:
	def __init__(self, many):
		self.particles = []
		for i in xrange(many):
			self.particles.append(Particle(True, 100.0, random.random(), (100,100,100), (0,0,0)))
		