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

cdef extern from "c_wonderful.h":
    cdef struct ring_buffer:
        complex * data
    
        unsigned int size
        unsigned int consume_index
        unsigned int write_index

    ctypedef struct inputData:
        ring_buffer * samples
    
    ring_buffer * ring_buffer_init(unsigned int size)
    int wonderful_init(inputData * data, PaStream ** stream) with gil
    int wonderful_terminate(inputData * data, PaStream ** stream)
    int wonderful_munch(inputData * data, complex * dest, unsigned int length)
    
cdef inputData _input_data
cdef PaStream * _stream 

cdef _init():
    global _input_data
    global _stream
    cdef int err

    _input_data.samples = ring_buffer_init(1024)
    print <int>_stream
    err = wonderful_init(&_input_data, &_stream)
    if err != 0:
        print "An error occurred. I hate you"
    print <int>_stream
def init():
    """Initialize the wonderful library. This routine MUST be called before the others."""

    _init()

cdef _terminate():
    global _input_data
    global _stream
    
    wonderful_terminate(&_input_data, &_stream)

def terminate():
    """Terminate and clean up the wonderful library and kill the portaudio thread. 
    This routine MUST be called before exiting the program, or the sound might
    stop working."""

    _terminate()

cdef _munch(int size):
    global _input_data
    global _stream
    cdef complex * dest
    cdef int err
    
    err = wonderful_munch(&_input_data, dest, 1024)
    if err < 0:
        raise Exception("You must call wonderful.init before calling wonderful.munch!")
        
def munch(size):
    """Poll for data and return the FFT of it. No data will be returned unless there is 
    at least size samples available."""

    _munch(size)
