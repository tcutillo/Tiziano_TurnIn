#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <stdbool.h>
#include <curses.h>
#include <termios.h>
#include <pthread.h>
#include <time.h>

typedef struct Data {
	int bytes;
	void *arr;
} Data;

bool littleEndian();
Data *makeData(void *dat, int bytes);
void *writeData(Data *d);
Data *readData(void *buffer);
void freeData(Data *d);
void *flipEndian(void *buff, int size);
void *inputThread(void *buffer);

extern bool runningMainThread;