# -*- coding: utf-8 -*-
# Bajs

import multiprocessing
import time

import scene

class TestProcess(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.quit = False

    def run(self):
        while not self.quit:
            print "Hej"
            time.sleep(0.1)

class ThreadedScene(scene.TestScene):
    def __init__(self):
        scene.Scene.__init__(self)
        self.otherprocess = TestProcess()
        self.otherprocess.start()
        print "okej"

    def end(self):
        self.otherprocess.quit = True

    def do_logic(self, dt):
        print "hå"
