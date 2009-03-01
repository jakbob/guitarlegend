import wonderful
import heapq

SAMPLE_RATE = 44100
N = 16384
wonderful.init(SAMPLE_RATE, N)

try:
    while True:
        freqs = wonderful.munch()
        if freqs is not None:
            largest = heapq.nlargest(6, enumerate(freqs), key=(lambda (num, amp): amp))
            print " ".join(["%.3f" % (p*float(SAMPLE_RATE)/N) for (p, mag) in largest])
            #print " ".join(["%.3f" % mag for (p, mag) in largest])
except KeyboardInterrupt:
    pass

wonderful.terminate()
