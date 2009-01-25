#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Demonstrates how to interface to Matplotlib using Pyglet.
# Could be further abstracted, of course. All Matplotlib functions
# work as in all other interfaces, of course.
#
#
# (c) Jonne Mickelin 2008

import pyglet
from pyglet.window import key
import matplotlib

import matplotlib.backends.backend_agg as agg
matplotlib.use("Agg")
import pylab

window = pyglet.window.Window()


import math
y = []
for el in range(100):
    y.append(math.sin(2*math.pi * el / 100.0))

# Plot
fig = pylab.figure(figsize=[4, 4], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()
ax.plot(y)

# Platt
canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_argb() # Why isn't rgb and pitch=-3*400 below working?

pyglet_plot = pyglet.image.create(400, 400)
raw_pyglet_image = pyglet_plot.get_image_data()
raw_pyglet_image.set_data("ARGB", -4*400, raw_data)

@window.event
def on_draw():
    window.clear()
    pyglet_plot.blit(0,0)

pyglet.app.run()
