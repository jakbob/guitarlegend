#!/usr/bin/env python
# Disect the wav data and plot it using pylab.

import pylab
import wave # Contains reference to struct. No point in importing it twice

FORMAT = { "11" : "1b",  # Mono, 8-bit sound
           "12" : "1h",  # Mono, 16-bit sound
           "21" : "2b",  # Stereo, 8-bit sound
           "22" : "2h",  # Stereo, 16-bit sound
           }
WAVE_INPUT_FILE = "output.wav"

wf = wave.open(WAVE_INPUT_FILE, "rb")

params = wf.getparams()

# < == little endian
fmt = "<" + FORMAT[str(params[0]) + # nchannels
                   str(params[1])]  # sampwidth

wavdata = wf.readframes(params[3]) # params[3] is nframes; Of course, don't attempt this with a large file
wf.close()

# Time to unpack
python_data = []
for i in range(0, params[3]): 
    size = wave.struct.calcsize(fmt)
    data = wave.struct.unpack(fmt, wavdata[i:i+size]) # Little endian

    python_data.append(data[0]) # The above function returns 1-tuples

assert(len(wavdata) == params[0]*params[1]*len(python_data))

x = pylab.arange(0, float(params[3])/params[2], 1/float(params[2]))
pylab.xlabel("time (s)")

pylab.plot(x, python_data)
pylab.show()
