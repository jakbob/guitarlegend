# -*- coding: utf-8 -*-
#
# tab.py
#
# Functions for tabs 'n' shit, yo.
#
# (c) Jakob Florell 2009

import struct

import midi

class Note:
    """Symbolises a note. Which string to play and what fret.""" 

    def __init__(self, pitch, string, start, stop):
        self.pitch = pitch
        self.string = string
        self.start = start
        self.stop = stop
        
        if string == 1:   #guitar string nr 1=high e
            base = 64     #midi number for high e
        elif string == 2: #b
            base = 59
        elif string == 3: #g
            base = 55
        elif string == 4: #d
            base = 50
        elif string == 5: #a
            base = 45
        elif string == 6: #E
            base = 40
            
        self.fret = self.pitch - base
    
    def __repr__(self):
        return "<NOTE! String: " + str(self.string) \
            + " Fret: " + str(self.fret)\
            + " Start: " + str(self.start)\
            + " Stop: " + str(self.stop) + ">"
    
    def __cmp__(self, other):
        return cmp(self.start, other.start)


class Tab:
    """Opens up a midifile and converts all midi events into Notes"""
    def __init__(self, midifile):
        f = midi.MidiFile()
        f.open(midifile)
        f.read()
        f.close()

        self.ticksPerSec = f.ticksPerSecond
        self.ticksPerQuarter = f.ticksPerQuarterNote

        #self.string=[[],[],[],[],[],[],] #array to hold all notes, grouped in strings
        self.all_notes = [] # List of all the notes. Should be sorted by time.
        self.tempo = []     # List of tempo changes

        # Go through all the tracks (== strings for the purposes of the game)
        for track in f.tracks:
            startevent = None

            # Go through all the events in this track and collect all the interesting ones
            for event in track.events:

                # First, check the tempo:
                if event.type == "SET_TEMPO":
                    t = (event.time, struct.unpack('>I','\x00'+event.data)[0])
                    self.tempo.append(t)
                    #datan finns i 24bit binary, \x00 är ett hack som fungerar bra

                elif event.channel < 1 or event.channel > 6 or event.velocity == 0: 
                    # Most of these events shuoldn't be in the file, but if they are, skip them.
                    pass

                elif not startevent:

                    if event.type == "NOTE_ON":
                        startevent = event

                else:# When the corresponding NOTE_OFF event shows up, make the note
                    if (event.type == "NOTE_OFF" and startevent.pitch == event.pitch)\
                            or event.type == "NOTE_ON": 
                        # or if we get a new note on message before. 
                        # This isn't supposed to happen so I implemented 
                        # this as a sequrity messure.
                        
                        if not startevent.time == event.time:
                          #removes problems when 2 notes play simultaniously
                            note = Note(startevent.pitch, startevent.channel, startevent.time, event.time)
                            #self.string[event.channel-1].append(note)
                            self.all_notes.append(note)
                        startevent = None

                    if event.type == "NOTE_ON": 
                        # If we got a new NOTE_ON before the NOTE_OFF 
                        # stop the old note and start a new
                        startevent = event

            self.all_notes.sort()
