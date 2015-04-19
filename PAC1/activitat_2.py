# author: daniel roca roca486@gmail.com
# Activitat 2 - PAC 1 IAA - UOC 2015

import kmeans_dictio as kmeans
import createWebsDict as cDict

# We treat the original data file and build a dictionary to work with it
dictionary = cDict.createWebsDict()

# We create a dictionary that contains the mean of each property of each web
meansDict = cDict.calculateMeanDictionary(cDict.transformWebsDict(dictionary))

# We calculate the k-mean grouping
kmeansGrouping = kmeans.kmeans_dictio(meansDict, 6, 6)

print (kmeansGrouping[0])


