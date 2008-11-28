/* dft.h
 * Provide functions for the Discrete Fourier Transform (O(n^2))
 *
 * (c) Jonne Mickelin 2008
 * License: GPL version 3
 */

typedef struct {
  double re;
  double im;
} complex;

complex* DFT(float * data_points, int N);

