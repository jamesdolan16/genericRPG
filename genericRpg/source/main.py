#!usr/bin/env python
# main python file of game engine, this is where it all runs from.

import engine
from libraries import fileHandler


def main():
	global engine
	engine = engine.Engine()
	engine.run()

main()
