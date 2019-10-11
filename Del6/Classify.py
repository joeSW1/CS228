# Deliverable 6
# Classify.py
# 10/03/2019

import sys
sys.path.insert(0, '../..')
import Leap
sys.path.insert(0, '..')
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

train0 = ("userData/Ortigara_train0.p")
train1 = ("userData/Ortigara_train1.p")
train2 = ("userData/Ortigara_train2.p")
train3 = ("userData/Ortigara_train3.p")
train4 = ("userData/Ortigara_train4.p")
train5 = ("userData/Ortigara_train5.p")
train6 = ("userData/Ortigara_train6.p")
train7 = ("userData/Ortigara_train7.p")
train8 = ("userData/Ortigara_train8.p")
train9 = ("userData/Ortigara_train9.p")

test0 = ("userData/Ortigara_test0.p")
test1 = ("userData/Ortigara_test1.p")
test2 = ("userData/Ortigara_test2.p")
test3 = ("userData/Ortigara_test3.p")
test4 = ("userData/Ortigara_test4.p")
test5 = ("userData/Ortigara_test5.p")
test6 = ("userData/Ortigara_test6.p")
test7 = ("userData/Ortigara_test7.p")
test8 = ("userData/Ortigara_test8.p")
test9 = ("userData/Ortigara_test9.p")

# Reading in training sets
pickle_in = open(train0, "rb")
train0 = pickle.load(pickle_in)
pickle_in = open(train1, "rb")
train1 = pickle.load(pickle_in)
pickle_in = open(train2, "rb")
train2 = pickle.load(pickle_in)
pickle_in = open(train3, "rb")
train3 = pickle.load(pickle_in)
pickle_in = open(train4, "rb")
train4 = pickle.load(pickle_in)
pickle_in = open(train5, "rb")
train5 = pickle.load(pickle_in)
pickle_in = open(train6, "rb")
train6 = pickle.load(pickle_in)
pickle_in = open(train7, "rb")
train7 = pickle.load(pickle_in)
pickle_in = open(train8, "rb")
train8 = pickle.load(pickle_in)
pickle_in = open(train9, "rb")
train9 = pickle.load(pickle_in)

# Reading in test sets
pickle_in = open(test0, "rb")
test0 = pickle.load(pickle_in)
pickle_in = open(test1, "rb")
test1 = pickle.load(pickle_in)
pickle_in = open(test2, "rb")
test2 = pickle.load(pickle_in)
pickle_in = open(test3, "rb")
test3 = pickle.load(pickle_in)
pickle_in = open(test4, "rb")
test4 = pickle.load(pickle_in)
pickle_in = open(test5, "rb")
test5 = pickle.load(pickle_in)
pickle_in = open(test6, "rb")
test6 = pickle.load(pickle_in)
pickle_in = open(test7, "rb")
test7 = pickle.load(pickle_in)
pickle_in = open(test8, "rb")
test8 = pickle.load(pickle_in)
pickle_in = open(test9, "rb")
test9 = pickle.load(pickle_in)

#print(gestureData)
#print(gestureData.shape)

def ReshapeData(set0,set1,set2,set3,set4,set5, set6, set7, set8, set9):
    # add 1000
    X = np.zeros((10000,5*2*3),dtype='f')
    Y = np.zeros((10000,5*4*6),dtype='f')
    
    for row in range(0,1000):
        # add 1000
        Y[row] = 0
        Y[row + 1000] = 1
        Y[row + 2000] = 2
        Y[row + 3000] = 3
        Y[row + 4000] = 4
        Y[row + 5000] = 5
        Y[row + 6000] = 6
        Y[row + 7000] = 7
        Y[row + 8000] = 8
        Y[row + 9000] = 9
        col = 0
        for finger in range(0,5):
            for bone in range(0,2):
                for coord in range(0,3):
                    # add 1000
                    X[row,col] = set0[finger,bone,coord,row]
                    trainRow1 = row + 1000
                    X[trainRow1,col] = set1[finger,bone,coord,row]
                    trainRow2 = row + 2000
                    X[trainRow2,col] = set2[finger,bone,coord,row]
                    trainRow3 = row + 3000
                    X[trainRow3,col] = set3[finger,bone,coord,row]
                    trainRow4 = row + 4000
                    X[trainRow4,col] = set4[finger,bone,coord,row]
                    trainRow5 = row + 5000
                    X[trainRow5,col] = set5[finger,bone,coord,row]
                    trainRow6 = row + 6000
                    X[trainRow6,col] = set6[finger,bone,coord,row]
                    trainRow7 = row + 7000
                    X[trainRow7,col] = set7[finger,bone,coord,row]
                    trainRow8 = row + 8000
                    X[trainRow8,col] = set8[finger,bone,coord,row]
                    trainRow9 = row + 9000
                    X[trainRow9,col] = set9[finger,bone,coord,row]
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
    allYCoordinates = X[:,:,2,:]
    meanValue = allYCoordinates.mean()
    X[:,:,1,:] = allYCoordinates - meanValue
    # Centering z data
    allZCoordinates = X[:,:,1,:]
    meanValue = allZCoordinates.mean()
    X[:,:,2,:] = allZCoordinates - meanValue
    return X

# add new one
train0 = ReduceData(train0)
train1 = ReduceData(train1)
train2 = ReduceData(train2)
train3 = ReduceData(train3)
train4 = ReduceData(train4)
train5 = ReduceData(train5)
train6 = ReduceData(train6)
train7 = ReduceData(train7)
train8 = ReduceData(train8)
train9 = ReduceData(train9)

# add new one
test0 = ReduceData(test0)
test1 = ReduceData(test1)
test2 = ReduceData(test2)
test3 = ReduceData(test3)
test4 = ReduceData(test4)
test5 = ReduceData(test5)
test6 = ReduceData(test6)
test7 = ReduceData(test7)
test8 = ReduceData(test8)
test9 = ReduceData(test9)

# add new one
train0 = CenterData(train0)
train1 = CenterData(train1)
train2 = CenterData(train2)
train3 = CenterData(train3)
train4 = CenterData(train4)
train5 = CenterData(train5)
train6 = CenterData(train6)
train7 = CenterData(train7)
train8 = CenterData(train8)
train9 = CenterData(train9)

# add new one
test0 = CenterData(test0)
test1 = CenterData(test1)
test2 = CenterData(test2)
test3 = CenterData(test3)
test4 = CenterData(test4)
test5 = CenterData(test5)
test6 = CenterData(test6)
test7 = CenterData(test7)
test8 = CenterData(test8)
test9 = CenterData(test9)

# add new one
trainX, trainy = ReshapeData(train0, train1, train2, train3, train4, train5, train6, train7, train8, train9)
testX, testy = ReshapeData(test0, test1, test2, test3, test4, test5, test6, test7, test8, test9)

knn = KNN()
knn.Use_K_Of(25)

trainX = trainX.astype(int)
trainy = trainy.astype(int)
knn.Fit(trainX,trainy[:,0])

actualClass = testy[0]
prediction = knn.Predict(testX[0,:])
#print(actualClass, prediction)

#prediction = knn.Predict(testX[1])
#print(prediction)
counter = 0
# add 1000
for row in range(0,10000):
    prediction = int(knn.Predict(testX[row,:]))
    if prediction == int(testy[row,0]):
        counter += 1
print("Number correct is %s" % str(counter))

pickle.dump(knn, open('userData/classifier.p','wb'))








