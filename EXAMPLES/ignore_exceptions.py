#!/usr/bin/python3

try:
	x = 5
	y = "cheese"
	z = x + y
	f = open("sesame.txt")
	print("Bottom of try")

except(TypeError,IOError) as e:
	pass

