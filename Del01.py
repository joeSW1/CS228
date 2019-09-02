# RealTimeDraw.py
# deliverable 1 program
# 9/1/2019

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
    indexFingerList = fingers.finger_type(1)
    indexFinger = indexFingerList[0]
    distalPhalanx = indexFinger.bone(3)
    tip = distalPhalanx.next_joint
    x = int(tip[0])
    y = int(tip[1])
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
xRawMin = -240
xRawMax = 404
yRawMin = 730
yRawMax = -21

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
    frame = controller.frame()
    handlist = frame.hands
    for hand in handlist:
        if(str(hand) > 0):
            Handle_Frame(frame)

    pygameWindow.Prepare()
#    Perturb_Circle_Position()
    pygameWindow.Draw_Black_Circle(Scale(x, xRawMin, xRawMax, xScaledMin, xScaledMax),
                                   Scale(y, yRawMin, yRawMax, yScaledMin, yScaledMax))
    pygameWindow.Reveal()
