#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Demonstrates how to interface to Matplotlib using Pygame.
# Could be further abstracted, of course. All Matplotlib functions
# work as in all other interfaces, of course.
#
# Don't use this on a 64-bit architecture and pygame <= 1.8.0
#
# (c) Jonne Mickelin 2008

import pygame
from pygame.locals import *

import os

ver = pygame.version.vernum
if ver[0] <= 1 and ver[1] < 8 and os.uname == "x86_64":
    raise EnvironmentError("This module does not work on 64-bit machines, due to a bug in Pygame releases before version 1.8.0. Please upgrade to the latest version of Pygame and try again.")

import matplotlib
import matplotlib.backends.backend_agg as agg
matplotlib.use("Agg")

import pylab

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
raw_data = renderer.tostring_rgb()

# Plutt
pygame.init()

window = pygame.display.set_mode((600, 400), DOUBLEBUF)
screen = pygame.display.get_surface()

size = canvas.get_width_height()

surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0,0))
pygame.display.flip()

# Plätt (fast inte lätt som en, mrkte jag. Hata Pygame 1.7)
while True:
    pass

