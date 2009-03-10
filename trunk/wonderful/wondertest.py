import wonderful
import heapq
import time

SAMPLE_RATE = 8000#44100
N = 2048
wonderful.init(SAMPLE_RATE, N)

THRESHOLD_K = 1600
MAG_THRESHOLD = float(N)/THRESHOLD_K # N samples, each between -1.0 and 1.0. The freqs[0] is the sum of all samples.
lasttime = time.clock()

lowest_hearable = int(20 * N/float(SAMPLE_RATE))

try:
    while True:
        freqs = wonderful.munch()
        if freqs is not None:
            largest = heapq.nlargest(6, enumerate(freqs[lowest_hearable:N/2]), key=(lambda (num, amp): amp))
            t = time.clock()
            print " ".join(["(%.3f,%.5f)" % (((p+lowest_hearable)*float(SAMPLE_RATE)/N), mag) for (p, mag) in largest if mag > MAG_THRESHOLD]),
            print " Idle time:", t-lasttime
            lasttime = t
            #print " ".join(["%.3f" % mag for (p, mag) in largest])
except KeyboardInterrupt:
    pass

wonderful.terminate()
