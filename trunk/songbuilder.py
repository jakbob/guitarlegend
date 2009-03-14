import getopt
import sys

import midi

#constants
keycodes = {1 : 64, #midi keycodes
   2 : 59,
   3 : 55,
   4 : 50,
   5 : 45,
   6 : 40,
   -1 : -1,} #flag for deletition

def rearange(infile, outfile):
    #read infile
    mid = midi.MidiFile()
    mid.open(infile)
    mid.read()
    mid.close()

    #rearange notes
    for track in mid.tracks:
        for event in track.events:
            if event.type == "SEQUENCE_TRACK_NAME":
                event.data = str(event.channel)
            if hasattr(event, "pitch"):
                for string, code in keycodes.iteritems():
                    if event.pitch >= code:
                        if code == -1:
                            del event #perhaps it helps...
                        else:
                            event.channel = string
                            event.track = string
                        break
                #if event.channel == -1:
                #    track.events.remove(event)

    #write new file
    mid.open(outfile, "wb")
    mid.write()
    mid.close()

if __name__ == "__main__":
    infile = outfile = None

    optlist, args = getopt.getopt(sys.argv[1:], "i:o:")
    for flag, value in optlist:
        if flag == "-i":
            infile = value
        elif flag == "-o":
            outfile = value
    if not (infile and outfile):
        raise "Must specifile infile (-i) and outfile (-o)"
    rearange(infile, outfile)