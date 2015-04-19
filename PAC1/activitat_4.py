# author: daniel roca roca486@gmail.com
# Activitat 4 - PAC 1 IAA - UOC 2015

import kmeans_dictio as kmeans
import createWebsDict as cDict


# Read favorits.data, return a dict with format {usuari: web}
def createFavoritsDict(filename):
    with open(filename,'r') as arxiu:
    	lines = [l.strip().split("\t") for l in arxiu.readlines()]

    dictio = {int(l[0]) : int(l[1])  for l in lines}
    return dictio


# Read both files to compare
webValues = cDict.createWebsDict()
favorits  = createFavoritsDict("favorits.data")   

# Execute memory recommender. Intended output {usuari: [recommended webs]}
for usr in webValues:
	pearson = {usr : zip(*kmeans.weightedRating(webValues, usr, kmeans.pearsonCoeff))[0]}

# Average position of the most liked web for each user
for usr in favorits:
	webPositions = [pearson[usr].index(favorits[usr])]                    

meanPosition = sum(webPositions)/float(len(webPositions))