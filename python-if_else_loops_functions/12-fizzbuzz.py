#!/usr/bin/python3
def fizzbuzz():
	for n in range(1, 100):
		if n % 3 == 0 and n % 5 == 0:
			print(f"FizzBuzz")
		elif n % 3 == 0:
			print(f"Buzz")
		else:
			print(n)
