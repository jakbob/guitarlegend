import pyglet
from pyglet.gl import *

import options
glClearDepth(1.0)
glEnable(GL_DEPTH_TEST)

def tilt():
    #glMatrixMode(GL_PROJECTION)
    #glLoadIdentity()
    buffman = pyglet.image.get_buffer_manager()
    colbuff = buffman.get_color_buffer()
    tex = colbuff.get_texture()
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT)
    glEnable(tex.target)
    glBindTexture(tex.target, tex.id)
    
    glBegin(GL_QUADS);
    #bottom left
    glTexCoord2f(0.0, 0.0)
    glVertex3i(0, 0, 0)
    #bottom right
    glTexCoord2f(1.0, 0.0)
    glVertex3i(options.window_width, 0, 0) 
    #top right
    glTexCoord2f(1.0, 1.0)
    glVertex3i(options.window_width, \
       options.window_height, 0)#options.window_height/2)
    #top left
    glTexCoord2f(0.0, 1.0)
    glVertex3i(0, options.window_height, \
       0)#options.window_height/2)
    glEnd();

