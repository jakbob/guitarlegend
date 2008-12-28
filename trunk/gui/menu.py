import pygame

def test_fun():
    print "test_fun called!"

menu = { "Menu1" : ("Header 1", { "Menu item 1" : None,
                                  "Menu item 2" : test_fun,
                                  }),
         "Menu2" : ("Header 2", { "Menu 2 item 1" : None,
                                  "Menu 2 item 2" : None,
                                  }),
         }

class MenuItem:
    def __init__(self, name, children=[]):
        self.children = children
        self.name = name
    def call(self, num):
        self.children[num].function()
    def draw(self, surface):
        for child in self.children:
            "+--%s" % child
    @staticmethod
    def _draw(label, surface):
        print "bajs"

def init():
    pygame.init()
    return pygame.display.set_mode((1024, 786))

def main():
    
    screen = init()

    main_menu = MenuItem("Main", ["Hej", "Hoe", "Moe"])
    main_menu.draw(screen)

if __name__ == "__main__":
    main()
