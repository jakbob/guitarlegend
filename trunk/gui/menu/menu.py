# -*- coding: utf-8 -*-
import pyglet
from pyglet.window import key

window = pyglet.window.Window()

env = { "kb" : { "menu" : { "up" : key.UP,
                            "down" : key.DOWN,
                            },          
                 },
        }

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

class Borg:
    _shared_state = {"items": [], "selected" : -1}
    def __init__(self):
        self.__dict__ = self._shared_state
        
class Menu(Borg):
    def __init__(self):
        Borg.__init__(self)

        self._shared_state.setdefault("items", [])
        self._shared_state.setdefault("selected", -1)

    def draw(self):
        """Draw the contents of the menu to the screen."""
        for item in self.items:
            item.draw()

    def select(self, number):
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

        self.select(self.selected + 1)
        return self.selected

    def prev(self):
        """Select the previous menu item.
        Returns the index of the selected item."""
        self.select(self.selected - 1)
        return self.selected

    def append(self, menu_item):
        """Append a menu item to the end of the menu.
        Returns the menu itself. This can be used for appending multiple objects
        at the same time."""
        self.items.append(menu_item)
        return self

    def on_key_press(self, symbol, modifiers):
        """Catches keyboard events.
        Returns True if the symbol was handled or False otherwise."""
        if symbol == key.UP:
            self.prev()
        elif symbol == key.DOWN:
            self.next()
        else:
            return False
        return True
        
@window.event
def on_draw():
    window.clear()
    current_menu = Menu()
    current_menu.draw()

@window.event
def on_key_press(symbol, modifiers):
    current_menu = Menu()
    current_menu.on_key_press(symbol, modifiers)

current_menu = Menu()

entry1 = TextMenuItem(None, 0, window.height, "Hej")
entry2 = TextMenuItem(None, 0, window.height - 50, u"Hå")
entry_on_the_side = TextMenuItem(None, 588, window.height-50, u"Här!")

current_menu.append(entry1)
current_menu.append(entry2)
current_menu.append(entry_on_the_side)
current_menu.select(0)

pyglet.app.run()
