import wonderful
import heapq
import time

SAMPLE_RATE = 44100
N = 8192#16384
wonderful.init(SAMPLE_RATE, N)
wonderful.terminate()
wonderful.init(SAMPLE_RATE, N)

lasttime = time.clock()

lowest_hearable = int(20 * N/float(SAMPLE_RATE))

try:
    while True:
        freqs = wonderful.munch()
        if freqs is not None:
            largest = heapq.nlargest(6, enumerate(freqs[lowest_hearable:N/2]), key=(lambda (num, amp): amp))
            t = time.clock()
            print " ".join(["%.3f" % ((p+lowest_hearable)*float(SAMPLE_RATE)/N) for (p, mag) in largest if mag > 100]),
            print " Idle time:", t-lasttime
            lasttime = t
            #print " ".join(["%.3f" % mag for (p, mag) in largest])
except KeyboardInterrupt:
    pass

wonderful.terminate()
