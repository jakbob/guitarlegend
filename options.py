# -*- coding: utf-8 -*-
#
# options.py
#
# Provides a centralized storage for all options.
#
# (c) Jonne Mickelin 2008

class AttrDict(dict):
    """A dictionary, whose elements can be accessed 
    as attributes.
    """
    def __getattr__(self, attr):
        return self[attr]
    def __setattr__(self, attr, value):
        self[attr] = value

######################
#      Metadata      #
######################
__author__ = "Jonne Mickelin, Jakob Florell"
__copyright__ = "Copyright (c) Jonne Mickelin & Jakob Florell 2008-09"
__license__ = "GNU General Public License v3"
__version__ = "0.0.1"
__appname__ = "bosseonfire"

##########################
# Is debuging turned on? #
########################## 
DEBUG = False

from pyglet.window import key

#################################################
#                                               #
# Keys are specified in a number of different   #
# namespaces. For example, to set the key for   #
# bringing up the menu in-game, change the      #
# value of kb.game.menu.                        #
# Two keys can be used for the same action.     #
# This is done by OR:ing the keys together.     #
# For example, to make both the P and the Pause #
# key pause the game, type                      #
# kb.game.pause = key.P | key.PAUSE             #
#                                               #
#################################################

######################
kb = AttrDict()      #
######################

######################
kb.menu = AttrDict() #
######################
kb.menu.up = key.UP
kb.menu.down = key.DOWN
kb.menu.left = key.LEFT
kb.menu.right = key.RIGHT

######################
kb.game = AttrDict() #
######################
kb.game.menu = key.ESCAPE
kb.game.pause = key.P
