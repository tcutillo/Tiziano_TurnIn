#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <stdbool.h>
#include <sys/types.h>
#include <fcntl.h>

typedef struct Client {
    int sock;
    struct timeval tv;
} Client;

Client* connectAsClient(char *ip);
int receiveData(Client *c_, char *buffer);
struct sockaddr_in setServerAddr(char *ip);
Client* setClient(Client *client);

#define BUFF 1024

extern Client *c;