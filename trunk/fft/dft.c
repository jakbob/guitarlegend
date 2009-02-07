
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

complex complex_mul(complex z, complex w)
{
  complex answer;
  
  answer.re = z.re * w.re - z.im * w.im;
  answer.im = z.re * w.im + z.im * w.re;
  
  return answer;
}

/* Arguments: 
   data -- real valued time domain input (double*)
   N    -- length of data (int)
*/
complex *
FFT(complex* data, int N)
{
  unsigned int i, I, j, k, w, t;
  complex temp, temp2;
  complex W_N_w;                     // Holds the complex twiddle factors

  // Shuffle input
  for (i = 0; i < N/2; i+=2)
    {
      temp = data[i+1];              // Swap the values of the odd indexed 
      data[i+1] = data[i+N/2];       // data points so that i - (i+1) == N/2 
      data[i+N/2] = temp;            // for all even i.
    }                                
  
  for (t = 0; t < N; t++)
    {
      printf("%lf\n", data[t].re+data[t].im);
    }
  
  printf("\n");
  
  for (i = 1, I = N>>1; i < N; i<<=1, I>>=1)           // Do the loop log N times, corresponding to the depth of the
                                      // recursive algorithm.
    {
      //printf("i=%i, I=%i:\n", i, I);
      // Now, iterate over all of the elements and do the summations.

      for (j = 0; j < N; j+=2*i)      // Iterate over the first elements of all the subsequences
	{
	  for (k = 0; k < i; k++)     // and if you know the first element, it's easy to find
	                              // all the other elements to be "added down" If there are
	                              // n first elements, there are log2 n consequtive elements
	                              // to "add down".
	    {
	      w = (I*(j+k))%(N/2);    // Exponent of the twiddle factor. The positive and negative signs
	                              // are handled simultaneously, thus we use only half of N as a modulo thing.
	      
	      if (0 == w)             // Twiddle factor is 1
		{
		  printf("0\n");
		  temp.re = data[j+k].re;
		  temp.im = data[j+k].im;

		  data[j+k].re = data[j+k].re + data[j+k+i].re;     //  1   
		  data[j+k].im = data[j+k].im + data[j+k+i].im;
		  
		  data[j+k+i].re = temp.re - data[j+k+i].re;        // -1
		  data[j+k+i].im = temp.im - data[j+k+i].im;
		}
	      //else if (N/2 == w)
	      //	{
	      //  printf("N/2\n");
	      //  temp.re = data[j+k].re;
	      //  temp.im = data[j+k].im;

	      //  data[j+k].re += data[j+k+i].re;                   
	      //  data[j+k].im += data[j+k+i].im;
		  
	      //  data[j+k+i].re = temp.re - data[j+k+i].re;        
	      //  data[j+k+i].im = temp.im - data[j+k+i].im;
	      //  }
	      else if (N/4 == w)
		{
		  printf("N/4\n");
		  temp.re = data[j+k].re;
		  temp.im = data[j+k].im;

		  data[j+k].re = data[j+k].re + data[j+k+i].im;    //  i
		  data[j+k].im = data[j+k].im + data[j+k+i].re;
		  
		  temp2.re = data[j+k+i].re;
		  temp2.im = data[j+k+i].im;
		  // We need to save the value in a temporary variable
		  // because we need both the real and imaginary parts
		  data[j+k+i].re = temp.re - temp2.im;       // -i
		  data[j+k+i].im = temp.im - temp2.re;
		}
	      //else if (0.75*N == w)
	      //{
	      //printf("3*N/4\n");
	      //}
	      else                                  // The twiddle factor is complex
	      {
		  printf("else, w=%i\n", w);
		  for (t = 0; t < N; t++)
		    {
		      printf("%lf\n", data[t].re+data[t].im);
		    }
		  
		  temp.re = data[j+k].re;
		  temp.im = data[j+k].im;
		  
		  W_N_w.re = cos(-2*PI/N * w);
		  W_N_w.im = sin(-2*PI/N * w);
		  printf("\tW = %.2lf + %.2lfi\n", W_N_w.re, W_N_w.im);

		  data[j+k].re = data[j+k].re + (data[j+k+i].re * W_N_w.re
						 - data[j+k+i].im * W_N_w.im);   //  Complex multiplication
		  data[j+k].im = data[j+k].im + (data[j+k+i].re * W_N_w.im
						 + data[j+k+i].im * W_N_w.re);   //  Complex multiplication
		  

		  temp2.re = data[j+k+i].re;
		  temp2.im = data[j+k+i].im;
		  // We need to save the value in a temporary variable
		  // because we need both the real and imaginary parts
		  data[j+k+i].re = temp.re - (temp2.re * W_N_w.re
					      - temp2.im * W_N_w.im);      //  Complex multiplication
		  
 		  data[j+k+i].im = temp.im - (temp2.re * W_N_w.im
					      + temp2.im * W_N_w.re);      //  Complex multiplication		  

		  for (t = 0; t < N; t++)
		    {
		      printf("%lf\n", data[t].re+data[t].im);
		    }

	      }

	      //printf("\n");
	      //printf("W^%i, %i, %i, %i\n", (-I*(j+k))%N, I, j+k, -I*(j+k));
	      //printf("\t%.0lf + %.0lf (data[%i], data[%i]) => data[%i]\t-W^%i\n",  
	      //     data[j+k].re, data[j+k+i].re, j+k, j+k+i, j+k, (I*(j+k))%(N/2));

	      //printf("W^%i, %i, %i, %i\n", (I*(j+k))%N, I, j+k, I*(j+k));
	      //printf("\t%.0lf + %.0lf (data[%i], data[%i]) => data[%i]\t W^%i\n", 
	      //     data[j+k+i].re, data[j+k].re, j+k+i, j+k, j+k+i, (I*(j+k))%(N/2));	      
	    }
	  
	}
      //printf("\n");
    }
  
  // Print the result
  /*for (i = 0; i < N; i++)
    {
      printf("%lf\n", data[i].re);
    }
  */
  return data;
}

#ifdef DEBUG
#define NUM 8
int main()
{
  complex data[NUM], data2[NUM];
  complex* freqs;
  int t;
  
  for (t = 0; t < NUM; t++)
    {
      data[t].re = sin(2*PI*t/NUM);// + sin(2*PI * 2 * t/NUM) - sin(2*PI * 5 * t/NUM);
      data[t].im = 0;

      data2[t].re = sin(2*PI*t/NUM);// + sin(2*PI * 2 * t/NUM) - sin(2*PI * 5 * t/NUM);
      data2[t].im = 0;
    }
  
  /*for (t = 0; t < NUM; t++)
    {
      data[t].re = t;
      data[t].im = 0;
      }*/
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
