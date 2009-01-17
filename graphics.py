# -*- coding: utf-8 -*-
#
# Module for handling graphic operations.
# As it is, it depends on Pyglet, but it should
# be easily exchanged for other libraries.
#
# (c) Jonne Mickelin & Jakob Florell 2008-09

import error

try:
    import pyglet
except ImportError, err:
    # put an error on the log
    error.critical("This game requires pyglet. If you are using Windows, seeing this message is a BUG. Please file a bug report on http://guitarlegend.googlecode.com. Linux and OS X users should download Pyglet from http://www.pyglet.org.")
    error.bail_out(err)
