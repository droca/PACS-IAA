# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PRAC IAA - UOC 2015

from numpy import *
from sklearn.decomposition import PCA

# This file contains the implementation of all the methods needed
# for processing the array's data

# Converts a normal array into a numpy array
def convertToNumpyArray(array):
	array = array(array)
	return array

# Calculate mean of the provided numpy array values
def meanCalculation(numpyArray):
	mean = average(numpyArray)
	return mean

# Calculate Standard Deviation of the provided numpy array values
def stdDeviationCalculation(numpyArray):
	stdDev = std(numpyArray)
	return stdDev

# Data normalisation, knowing the mean and the stdDev
def dataNormalization(array, mean=None, stdDev=None):
	if (mean==None): 	mean = meanCalculation(array)
	if (stdDev==None): stdDev = stdDeviationCalculation(array)
	for i in range(len(array)):
		array[i] = (array[i]-mean) / stdDev
	return array

# Calculation of how many components are needed to achieve the 95% variance
def pcaComponentsCalc(numpyArray):

	# New PCA class instance
	pca = PCA()
	pca.fit(numpyArray)

	# Sum of the variances for each component
	# With this progression we can see clearly how many components
	# do we need to achieve the 95% of acceptance
	# If that percentage cannot be reached, it returns nothing
	progress = [sum(pca.explained_variance_ratio_[:i]) 
		for i in range(len(pca.explained_variance_ratio_)+1)]

	print("Progression of components and '%' of acceptance: ")
	print(list(zip(range(len(progress)), progress)))
	
	# Actually return the number of components needed for the 95% variance
	for i in progress:
		if i >= 0.95:
			break

	if i >= 0.95:
		compNumber = where(progress==i)[0][0]
		print ("The number of components needed for the 95% is: ", compNumber)
		return compNumber
	else:
		print("The 95% of confidence cannot be reached with this data")
		return

# Calculate the pca with the number of components passed as parameter
def pcaWithComponents(numpyArray, numComponents):

	pca = PCA(n_components=numComponents)
	pca.fit(numpyArray)

	# NumpyArray is projected on the first principal components previous 
	# extracted from a training set.
	projection = pca.transform(numpyArray)

	return projection



