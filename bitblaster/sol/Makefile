# Makes all Versions and Compares output

CC="gcc"
CEXEC="sol"
JC="javac"

all: c java	

c:
	@$(CC) main.c -Wall -o $(CEXEC)
java:
	@$(JC) main.java

run: 
	echo "Use 'run-c', 'run-java', or 'run-py'"

run-c: c
	@./$(CEXEC)

run-java: java
	@java main

run-py: 
	@python3 main.py

clean:
	rm $(CEXEC) main.class
