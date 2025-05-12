#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
	for item in my_list:
		if idx < 0:
			item.remove()
			print(my_list)
		else:
			print(my_list)