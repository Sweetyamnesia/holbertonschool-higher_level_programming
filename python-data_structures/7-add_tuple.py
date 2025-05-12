#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
	for number in tuple_a and tuple_b:
		number = tuple_a + tuple_b
		print(number)