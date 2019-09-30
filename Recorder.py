import sys
sys.path.insert(0, '..')
import Leap

from random import randint
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowWidth
from constants import pygameWindowDepth


class DELIVERABLE:

    numberOfGestures = 100
    gestureIndex = 0
    
    def __init__(self, x, y, xRawMin, xRawMax, yRawMin, yRawMax, xScaledMin, xScaledMax, yScaledMin, yScaledMax):
        self.x = x
        self.y = y
        self.xScaledMin = xScaledMin
        self.xScaledMax = xScaledMax
        self.yScaledMin = yScaledMin
        self.yScaledMax = yScaledMax
        pass

    def Scale(value, rawMin, rawMax, scaledMin, scaledMax):
        rawFromLeft = value - rawMin
        ratio = float(float(rawFromLeft) / float(-rawMin + rawMax))
        scaledValue = int(ratio * scaledMax)
        return scaledValue
    
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
        scaledX = Scale(v[0], xRawMin, xRawMax, xScaledMin, xScaledMax)
        scaledY = Scale(v[2], yRawMin, yRawMax, yScaledMin, yScaledMax)
        return (scaledX, scaledY)
