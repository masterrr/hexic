# -*- coding: utf-8 -*-
import random
from termcolor import colored #for super-colors! 


def print_first_line():
	print (' _  ') * 5;

def print_even_line(line):
	print '╲_╱' + '╲_╱'.join([str(c) for c in line]) + '╲\t' + str(line)

def print_uneven_line(line):
	print '╱' + '╲_╱'.join([str(c) for c in line]) + '╲_╱\t' + str(line)

def print_last_line():
	print '  ' + '╲_╱ ' * 5;
		

# Printing filled field
def print_field(data):
	print_first_line()
	for i in xrange(1, len(data)):
		print_even_line(data[i]) if i%2==0 else print_uneven_line(data[i])
	print_last_line()

#DATA MANIPULATION
def get_columns(data):
	return [[row[i] for row in data] for i in xrange(5)]

def get_mixed_columns(data):
	columns = get_columns(data)
	for i in xrange(4):
		for j in xrange(1, 15, 2):
			columns[i][j]=columns[i+1][j]
	return columns[:4]


#TESTING & DEBUGGING
hexic_data=[[chr(random.randrange(65, 90)) for i in xrange(5)] for j in xrange(15)]

# Printing filled field 
print_field(hexic_data)

print get_columns(hexic_data)
print get_mixed_columns(hexic_data)
