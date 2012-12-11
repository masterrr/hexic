# -*- coding: utf-8 -*-
import random

def print_first_line(line):
	print '   _   _   _   _   _\n _╱{}╲_╱{}╲_╱{}╲_╱{}╲_╱{}╲\t{}'.format(line[0],line[1],line[2],line[3],line[4],line)

def print_even_line(line):
	print '╲_╱{}╲_╱{}╲_╱{}╲_╱{}╲_╱{}╲\t{}'.format(line[0],line[1],line[2],line[3],line[4], line)

def print_uneven_line(line):
	print '╱{}╲_╱{}╲_╱{}╲_╱{}╲_╱{}╲_╱\t{}'.format(line[0],line[1],line[2],line[3],line[4], line)

def print_last_line():
	print '  ╲_╱ ╲_╱ ╲_╱ ╲_╱ ╲_╱'
		
def print_field(data):
	"""Print hexic game field to console"""
	print_first_line(data[0])
	for i in xrange(1, len(data)):
		print_uneven_line(data[i]) if i%2!=0 else print_even_line(data[i])
	print_last_line()

hexic_data=[[random.randrange(10) for i in xrange(5)] for j in xrange(15)]

print_field(hexic_data)