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
    ctypedef int PaError
    PaError Pa_IsStreamActive(PaStream * stream)

cdef extern from "c_wonderful.h":
    cdef struct ring_buffer:
        complex * data
    
        unsigned int size
        unsigned int consume_index
        unsigned int write_index

    ctypedef struct inputData:
        ring_buffer * samples
        unsigned int consumed

    ring_buffer * ring_buffer_init(unsigned int size)

    int wonderful_init(inputData * data, PaStream ** stream, unsigned int sample_rate, unsigned int size) with gil
    int wonderful_terminate(inputData * data, PaStream ** stream)
    complex* wonderful_munch(inputData * data, complex * dest, unsigned int length)
    
cdef inputData _input_data
cdef PaStream * _stream 
cdef complex * _retdata
cdef int _size

cdef _init(int sample_rate, int size):
    global _input_data
    global _retdata
    global _stream
    global _size

    cdef int err

    err = Pa_IsStreamActive(_stream)
    if err == 1:
        raise Exception("wonderful is already initialized!")
    _size = size

    # Initialize the temporary container for munch. 
    # It's better to do this once and reuse it
    # Recall that the ringbuffer keeps one sample of 
    # inaccessible data between the write and consume
    # pointers
    _retdata = <complex *>malloc(_size*sizeof(complex)) # FREEME
    if _retdata == NULL:
        raise Exception("Could not allocate memory")

    # Freed by wonderful_terminate. This is a bad design decision, yes.
    _input_data.samples = ring_buffer_init(2*_size) 
    if _input_data.samples == NULL:
        raise Exception("Could not allocate memory")
    _input_data.consumed = 0

    # Starts the thread
    err = wonderful_init(&_input_data, &_stream, sample_rate, _size)

    if err != 0:
        _terminate()
        raise Exception("Could not initialize portaudio.")

def isactive():
    if Pa_IsStreamActive(_stream):
        return True
    else:
        return False

def init(sample_rate, size):
    """Initialize the wonderful library and start the sound recording. 
    This routine MUST be called before the others.

    Arguments:
    sample_rate -- sampling frequency
    size -- size of the sound buffer and resulting DFT"""

    _init(sample_rate, size)

cdef _terminate():
    global _input_data
    global _retdata
    global _stream

    cdef int err

    err = Pa_IsStreamActive(_stream)
    if err != 1:
        raise Exception("wonderful is not initialized!")
    
    free(_retdata)

    # Stops the thread
    wonderful_terminate(&_input_data, &_stream)
    _input_data.consumed = 0

def terminate():
    """Terminate and clean up the wonderful library and kill the portaudio thread. 
    This routine MUST be called before exiting the program, or the sound might
    stop working."""

    _terminate()

cdef complex_to_mag_list(complex* data, int length):
    cdef list ret_list # Bypass python attribute lookup
    cdef int i
    cdef double re
    cdef double im

    ret_list = []
    for i from 0 <= i < length:
        re = data[i].re
        im = data[i].im
        ret_list.append(sqrt(re*re + im*im)) ## Ger overflow varannan buffer.
    
    return ret_list

cdef _munch():
    global _input_data
    global _retdata
    global _stream
    global _size

    cdef complex * ret
    cdef PaError err

    err = Pa_IsStreamActive(_stream)
    if err != 1:
        raise Exception("You must call wonderful.init before calling wonderful.munch!")
    else:
        ret = wonderful_munch(&_input_data, _retdata, _size)
        if ret == NULL: # Unsuccessful to perform the DFT
            return None # Better luck next time
        else:
            ret_list = complex_to_mag_list(_retdata, _size)
            return ret_list

def munch():
    """Poll the Portaudio thread for data. If enough
    data has accumulated, return the DFT on it.
    If not, None will be returned.
    The size of the returned list is the one provided to
    wonderful.init"""

    return _munch()

