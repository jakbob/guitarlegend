#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# main.py
#
# Guitar game using DSP.
# Main file. Reads command line options, initializes 
# the graphics system, the scene director and hands 
# over the control to the latter.
#
# Copyright (c) 2008-09 Jonne Mickelin & Jakob Florell
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import error

######################
#  Standard library  #
######################
import sys, os
import optparse

######################
# Required libraries #
######################

try:
    import pyglet
except ImportError, err:
    # put an error on the log
    error.critical("This game requires pyglet. If you are using Windows, seeing this message is a BUG. Please file a bug report on http://guitarlegend.googlecode.com. Linux and OS X users should download Pyglet from http://www.pyglet.org.")
    error.bail_out(err)

######################
#    Game modules    #
######################
import options
from manager import game_manager, BasicWindow, MainWindow

def main():
    # Parse the command line options
    parser = optparse.OptionParser()
    parser.add_option("--debug", 
                      action="store_true", 
                      dest="debug", 
                      default=False,
                      help="start game in debugging mode")
    parser.add_option("--show-fps", 
                      action="store_true", 
                      dest="show_fps",
                      default=False,
                      help="start game in debugging mode")
    
    (opts, args) = parser.parse_args()

    options.DEBUG = opts.debug
    options.SHOW_FRAMERATE = opts.show_fps

    # Setup a custom data directory
    pyglet.resource.path = ["data"]
    pyglet.resource.reindex()

    import scene # Imported here, because it depends on the options used
    
    # Add two windows
    game_manager.add_window(MainWindow(caption=options.__appname__), "game_draw")
    if options.DEBUG: game_manager.add_window(BasicWindow(caption="Debug"), "debug_draw")
    
    # Add one scene
    game_manager.push(scene.TestScene())

    # Hand control over to the Game manager
    game_manager.run()

if __name__ == "__main__":
    main()
