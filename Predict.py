import matplotlib.pyplot as plt
import csv
import numpy as np
from knn import KNN

f = open('iris.csv')
csv_f = csv.reader(f)

print(1)

knn = KNN()
knn.Load_Dataset('iris.csv')

knn.Determine_Data_Shape('iris.csv')
print(knn.numColumnsOfData)
print(knn.numRowsOfData)

sp0 = 0
sp1 = 0
sp2 = 0

#for row in csv_f:
#    if (int(row[4]) == 0):
#        count += 1
#
#print("There are %s samples of Iris setosa in the sample." % count)

x = knn.data[:,0:1]
y = knn.data[:,1:2]

# Switched from 0:2 to :
trainX = knn.data[::2, 1:3]
trainy = knn.target[::2]

# Switched from 0:2 to :
testX = knn.data[1::2, 1:3]
testy = knn.target[1::2]

colors = np.zeros((3,3),dtype='f')
colors[0,:] = [1.0, 0.5, 0.5]
colors[1,:] = [0.5, 1.0, 0.5]
colors[2,:] = [0.5, 0.5, 1.0]

#print(testX)
#print(testy)

knn.Use_K_Of(15)
knn.Fit(trainX,trainy)

#for i in range(0, 75):
#    actualClass = testy[i]
#    prediction = knn.Predict(testX[i,0:2])
#    print(actualClass, prediction)

# commented out at line 45
plt.figure()


#plt.scatter(trainX[:,0:1], trainX[:,1:2], trainy)
#plt.scatter(testX[:,0:1], testX[:,1:2], testy)

counter = 0
total = 0

[numItems, numFeatures] = knn.data.shape
for i in range(0, numItems/2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass,:]
    plt.scatter(trainX[i,0], trainX[i,1], c = currColor, edgecolors = (0,0,0), lw = 2)

for i in range(0, numItems/2):
    prediction = int(knn.Predict( testX[i,:] ) )
    edgeColor = colors[prediction,:]
    
    itemClass = int(testy[i])
    currColor = colors[itemClass,:]
    plt.scatter(testX[i,0], testX[i,1], c = currColor, edgecolors = edgeColor, lw = 2)

    total += 1
    if prediction != itemClass:
        counter += 1
        print(testX[i,0], testX[i,1])

print(counter)
print(total)
percentCorrect = (float(total - counter) / float(total)) * 100
print("Percent correct: %s%%" % str(percentCorrect))
plt.show()
