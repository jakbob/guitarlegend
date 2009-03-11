import wonderful
import heapq
import time
import math

SAMPLE_RATE = 8000#44100
N = 2048
wonderful.init(SAMPLE_RATE, N)

THRESHOLD_K = 1600
MAG_THRESHOLD = float(N)/THRESHOLD_K # N samples, each between -1.0 and 1.0. The freqs[0] is the sum of all samples.
lasttime = time.clock()

lowest_hearable = int(20 * N/float(SAMPLE_RATE))

def midify(f):                       
    """                              
    Returns the midi keycode for given frequency.
    Could probably be more optimized but this will have to do
    for now.
    """
    n = round(69.0 + 12.0 * math.log(f / 440.0, 2))
    return int(n)

#index_to_midi = {}
#for num in xrange(N):
#    index_to_midi[num] = midify(num*float(SAMPLE_RATE)/N)

def uniq(iterable):
    rets = {}
    for (num, amp) in iterable:
        try:
            p = midify(num * float(SAMPLE_RATE)/N)
            if p < 0:
                raise OverflowError("Bajs")
        except OverflowError:
            continue

        if p in rets:
            if rets[p] < amp:
                rets[p] = amp
        else:
            rets[p] = amp
    return rets

def get_note_numbers(mag_list):
    if mag_list is not None:
        note_numbers = uniq(enumerate(mag_list))
        return [p for p in get_largest(note_numbers) if note_numbers[p] > MAG_THRESHOLD]
    else:
        return None

def get_largest(l):
    largest = heapq.nlargest(6, l, key=(lambda key: l[key]))
    return largest

#[((p+lowest_hearable)*float(SAMPLE_RATE)/N), mag) for (p, mag) in largest if mag > MAG_THRESHOLD]

def get_sound():
    mag_list = wonderful.munch()
    return get_note_numbers(mag_list)

try:
    while True:
        t = time.clock()
        s = get_sound()
        if s is not None:
            print s, " in %lf seconds", t-lasttime
        lasttime = t

except KeyboardInterrupt:
    pass

wonderful.terminate()
