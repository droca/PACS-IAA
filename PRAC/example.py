import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB

# turn of data table rendering

def shuffle(data, n):
    ind = data.index
    for i in range(n):
       sampler = np.random.permutation(data.shape[0])
       new_vals = data.take(sampler).values
       data = pd.DataFrame(new_vals, index=ind)
    return data

# Create and plot a linear descision surface
df = pd.DataFrame({'feature_a': np.random.rand(100) * 6, 
                   'feature_b': np.random.rand(100) * 4.2, 
                   'class': 1})
df = df.append(pd.DataFrame({
                   'feature_a': np.random.rand(100) * 6 + 1.7, 
                   'feature_b': np.random.rand(100) * np.random.randint(5,6) + 3.8, 
                   'class': 2}))


df = shuffle(df, 1)
df.columns = ['class', 'feature_a', 'feature_b']
print(df.head())

# Create a training set of 3/4 of the data
train_n = 150

train_features = df[['feature_a', 'feature_b']][:train_n]
train_labels = df['class'][:train_n]
print(train_features.describe())

# Create a test set of 1/4 of the data to evaluate the classifier
test_features = df[['feature_a', 'feature_b']][train_n:]
test_labels = df['class'][train_n:]
print(test_features.describe())

# Train a Gaussian Naive Bayes Classifier
clf = GaussianNB()
clf.fit(train_features, train_labels)


# Query the accuracy of the model with the test set
accuracy = clf.score(test_features, test_labels)
print("Accuracy: ",accuracy)