
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

/* Multiply two complex numbers */
inline complex complex_mul(complex z, complex w)
{
  complex answer;
  
  answer.re = z.re * w.re - z.im * w.im;
  answer.im = z.re * w.im + z.im * w.re;
  
  return answer;
}

/* Return the 2-logarithm of a power of 2 */
inline int log_2(int N)
{
  int i;
  int log_N = 0;
  
  for (i = N; i > 1; i>>=1)
    {
      log_N++;
    }
  
  return log_N;
}

/* Return input with the bits in opposite order */
inline int bitreverse(int input, int N)
{
  unsigned int n = 0, i, bit;

  bit = input & 1;
  n |= bit;
  for (i = 0; i < N - 1; i++)
    {
      n<<=1;
      input>>=1;
      bit = input & 1;
      n |= bit;
    }
  
  return n;
}      

/* Arguments: 
   data -- complex time domain input (complex*)
   N    -- length of data (int)
*/
complex *
FFT(complex* data, int N)
{
  unsigned int i;                     // Half the size of the DFT
  unsigned int j, k;                  // j+k = the index of a sample in the frequency plane
  unsigned int w;                     // the exponent of the twiddle factor
  unsigned int log_N;
  
  complex temp, temp2;
  complex W_N_w;                      // Holds the complex twiddle factors
  
  /* Shuffle input */
  log_N = log_2(N);
  for (i = 0; i < N; i++)
    {
      j = bitreverse(i, log_N);
      if (j > i)                      // Only swap values once, and don't touch values when j==i
	{
	  temp = data[i];
	  data[i] = data[j];
	  data[j] = temp;
	}
    }
  
  /* Commence the alorithm! */
  for (i = 1; i < N; i<<=1)           // Do the loop log N times, corresponding to the depth of the
                                      // recursive algorithm.
    {
      // Now, iterate over all of the elements and do the summations.
      for (j = 0; j < N; j+=2*i)      // Iterate over the first elements of all the subsequences
	{
	  for (k = 0; k < i; k++)     // and if you know the first element, it's easy to find
	                              // all the other elements to be "added down" If there are
	                              // n first elements, there are log2 n consequtive elements
	                              // to "add down".
	    {
	      w = (j+k)%(2*i);
	      
	      // The positive and negative signs are handled simultaneously

	      if (0 == w)       // Twiddle factor is 1
		{
		  // Just add or subtract the data
		  temp.re = data[j+k].re;
		  temp.im = data[j+k].im;
		  
		  data[j+k].re = data[j+k].re + data[j+k+i].re;     //  1   
		  data[j+k].im = data[j+k].im + data[j+k+i].im;
		  
		  data[j+k+i].re = temp.re - data[j+k+i].re;        // -1
		  data[j+k+i].im = temp.im - data[j+k+i].im;
		}
	      else if (i == w)  // The twiddle factor is i. Recall that i is half the length of the DFT
		{
		  // Just swap the real and imaginary parts of data[j+k+i]
		  // and add
		  temp.re = data[j+k].re;
		  temp.im = data[j+k].im;
		  temp2.re = data[j+k+i].re;
		  temp2.im = data[j+k+i].im;
		  
		  data[j+k].re = data[j+k].re + data[j+k+i].im;    //  i
		  data[j+k].im = data[j+k].im + data[j+k+i].re;
		  
		  data[j+k+i].re = temp.re - temp2.im;             // -i
		  data[j+k+i].im = temp.im - temp2.re;
		}
	      else              // The twiddle factor is complex
	      {
		// Calculate the twiddle factor in rectangular form
		// and multiply it to data[j+k+i] before adding it 
		// to data[j+k]
		temp.re = data[j+k].re;
		temp.im = data[j+k].im;
		
		// TODO: This could be optimised with a lookup table
		W_N_w.re = cos(-2*PI/(2*i) * w);
		W_N_w.im = sin(-2*PI/(2*i) * w);
		
		temp2 = complex_mul(data[j+k+i], W_N_w);
		
		data[j+k].re = data[j+k].re + temp2.re;
		data[j+k].im = data[j+k].im + temp2.im;
		
		data[j+k+i].re = temp.re - temp2.re;
		data[j+k+i].im = temp.im - temp2.im;
	      }
	    }	  
	}
    }

  return data;
}

#ifdef DEBUG
#define NUM 16
int main()
{
  complex data[NUM];
  complex data2[NUM];
  complex* freqs;
  int t;
  
  for (t = 0; t < NUM; t++)
    {
      data[t].re = sin(2*PI*t/NUM);// + sin(2*PI * 2 * t/NUM) - sin(2*PI * 5 * t/NUM);
      data[t].im = 0;

      data2[t].re = sin(2*PI*t/NUM);// + sin(2*PI * 2 * t/NUM) - sin(2*PI * 5 * t/NUM);
      data2[t].im = 0;
    }

  freqs = FFT(data, NUM);
  
  // Ok, I put in some stuff for easy printing and plotting with python
  printf("import pylab\n");
  
  printf("#*** Time domain ***\n");
  
  printf("timedomain = ( ");
  for (t = 0; t < NUM; t++)
    {
      printf("%f, ", data2[t].re);
    }
  printf(" )\n\n");

  printf("#*** Frequency domain ***\n");
  printf("frequencydomain = ( ");
  for (t = 0; t < NUM; t++)
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
