.PHONY: all clean

all: ./build
	./run.sh

./build: foreign.c
	python3 setup.py build

clean:
	python3 setup.py clean
