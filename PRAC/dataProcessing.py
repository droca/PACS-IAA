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
	#array = arrayCleanup(array)
	# I'm not sure of this step, since we are already working with numpy arrays
	# numpyArray = convertToNumpyArray(array)
	if (mean==None): 	mean = meanCalculation(array)
	if (stdDev==None): stdDev = stdDeviationCalculation(array)
	for i in range(len(array)):
		array[i] = (array[i]-mean) / stdDev
	return array

# Calculation of how many components are needed to achieve the 95% variance
def pcaComponentsCalc(array):

	numpyArray = dataNormalization(array)
	# New PCA class instance
	pca = PCA()
	# With all components
	pca.fit(numpyArray)

	# Sum of the variances for each component
	# With this progression we can see clearly how many components
	# do we need to achieve the 95% of acceptance
	progress = [sum(pca.explained_variance_ratio_[:i]) 
		for i in range(len(pca.explained_variance_ratio_))]

	print("Progression of components and '%' of acceptance: ")
	print(list(zip(range(len(progress)), progress)))

	# Actually return the number of components needed for the 95% variance
	for numberComps in progress:
		if numberComps >= 0.95:
			break
	return np.where(progress==numberComps)[0][0]

# Calculate the pca with the number of components passed as parameter
def pcaWithComponents(array, numComponents):

	numpyArray = dataNormalization(array)

	pca = PCA(n_components=numComponents)
	pca.fit(numpyArray)

	# NumpyArray is projected on the first principal components previous 
	# extracted from a training set.
	projection = pca.transform(numpyArray)

	return projection



