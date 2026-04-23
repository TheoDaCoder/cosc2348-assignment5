# Compiler and flags
CC = gcc
CFLAGS = -Wall -g  # Enable warnings and debugging information

# Source files
SRC = main.c addition.c subtraction.c multiplication.c division.c
OBJ = main.o addition.o subtraction.o multiplication.o division.o

# The output executable
TARGET = calculator

# Default rule to build the executable
all: $(TARGET)

# Linking the object files into the final executable
$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $(TARGET)

# Rules to compile the individual source files
main.o: main.c operations.h
	$(CC) $(CFLAGS) -c main.c -o main.o

addition.o: addition.c operations.h
	$(CC) $(CFLAGS) -c addition.c -o addition.o

subtraction.o: subtraction.c operations.h
	$(CC) $(CFLAGS) -c subtraction.c -o subtraction.o

multiplication.o: multiplication.c operations.h
	$(CC) $(CFLAGS) -c multiplication.c -o multiplication.o

division.o: division.c operations.h
	$(CC) $(CFLAGS) -c division.c -o division.o

# Clean up object files and executable
clean:
	rm -f *.o $(TARGET)

# Phony targets (not associated with real files)
.PHONY: all clean
