# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 2 IAA - UOC 2015

import fileProcessing as fp
import numpy as np
from sklearn.decomposition import PCA

# --- Activitat 1 --- #
def pcaComponentsCalc(numpyArray):
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

# --- Program execution --- #
rawData = fp.readFileData()
normalised = fp.dataNormalization(rawData)
print("The number of components needed for the 95% variance acceptance is: ", pcaComponentsCalc(normalised))
