/* The code for the ringbuffer was inspired by
 * the Audacity source code (audacity.sourceforge.net), 
 * so creds to one Dominic Mazzoni wbo wrote the original.
 *
 * The other code is (c) Jonne Mickelin 2009
 */

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#define SIZE (8)

struct ring_buffer
{
  int * data;
  
  unsigned int size;            /* Thread safe on x86 and x86-64 machines  */
  unsigned int consume_index;   /* because lookup and reading of ints is   */
  unsigned int write_index;     /* atomic. long (*NIX, etc.) and long long */
                                /* (MS Windows) is not atomic, so using it */
                                /* would be a bad idea. Correct me if I'm  */
                                /* wrong. */
};

struct ring_buffer *
ring_buffer_init(unsigned int size)
{
  struct ring_buffer * rb;
  
  rb = (struct ring_buffer *) malloc(sizeof(struct ring_buffer));
  rb->data = (int *) malloc(sizeof(int) * size);
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
ring_buffer_write_2(struct ring_buffer * rb, int * src, unsigned int lendata)
{
  int i;
  int block;
  int free_space = ring_buffer_free_space(rb);
  int written;
  
  if (lendata > free_space)
    {
      lendata = free_space;
    }
  printf("Will write %i out of a maximum of %i free space\n", lendata, free_space);
  
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
	  rb->data[rb->write_index + i] = src[i];
	}

      rb->write_index = rb->write_index + block;

      if (rb->write_index == rb->size)
	{
	  rb->write_index = 0;
	}
      lendata -= block;
    }  
}

int
ring_buffer_consume_2(struct ring_buffer * rb, int * dest, unsigned int lendata)
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
  printf("Will consume %i out of a maximum of %i written data\n", lendata, length);
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

int
ring_buffer_consume(struct ring_buffer * rb, int * dest, unsigned int lendata)
{
  int i;
  int wrote;

  printf("%i, %i\n", (rb->consume_index + lendata) % rb->size, rb->write_index);
  
  if (dest == NULL)
    {
      return 0;
    }
  else if ((rb->consume_index + lendata) % rb->size < rb->write_index)
    {
      for (i = 0; i < lendata; i++)
	{
	  dest[i] = rb->data[(rb->consume_index + i)%rb->size];
	}
      rb->consume_index = (rb->consume_index + lendata) % rb->size;

      return lendata;
    }
  else
    {
      wrote = (rb->write_index - rb->consume_index - 1) % rb->size;

      for (i = 0; i < wrote; i++)
	{
	  dest[i] = rb->data[(rb->consume_index + i)%rb->size];
	}
      rb->consume_index = (rb->consume_index + wrote) % rb->size;

      return wrote;
    }  
}

int
ring_buffer_write(struct ring_buffer * rb, int * data, unsigned int lendata)
{
  int i;
  int wrote;
  
  if (data == NULL)
    {
      return 0;
    }
  else if ((rb->write_index + lendata) % rb->size > rb->consume_index)
    {
      wrote = (rb->consume_index - rb->write_index) % rb->size;
      for (i = 0; i < wrote; i++)
	{
	  rb->data[(rb->write_index + i) % rb->size] = data[i];
	}
    }
}

void
print_ringbuffer(struct ring_buffer * rb)
{
  int i;
  
  printf("Free space: %i\n", ring_buffer_free_space(rb));
    
  for (i = 0; i < rb->size; i++)
    {
      printf("  - ");
      if (i == rb->write_index){ printf("<- write"); }
      if (i == rb->consume_index){ printf("<- consume"); }
      printf("\n");
	  
      if (i != rb->consume_index) { printf(" |%i|", rb->data[i]); }
      else { printf("X[%i]", rb->data[i]); }
      printf("\n");
      fflush(stdout);
    }
  printf("  - \n");
}

void print_array(int * buf, int len)
{
  int i;
  printf("\n[");
  for (i = 0; i < len - 1; i++)
    {
      printf("%i, ", buf[i]);
    }
  printf("%i]\n", buf[len - 1]);
}

int
main()
{
  int i;
  
  int * dest;
  int * data;
  
  struct ring_buffer * rb;

  rb = ring_buffer_init(SIZE);
  data = (int*) malloc(13*sizeof(int));
  dest = (int*) malloc(13*sizeof(int));

  for (i = 0; i < 13; i++)
    {
      data[i] = i;
      dest[i] = 0;
    }

  print_ringbuffer(rb);
  print_array(dest, 13);
  
  ring_buffer_write_2(rb, data, 5);
  
  print_ringbuffer(rb);
  print_array(dest, 13);

  ring_buffer_consume_2(rb, dest, 5);
  ring_buffer_write_2(rb, data+5, 6);
  ring_buffer_write_2(rb, data+6, 6);

  print_ringbuffer(rb);
  print_array(dest, 13);

  i = ring_buffer_consume_2(rb, dest, 1);
  
  assert(i==0);
  
  print_ringbuffer(rb);
  print_array(dest, 13);
  free(rb);
  free(data);
  free(dest);
  
}

