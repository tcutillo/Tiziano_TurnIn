#include "data.h"

bool runningMainThread;

bool littleEndian() {
    unsigned int i = 1;
    char *c = (char*)&i;
    if (*c)   
        return true;
    else
        return false;
}

Data *makeData(void *dat, int bytes) {
    Data *data = malloc(sizeof(Data));

    data->arr = malloc(bytes);
    memcpy(data->arr, dat, bytes);
    
    return data;
}

void *writeData(Data *d) {
    void *buffer = calloc(d->bytes + sizeof(int), 1);

    memcpy(buffer, &d->bytes, sizeof(int));
    memcpy(buffer + sizeof(int), d->arr, d->bytes);

    return buffer;
}

Data *readData(void *buffer) {
    Data *d = malloc(sizeof(Data));

    memcpy(&d->bytes, buffer, sizeof(int));
    d->arr = calloc(d->bytes, 1);
    memcpy(d->arr, buffer + sizeof(int), d->bytes);

    return d;
}

void freeData(Data *d) {
    free(d->arr);
    free(d);
}

void *flipEndian(void *buff, int size) {
    return NULL;
}