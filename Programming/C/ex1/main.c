#define BUFF 1024
#include "inputThread.c"

int main() {
	if (littleEndian()) {
		printf("little endian\n");
	} else {
		printf("big endian\n");
	}
	int *poo = (int*)calloc(1, sizeof(int));
	*poo = 10;
	Data *d = makeData(poo, sizeof(int));
	free(poo);
	void *buffer = writeData(d);
	freeData(d);
	Data *read = readData(buffer);
	printf("got %i - expected 10\n", *(int*)read->arr);
	free(buffer);
	freeData(read);
	
	pthread_mutex_t *lock = calloc(sizeof(pthread_mutex_t), 1);
	if (pthread_mutex_init(lock, NULL) != 0) {
		printf("mutex initialization failed\n");
		return 1;
	}

	void *inputBuffer = calloc(sizeof(char), BUFF + 1);
	memcpy(inputBuffer, &lock, sizeof(pthread_mutex_t));

	pthread_t handle;
	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);
	pthread_create(&handle, &attr, inputThread, inputBuffer);
	pthread_attr_destroy(&attr);
	
	memset(inputBuffer, 0 , BUFF);
	while (runningMainThread) {
		if (pthread_mutex_trylock(lock) == 0) {
			if (*(int*)inputBuffer != 0) {
				Data *read = readData(inputBuffer);
				if (read) {
					printf("got data: %s\n", (char*)read->arr); 
					memset(inputBuffer, 0, read->bytes + sizeof(int));
					freeData(read);
				} else {
					memset(inputBuffer, 0, BUFF + 1);
				}
			}
			pthread_mutex_unlock(lock);
		}
	}
	free(lock);
	free(inputBuffer);
	pthread_join(handle, 0);
	pthread_exit(0);
}