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

cdef extern from "portaudio.h":
    ctypedef struct PaStream

cdef extern from "wonderful.h":
    cdef struct ring_buffer:
        complex * data
    
        unsigned int size
        unsigned int consume_index
        unsigned int write_index

    ctypedef struct inputData:
        ring_buffer * samples

    int wonderful_init(inputData * data, PaStream * stream)
    int wonderful_terminate(inputData * data, PaStream * stream)
