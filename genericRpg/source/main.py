#!usr/bin/env python
# main python file of game engine, this is where it all runs from.
#import engine
from libraries import fileHandler

# creating objects

#engine = engine.engine()

def main():
	global fileHandler
	fileHandler = fileHandler.fileHandler()

main()
