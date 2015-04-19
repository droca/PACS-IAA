# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 2 IAA - UOC 2015

import fileProcessing as fp
from sklearn.decomposition import PCA

# --- Activitat 1 --- #
def allComponentsPCA(numpyArray):
	# New PCA class instance
	pca = PCA()
	pca.fit(numpyArray)

	# How many components are required to explain 95% of the variance
	acumvar = [sum(pca.explained_variance_ratio_[:i]) 
		for i in range(len(pca.explained_variance_ratio_))]
	print(list(zip(range(len(acumvar)), acumvar)))

# --- Program execution --- #
numpyArray = fp.readFileData()
normalised = fp.dataNormalization(numpyArray)

allComponentsPCA(normalised)

