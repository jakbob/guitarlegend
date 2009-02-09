# See the discussion in the definition of DFT
#cdef extern from "Python.h":
#    object PyTuple_GET_ITEM(object p, int pos)
#    void Py_INCREF(object)

cdef extern from "math.h":
    double sqrt(double)
    double tan(double)

cdef extern from "stdlib.h":
    ctypedef int size_t
    ctypedef long intptr_t
    void * malloc(size_t size)
    void free(void * ptr)

cdef struct complex:
    double re
    double im

cdef extern complex* c_DFT "DFT" (float * data_points, int N)
cdef extern complex* c_FFT "FFT" (complex * data, int N)

cdef _DFT(object data):

    cdef complex * freqs
    cdef float * cdata
    cdef int i, N

    N = len(data)

    # Convert python list to C array of floats
    cdata = <float *>malloc(sizeof(float)*N) # FREEME
    for i from 0 <= i < N:
        # Apparently, this method is slow. One should use PyTuple_GET_ITEM and PyMem_Malloc
        # from Python.h unless you use a new version of Cython. The former gives me a 
        # segfault, though. 
        # TODO: Fix this.
        cdata[i] = data[i]

    # Perform the DFT
    freqs = c_DFT(cdata, N) # FREEME

    # Copy the data back to a Python list. I know that calculating the 
    # magnitude means extra overhead, but this is for testing purposes.
    # TODO: Fix this.
    # Update and more TODO. Apparently, filtering the magnitude messes up
    # the complex values. You need to fix this stuff right away.
    pyfreqs = []
    for i from 0 <= i < N:
        pyfreqs.append((freqs[i].re, freqs[i].im))

    # Free those little fuckers
    free(freqs)
    free(cdata)
       
    return pyfreqs

def DFT(data):
    # Use early binding for speedup in other modules
    """Perform the Discrete Fourier Transform.
    
    Arguments
    data -- iterable of the samples on which to perform the transform
    
    Returns
    freq -- list of the magnitudes of the frequencies. Yes, we need to change this."""
    
    return _DFT(data)

cdef _FFT(object data):

    cdef complex * freqs
    cdef complex * cdata
    cdef int i, N

    N = len(data)

    # Convert python list to C array of floats
    cdata = <complex *>malloc(sizeof(complex)*N) # FREEME
    for i from 0 <= i < N:
        # Apparently, this method is slow. One should use PyTuple_GET_ITEM and PyMem_Malloc
        # from Python.h unless you use a new version of Cython. The former gives me a 
        # segfault, though. 
        # TODO: Fix this.
        cdata[i].re = data[i]
        cdata[i].im = 0

    # Perform the DFT
    freqs = c_FFT(cdata, N) # FREEME

    # Copy the data back to a Python list. I know that calculating the 
    # magnitude means extra overhead, but this is for testing purposes.
    # TODO: Fix this.
    # Update and more TODO. Apparently, filtering the magnitude messes up
    # the complex values. You need to fix this stuff right away.
    pyfreqs = []
    for i from 0 <= i < N:
        pyfreqs.append((freqs[i].re, freqs[i].im))

    # Free those little fuckers
    free(freqs)
    #free(cdata)
       
    return pyfreqs

def FFT(data):
    # Use early binding for speedup in other modules
    """Perform the Fast Fourier Transform.
    
    Caveats: The function only works on data whose length is a power of 2.
    Anything else results in a core dump.

    Arguments
    data -- iterable of the samples on which to perform the transform
    
    Returns
    freq -- list of the magnitudes of the frequencies. Yes, we need to change this."""
    
    return _FFT(data)
