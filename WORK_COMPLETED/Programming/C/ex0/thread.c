#include <pthread.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

pthread_mutex_t lock;

void *func(void *data) {
    int *num = calloc(1, sizeof(int));
    memcpy(num, data, sizeof(int));
    printf("got number %i\n", *num);
    int i = 0;
    while (i < 5) {
        if (pthread_mutex_trylock(&lock)) {
            sleep(3);
            printf("%i\n", *num);
            *num += 2;
            i++;
            pthread_mutex_unlock(&lock);
        }
    }
}


int main() {
    pthread_t handle1;
    pthread_t handle2;

    pthread_attr_t attr;
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    if (pthread_mutex_init(&lock, NULL) != 0) {
        printf("oh no\n");
        return 1;
    }

    int num1 = 0;
    pthread_create(&handle1, &attr, func, &num1);
    printf("thread created\n");
    int num2 = 1;
    pthread_create(&handle1, &attr, func, &num2);

    void *v1;
    void *v2;

    pthread_join(handle1, &v1);
    printf("thread1 counted to %i\n", *(int*)v1);
    pthread_join(handle2, &v2);
    printf("thread2 counted to %i\n", *(int*)v2);

    free(v1);
    free(v2);
    pthread_exit(0);
    return 0;
}