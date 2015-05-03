# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PRAC IAA - UOC 2015

from variablesCreator import *
from dataProcessing import *
from math import exp
import matplotlib.pyplot as plt
import matplotlib.colors as clr

OBSERVATIONS_NUMBER = 1000

# --- Apartat A ---#

# Generate the values for the variables x1..x4
x1 = createVariable('x1', OBSERVATIONS_NUMBER, 0.5, 0.1)
x2 = createVariable('x2', OBSERVATIONS_NUMBER, 4.5, 0.6)
x3 = createVariableEscalarMultiplication('x3', OBSERVATIONS_NUMBER, 3, x1)
x4 = createVariableExpAndSum('x4', OBSERVATIONS_NUMBER, 2, x1, x2)
print('All arrays correctly generated, proceeding to build the matrix')

# Build the matrix A, with ñthe data of the 4 variables
A = buildMatrix(x1, x2, x3, x4)
#print(A)

# --- Apartat B --- #

# Normalise the data of the variables so we can compare and plot them correctly

normalizedX1 = dataNormalization(x1, 0.5, 0.1)
normalizedX2 = dataNormalization(x2, 4.5, 0.6)
normalizedX3 = dataNormalization(x3)
normalizedX4 = dataNormalization(x4)

# Array for color of the points
colorAr1 = [0]*int((OBSERVATIONS_NUMBER/2))
colorAr2 = [1]*int((OBSERVATIONS_NUMBER/2))
colorAr1.extend(colorAr2)

# Figure representing x1 & x2
fig1 = plt.figure()
fig1.canvas.set_window_title('Color by variables, x1 & x2')
plt.scatter(normalizedX1,normalizedX2,marker='o', c=colorAr1)

# Figure representing x1 & x3
fig2 = plt.figure()
fig2.canvas.set_window_title('Color by variables, x1 & x3')
plt.scatter(normalizedX1,normalizedX3,marker='o', c=colorAr1)

# Figure representing x1 & x4
fig3 = plt.figure()
fig3.canvas.set_window_title('Color by variables, x1 & x4')
plt.scatter(normalizedX1,normalizedX4,marker='o', c=colorAr1)

# Figure representing x2 & x3
fig4 = plt.figure()
fig4.canvas.set_window_title('Color by variables, x2 & x3')
plt.scatter(normalizedX2,normalizedX3,marker='o', c=colorAr1)

# Figure representing x2 & x4
fig5 = plt.figure()
fig5.canvas.set_window_title('Color by variables, x2 & x4')
plt.scatter(normalizedX2,normalizedX4,marker='o', c=colorAr1)

# Figure representing x3 & x4
fig6 = plt.figure()
fig6.canvas.set_window_title('Color by variables, x3 & x4')
plt.scatter(normalizedX3,normalizedX4,marker='o', c=colorAr1)

plt.show()




