# -*- coding: utf-8 -*-
import random
#PRINTING
def print_first_line(line):
	print '   _   _   _   _   _\n _╱' + '╲_╱'.join([str(c) for c in line]) + '╲\t' + str(line)

def print_even_line(line):
	print '╲_╱' + '╲_╱'.join([str(c) for c in line]) + '╲\t' + str(line)

def print_uneven_line(line):
	print '╱' + '╲_╱'.join([str(c) for c in line]) + '╲_╱\t' + str(line)

def print_last_line():
	print '  ╲_╱ ╲_╱ ╲_╱ ╲_╱ ╲_╱'
		
def print_field(data):
	"""Print hexic game field to console"""
	print_first_line(data[0])
	for i in xrange(1, len(data)):
		print_uneven_line(data[i]) if i%2!=0 else print_even_line(data[i])
	print_last_line()
#!PRINTING

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

print_field(hexic_data)



print get_columns(hexic_data)
print get_mixed_columns(hexic_data)
