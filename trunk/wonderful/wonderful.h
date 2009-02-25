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

#include <portaudio.h>
#include "dft.h"

#ifndef WONDERFUL_H
#define WONDERFUL_H

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

struct ring_buffer * ring_buffer_init(unsigned int size);
unsigned int ring_buffer_free_space(struct ring_buffer * rb)
int ring_buffer_write(struct ring_buffer * rb, const float * src, unsigned int lendata)
int ring_buffer_consume(struct ring_buffer * rb, complex * dest, unsigned int lendata)

int wonderful_init(inputData * data, PaStream * stream)
int wonderful_terminate(inputData * data, PaStream * stream)

#endif
