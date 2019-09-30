# RealTimeDraw.py
# deliverable 3 program
# 9/16/2019

import sys
sys.path.insert(0, '..')
import Leap
import numpy as np
import pickle
import os
import shutil

from random import randint
from pygameWindow_Del03 import PYGAME_WINDOW
from constants import pygameWindowWidth
from constants import pygameWindowDepth
from Deliverable import DELIVERABLE

gestureData = np.zeros((5,4,6),dtype='f')

x = (pygameWindowWidth/2)
y = (pygameWindowDepth/2)

##xMin = 1000.0
##xMax = -1000.0
##yMin = 1000.0
##yMax = -1000.0

##def Perturb_Circle_Position():
##   global x, y
##    fourSidedDieRoll = randint(1,4)
##    if fourSidedDieRoll == 1:
##        x -= 1
##    elif fourSidedDieRoll == 2:
##       x += 1
##    elif fourSidedDieRoll == 3:
##        y -= 1
##    else:
##        y += 1


pygameWindow = PYGAME_WINDOW()
print(pygameWindow)

previousNumberOfHands = 0
currentNumberOfHands = 0

fileNumber = 0

def Handle_Frame(frame):
    global x, y, xMin, xMax, yMin, yMax, currentNumberOfHands
    ##handlist = frame.hands
    ##numberOfHands = 0
    ## print(str(hand))
    currentNumberOfHands = len(frame.hands)
    hand = frame.hands[0]
        
    fingers = hand.fingers
    for f in range(0,len(fingers)):
        
        Handle_Finger(fingers[f], f)

def Handle_Finger(finger, f):
    for b in range(0, 4):
        Handle_Bone(finger, f, b)

def Handle_Bone(finger, f, b):
    global previousNumberOfHands
    global currentNumberOfHands
    bone = finger.bone(b)
    base = bone.prev_joint
    tip = bone.next_joint
    xBase, yBase = Handle_Vector_From_Leap(base)
    xTip, yTip = Handle_Vector_From_Leap(tip)
    if (currentNumberOfHands == 1):
        color = (0, 255 , 0)
    if (currentNumberOfHands == 2):
        color = (255, 0, 0)
    pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, b, color)
    ##print(f)
    ##print("Finger #%s" % str(f))
    ##print("Bone #%s" % str(b))
    
    gestureData[f,b,0] = base[0]
    gestureData[f,b,1] = base[1]
    gestureData[f,b,2] = base[2]
    gestureData[f,b,3] = tip[0]
    gestureData[f,b,4] = tip[1]
    gestureData[f,b,5] = tip[2]
    
    # print("Base coordinates are %s and %s" % (base[0], base[1]))
    # print("Tip coordinates are %s and %s" % (tip[0], tip[1]))

def Save_Gesture():
    global fileNumber
    pickle_out = open("userData/gesture%s.p" % (str(fileNumber)), "wb")
    pickle.dump(gestureData, pickle_out)
    pickle_out.close()
    fileNumber += 1

def Recording_Is_Ending():
    if currentNumberOfHands == 1 and previousNumberOfHands == 2:
        print(gestureData)
        Save_Gesture()

def Handle_Vector_From_Leap(v):
    global xRawMin, xRawMax, yRawMin, yRawMax, xScaledMin, xScaledMax, yScaledMin, yScaledMax
    
    scaledX = Scale(v[0], xRawMin, xRawMax, xScaledMin, xScaledMax)
    scaledY = Scale(v[2], yRawMin, yRawMax, yScaledMin, yScaledMax)
    return (scaledX, scaledY)

def Delete_And_Replace():
    cwd = os.getcwd()
    oldUserData = (cwd + "/userData")
    shutil.rmtree(oldUserData)
    os.mkdir("userData")
    

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


xScaledMin = 0
xScaledMax = 800
yScaledMin = 0
yScaledMax = 650

def Scale(value, rawMin, rawMax, scaledMin, scaledMax):
    rawFromLeft = value - rawMin
    ratio = float(float(rawFromLeft) / float(-rawMin + rawMax))
    scaledValue = int(ratio * scaledMax)
    return scaledValue

Delete_And_Replace()

controller = Leap.Controller()


while True:
    pygameWindow.Prepare()
    
    frame = controller.frame()
    handlist = frame.hands
    for hand in handlist:
        if(str(hand) > 0):
            Handle_Frame(frame)
            Recording_Is_Ending()
            previousNumberOfHands = currentNumberOfHands
    
    pygameWindow.Reveal()
