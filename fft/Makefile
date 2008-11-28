all : pydft.so

pydft.so : pydft.o dft.o
	gcc -shared pydft.o dft.o -lm -o pydft.so

pydft.o : pydft.pyx
	pyrexc pydft.pyx
	gcc -c -fPIC -I/usr/include/python2.6/ pydft.c

dft.o : dft.c dft.h
	gcc -c -fPIC dft.c

clean :
	rm *.o

developer-clean : clean
	rm pydft.c