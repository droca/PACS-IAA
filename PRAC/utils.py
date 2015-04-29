# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PRAC IAA - UOC 2015

from numpy import *

# Generation a number of random values that will have the mean and stdDev indicated
def generateVariableObs(number, mean, stdDev):
	return 	random.normal(mean, stdDev, number)

# Builds a matrix concatenating the 4 arrays
def buildMatrix(ar1, ar2, ar3, ar4):
	return concatenate((ar1, ar2, ar3, ar4),0)







