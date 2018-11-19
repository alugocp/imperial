# A makefile for the Imperial project \
  Created by Alex Lugo

all: clean build

clean:
	rm -f bin/*

build:
	python -m py_compile src/*.py
	mv src/*.pyc bin
