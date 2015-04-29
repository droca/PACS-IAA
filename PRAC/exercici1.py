# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PRAC IAA - UOC 2015

from utils import *
from math import exp

OBSERVATIONS_NUMBER = 1000
GENERATION_CORRECT = 'Correctly generated'
GENERATION_ERROR = 'Error in generation'

# --- Apartat a ---#

# Generate the values for the variable x1
print('Begin the generation of the x1 variable: ',end="")
try:
	x1 = generateVariableObs(OBSERVATIONS_NUMBER, 0.5, 0.1)
	print(GENERATION_CORRECT)
except:
	print (GENERATION_ERROR)
	raise

# Generate the values for the variable x2
print('Begin the generation of the x2 variable: ',end="")
try:
	x2 = generateVariableObs(OBSERVATIONS_NUMBER, 4.5, 0.6)
	print (GENERATION_CORRECT)
except:
	print (GENERATION_ERROR)
	raise

# Calculate the values for the variable x3
print('Begin the generation of the x3 variable: ',end="")
try:
	x3 = [i*3 for i in x1]
	print(GENERATION_CORRECT)
except:
	print (GENERATION_ERROR)
	raise

# Calculate the values for the variable x4
print('Begin the generation of the x4 variable: ',end="")
try:
	x4=ndarray((1000,),int)
	for i in range(OBSERVATIONS_NUMBER-1):
		x4[i] = exp(x1[i])*2+x2[i]
	print (GENERATION_CORRECT)
except:
	print (GENERATION_ERROR)
	raise

print()
print('All arrays correctly generated, proceeding to build the matrix')

# Build the matrix A, with the data of the 4 variables
print('Begin building the matrix with all the arrays: ',end="")
try:
	A = buildMatrix(x1, x2, x3, x4)
	print (GENERATION_CORRECT)
except:
	print(GENERATION_ERROR)
	raise

