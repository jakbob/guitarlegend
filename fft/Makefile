#PYREX = pyrexc
PYREX = cython
LDFLAGS = -lm
CFLAGS =
CC = gcc

PYTHON_VERSION = 2.5
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)/

all : pydft.so

pydft.so : pydft.o dft.o
	$(CC) -shared pydft.o dft.o -lm -o $@

pydft.o : pydft.pyx
	$(PYREX) pydft.pyx
	$(CC) -c -fPIC -I$(PYTHON_INCLUDE) pydft.c

dft.o : dft.c dft.h
	$(CC) -c -fPIC dft.c

clean :
	-rm *.o

developer-clean : clean
	-rm pydft.c