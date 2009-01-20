#coding:utf8
#tab.py

import midi

class Note:
  def __init__(self, pitch, string, start, stop):
        print string

        self.pitch=pitch
        self.string=string
        self.start=start
        self.stop=stop
        
        if string==1:
            base = 64
        elif string==2:
            base = 59
        elif string==3:
            base = 55
        elif string==4:
            base = 50
        elif string==5:
            base = 45
        elif string==6:
            base = 40
        else:
            print "fräs"
        self.fret=self.pitch-base
    
  def __repr__(self):
      return "<NOTE! String: " + str(self.string+1) + " Fret: " + str(self.fret) + " Start: " + str(self.start) + " Stop: " + str(self.stop) + ">"

class Tab:
    def __init__(self, midifile):
        f=midi.MidiFile()
        f.open(midifile)
        f.read()
        f.close()
        
        self.string=[[],[],[],[],[],[],]
        #for t in xrange(1,7):
        for track in f.tracks:
            startevent=None
            #try: #litesmahackigt. menmen
                #f.tracks[i]
            #except IndexError:
                #break
            for event in track.events:
                if event.channel>6 or event.velocity==0: #
                  continue #else
                if not startevent:
                    if event.type=="NOTE_ON":
                        startevent=event
                else:
                    if (event.type=="NOTE_OFF" and startevent.pitch==event.pitch)\
                    or event.type=="NOTE_ON":
                        self.string[event.channel-1].append(Note(startevent.pitch, startevent.channel, startevent.time, event.time))
                        startevent=None
                    if event.type=="NOTE_ON":
                        startevent=event
                        
                    
                