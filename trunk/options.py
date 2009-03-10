# -*- coding: utf-8 -*-
#
# options.py
#
# Provides a centralized storage for all options.
#
# (c) Jonne Mickelin, Jakob Florell 2008

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

SAMPLE_RATE = 44100
DFT_SIZE = 8192
FREQ_THRESHOLD = 200

##########################
#     Window settings    #
##########################
window_width = 800 #1024
window_height = 600 #786


from pyglet.window import key

#################################################
#                                               #
# Keys are specified in a number of different   #
# namespaces. For example, to set the key for   #
# bringing up the menu in-game, change the      #
# value of kb.game.menu.                        #
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
kb.menu.select = key.ENTER

######################
kb.game = AttrDict() #
######################
kb.game.menu = key.ESCAPE
kb.game.pause = key.P

######################
kb.test = AttrDict() #
######################
kb.test.exit = key.Q
kb.test.threadtest = key.S
kb.test.tabtest = key.T
kb.test.maintest = key.M
kb.test.up = key.ESCAPE

#########
# Paths #
#########
data_dir = "data" #bettrify later

#########################
# Guitar scene settings #
#########################

# The colours of the strings (rgb)
string_base_colors = [ 0x291275,  # e'
                       0x7c3408,  # h
                       0x5e0a06,  # g
                       0x1b5e06,  # d
                       0x502368,  # A
                       0x1e2e68   # E
                       ]

# Difference in colour between consequitive frets on a string
# These value are carefully set by yours truly to avoid sudden changes
# of colour and to give a generally nice result. Change them at your
# own risk. You won't die, or anything, but it's not funASDFASBEWR DEJA VU!
string_color_step = [ 0x050c08,   # e'
                      0x020703,   # h
                      0x090a02,   # g
                      0x0d0904,   # d
                      0x040a08,   # A
                      0x040a08    # E
                      ]

# Fine tune the brightness of the string_base_colors. 
# Negative value means darker color. Note that too
# high values can give entirely different colors
string_brightness = -0x010101*3

dead_note_color = (200, 200, 200)

note_label_size = 20
note_label_color = (255,255,255,200) 

# Rotation for the guitar note plane (in degrees)
notes_x_rot = 0.0#-85.0
notes_y_rot = 45.0
notes_z_rot = 0.0#-5.0
