# -*- coding: utf-8 -*-
#
# tab.py
#
# Functions for tabs 'n' shit, yo.
#
# (c) Jakob Florell 2009

import midi

class Note:
    """Symbolises a note. Which string to play and what fret."""
    def __init__(self, pitch, string, start, stop):
        self.pitch=pitch
        self.string=string
        self.start=start
        self.stop=stop
        
        if string==1: #guitar string nr 1=high e
            base = 64 #midi number for high e
        elif string==2: #b
            base = 59
        elif string==3: #g
            base = 55
        elif string==4: #d
            base = 50
        elif string==5: #a
            base = 45
        elif string==6: #E
            base = 40
            
        self.fret=self.pitch-base
    
    def __repr__(self):
        return "<NOTE! String: " + str(self.string) + " Fret: " + str(self.fret) + " Start: " + str(self.start) + " Stop: " + str(self.stop) + ">"

class Tab:
    """Opens up a midifile and converts all midi events into Notes"""
    def __init__(self, midifile):
        f=midi.MidiFile()
        f.open(midifile)
        f.read()
        f.close()

        self.ticksPerSec = f.ticksPerSecond
        self.ticksPerQuarter = f.ticksPerQuarterNote
        self.string=[[],[],[],[],[],[],] #array to hold all notes, grouped in strings
        #for t in xrange(1,7):
        for track in f.tracks:
            startevent=None
            #try: #litesmahackigt. menmen
                #f.tracks[i]
            #except IndexError:
                #break
            for event in track.events:
                if event.channel<1 or event.channel>6 or event.velocity==0: #most of these events shuoldn't be in the file, but if they are, skip them.
                    continue #else
                if not startevent:
                    if event.type=="NOTE_ON":
                        startevent=event
                else:#when the corresponding NOTE_OFF event shows up, make the note
                    if (event.type=="NOTE_OFF" and startevent.pitch==event.pitch)\
                    or event.type=="NOTE_ON": #or if we get a new note on message before. This isn't supposed to happen so I implemented this as a sequrity messure.
                        self.string[event.channel-1].append(Note(startevent.pitch, startevent.channel, startevent.time, event.time))
                        startevent=None
                    if event.type=="NOTE_ON": #If we got a new NOTE_ON before the NOTE_OFF stop the old note and start a new
                        startevent=event

