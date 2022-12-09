#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include<stdbool.h>
#include <curses.h>
#include <termios.h>
#include <pthread.h>

typedef struct BuffLock {
	pthread_mutex_t *lock;
	void *buffer;
} BuffLock;

void *inputThread(void *buffer);
BuffLock *makeBuffLock();
void freeBuffLock(BuffLock *bl);