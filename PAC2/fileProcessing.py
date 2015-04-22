# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 2 IAA - UOC 2015

import numpy as np
from sklearn.decomposition import PCA


# Creates a matrix with all the values for all customers
# We are assuming that the first line of the source file is a header that contains
# no important data for the study
# We are also assuming that the first two values of each line also don't have
# important value

def readFileData(filename="Wholesale customers.csv"):

	# Reading the file
	with open(filename,'r') as dades:
		dades.readline() # we are skipping the first line of the file, it's a header
		# Data extraction converting the strings to integers for easier processing
		lines = list(map(lambda l: [int(i) for i in (l.strip().split(","))],
			dades.readlines()))

	return lines

# Extracts the channel of the data array
# The first element of each row is the value of the channel
# Returns an array with all the channels
def channelsExtraction(array):
	channels = []
	for i in array:
		channels.append(i[0])

	return channels

# Extracts the region of the data array
# The second element of each row is the value of the region
# Returns an array with all the regions
def regionsExtraction(array):
	regions = []
	for i in array:
		regions.append(i[1])

	return regions

# Removes the channel & the region values from the array
def arrayCleanup(array):
	for i in array:
		i.pop(0)
		i.pop(0)
	return array

# Converts a normal array into a numpy array
def convertToNumpyArray(array):
	array = np.array(array)
	return array

# Calculate mean of the provided numpy array values
def meanCalculation(numpyArray):
	mean = list(map(np.average, numpyArray))
	return mean

# Calculate Standard Deviation of the provided numpy array values
def stdDeviationCalculation(numpyArray):
	stdDev = list(map(np.std, numpyArray))
	return stdDev

# Data normalisation
def dataNormalization(array):
	array = arrayCleanup(array)
	numpyArray = convertToNumpyArray(array)
	mean = meanCalculation(numpyArray)
	stdDev = stdDeviationCalculation(numpyArray)
	numpyArray = [list(map(lambda i: (i - mean[j]) / stdDev[j], numpyArray[j]))
		for j in range(len(numpyArray))]
	return numpyArray

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


