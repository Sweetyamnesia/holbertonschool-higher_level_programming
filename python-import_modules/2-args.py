#!/usr/bin/python3
import sys
if __name__ == "__main__":
	n = len(sys.argv)
	if len(sys.argv) == 1:
		print("{} argument.".format(n - 1), end="\n")
	elif len(sys.argv) == 2:
		print("{} argument:".format(n - 1), end="\n")
	else:
		print("{} arguments:".format(n - 1), end="\n")

	for i in range(1, n):
		print("{}: {}".format(i, sys.argv[i]), end="\n")
