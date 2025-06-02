#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file
and returns the number of characters written.
"""

def write_file(filename="", text=""):
	"""Write a string to a text file and prints number of characters."""
	with open(filename, "w", encoding="utf-8") as file:
		content = file.write(text)
	print(content)
	