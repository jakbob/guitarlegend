# -*- coding: utf-8 -*-
import pyglet
from pyglet.window import key
from pyglet.gl import *
import os
import re
import math

import scene
import options
from manager import game_manager

def parse_info(info_path):
    """Parse an information file and return name of song and artist"""
    f = open(info_path, "r")
    song = artist = ""
    for line in f:
        keyword = line.split()[0].strip(":").lower()
        information = "".join(line.split()[1:])
        if keyword == "song" or keyword == "name":
            song = information
        elif keyword == "artist":
            artist = information
    return song, artist

class MenuItem:
    """Base class for menu objects."""

    def __init__(self, cb):
        """Initiate the menu object.

        Arguments:
        cb -- callback function. This is what is called when the user
              activates the menu item.
        """
        self.cb = cb

    #def draw(self):
        #"""Draw the menu object to the screen."""
        #pass

    def highlight(self):
        """Switch to the active state of the menu object. What this means
        depends on the exact type of the object. This should _not_ call the 
        callback function, unless the callback function manipulates the menu
        itself.
        """
        pass

    def lowlight(self):
        """Switch to the inactive state of the menu object. What this means
        depends on the exact type of the object. This should _not_ call the 
        callback function, unless the callback function manipulates the menu
        itself.
        """
        pass

    def select(self):
        """Call the callback function of the menu object."""
        self.cb()


class TextMenuItem(MenuItem, pyglet.text.Label):
    def __init__(self, cb, x, y, caption, batch, size=25, 
                 hicolor=(255, 255, 0, 255), locolor=(255, 255, 255, 255),
                 **kwargs):
        self.hicolor = hicolor
        self.locolor = locolor
        pyglet.text.Label.__init__(self, caption, x=x, y=y, batch=batch, 
                                   color=self.locolor, font_size=size, 
                                   anchor_y="top", anchor_x="center", 
                                   font_name="Arial", **kwargs)
        MenuItem.__init__(self, cb)
    
    def highlight(self):
        self.color = self.hicolor

    def lowlight(self):
        self.color = self.locolor

class SpriteMenuItem(MenuItem, pyglet.sprite.Sprite):
    def __init__(self, cb, x, y, image, batch, **kwargs):
        pyglet.sprite.Sprite.__init__(self, image, x, y, batch=batch, **kwargs)
        MenuItem.__init__(self, cb)

        self.lowlight()
        
    def highlight(self):
        self.opacity = 255

    def lowlight(self):
        self.opacity = 128

class MenuItemGroup(MenuItem, pyglet.graphics.Group):
    #arvet är inte helt snyggt, men vafan. Det borde va det bästa sättet
    def __init__(self, cb, x, y, z, members):
        pyglet.graphics.Group.__init__(self)
        MenuItem.__init__(self, cb)
        self.members = members
        for member in self.members:
            try:
                #workaround för labels, hitta gärna nåt snyggare sätt
                member._init_groups(self) #riktigt hackigt
            except AttributeError:
                member.group = self
        self.x = x
        self.y = y
        self.z = z
        self.yrot = 0

    def set_state(self):
        glPushMatrix()
        glEnable(GL_DEPTH_TEST)
        glLoadIdentity()
        glTranslatef(self.x, self.y, self.z)
        glTranslatef(self.members[0].image.width/2, 0, 0) # Do not rotate around x=0
        glRotatef(self.yrot, 0, 1, 0)
        glTranslatef(-self.members[0].image.width/2, 0, 0)


    def unset_state(self):
        glDisable(GL_DEPTH_TEST)
        glPopMatrix()

    def highlight(self):
        for member in self.members:
            member.highlight()

    def lowlight(self):
        for member in self.members:
            member.lowlight()
    
class VertexMenuItem(MenuItem):
    def __init__(self, cb, vertices):
        self.vertex_list = pyglet.graphics.vertex_list(len(vertices), "v2f", "c4B")
        self.vertex_list.colors = (255, 255, 0, 0) * len(vertices)
        print len(vertices)
        for i in range(len(vertices)):
            print i
            self._add_nth_vertex(i, vertices[i])

    def _add_nth_vertex(self, n, vertex):
        print vertex
        self.vertex_list.vertices[2*n : 2*n + 2] = vertex

    def draw(self):
        self.vertex_list.draw(pyglet.graphics.GL_LINE_LOOP)
        
class BaseMenu(scene.Scene):
    def __init__(self, bgimage=None):
        self.name = "Menu"

        self.bgimage = bgimage
        self.items = []
        self.selected = None
        self.batch = pyglet.graphics.Batch() #to be implemented

    def game_draw(self, window):
        """Draw the contents of the menu to the screen."""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glLoadIdentity()
        
        if self.bgimage:
            glTranslatef(0, 0, 1.0)
            self.bgimage.blit(0,0)
        self.batch.draw()

        glPopMatrix()

    def _select(self, number):
        """Select the menu item given by the index number.

        Arguments:
        number -- index of the menu item.

        Returns the item that was selected or None if the index is out of range."""

        #if self.selected is not None and not (0 <= number < len(self.items)):
        #    return
        if self.items:
            number %= len(self.items)

        if self.selected is not None:
            self.items[self.selected].lowlight()
        self.items[number].highlight()
        self.selected = number

        return self.items[number]

    def next(self):
        """Select the next menu item.
        Returns the index of the selected item."""

        self._select(self.selected + 1)
        return self.selected

    def prev(self):
        """Select the previous menu item.
        Returns the index of the selected item."""
        self._select(self.selected - 1)
        return self.selected

    def append(self, menu_item):
        """Append a menu item to the end of the menu.
        Returns the menu itself. This can be used for appending multiple objects
        at the same time."""
        self.items.append(menu_item)
        return self

    def on_key_press(self, window, symbol, modifiers):
        """Catches keyboard events.
        Returns True if the symbol was handled or False otherwise."""
        if symbol == options.kb.menu.up:
            self.prev()
        elif symbol == options.kb.menu.down:
            self.next()
        elif symbol == options.kb.test.up:
            game_manager.pop()
        elif symbol == options.kb.menu.select:
            self.items[self.selected].select()

class MainMenu(BaseMenu):
    def __init__(self):
        bg = pyglet.resource.image("menubg.png")
        
        BaseMenu.__init__(self, bg)
        
        #add menuitems
        run_game = lambda: game_manager.push(SongSelect())
        self.items.append(TextMenuItem(run_game, options.window_width/2,
                                       options.window_height, "Song Select", self.batch))
        self.items.append(TextMenuItem(game_manager.pop, 
                                       options.window_width/2, options.window_height - 50,
                                       u"Exit", self.batch))

        #required
        self._select(0)

class SongSelect(BaseMenu):
    def __init__(self):
        BaseMenu.__init__(self)
        for name in os.listdir("songs"): #hackigt ("songs"), förbättra nån gång
            path = os.path.join("songs", name)
            if os.path.isdir(path): #now we're talking!!
                data = {}
                
                for fil in os.listdir(path):
                    attr = None
                    
                    if re.search("\.(mp3|ogg)$", fil): #ska sättas i options
                        attr = "sound"
                    elif re.search("\.(mid|midi)$", fil):
                        attr = "midi"
                    elif re.search("\.(jpg|png|bmp)$", fil):
                        attr = "image"
                    elif fil == "info.txt":
                        attr = "info"
                        
                    data[attr] = os.path.join(path, fil)
                    
                if data.has_key("sound") and data.has_key("midi") \
                        and data.has_key("info"):

                    if not data.has_key("image"):
                        img = defaultimage
                    else:
                        img = pyglet.image.load(data["image"])

                    picture = SpriteMenuItem(None, 0, -img.height/2, 
                                             img, self.batch)
                    
                    songname, artist = parse_info(data["info"]) #kan förbättras
                    songtext = TextMenuItem(None, img.width/2, 0, songname, self.batch)
                    artisttext = TextMenuItem(None, img.width/2, 
                       -songtext.content_height - 5, artist, self.batch)

                    select_song = lambda d: lambda: game_manager.push(scene.GameScene(d["sound"], 
                                                                                      d["midi"]))
                    item = MenuItemGroup(select_song(data), 0, 0, 0, 
                                         (picture, songtext, artisttext)) 
                    self.items.append(item)
                else:
                    pass #hoppa över blir nog lättast

        self._select(0)

        #glClearColor(0x4b/255.0, 0x4b/255.0, 0x4b/255.0, 0)
            
        glClearDepth(1.0)               # Prepare for 3d. Actually, this might as well 
                                        # be in on_resize, no? Or maybe not. I don't know.

        glDepthFunc(GL_LEQUAL)          # Change the z-priority or whatever one should call it

        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)

    def on_resize(self, width, height):
        # Perspective
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / float(height), 0, 10000)
        glMatrixMode(GL_MODELVIEW)

    def _select(self, number):
        #BaseMenu._select(self, number)

        
        if self.items:
            number %= len(self.items)
        if self.selected is not None:
            self.items[self.selected].lowlight()
        print number
        self.items[number].highlight()
        self.selected = number

        r = 500 #sum([item.members[0].width for item in self.items])/(2*math.pi)
        x_offset = options.window_width/2 - r# inte options!
        z_offset = -(2000 - r)
        for n in xrange(len(self.items)):
            i = (n - (len(self.items) - self.selected))
            v = 3 * math.pi / 2 + i * 2 * math.pi / len(self.items)
            self.items[n].x = r * math.cos(v) + x_offset
            #self.items[n].y = 0
            self.items[n].z = -r * math.sin(v) + z_offset
            self.items[n].yrot = (270 - v * 180 / math.pi)

        return self.items[number]

    def on_key_press(self, window, symbol, modifiers):
        """Catches keyboard events.
        Returns True if the symbol was handled or False otherwise."""
        if symbol == options.kb.menu.left:
            self.next()
        elif symbol == options.kb.menu.right:
            self.prev()
        elif symbol == options.kb.test.up:
            game_manager.pop()
        elif symbol == options.kb.menu.select:
            self.items[self.selected].select()
