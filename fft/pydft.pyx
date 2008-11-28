cdef struct complex:
    float im
    float re

cdef extern complex* DFT(float * data_points, int N)

def hej(data):
    cdef complex * a
    a = DFT(<float*>data, len(data))
    return a[3].im
