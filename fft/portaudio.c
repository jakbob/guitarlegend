/* portaudio.c
 * 
 * Test portaudio's capabilities
 *
 * (c) Jonne Mickelin 2009
 */
#include <stdio.h>
#include <stdlib.h>

#include <portaudio.h>

#include "dft.h"

#define SAMPLES (1024)

struct ring_buffer
{
  complex * data;
  
  unsigned long size;
  unsigned long read_index;
  unsigned long write_index;
};

void
init_ring_buffer(struct string_buffer * buf, unsigned long size)
{
  buf.data = (complex *) malloc(size * sizeof(complex));
  

int number_of_free(struct ring_buffer buf)
{
  return 
  
		   

typedef struct
{
  complex * samples;
  long max_frame_index;
  long frame_index;
  
} inputData;

static int FFT_on_input( const void * input, 
			 void * output,
			 unsigned long frames_per_buffer,
			 const PaStreamCallbackTimeInfo * timeInfo,
			 PaStreamCallbackFlags statusFlags,
			 void * userData )
{
  inputData * data = (inputData*) userData;
  const float * in = (const float*) input;
  complex * out = data->samples;
  long frames_to_calc;
  long i;
  int finished;
  
  for (i = 0; i < SAMPLES; i++)
    {
      out++;
      out->re = *in++;
    }
  return 0;
}


int
main()
{
  PaStreamParameters input_parameters;
  PaStream * stream;

  PaError err;
  inputData data;
  
  int i;

  data.samples = (complex *) malloc(SAMPLES * sizeof(complex));
  data.max_frame_index = SAMPLES;
  data.frame_index = 0;
  
  if (data.samples == NULL)
    {
      printf("Could not allocate memory for complex input samples!\n");
      return 1;
    }
  printf("Hejr\n"); fflush(stdout);
  for (i = 0; i < SAMPLES; i++)
    {
      data.samples[i].re = data.samples[i].im = 0;
    }
  
  err = Pa_Initialize();
  
  input_parameters.device = Pa_GetDefaultInputDevice();
  input_parameters.channelCount = 1;
  input_parameters.sampleFormat = paFloat32;
  input_parameters.suggestedLatency = Pa_GetDeviceInfo(input_parameters.device)->defaultLowInputLatency;
  input_parameters.hostApiSpecificStreamInfo = NULL;
  
  err = Pa_OpenStream( &stream,
		       &input_parameters,
		       NULL, // Output parameters
		       44100, // sample rate
		       256,   // frames per buffer
		       0, //special flags
		       FFT_on_input,
		       &data);
  if (err != paNoError)
    {
      printf("error, mon!");
    }
  
  err = Pa_StartStream(stream);
  if (err != paNoError)
    {
        printf("error, mon!");
    }
  //FFT(data.samples, SAMPLES);
  
  for (i = 0; i < SAMPLES; i++)
    {
      printf("%.8f, %.8f\n", data.samples[i].re, data.samples[i].im);
    }
  
  return 0;
}
