import math
import pydft

N = 128

data = []
for i in range(N):
    data.append(math.sin(2*math.pi*i/N))

# Time the function by running it over 9000 times.
# import timeit
# repeats = 9001
# t1 = timeit.Timer("b = pydft.DFT(a)", "from __main__ import pydft, a").timeit(repeats)
# t2 = timeit.Timer("b = pydft.FFT(a)", "from __main__ import pydft, a").timeit(repeats)
# print repeats, "DFT:s ran in", t1, "seconds. Mean execution time:", t1/repeats
# print repeats, "FFT:s ran in", t2, "seconds. Mean execution time:", t2/repeats
# print "Increased speed by a factor of", t1/t2, "with N=" + str(N)

#Perform the fft and print it
freqs = pydft.FFT(data)
mags = [math.sqrt(a**2 + b**2) for a,b in freqs]
angles = [math.tan(b/a) for a,b in freqs]
#print b

# Or plot it
from pylab import bar, show, subplot, plot
# Making it sexy. It's just a test plot anyway.
kwargs = { "color": "r", 
           "align": "center", 
           "edgecolor" :"w", 
           "width": 1, 
           "alpha": 0.5,
           }
subplot(311)
bar(range(N), data, **kwargs)
subplot(312)
bar(range(N), mags, **kwargs)
subplot(313)
bar(range(N), angles, **kwargs)
show()
