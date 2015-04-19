# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 2 IAA - UOC 2015

import numpy as np

# Creates a matrix with all the values for all customers
# We are assuming that the first line of the source file is a header that contains
# no important data for the study
# We are also assuming that the first two values of each line also don't have
# important value

def readFileData(filename="Wholesale customers.csv"):

	# Reading the file
	with open(filename,'r') as dades:
		dades.readline() # we are skipping the first line of the file, it's a header
		# Data extraction converting the strings to integers for easier processing
		lines = list(map(lambda l: [int(i) for i in (l.strip().split(","))],
			dades.readlines()))

	# Elimination of the frist two values, which are useless for us right now
	# TODO: improve this part
	for i in lines:
		i.pop(0)
		i.pop(0)
	
	lines = np.array(lines)

	return lines

# Calculate mean of the provided numpy array values
def meanCalculation(numpyArray):
	mean = list(map(np.average, numpyArray))
	return mean

# Calculate Standard Deviation of the provided numpy array values
def stdDeviationCalculation(numpyArray):
	stdDev = list(map(np.std, numpyArray))
	return stdDev

def dataNormalization(numpyArray):
	mean = meanCalculation(numpyArray)
	stdDev = stdDeviationCalculation(numpyArray)
	numpyArray = [list(map(lambda i: (i - mean[j]) / stdDev[j], numpyArray[j]))
		for j in range(len(numpyArray))]
	return numpyArray

# -----


# To test the program execution
numpyArray = readFileData()





