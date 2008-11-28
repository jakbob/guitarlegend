cdef extern from "stdlib.h":
    ctypedef int size_t
    ctypedef long intptr_t
    void * malloc(size_t size)
    void free(void * ptr)

cdef struct complex:
    double re
    double im

cdef extern complex* c_DFT "DFT" (float * data_points, int N)

def DFT(data):
    cdef complex * freqs
    cdef float * cdata
    cdef int i, N

    N = len(data)
    
    # Convert python list to C array of floats
    cdata = <float *>malloc(sizeof(float)*N)
    for i from 0 <= i < N:
        cdata[i] = data[i]
        
    # Perform the DFT
    freqs = c_DFT(cdata, N)

    # Copy the data back to a Python list
    pyfreqs = []
    for i from 0 <= i < N:
        pyfreqs.append(freqs[i].re + freqs[i].im)

    free(freqs)
    free(cdata)
       
    return pyfreqs
