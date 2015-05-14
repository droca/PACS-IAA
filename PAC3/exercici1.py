# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 3 IAA - UOC 2015

from naive_bayes import *
from decisionTree import *
from knn import *
from vectorMachine import *

FILE = 'Wholesale_customers.txt'

# Read the file
l = readFile(FILE)
# Evaluation and classification of the data
classification(l)

method = input("Choose what do you want to execute: knn, bayes, tree, vector: ")
if method == 'knn':
  knn(l)
elif method == 'bayes':
  naiveBayes(l)
elif method == 'tree':
  decisionTree(l)
elif method == 'vector':
  vectorMachine(FILE)