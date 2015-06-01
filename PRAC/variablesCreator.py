# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PRAC IAA - UOC 2015

from numpy import *
from math import exp

# This file contains the implementation of all the methods needed
# for the creation of the variables and the generation of the values

# Feedback Messages definition
GENERATION={
	'INIT':'Begin the generation of the %s variable: ' ,
	'CORRECT':'Correctly generated',
	'ERROR':'Error in generation'
}

# ------------------------------------------------------- #
# Methods used in exercici1 #
# ------------------------------------------------------- #

# Builds a matrix concatenating the 4 arrays
def buildMatrix(ar1, ar2, ar3, ar4):
	print('Begin building the matrix with all the arrays: ',end="")

	try:
		m = column_stack((ar1, ar2, ar3, ar4))
		print (GENERATION['CORRECT'])
	except:
		print(GENERATION['ERROR'])
		raise
	return m

# Create the standard variable, normal distribution
def createVariable(name, number, mean, stdDev):
	print(GENERATION['INIT'] % (name,),end="")
	try:
		x = random.normal(mean, stdDev, number)
		print(GENERATION['CORRECT'])
	except:
		print (GENERATION['ERROR'])
		raise
	return x

# Create the variable using a linear function, escalar product
def createVariableEscalarMultiplication(name, number, escalar, ar1):
	print(GENERATION['INIT'] % (name,),end="")
	try:
		x = [i*escalar for i in ar1]
		x=array(x)
		
		print(GENERATION['CORRECT'])
	except:
		print (GENERATION['ERROR'])
		raise
	return x

# Create the variable using a non-linear function, using two arrays and exponentials
def createVariableExpAndSum(name, number, constant, array1, array2):
	print(GENERATION['INIT'] % (name,),end="")
	try:
		x=ndarray((number,),float)
		for i in range(number):
			temp1 = exp(array1[i])
			temp2 = temp1*constant
			x[i] = temp2 + array2[i]
			#x[i] = exp(array1[i])*constant+array2[i]
		print (GENERATION['CORRECT'])
	except:
		print (GENERATION['ERROR'])
		raise
	return x

# ------------------------------------------------------- #
# Methods used in exercici2 #
# ------------------------------------------------------- #

# Generate data for normal distribution, multivariada 2D
def createBidimensionalVariable(mean, cov, obsNumber):
 biVar = random.multivariate_normal(mean,cov,obsNumber)
 return biVar


