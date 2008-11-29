/* dft.c
 * Provide functions for the Discrete Fourier transform (O(n^2) time).
 *
 * (c) Jonne Mickelin 2008
 * License: GPL version 3
 */

//#define DEBUG

#include <math.h> // It's math, duh
#include <stdlib.h> // For malloc, free

#ifdef DEBUG
#include <stdio.h>
#endif

#include "dft.h"

#define PI 3.14159265359

complex* DFT(float * data_points, int N)
{
  int k, n;
  complex * frequencies = malloc(N*sizeof(complex));
  complex freq;

  float w = 2 * PI / N;
  int mod;
  
  float * sin_table = malloc(N*sizeof(float));
  float * cos_table = malloc(N*sizeof(float));

  for (k = 0; k < N; k++)
    {
      sin_table[k] = sin(w*k);
      cos_table[k] = cos(w*k);
    }
  
  for (k = 0; k < N; k++) // Iterate over the frequencies
    {
      freq.re = 0;
      freq.im = 0;

      for (n = 0; n < N; n++) // Iterate over the samples
	{
	  // DONE: Define sin and cos by means of a lookup table instead. 
	  // Is this correct?
	  // Seems to be
	  mod = k*n % N;
	  
	  freq.re += data_points[n] * cos_table[mod];	  
	  freq.im -= data_points[n] * sin_table[mod];
	}

      frequencies[k] = freq;
    }
  
  return frequencies;
}

#ifdef DEBUG
int main()
{
  float data[1024];
  complex* freqs;
  int t;
  
  for (t = 0; t < 1024; t++)
    {
      data[t] = sin(2*PI*t/1024) + sin(2*PI * 2 * t/1024) - sin(2*PI * 5 * t/1024);
    }
  
  freqs = DFT(data, 1024);

  // Ok, I put in some stuff for easy printing and plotting with python
  printf("import pylab");
  
  printf("#*** Time domain ***\n");
  
  printf("timedomain = ( ");
  for (t = 0; t < 1024; t++)
    {
      printf("%f, ", data[t]);
    }
  printf(" )\n\n");

  printf("#*** Frequency domain ***\n");
  printf("frequencydomain = ( ");
  for (t = 0; t < 1024; t++)
    {
      printf("%f, ", freqs[t].re + freqs[t].im);
    }
  printf(" )\n\n");
  printf("t = range(len(timedomain))\n\n");
  
  printf("pylab.subplot(211)\npylab.bar(t, timedomain)\n");
  printf("pylab.subplot(212)\npylab.bar(t, frequencydomain)\n\n");
  
  printf("pylab.show()\n\n");

  return 0;
}
#endif
