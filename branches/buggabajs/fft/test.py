import math
import pydft

N = 128

a = []
for i in range(N):
    a.append(math.sin(2*math.pi*i/N))

# Time the function by running it over 9000 times.
#import timeit
#t = timeit.Timer("b = pydft.DFT(a)", "from __main__ import pydft, a").timeit(1)
#print t

# Get the DFT and print it
b = pydft.DFT(a)
#print b

# Or plot it
from pylab import bar, show, subplot
subplot(211)
# Making it sexy. It's just a test plot anyway.
kwargs = { "color": "r", 
           "align": "center", 
           "edgecolor" :"w", 
           "width": 1, 
           "alpha": 0.5,
           }
bar(range(N), a, **kwargs)
subplot(212)
bar(range(N), b, **kwargs)
show()
