
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
  complex * frequencies = malloc(N*sizeof(complex)); // FREEME, caller
  complex freq;

  float w = 2 * PI / N;
  int mod;
  
  float * sin_table = malloc(N*sizeof(float)); // FREEME
  float * cos_table = malloc(N*sizeof(float)); // FREEME

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

  free(sin_table);
  free(cos_table);
  
  // Responsibility over frequencies is passed on to the caller
  return frequencies;
}

/* Arguments: 
   data -- real valued time domain input (double*)
   N    -- length of data (int)
*/
complex *
FFT(double* data, int N)
{
  unsigned int i, I, j, k;
  double temp;
  
  // Shuffle input
  /*for (i = 0; i < N/2; i+=2)
    {
      temp = data[i+1];              // Swap the values of the odd indexed 
      data[i+1] = data[i+N/2];       // data points so that i - (i+1) == N/2 
      data[i+N/2] = temp;            // for all even i.
    }                                
  */
  /*
  // Do the FFT
  for (i = 1, I = N>>1; i < N; i<<=1, I>>=1)
    {
      printf("%i:\n", i);
      
      // Loop over each data point and do the summations
      for (j = 0; j < N; j+=1)
	{
	  //if (j < N/2)
	  //  {
	  printf("\t%.0lf + %.0lf => %i, %i\n", data[j], data[(j+I)%N], j, (j+I)%N);
	  //  }
	  //else
	  //{
	  //printf("\t%.0lf + %.0lf => %i, %i\n", data[j], data[j-i/2], j, j-i/2);
	  //printf("\t%.0lf + %.0lf => %i, %i\n", data[j+i], data[j], j+i, j);
	  //  }
	  
	  
	  //printf("%.0lf + %.0lf => %i\n", data[(j+1)%N], data[j], (j+i)%N);
	}
      printf("\n");
      
    }
  */
  for (i = 1; i < N; i<<=1)           // Do the loop log N times
    {
      printf("%i:\n", i);      
      for (j = 0; j < N; j+=2*i)      // Iterate over the first elements of all the subsequences
	{
	  for (k = 0; k < i; k++)     // and if you know the first element, it's easy to find
	                              // all the other elements to be "added down" If there are
	                              // n first elements, there are log2 n consequtive elements
	                              // to "add down".
	    {
	      printf("\n");
	      printf("\t%i, %i\n", j+k, j+k+i);
	      printf("\t%i, %i\n", j+k+i, j+k);
	    }
	  
	}
      printf("\n");
    }
  /*
    i = 1, 0 2 4 6 j_n = 2*n
    i = 2, 0 1 4 5 j_n = ?
    i = 4, 0 1 2 3 j_n = n
  */
  //*/

  /*for (i = N; i > 1; i>>=1)
    {
      for (j = 0; j < N; j++)
	{
	  printf("%i, %i\n", i, i+j);
	}
    }
  */
  
  // Print the result
  /*for (i = 0; i < N; i++)
    {
      printf("%lf\n", data[i]);
    }

    return data;*/
}

#ifdef DEBUG
#define NUM 8
int main()
{
  double data[NUM];
  complex* freqs;
  int t;
  
  /*for (t = 0; t < 1024; t++)
    {
      data[t] = sin(2*PI*t/1024) + sin(2*PI * 2 * t/1024) - sin(2*PI * 5 * t/1024);
    }
  */
  for (t = 0; t < NUM; t++)
    {
      data[t] = t;
    }
  freqs = FFT(data, NUM);

  // Ok, I put in some stuff for easy printing and plotting with python
  /*printf("import pylab");
  
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
  */
  return 0;
}
#endif
