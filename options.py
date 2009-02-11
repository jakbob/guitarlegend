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
SHOW_FRAMERATE = False

##########################
#   Microphone settings  #
##########################
import pyaudio

INPUT_FORMAT         = pyaudio.paInt16 # 16 bit sample format.
STRUCT_INPUT_FORMAT  = "1h"            # The setting for struct.unpack. 16 bits per sample.
INPUT_CHANNELS       = 1               # Number of channels to record.
INPUT_RATE           = 22050           # Sampling rate.
INPUT_CHUNK_SIZE     = 2048            # Number of samples to be captured and analyzed at a time.

from pyglet.window import key

#################################################
#                                               #
# Keys are specified in a number of different   #
# namespaces. For example, to set the key for   #
# bringing up the menu in-game, change the      #
# value of kb.game.menu.                        #
### Two keys can be used for the same action.     #  ## Apparently not.
### This is done by OR:ing the keys together.     #
### For example, to make both the P and the Pause #
### key pause the game, type                      #
### kb.game.pause = key.P | key.PAUSE             #
###                                               #
###################################################

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

######################
kb.test = AttrDict() #
######################
kb.test.exit = key.ESCAPE
kb.test.threadtest = key.S
kb.test.tabtest = key.T
kb.test.maintest = key.M
kb.test.up = key.U

######################
#       Colours      #
######################

# The colours of the strings (rgb)
string_base_colors = [ 0x1a6cdc,  # e'
                       0xdc631a,  # h
                       0x0dbc2a,  # g
                       0xbc260d,  # d
                       0x3a642e,  # A
                       0x0f458e   # E
                       ]

# Difference in colour between consequitive frets on a string
string_color_step = 0x091509

# Fine tune the brightness of the string_base_colors. 
# Negative value means darker color. Note that too
# high values can give entirely different colors
string_brightness = -0x010101
