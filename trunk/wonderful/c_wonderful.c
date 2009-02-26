/* wonderful.c
 *
 * The magic gears of wonderful things. This 
 * module utilizes portaudio to (nonblockingly)
 * fill a buffer and provides functions for 
 * querying for data. These functions perform 
 * an FFT before the data is returned.
 * The module needs to be initialized by calling
 * wonderful_init and terminated by calling 
 * wonderful_terminate.
 *
 * The code for the ringbuffer consume and write was inspired by
 * the Audacity source code (audacity.sourceforge.net), 
 * so creds to one Dominic Mazzoni wbo wrote the original.
 *
 * The other code is (c) Jonne Mickelin 2009
 */

#include <stdio.h>
#include <stdlib.h>

#include <portaudio.h>

#include "dft.h"

#define SAMPLES (1024)

struct ring_buffer
{
  complex * data;
  
  unsigned int size;            /* Thread safe on x86 and x86-64 machines  */
  unsigned int consume_index;   /* because lookup and reading of ints is   */
  unsigned int write_index;     /* atomic. long (*NIX, etc.) and long long */
                                /* (MS Windows) is not atomic, so using it */
                                /* would be a bad idea. Correct me if I'm  */
                                /* wrong. */
};

typedef struct
{
  struct ring_buffer * samples;

} inputData;

/********************************************
 * Functions for controlling the ringbuffer *
 ********************************************/

struct ring_buffer *
ring_buffer_init(unsigned int size)
{
  struct ring_buffer * rb;
  
  rb = (struct ring_buffer *) malloc(sizeof(struct ring_buffer));
  rb->data = (complex *) malloc(sizeof(complex) * size);
  rb->size = size;
  rb->consume_index = 0;
  rb->write_index = 1;

  return rb;
}

unsigned int
ring_buffer_free_space(struct ring_buffer * rb)
{
  return (int)(rb->consume_index + rb->size - rb->write_index) % rb->size;
}

int
ring_buffer_write(struct ring_buffer * rb, const float * src, unsigned int lendata)
{
  int i;
  int block;
  int free_space = ring_buffer_free_space(rb);
  int written;
  
  if (lendata > free_space)
    {
      lendata = free_space;
    }
  written = lendata;
  
  while (lendata)
    {
      block = lendata;
      if (block > rb->size - rb->write_index)
	{
	  block = rb->size - rb->write_index;
	}

      for (i = 0; i < block; i++)
	{
	  rb->data[rb->write_index + i].re = src[i];
	  rb->data[rb->write_index + i].im = 0.0;
	}

      rb->write_index = rb->write_index + block;

      if (rb->write_index == rb->size)
	{
	  rb->write_index = 0;
	}
      lendata -= block;
    }  
  return written;
}

int
ring_buffer_consume(struct ring_buffer * rb, complex * dest, unsigned int lendata)
{
  int i;
  int block;
  int free_space = ring_buffer_free_space(rb);
  int length = (rb->write_index + rb->size - rb->consume_index - 1) % rb->size;
  int consumed;
  
  if (lendata > length)
    {
      lendata = length;
    }
  consumed = lendata;
  
  while (lendata)
    {
      block = lendata;
      if (block > rb->size - rb->consume_index)
	{
	  block = rb->size - rb->consume_index;
	}

      for (i = 1; i <= block; i++)
	{
	  dest[i] = rb->data[rb->consume_index + i];
	}

      rb->consume_index = rb->consume_index + block;

      if (rb->consume_index == rb->size)
	{
	  rb->consume_index = 0;
	}
      lendata -= block;
    }  
  return consumed;
}

/**
 * Get sound input from portaudio.
 */
static int 
input_callback( const void * input, 
		void * output,
		unsigned long frames_per_buffer,
		const PaStreamCallbackTimeInfo * timeInfo,
		PaStreamCallbackFlags statusFlags,
		void * userData )
{
  inputData * data = (inputData*) userData;
  const float * in = (const float*) input;
  struct ring_buffer * out = data->samples;
  unsigned int len = frames_per_buffer;
  int written;

  // Just copy the stuffs! I hope this is enough to make it work. 
  // Oh, and if frames_per_buffer is more than is available, we
  // will start dropping frames, which is doubleplusungood.
  written = ring_buffer_write(out, in, frames_per_buffer);
  //printf("Dropped %i frames!\n", frames_per_buffer - written);

  return paContinue;
}

/**
 * Initialize the wonderful module
 */
int
wonderful_init(inputData * data, PaStream * stream)
{
  PaStreamParameters input_parameters;
  PaError err;

  /* Initialize portaudio */
  printf("Initializing\n"); fflush(stdout);
  err = Pa_Initialize();
  if (err != paNoError)
    {
      printf("Portaudio error: %s\n", Pa_GetErrorText(err));
      return 1;
    }

  /* Define the format of the returned sound.
   * Default is from the default microphone, mono, and 
   * as a floating number between -1.0 and 1.0.
   * The sampling frequency is 44100 and the number of 
   * samples to process each time is 256. Note that the last
   * value is not necessarily the size of what we send to 
   * the FFT.
   */
  printf("Setting input params\n"); fflush(stdout);
  input_parameters.device = Pa_GetDefaultInputDevice();
  input_parameters.channelCount = 1;
  input_parameters.sampleFormat = paFloat32;
  input_parameters.suggestedLatency = Pa_GetDeviceInfo(input_parameters.device)->defaultLowInputLatency;
  input_parameters.hostApiSpecificStreamInfo = NULL;
  
  printf("Opening stream\n"); fflush(stdout);
  err = Pa_OpenStream( &stream,
		       &input_parameters,
		       NULL,              // Output parameters
		       44100,             // sample rate
		       256,               // frames per buffer
		       paClipOff,         //special flags
		       input_callback,
		       data);
  if (err != paNoError)
    {
      printf("Portaudio error: %s\n", Pa_GetErrorText(err));
      return 1;
    }
  
  /* The callback function now runs in its own thread */
  printf("Starting stream\n"); fflush(stdout);
  err = Pa_StartStream(stream);
  if (err != paNoError)
    {
      printf("Portaudio error: %s\n", Pa_GetErrorText(err));
      return 1;
    }
  printf("Returning\n"); fflush(stdout);
  return 0;
}

/**
 * Terminate the module and clear up the data
 */
int
wonderful_terminate(inputData * data, PaStream * stream)
{
  PaError err;
  err = Pa_Terminate();
  if (err != paNoError)
    {
      printf("Portaudio error: %s\n", Pa_GetErrorText(err));
      return 1;
    }
  free(stream);
  /* Yes, ring_buffer_terminate. I don't want to write such a function */
  free(data->samples->data);
  free(data->samples);
  free(data);
  
  return 0;
}

#ifdef DEBUG
int
main()
{
  PaStream * stream;
  inputData data;
  
  complex * consumed = (complex *)malloc(2*sizeof(complex)*SAMPLES);
  int i,j;
  int lenconsumed;
  int err;
  int numspaces = 0;
  
  /* Set up the struct that we send to the callback function */
  data.samples = ring_buffer_init(2*SAMPLES);     // FREE ME
  if (data.samples == NULL)
    {
      printf("Could not allocate memory for complex input samples!\n");
      return 1;
    }
  err = wonderful_init(&data, stream);
  if (err != 0)
    {
      printf("An error occurred. Could not initialize portaudio\n");
    }
  
  //FFT(data.samples, SAMPLES);
  while (1)
    {
      lenconsumed = ring_buffer_consume(data.samples, consumed, 2*SAMPLES);
      //printf("Consumed %i frames\n", lenconsumed);
      for (i = 0; i < lenconsumed; i++)
	{
	  numspaces = fabs(consumed[i].re)*10;
	  for (j = 0; j < numspaces; j++)
	    {
	      printf(" ");
	    }
	  printf("|\n");
	}
    }
  
  err = wonderful_terminate(&data, stream);

  return 0;
}
#endif
