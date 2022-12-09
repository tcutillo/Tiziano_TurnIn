COM = gcc -Wall -w -pedantic -c -g

data: main.c data.c data.h inputThread.c inputThread.h
	gcc -o data -g -Wall -w -pedantic -pthread -g3 main.c

test:
	valgrind --fair-sched=yes --leak-check=full --show-leak-kinds=all ./data

clean:
	rm *.o

fclean:
	rm data
	rm -rf data.dSYM
	