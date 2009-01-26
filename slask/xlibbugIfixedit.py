#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyglet

class PeesicWindow(pyglet.window.Window):
    pass

#Uncommenting these lines fixes it.
#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.backends.backend_agg as agg

import pylab

pyglet.window.Window()
pyglet.app.run()

#
# Copy of the error message:
#
# The program 'bresk.py' received an X Window System error.
# This probably reflects a bug in the program.
# The error was 'BadMatch (invalid parameter attributes)'.
#   (Details: serial 108 error_code 8 request_code 42 minor_code 0)
#   (Note to programmers: normally, X errors are reported asynchronously;
#    that is, you will receive the error a while after causing it.
#    To debug your program, run it with the --sync command line
#    option to change this behavior. You can then get a meaningful
#   backtrace from your debugger if you break on the gdk_x_error() function.)
