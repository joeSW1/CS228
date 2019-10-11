# RealTimeDraw.py
# deliverable 2 program for Del6
# 10/03/2019

import sys
sys.path.insert(0, '../..')
import Leap
sys.path.insert(0, '..')
from random import randint
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowWidth
from constants import pygameWindowDepth
import numpy as np
import pickle

clf = pickle.load( open('userData/classifier.p','rb') )
testData = np.zeros( (1,30), dtype='f')

x = (pygameWindowWidth/2)
y = (pygameWindowDepth/2)

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

def Perturb_Circle_Position():
    global x, y
    fourSidedDieRoll = randint(1,4)
    if fourSidedDieRoll == 1:
        x -= 1
    elif fourSidedDieRoll == 2:
        x += 1
    elif fourSidedDieRoll == 3:
        y -= 1
    else:
        y += 1


pygameWindow = PYGAME_WINDOW()
print(pygameWindow)


def Handle_Frame(frame):
    global x, y, xMin, xMax, yMin, yMax, testData
    hand = frame.hands[0]
    fingers = hand.fingers
    for finger in fingers:
        Handle_Finger(finger)
    testData = CenterData(testData)
    predictedClass = clf.Predict(testData)
    print(predictedClass)
    
def Handle_Finger(finger):
    for b in range(0, 4):
        Handle_Bone(finger, b)

def Handle_Bone(finger, b):
    global k, testData
    bone = finger.bone(b)
    base = bone.prev_joint
    tip = bone.next_joint
    xBase, yBase, zBase = Handle_Vector_From_Leap(base)
    xTip, yTip, zTip = Handle_Vector_From_Leap(tip)
    pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, b)
    if ( (b==0) or (b==3) ):
            testData[0,k] = xTip
            testData[0,k+1] = yTip
            testData[0,k+2] = zTip
            k = k + 3
    # print("Base coordinates are %s and %s" % (base[0], base[1]))
    # print("Tip coordinates are %s and %s" % (tip[0], tip[1]))

def Handle_Vector_From_Leap(v):
    global xRawMin, xRawMax, yRawMin, yRawMax, xScaledMin, xScaledMax, yScaledMin, yScaledMax, zRawMin, zRawMax, zScaledMin, zScaledMax
    
    scaledX = Scale(v[0], xRawMin, xRawMax, xScaledMin, xScaledMax)
    scaledY = Scale(v[2], yRawMin, yRawMax, yScaledMin, yScaledMax)
    scaledZ = Scale(v[1], zRawMin, zRawMax, zScaledMin, zScaledMax)
    return (scaledX, scaledY, scaledZ)
    
#    indexFingerList = fingers.finger_type(1)
#    indexFinger = indexFingerList[0]
#    distalPhalanx = indexFinger.bone(3)
#    tip = distalPhalanx.next_joint
#    x = int(tip[0])
#    y = int(tip[1])
    #print(x)
    #print(y)
##    if (x < xMin):
##        xMin = x
##    if (x > xMax):
##        xMax = x
##    if (y < yMin):
##        yMin = y
##    if (y > yMax):
##        yMax = y
##    print("x: %x to %x" % (xMin,xMax))
##    print("y: %x to %x" % (yMin,yMax))

# Raw mins and maxes derived from testing found above (it is now commented out)
xRawMin = -70
xRawMax = 244
yRawMin = -120
yRawMax = 204
#yRawMin = 730
#yRawMax = -21
zRawMin = 400
zRawMax = -30


xScaledMin = 0
xScaledMax = 800
yScaledMin = 0
yScaledMax = 650
zScaledMin = 0
zScaledMax = 800

def Scale(value, rawMin, rawMax, scaledMin, scaledMax):
    rawFromLeft = value - rawMin
    ratio = float(float(rawFromLeft) / float(-rawMin + rawMax))
    scaledValue = int(ratio * scaledMax)
    return scaledValue

def CenterData(X):
    # Centering x data
    allXCoordinates = X[0,::3]
    meanValue = allXCoordinates.mean()
    X[0,::3] = allXCoordinates - meanValue
    # Centering y data
    allYCoordinates = X[0,1::3]
    meanValue = allYCoordinates.mean()
    X[0,1::3] = allYCoordinates - meanValue
    # Centering z data
    allZCoordinates = X[0,2::3]
    meanValue = allZCoordinates.mean()
    X[0,2::3] = allZCoordinates - meanValue
    return X

controller = Leap.Controller()

while True:
    pygameWindow.Prepare()
    
    frame = controller.frame()
    handlist = frame.hands
    for hand in handlist:
        if(str(hand) > 0):
            k = 0
            Handle_Frame(frame)

    pygameWindow.Reveal()
