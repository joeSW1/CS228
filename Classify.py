# Deliverable 5
# Classify.py
# 9/29/2019

import sys
sys.path.insert(0, '..')
import Leap
import numpy as np
import pickle
import os
import shutil
import matplotlib.pyplot as plt
import csv
import numpy as np
from knn import KNN

from random import randint
from pygameWindow_Del03 import PYGAME_WINDOW
from constants import pygameWindowWidth
from constants import pygameWindowDepth
from Deliverable import DELIVERABLE

train4 = ("userData/train4.p")
train5 = ("userData/train5.p")
test4 = ("userData/test4.p")
test5 = ("userData/test5.p")

pickle_in = open(train4, "rb")
train4 = pickle.load(pickle_in)
pickle_in = open(train5, "rb")
train5 = pickle.load(pickle_in)

pickle_in = open(test4, "rb")
test4 = pickle.load(pickle_in)
pickle_in = open(test5, "rb")
test5 = pickle.load(pickle_in)
#print(gestureData)
#print(gestureData.shape)

def ReshapeData(set1,set2):
    X = np.zeros((2000,5*2*3),dtype='f')
    Y = np.zeros((2000,5*4*6),dtype='f')
    
    for row in range(0,1000):
        Y[row] = 4
        Y[row + 1000] = 5
        col = 0
        for finger in range(0,5):
            for bone in range(0,2):
                for coord in range(0,3):
                    X[row,col] = set1[finger,bone,coord,row]
                    secondTrainRow = row + 1000
                    X[secondTrainRow,col] = set2[finger,bone,coord,row]
                    col = col + 1
    return X, Y

def ReduceData(X):
    X = np.delete(X,1,1)
    X = np.delete(X,1,1)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    return X

def CenterData(X):
    # Centering x data
    allXCoordinates = X[:,:,0,:]
    meanValue = allXCoordinates.mean()
    X[:,:,0,:] = allXCoordinates - meanValue
    # Centering y data
    allYCoordinates = X[:,:,1,:]
    meanValue = allYCoordinates.mean()
    X[:,:,1,:] = allYCoordinates - meanValue
    # Centering z data
    allZCoordinates = X[:,:,2,:]
    meanValue = allZCoordinates.mean()
    X[:,:,2,:] = allZCoordinates - meanValue
    return X

train4 = ReduceData(train4)
train5 = ReduceData(train5)
test4 = ReduceData(test4)
test5 = ReduceData(test5)

train4 = CenterData(train4)
train5 = CenterData(train5)
test4 = CenterData(test4)
test5 = CenterData(test5)

trainX, trainy = ReshapeData(train4,train5)
testX, testy = ReshapeData(test4, test5)

knn = KNN()
knn.Use_K_Of(15)


knn.Fit(trainX,trainy[:,0])

actualClass = testy[0]
prediction = knn.Predict(testX[0,:])
#print(actualClass, prediction)

#prediction = knn.Predict(testX[1])
#print(prediction)
counter = 0
for row in range(0,2000):
    prediction = int(knn.Predict(testX[row,:]))
    if prediction == int(testy[row,0]):
        counter += 1
print("Number correct is %s" % str(counter))










