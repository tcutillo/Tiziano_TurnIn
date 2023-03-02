#include "inputThread.h"
#include "data.c"

void *inputThread(void *buffer) {
    return NULL;
}

BuffLock *makeBuffLock() {
    BuffLock *bl = malloc(sizeof(BuffLock));
    
    return bl;
}

void freeBuffLock(BuffLock *bl) {
    free(bl);
    return;
}