# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PRAC IAA - UOC 2015

from variablesCreator import *
from dataProcessing import *
from graphics import *
from math import exp

OBSERVATIONS_NUMBER = 1000
APARTAT = {
	"a":"Apartat A",
	"b":"Apartat B",
	"c":"Apartat C",
	"d":"Apartat D"
}
FIGURE = {
	"x1x2":"Color by variables, x1 & x2",
	"x1x3":"Color by variables, x1 & x3",
	"x1x4":"Color by variables, x1 & x4",
	"x2x3":"Color by variables, x2 & x3",
	"x2x4":"Color by variables, x2 & x4",
	"x3x4":"Color by variables, x3 & x4"
}

# ------------------------------------------------------- #
# --- Apartat A --- #
# ------------------------------------------------------- #

apartatBeginning(APARTAT["a"])

# Generate the values for the variables x1..x4
x1 = createVariable('x1', OBSERVATIONS_NUMBER, 0.5, 0.1)
x2 = createVariable('x2', OBSERVATIONS_NUMBER, 4.5, 0.6)
x3 = createVariableEscalarMultiplication('x3', OBSERVATIONS_NUMBER, 3, x1)
x4 = createVariableExpAndSum('x4', OBSERVATIONS_NUMBER, 2, x1, x2)
print('All arrays correctly generated, proceeding to build the matrix')

# Build the matrix, with the data of the 4 variables
matrix = buildMatrix(x1, x2, x3, x4)

apartatEnding(APARTAT["a"])

# ------------------------------------------------------- #
# --- Apartat B --- #
# ------------------------------------------------------- #

apartatBeginning(APARTAT["b"])

# Normalise the data of the variables so we can compare and plot them correctly
normX1 = dataNormalization(x1, 0.5, 0.1)
normX2 = dataNormalization(x2, 4.5, 0.6)
normX3 = dataNormalization(x3)
normX4 = dataNormalization(x4)

# Array for color of the points
colorAr1 = [0]*int((OBSERVATIONS_NUMBER/2))
colorAr2 = [1]*int((OBSERVATIONS_NUMBER/2))
colorAr1.extend(colorAr2)

# Figures representing variable combinations
fig1 = figureDefinition(FIGURE["x1x2"], normX1, normX2, colorAr1)
fig2 = figureDefinition(FIGURE["x1x3"], normX1, normX3, colorAr1)
fig3 = figureDefinition(FIGURE["x1x4"], normX1, normX4, colorAr1)
fig4 = figureDefinition(FIGURE["x2x3"], normX2, normX3, colorAr1)
fig5 = figureDefinition(FIGURE["x2x4"], normX2, normX4, colorAr1)
fig6 = figureDefinition(FIGURE["x3x4"], normX3, normX4, colorAr1)


inText = input("Do you want to see the figures now? If you say yes, you'll have to close all the pop up windows before continuing the program execution (y/n)")
if inText=="y":
	showFigures()

apartatEnding(APARTAT["b"])

# ------------------------------------------------------- #
# --- Apartat C --- #
# ------------------------------------------------------- #

apartatBeginning(APARTAT["c"])

# Unite all the normalized variables in a matrix
normMatrix = buildMatrix(normX1, normX2, normX3, normX4)

# Calculate and print how many components are needed to reach the 95% acceptance
pcaComponentsCalc(normMatrix)

apartatEnding(APARTAT["c"])

# ------------------------------------------------------- #
# --- Apartat D --- #
# ------------------------------------------------------- #

apartatBeginning(APARTAT["d"])

# Generate the values of 4 variables with the same mean and stDev
# Those are independent variables, not dependant from each other
newx1 = createVariable('newx1', OBSERVATIONS_NUMBER, 1, 0.1)
newx2 = createVariable('newx2', OBSERVATIONS_NUMBER, 1, 0.1)
newx3 = createVariable('newx3', OBSERVATIONS_NUMBER, 1, 0.1)
newx4 = createVariable('newx4', OBSERVATIONS_NUMBER, 1, 0.1)

# Normalise the data of the variables so we can compare and plot them correctly
newx1Norm = dataNormalization(newx1, 1, 0.1)
newx2Norm = dataNormalization(newx2, 1, 0.1)
newx3Norm = dataNormalization(newx3, 1, 0.1)
newx4Norm = dataNormalization(newx4, 1, 0.1)

# Unite all the normalized variables in a matrix
newMatrixNorm = buildMatrix(newx1Norm, newx2Norm, newx3Norm, newx4Norm)

# Calculate and print how many components are needed to reach the 95% acceptance
pcaComponentsCalc(newMatrixNorm)
apartatEnding(APARTAT["d"])









