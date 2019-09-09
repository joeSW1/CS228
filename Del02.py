# RealTimeDraw.py
# deliverable 2 program
# 9/8/2019

import sys
sys.path.insert(0, '..')
import Leap

from random import randint
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowWidth
from constants import pygameWindowDepth

x = (pygameWindowWidth/2)
y = (pygameWindowDepth/2)

##xMin = 1000.0
##xMax = -1000.0
##yMin = 1000.0
##yMax = -1000.0

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
    global x, y, xMin, xMax, yMin, yMax
    hand = frame.hands[0]
    fingers = hand.fingers
    for finger in fingers:
        Handle_Finger(finger)

def Handle_Finger(finger):
    for b in range(0, 4):
        Handle_Bone(finger, b)

def Handle_Bone(finger, b):
    bone = finger.bone(b)
    base = bone.prev_joint
    tip = bone.next_joint
    xBase, yBase = Handle_Vector_From_Leap(base)
    xTip, yTip = Handle_Vector_From_Leap(tip)
    pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, b)
    # print("Base coordinates are %s and %s" % (base[0], base[1]))
    # print("Tip coordinates are %s and %s" % (tip[0], tip[1]))

def Handle_Vector_From_Leap(v):
    global xRawMin, xRawMax, yRawMin, yRawMax, xScaledMin, xScaledMax, yScaledMin, yScaledMax
    
    scaledX = Scale(v[0], xRawMin, xRawMax, xScaledMin, xScaledMax)
    scaledY = Scale(v[2], yRawMin, yRawMax, yScaledMin, yScaledMax)
    return (scaledX, scaledY)
    
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

controller = Leap.Controller()

while True:
    pygameWindow.Prepare()
    
    frame = controller.frame()
    handlist = frame.hands
    for hand in handlist:
        if(str(hand) > 0):
            Handle_Frame(frame)

    pygameWindow.Reveal()
