# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PRAC IAA - UOC 2015

from utils import *
from math import exp

OBSERVATIONS_NUMBER = 1000

# --- Apartat a ---#

# Generate the values for the variables x1..x4
x1 = createVariable('x1', OBSERVATIONS_NUMBER, 0.5, 0.1)
x2 = createVariable('x2', OBSERVATIONS_NUMBER, 4.5, 0.6)
x3 = createVariableEscalarMultiplication('x3', OBSERVATIONS_NUMBER, 3, x1)
x4 = createVariableExpAndSum('x4', OBSERVATIONS_NUMBER, 2, x1, x2)

print()
print('All arrays correctly generated, proceeding to build the matrix')

# Build the matrix A, with the data of the 4 variables
A = buildMatrix(x1, x2, x3, x4)


