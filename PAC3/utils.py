# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 3 IAA - UOC 2015

# class definition
C1 = 1
C2 = 2
C3 = 3
C4 = 4
C5 = 5
C6 = 6

# We read the file with the filename provided
# We are assuming that the file is always in the same folder
def readFile(filename):
	with open(filename,'r') as dades:
	# we are skipping the first line of the file, it's a header
		dades.readline()
		# Data extraction converting the strings to integers for easier processing
		l = list(map(lambda l: [int(i) for i in (l.strip().split(","))],dades.readlines()))
	return l

# We evaluate the combinations in the first two columns
# then we add the corresponding class as the last column
# In the end of the process, we delete the two first columns

# This way we end up having the data classified in 6 classes
def classification(l):

  for i in l:
    if i[0] == 1:
      if i[1] == 1:
        i.append(C1)
      if i[1] == 2:
        i.append(C2)
      if i[1] == 3:
        i.append(C3)
    elif i[0] == 2:
      if i[1] == 1:
        i.append(C4)
      if i[1] == 2:
        i.append(C5)
      if i[1] == 3:
        i.append(C6)

  for i in l:
    i.pop(0)
    i.pop(0)

# Build up the training, 2 out of 3 elements
def training(l):
	train = list(map(lambda x: x[1],
                 filter(lambda v: v[0] % 3 != 0, enumerate(l))))
	return train

def classesTrain(train):
	classesTrain = list(map(lambda x: x.pop(), train))
	return classesTrain







