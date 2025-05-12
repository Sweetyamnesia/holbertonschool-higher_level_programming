#!/usr/bin/python3

def new_in_list(my_list, idx, element):
	for element in my_list:
		if idx < element:
			return my_list.copy
		elif idx > element:
			return my_list.copy

