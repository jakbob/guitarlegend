cdef struct complex:
    float im
    float re

cdef extern complex* c_DFT(float * data_points, int N)

def hej(data):
    complex * a
    #a = c_DFT(<float*>data, len(data))
    return "o"
