CC = gcc
LIBS = -lncurses

bino: src/main.c src/util.c src/ui.c src/filemachine.c
	$(CC) -o bino src/main.c src/util.c src/ui.c src/filemachine.c $(LIBS)

install: SHELL:=/bin/bash
install:
	@a=$$(pwd);\
	b=/bino;\
	p='/usr/local/bin';\
	echo cd $$a > $$p$$b;\
	echo .$$b >> $$p$$b;\
	if [ "$$(uname)" == "Darwin" ];\
	then chmod 755 $$p$$b;\
	else chmod +x $$p$$b;\
	fi

clean:
	rm -f bino
	rm -f /usr/local/bin/bino