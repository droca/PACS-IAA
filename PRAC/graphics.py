# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PRAC IAA - UOC 2015

from matplotlib.pyplot import *

# This file contains implementation for the methods used for figure's representation
# and output embellishment

# Embellisher of the beginning of a section
def apartatBeginning(apartatName):
	print("# ------------------------------------------------------- #")
	print("# --- %s --- #" % apartatName)
	print("# ------------------------------------------------------- #")
	print("Beginning of %s" % apartatName)
	print()

# Embellisher of the ending of a section
def apartatEnding(apartatName):
	print()
	print("End of %s" % apartatName)
	print()

# Definition of a new figure to be represented using pyplot
def figureDefinition(title, variable1, variable2, color):
	fig1 = figure()
	fig1.canvas.set_window_title(title)
	scatter(variable1,variable2,marker='o', c=color)
	return fig1

def showFigures():
	show()


