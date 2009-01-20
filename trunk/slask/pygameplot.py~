#!/usr/bin/env python
# Demonstrates how to interface to Matplotlib using Pygame.
# Could be further abstracted, of course. All Matplotlib functions
# work as in all other interfaces, of course.
#
# (c) Jonne Mickelin 2008

import matplotlib
import matplotlib.backends.backend_agg as agg
matplotlib.use("Agg")

import pylab
import pygame
from pygame.locals import *

# Plot
fig = pylab.figure(figsize=[4, 4], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()
ax.plot([1, 2, 4])

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

# Plätt (fast inte lätt som en, märkte jag. Hata Pygame 1.7)
while True:
    pass

