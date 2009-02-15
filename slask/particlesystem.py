import pyglet
from pyglet.gl import *
import random

texture = pyglet.resource.image("Particle.bmp")


class ParticleGroup(pyglet.graphics.Group):
    def set_state(self):
        glEnable(texture.target)
        glBindTexture(texture.target, texture.id)
    
    def unset_state(self):
        glDisable(texture.target)

class Particle:
    def __init__(self, active, life, fadetime, pos, vel, batch, group=None):
        self.active = active
        self.life = life
        self.fade = fadetime
        self.x, self.y, self.z = pos
        self.dx, self.dy, self.dz = vel
        self.gravity = (0,0,0) #to be implemented
        self.r, self.g, self.b = (255,255,255) #temp
        
        self.vertex_list = batch.add(4, GL_TRIANGLE_STRIP, group,\
        'v3f/stream', 'c3B/stream', ('t2i/static',(1,1,0,1,1,0,0,0)))
        self.update(0) #set position and color

    def update(self,dt=1):
        self.dx += self.gravity[0]*dt
        self.dy += self.gravity[1]*dt
        self.dz += self.gravity[2]*dt

        self.x += self.dx*dt/5
        self.y += self.dy*dt/5
        self.z += self.dz*dt/5
        
        #update vertex positions
        self.vertex_list.vertices = \
        (self.x + 0.5, self.y + 0.5, self.z, #Top right
        self.x - 0.5, self.y + 0.5, self.z, #Top left
        self.x + 0.5, self.y - 0.5, self.z, #Bottom right
        self.x - 0.5, self.y - 0.5, self.z) #bottom left

        #update color, currently temp
        self.vertex_list.colors = \
        (self.r,self.g, self.b,
        self.r,self.g, self.b,
        self.r,self.g, self.b,
        self.r,self.g, self.b)


class ParticleSystem:
    def __init__(self, many, dampening=1):
        self.batch = pyglet.graphics.Batch()
        self.glGroup = ParticleGroup()
        self.particles = []
        for i in xrange(many):
            self.particles.append(Particle(True, 100.0, random.random(), \
               (0,0,0),(2*random.random(), 2*random.random(), \
               2*random.random()), self.batch, self.glGroup))
        self.draw = self.batch.draw

    def update(self, dt=1):
        for particle in self.particles:
            print dt
            particle.update(dt)
    
    

if __name__ == "__main__":
    window = pyglet.window.Window()
    system = ParticleSystem(20)
    
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
        system.update(pyglet.clock.tick())
        system.draw()
        
        #print pyglet.clock.get_fps()

    pyglet.app.run()
        