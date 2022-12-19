#include "server.h"

void *welcomeMessage;
int welcomeSize;

Server* setUpServerConnection(void) {
    Server* server = setServer(server);
    int clientConnFd, len;
    struct sockaddr_in cli;

    if (server->sock == -1) {
        printf("socket creation failed...\n");
        return (NULL);
    }

    if ((bind(server->sock, (struct sockaddr*)&server->addr, sizeof(server->addr))) != 0) {
        printf("socket bind failed...\n");
        return (NULL);
    }

    if ((listen(server->sock, 5)) != 0) {
        printf("Listen failed...\n");
        return (NULL);
    }

    printf("Server listening..\n");
    len = sizeof(cli);
    clientConnFd = accept(server->sock, (struct sockaddr*)NULL, NULL);
    if (clientConnFd < 0) {
        printf("server accept failed...\n");
        return(NULL);
    }

    printf("server accept the client...\n");

    return server;
}

void closeServer(Server *s) {
    close(s->sock);
    free(s);
    return;
}

int serverSendReceive(Server *s, void *buffer) {
    fd_set readfds;
    FD_ZERO(&readfds);
    FD_SET(s->sock, &readfds);
    int new_socket, active, readValue, sd;
    int max_sd = s->sock;
    struct sockaddr_in address;

    for (int i = 0 ; i < s->maxClients ; i++) {
        int sd = s->clientSocks[i];
        if(sd > 0)
            FD_SET( sd , &readfds);
        if(sd > max_sd)
            max_sd = sd;
    }
    active = select( max_sd + 1 , &readfds , NULL , NULL , NULL);
    if ((active < 0) && (errno!=EINTR)){
        printf("select error");
    }
    if (FD_ISSET(s->sock, &readfds)) {
        if ((new_socket = accept(s->sock, (struct sockaddr *)&address, (socklen_t*)&s->addrlen)) < 0) {
            perror("accept ");
            exit(EXIT_FAILURE);
        }
        printf("New connection, socket fd:%d, IP:%s:%d\n" , new_socket , inet_ntoa(address.sin_addr) , ntohs(address.sin_port));
        if( send(new_socket, welcomeMessage, welcomeSize, 0) != welcomeSize) {
            perror("send error");
        }
        printf("Welcome message is a success\n");
        for (int i = 0; i < s->maxClients; i++) {
            if( s->clientSocks[i] == 0 ) {
                s->clientSocks[i] = new_socket;
                break;
            }
        }
    }

    for (int i = 0; i < s->maxClients; i++) {
        sd = s->clientSocks[i];
        if (FD_ISSET( sd , &readfds)) {
            if ((readValue = read( sd , buffer, 1024)) == 0) {
                getpeername(sd , (struct sockaddr*)&address , (socklen_t*)&s->addrlen);
                close(sd);
                s->clientSocks[i] = 0;
            } else {
                send(sd ,buffer , strlen(buffer), 0 );
            }
        }
    }
    return readValue;
}

Server* setServer(Server *server) {

    server = malloc(sizeof(Server));

    server->sock = socket(AF_INET, SOCK_STREAM, 0);
    server->tv.tv_sec = 0;
    server->tv.tv_usec = 0;
    server->maxClients = 10;
    server->addr = setServerAddr();

    return server;
}

struct sockaddr_in setServerAddr(void) {

    struct sockaddr_in serverAddr;

    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(8080);

    return serverAddr;
}