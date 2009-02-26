#coding: utf8

import pyglet
from pyglet.gl import *
from random import random
import functools

#texture = pyglet.resource.texture("particle.png")
texture = pyglet.image.load("data/particle.png").get_texture()
# Av någon anledning är resource helt uppfuckad!!
whitespeed = 50.0
particlesize = 10


class ParticleGroup(pyglet.graphics.Group):
    def set_state(self):
        glEnable(texture.target)
        glBindTexture(texture.target, texture.id)
        self.enableDepth = glIsEnabled(GL_DEPTH_TEST)
        glDisable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA,GL_ONE)
    
    def unset_state(self):
        glDisable(texture.target)
        glDisable(GL_BLEND)
        if self.enableDepth:
            glEnable(GL_DEPTH_TEST)

class Particle:
    def __init__(self, active, life, fadetime, pos, vel, dampening, gravity,
       batch, group=None):
        self.active = active
        self.life = life
        self.fade = fadetime
        self.x, self.y, self.z = pos
        self.dx, self.dy, self.dz = vel
        self.gx, self.gy, self.gz = gravity
        self.dampening = dampening

        self.vertex_list = batch.add(4, GL_TRIANGLE_STRIP, group,
        'v3f/stream', 'c4f/stream', ('t2i/static',(1,1,0,1,1,0,0,0)))
        self.update(0) #set position and color

    def update(self,dt=1):
        self.dx += (self.gx - self.dx * self.dampening) * dt
        self.dy += (self.gy - self.dy * self.dampening) * dt
        self.dz += (self.gz - self.dz * self.dampening) * dt

        self.x += self.dx * dt
        self.y += self.dy * dt
        self.z += self.dz * dt

        #update vertex positions
        self.vertex_list.vertices = \
            (self.x + particlesize/2, self.y + particlesize/2, self.z, #Top right
             self.x - particlesize/2, self.y + particlesize/2, self.z, #Top left
             self.x + particlesize/2, self.y - particlesize/2, self.z, #Bottom right
             self.x - particlesize/2, self.y - particlesize/2, self.z) #bottom left
        
        #update color; ett försök att skapa färg baserat på hastighet
        total = (abs(self.dx) + abs(self.dy) + abs(self.dz)) / whitespeed
        if total > 3: total = 3
        self.r = 1.0 if total > 1 else total
        self.g = 1.0 if total-self.r > 1 else total-self.r
        self.b = 0.0 if total - self.g - self.r < 0 else total-self.g-self.r
        self.life -= self.fade
        
        if self.life < 0:
            return #några andra förslag?
        self.vertex_list.colors = \
            (self.r,self.g, self.b, self.life,
             self.r,self.g, self.b, self.life,
             self.r,self.g, self.b, self.life,
             self.r,self.g, self.b, self.life)


class ParticleSystem:
    def __init__(self, many=20, pos=(0.0,0.0,0.0), velfactor=1, dampening=0, 
       fadespeed=1.0, gravity=(0,0,0)):
        self.batch = pyglet.graphics.Batch()
        self.glGroup = ParticleGroup()
        self.particles = []
        self.draw = self.batch.draw
    
        #self.def_many = many #set default values
        #self.def_pos = pos #alternative solutions
        #self.def_vel = velfactor #are appreciated
        #self.def_damp = dampening
        #self.def_fade = fadespeed
        #self.def_grav = gravity
    
        def explode(many=many, pos=pos, velfactor=velfactor,
        dampening=dampening, fadespeed=fadespeed, gravity=gravity):
            for i in xrange(many):
                self.particles.append(Particle(True, 1.0, 
                random()*fadespeed+0.005, pos, (velfactor*2*(random()-.5), velfactor*2*(random()-.5), velfactor*2*(random()-.5)), 
                dampening, gravity, self.batch, self.glGroup))
        self.explode = explode # jag tror hacket funka!!
    
    def update(self, dt=1):
        for particle in self.particles:
            if particle.life > 0:
                particle.update(dt)
            else:
                particle.vertex_list.delete()
                self.particles.remove(particle)
    

if __name__ == "__main__":
    window = pyglet.window.Window()
    system = ParticleSystem(velfactor=2, dampening=0.4)
    system.explode(100)

    #init
    glShadeModel(GL_SMOOTH)
    glClearColor(0,0,0,0)
    glClearDepth(1.0)
    glDisable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA,GL_ONE)
    #glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST)
    #glHint(GL_POINT_SMOOTH_HINT,GL_NICEST)
    pyglet.clock.set_fps_limit(30)
    pyglet.clock.schedule_interval(system.update, 1/30.0)
    
    @window.event
    def on_resize(width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / float(height), .1, 1000)
        #glMatrixMode(GL_MODELVIEW)
        #glLoadIdentity()
        return pyglet.event.EVENT_HANDLED
    
    @window.event
    def on_draw():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        system.draw()

    pyglet.app.run()
        
