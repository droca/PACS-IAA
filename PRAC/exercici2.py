# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PRAC IAA - UOC 2015

from graphics import *
from variablesCreator import *
from numpy import *
from sklearn.naive_bayes import GaussianNB
import pandas as pd

OBSERVATIONS_NUMBER = 2000
APARTAT = {
	"a":"Apartat A",
	"b":"Apartat B",
	"c":"Apartat C",
	"d":"Apartat D"
}

def shuffle(df):
	df = df.copy()
	df.apply(random.shuffle,axis=1)
	return df

# ------------------------------------------------------- #
# --- Apartat A --- #
# ------------------------------------------------------- #

apartatBeginning(APARTAT["a"])

# Generate the values for A1 data set
mean = [5,-4]
cov = [[2,-1],[-1,2]]
A1 = createBidimensionalVariable(mean, cov, OBSERVATIONS_NUMBER)

# Generate the values for A2 data set
mean = [1,-3]
cov = [[1,1.5],[1.5,3]]
A2 = createBidimensionalVariable(mean, cov, OBSERVATIONS_NUMBER)

apartatEnding(APARTAT["a"])

# ------------------------------------------------------- #
# --- Apartat B --- #
# ------------------------------------------------------- #

apartatBeginning(APARTAT["b"])

# Array for color of the points
colorAr1 = [[0, 0]]*int(OBSERVATIONS_NUMBER/2)
colorAr2 = [[1, 1]]*int(OBSERVATIONS_NUMBER/2)
colorAr1.extend(colorAr2)

# Data representation in a graphic
fig1 = figureDefinition("Nuvol de punts, A1 & A2", A1, A2, colorAr1)

inText = input("Do you want to see the figures now? If you say yes, you'll have to close all the pop up windows before continuing the program execution (y/n)")
if inText=="y":
	showFigures()

apartatEnding(APARTAT["b"])

# ------------------------------------------------------- #
# --- Apartat C --- #
# ------------------------------------------------------- #

apartatBeginning(APARTAT["c"])

# We add a new element in the values of A1 and A2, representing its class
A1=insert(A1,2,1,axis=1)
A2=insert(A2,2,2,axis=1)

# We create DataFrames for A1 and A2 and append them
dataA1 = pd.DataFrame(A1)
dataA2 = pd.DataFrame(A2)
data = dataA1.append(dataA2)

shuffle(data)

train_num = 1000

train_features = data[[0,1]][:train_num]
train_labels = data[2][:train_num]
print(train_features.describe())

# Create a test set of 1/4 of the data to evaluate the classifier
test_features = data[[0,1]][train_num:]
test_labels = data[2][train_num:]
print(test_features.describe())

# Train a Gaussian Naive Bayes Classifier
clf = GaussianNB()
clf.fit(train_features, train_labels)


# Query the accuracy of the model with the test set
accuracy = clf.score(test_features, test_labels)
print("Accuracy: ",accuracy)

apartatEnding(APARTAT["c"])

# ------------------------------------------------------- #
# --- Apartat D --- #
# ------------------------------------------------------- #

apartatBeginning(APARTAT["d"])


# Generate the values for A1 data set
mean = [2,-4]
cov = [[2,-1],[-1,2]]
A1 = createBidimensionalVariable(mean, cov, OBSERVATIONS_NUMBER)

# We add a new element in the values of A1 and A2, representing its class
A1=insert(A1,2,1,axis=1)

# We create DataFrames for A1 and A2 and append them
dataA1 = pd.DataFrame(A1)
dataA2 = pd.DataFrame(A2)
data = dataA1.append(dataA2)

shuffle(data)

train_num = 1000

train_features = data[[0,1]][:train_num]
train_labels = data[2][:train_num]
print(train_features.describe())

# Create a test set of 1/4 of the data to evaluate the classifier
test_features = data[[0,1]][train_num:]
test_labels = data[2][train_num:]
print(test_features.describe())

# Train a Gaussian Naive Bayes Classifier
clf = GaussianNB()
clf.fit(train_features, train_labels)


# Query the accuracy of the model with the test set
accuracy = clf.score(test_features, test_labels)
print("Accuracy: ",accuracy)


apartatEnding(APARTAT["d"])

