# -*- coding: utf-8 -*-
import pyglet
from pyglet.window import key
try:
    from functools import partial
except ImportError:
    print "This game currently requires python >= 2.5"
    raise

import scene
import options
from manager import game_manager

#window = pyglet.window.Window()

#env = { "kb" : { "menu" : { "up" : key.UP,
                            #"down" : key.DOWN,
                            #},          
                 #},
        #}

class MenuItem:
    """Base class for menu objects."""

    def __init__(self, cb):
        """Initiate the menu object.

        Arguments:
        cb -- callback function. This is what is called when the user
              activates the menu item.
        """
        self.cb = cb

    def draw(self):
        """Draw the menu object to the screen."""
        pass

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


class TextMenuItem(MenuItem):
    def __init__(self, cb, x, y, caption):
        MenuItem.__init__(self, cb)
        self.x = x
        self.y = y
        self.caption = caption
        self.lowlight()

    def draw(self):
        self.label.draw()
    def highlight(self):
        self.label = pyglet.text.Label(self.caption, 
                                       x=self.x, 
                                       y=self.y,
                                       anchor_x="left",
                                       anchor_y="top",
                                       color=(255, 255, 0, 255))
    def lowlight(self):
        self.label = pyglet.text.Label(self.caption, 
                                       x=self.x, 
                                       y=self.y,
                                       anchor_x="left",
                                       anchor_y="top")

class VertexMenuItem(MenuItem):
    def __init__(self, cb, vertices):
        self.vertex_list = pyglet.graphics.vertex_list(len(vertices), "v2f", "c4B")
        #vertices[0], vertices[1]
        #vertices[1], vertices[2]
        #vertices[2], vertices[3]
        #vertices[3], vertices[4]
        self.vertex_list.colors = (255, 255, 0, 0) *len(vertices)
        print len(vertices)
        for i in range(len(vertices)):
            print i
            self._add_nth_vertex(i, vertices[i])
            #if i is not 0 and i is not len(vertices): self._add_nth_vertex(i + 1, vertices[i])
            #print i, i+1
    def _add_nth_vertex(self, n, vertex):
        #print 2*n, 2*n + 2
        print vertex
        self.vertex_list.vertices[2*n : 2*n + 2] = vertex
        #for num, vertex in enumerate(vertices):
        #    self.vertex_list.vertices[2*num:2*num+2] = vertex
        #    self.vertex_list.vertices[2*num+2:2*num+4] = vertex
        #for vertex in vertices:
        #    print vertex
    def draw(self):
        self.vertex_list.draw(pyglet.graphics.GL_LINE_LOOP)
        #pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ("v2f", self.vertices[0] + self.vertices[1]))

class Borg:
    _shared_state = {"items": [], "selected" : -1}
    def __init__(self):
        self.__dict__ = self._shared_state
        
class BaseMenu(scene.Scene):
    def __init__(self):
        self.name = "Menu"
        #Borg.__init__(self)

        #self._shared_state.setdefault("items", [])
        #self._shared_state.setdefault("selected", -1)
        
        self.items = []
        self.selected = 0
        self.batch = pyglet.graphics.Batch() #to be implemented

    def game_draw(self, window):
        """Draw the contents of the menu to the screen."""
        for item in self.items:
            item.draw()

    def _select(self, number):
        """Select the menu item given by the index number.

        Arguments:
        number -- index of the menu item.

        Returns the item that was selected or None if the index is out of range."""

        if self.selected is not None and not (0 <= number < len(self.items)):
            return

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

    #def append(self, menu_item):
        #"""Append a menu item to the end of the menu.
        #Returns the menu itself. This can be used for appending multiple objects
        #at the same time."""
        #self.items.append(menu_item)
        #return self

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
        #else:
            #return False
        #return True

class MainMenu(BaseMenu):
    def __init__(self):
        BaseMenu.__init__(self)
        
        run_game = partial(game_manager.push, 
           scene.GameScene("data/pokemon-melody.mid"))
        self.items.append(TextMenuItem(run_game, 0, options.window_height, 
           "Start game"))
        self.items.append(TextMenuItem(game_manager.pop, 0, 
           options.window_height - 50, u"Hå"))

        self._select(self.selected)

#if __name__ == "bajs":
    #@window.event
    #def on_draw():
        #window.clear()
        #current_menu = Menu()
        #current_menu.draw()

    #@window.event
    #def on_key_press(symbol, modifiers):
        #current_menu = Menu()
        #current_menu.on_key_press(symbol, modifiers)

    #current_menu = Menu()

    #entry1 = TextMenuItem(None, 0, window.height, "Hej")
    #entry2 = TextMenuItem(None, 0, window.height - 50, u"Hå")
    #entry_on_the_side = TextMenuItem(None, 588, window.height-50, u"Här!")

    #current_menu.append(entry1)
    #current_menu.append(entry2)
    #current_menu.append(entry_on_the_side)
    #current_menu.select(0)

    #vertex_entry = VertexMenuItem(None, ((0.0, 0.0), (window.width/2, window.height/2), (window.width, 0.0)))
    #current_menu.append(vertex_entry)

    #print dir(window)

    #pyglet.app.run()
