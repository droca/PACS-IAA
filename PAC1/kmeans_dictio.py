#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Modifications: daniel roca roca486@gmail.com
# PAC 1 IAA Assets - UOC 2015

# This file contains the methods used to calculate distances, grouping and compare
# qualities

from random import sample
from itertools import repeat
from math import sqrt

def euclideanDist(dic1, dic2):
    # Compute the sum of squares of the elements common
    # to both dictionaries
    sum2 = sum([pow(dic1[elem]-dic2[elem], 2)
                for elem in dic1 if elem in dic2])
    return sqrt(sum2)

def euclideanSimilarity(dic1, dic2):
    return 1/(1+euclideanDist(dic1, dic2))
    
# Given a dictionary like {key1 : {key2 : value}} it computes k-means
# clustering, with k groups, executing maxit iterations at most, using
# the specified similarity function.
# It returns two things (as a tuple):
# -{key1:cluster number} with the cluster assignemnts (which cluster
#  does each element belong to
# -[{key2:values}] a list with the k centroids (means of the values
#  for each cluster.
# Recall that input dictionary can be sparse, and that will be reflected
# on the centroids list.
def kmeans_dictio(dictionary, k, maxit, similarity = euclideanSimilarity):
    
   # First k random points are taken as initial centroids.
   # Each centroid is {key2 : value}
   centroids = [dictionary[x] for x in sample(dictionary.keys(), k)]
   
   # Assign each key1 to a cluster number 
   previous   = {}
   assignment = {}
   
   # On each iteration it assigns points to the centroids and computes
   # new centroids
   for it in range(maxit):

       # Assign points to the closest centroids
       for key1 in dictionary:
           simils = list(map(similarity,repeat(dictionary[key1],k), centroids))
           assignment[key1] = simils.index(max(simils))           

       # If there are no changes in the assignment then finish
       if previous == assignment:
           break
       previous.update(assignment)
        
       # Recompute centroids: annotate each key values at each centroid
       values   = {x : {} for x in range(k)}
       counters = {x : {} for x in range(k)}
       for key1 in dictionary:
           group = assignment[key1]
           for key2 in dictionary[key1]:
               if key2 not in values[group]:
                   values   [group][key2] = 0
                   counters [group][key2] = 0
               values  [group][key2] += dictionary[key1][key2]
               counters[group][key2] += 1
        
       # Compute means (new centroids)
       centroids = []
       for group in values:
           centr = {}
           for key2 in values[group]:
               centr[key2] = values[group][key2] / counters[group][key2]
           centroids.append(centr)
       
       if None in centroids: break

   return (assignment, centroids)


def pearsonCoeff(dic1, dic2):
    # Retrieve the elements common to both dictionaries
    commons  = [x for x in dic1 if x in dic2]
    nCommons = float(len(commons))

    # If there are no common elements, return zero; otherwise
    # compute the coefficient
    if nCommons==0:
        return 0

    mean1 = 0
    mean2 = 0
    # Compute the means of each dictionary
    for x in commons:
      mean1 = mean1 + sum(dic1[x].values())
      mean2 = mean2 + sum(dic2[x].values())
    
    mean1 = mean1/nCommons
    mean2 = mean2/nCommons

    '''
    mean1 = sum([dic1[x].values() for x in commons])/nCommons
    mean2 = sum([dic2[x].values() for x in commons])/nCommons
    '''

    # Compute numerator and denominator
    for x in commons:
      num =  num + sum(dic1[x]-mean1)

    num  = sum([(dic1[x]-mean1)*(dic2[x]-mean2) for x in commons])
    den1 = sqrt(sum([pow(dic1[x]-mean1, 2) for x in commons]))
    den2 = sqrt(sum([pow(dic2[x]-mean2, 2) for x in commons]))
    den  = den1*den2

    # Compute the coefficient if possible or return zero
    if den==0:
        return 0

    return num/den

# Produces a sorted list of weighted ratings from a dictionary of
# user ratings and a user id.
# You can choose the function of similarity between users.
def weightedRating(dictio, user, similarity = pearsonCoeff):
    # In the first place a dictionary is generated with the similarities
    # of our user with all other users.
    # This dictionary could be stored to avoid recomputing it.
    simils = {x: similarity(dictio[user], dictio[x])
              for x in dictio if x != user}

    # Auxiliary dictionaries {movieId: [rating*users similarity]}
    # and {movieId: [users similarity]} (numerator and denominator
    # of the weighted rating)
    numerator   = {}
    denominator = {}

    # The ratings dictionary is traversed, while filling the auxiliary
    # dictionaries with the values found.
    for userId in simils:
        for movieId in dictio[userId]:
            if not numerator.has_key(movieId):
                numerator  [movieId] = []
                denominator[movieId] = []
            s = simils[userId]
            numerator  [movieId].append(sum(dictio[userId][movieId])*s)
            denominator[movieId].append(s)

    # Compute and sort weighted ratings    
    result = []
    for movieId in numerator:
        s1 = sum(numerator  [movieId])
        s2 = sum(denominator[movieId])
        if s2 == 0:
            mean = 0.0
        else:
            mean = s1/s2
        result.append((movieId,mean))

    result.sort(key = lambda x: x[1], reverse=True)
    return result

