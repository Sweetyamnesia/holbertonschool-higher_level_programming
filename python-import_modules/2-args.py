#!/usr/bin/python3
import sys
if __name__ == "__main__":
	n = len(sys.argv)
	if len(sys.argv) == 1:
		print("{} arguments.".format(sys.argv[0]))
	elif len(sys.argv) == 2:
		print("{} argument:".format(sys.argv[1]), end="\n")
	else:
		print("{} arguments:".format(sys.argv), end="\n")
