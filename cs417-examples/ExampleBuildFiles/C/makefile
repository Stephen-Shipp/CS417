MAINPROG=machine-asst-3 # Replace this with your desired program name

SOURCES:=$(wildcard *.c)
OBJECTS=$(SOURCES:.c=.o)
FLAGS=-fsanitize=address,leak,undefined -Wall -Wextra -fuse-ld=gold

all: $(SOURCES) $(MAINPROG)

$(MAINPROG): $(OBJECTS)
	gcc $(FLAGS) $(OBJECTS) -o $@

.c.o:
	gcc $(FLAGS) -c $< -o $@

clean:
	rm *.o $(MAINPROG)
