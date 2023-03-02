#include "client.h"

Client* connectAsClient(char *ip) {

    Client *client = setClient(client);
    struct sockaddr_in serverAddr = setServerAddr(ip);
    struct sockaddr_in cli;

    if (client->sock == -1) {
        printf("socket creation failed...\n");
        return (NULL);
    }

    if (connect(client->sock, (struct sockaddr*)&serverAddr, sizeof(serverAddr))!= 0) {
        printf("connection with the server failed...\n");
        return (NULL);
    }

    printf("connected to the server..\n");

    return client;
}

int receiveData(Client *c_, char *buffer) {
    fd_set reader;
    ssize_t r = 0;
    int activity = 0;

    FD_ZERO(&reader);
    FD_SET(c_->sock, &reader);
    activity = select(c_->sock + 1, &reader, NULL, NULL, &c_->tv);
    if (activity < 0)
        return -1;
    if (c_->sock > 0 && FD_ISSET(c_->sock, &reader)) {
        r = read(c_->sock, buffer, BUFF);
        if (r == -1) {
            return -1;
        }
        buffer[r] = '\0';
    }
    return r;
}

Client* setClient(Client *client) {
    
    client = malloc(sizeof(Client));

    client->sock = socket(AF_INET, SOCK_STREAM, 0);
    client->tv.tv_sec = 0;
    client->tv.tv_usec = 0;

    return client;
}

struct sockaddr_in setServerAddr(char *ip) {

    struct sockaddr_in serverAddr;

    serverAddr.sin_addr.s_addr = inet_addr(ip);
    serverAddr.sin_family = INADDR_ANY;
    serverAddr.sin_port = htons(8080);

    return serverAddr;
}