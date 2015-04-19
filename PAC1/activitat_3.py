# author: daniel roca roca486@gmail.com
# Activitat 3 - PAC 1 IAA - UOC 2015

import kmeans_dictio as kmeans
import createWebsDict as cDict
import randIndexEvaluation as randEval

# We treat the original data file and build a dictionary to work with it
dictionary = cDict.createWebsDict()

# We create a dictionary that contains the mean of each property of each web
meansDict = cDict.calculateMeanDictionary(cDict.transformWebsDict(dictionary))

# We calculate the k-mean grouping
kmeansGrouping = kmeans.kmeans_dictio(meansDict, 4, 6)

# Calculate the grouping for the adjusted rand index eval
resultGrouping = randEval.buildResultingGroupingArray(kmeansGrouping)

# Define labels_true manually, for the sake of simpicity. We could do it programatically
labels_true = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]

# Calculate the ARI
ari = randEval.evalRandIndex(resultGrouping,labels_true)

print(ari)






