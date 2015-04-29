# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PRAC IAA - UOC 2015

from numpy import *
from math import exp

# Messages definition
GENERATION_INIT = "'Begin the generation of the %s variable: ' % name"
GENERATION_CORRECT = 'Correctly generated'
GENERATION_ERROR = 'Error in generation'


# Builds a matrix concatenating the 4 arrays
def buildMatrix(ar1, ar2, ar3, ar4):
	print('Begin building the matrix with all the arrays: ',end="")
	try:
		m = concatenate((ar1, ar2, ar3, ar4),0)
		print (GENERATION_CORRECT)
	except:
		print(GENERATION_ERROR)
		raise
	return m

# Create the standard variable, normal distribution
def createVariable(name, number, mean, stdDev):
	print(GENERATION_INIT,end="")
	try:
		x = random.normal(mean, stdDev, number)
		print(GENERATION_CORRECT)
	except:
		print (GENERATION_ERROR)
		raise
	return x

# Create the variable using a lineal function, escalar product
def createVariableEscalarMultiplication(name, number, escalar, array):
	print(GENERATION_INIT,end="")
	try:
		x = [i*escalar for i in array]
		print(GENERATION_CORRECT)
	except:
		print (GENERATION_ERROR)
		raise
	return x

# Create the variable using a lineal function, using two arrays and exponentials
def createVariableExpAndSum(name, number, constant, array1, array2):
	print(GENERATION_INIT,end="")
	try:
		x=ndarray((number,),int)
		for i in range(number-1):
			x[i] = exp(array1[i])*constant+array2[i]
		print (GENERATION_CORRECT)
	except:
		print (GENERATION_ERROR)
		raise
	return x




