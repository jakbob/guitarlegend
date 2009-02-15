#coding: utf8

import pyglet
from pyglet.gl import *
from random import random

texture = pyglet.resource.image("Particle.bmp")
whitespeed = 3.0


class ParticleGroup(pyglet.graphics.Group):
    def set_state(self):
        glEnable(texture.target)
        glBindTexture(texture.target, texture.id)
    
    def unset_state(self):
        glDisable(texture.target)

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
        self.dx += self.gx * dt
        self.dy += self.gy * dt
        self.dz += self.gz * dt

        self.x += self.dx * dt / self.dampening
        self.y += self.dy * dt / self.dampening
        self.z += self.dz * dt / self.dampening

        #update vertex positions
        self.vertex_list.vertices = \
            (self.x + 0.5, self.y + 0.5, self.z, #Top right
             self.x - 0.5, self.y + 0.5, self.z, #Top left
             self.x + 0.5, self.y - 0.5, self.z, #Bottom right
             self.x - 0.5, self.y - 0.5, self.z) #bottom left
        
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
    def __init__(self, many, pos=(0.0,0.0,0.0), velfactor=1, dampening=1, 
       life=1.0, gravity=(0,0,0)):
        self.batch = pyglet.graphics.Batch()
        self.glGroup = ParticleGroup()
        self.particles = []
        for i in xrange(many):
            self.particles.append(Particle(True, life, random()/10.0+0.005,
               (0,0,0), (velfactor*2*(random()-.5), velfactor*2*(random()-.5),               velfactor*2*(random()-.5)), dampening, gravity,
               self.batch, self.glGroup))
        self.draw = self.batch.draw

    def update(self, dt=1):
        for particle in self.particles:
            if particle.life > 0:
                particle.update(dt)
            else:
                self.particles.remove(particle)
                if not self.particles:
                    print "dags för likbilen"
    

if __name__ == "__main__":
    window = pyglet.window.Window()
    system = ParticleSystem(20, velfactor=3, dampening=5)
    
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
        
