import pickle
import os
import pygame
import sys
sys.path.insert(0, '..')
import Leap
import time
from pygameWindow_Del03 import PYGAME_WINDOW 
from constants import pygameWindowWidth
from constants import pygameWindowDepth

class READER:

    
    def __init__(self):
        self.numGestures = 0
        self.pygameWindow = PYGAME_WINDOW()
        self.controller = Leap.Controller()
        self.xRawMin = -130
        self.xRawMax = 324
        self.yRawMin = 350
        self.yRawMax = 20
        self.xScaledMin = 0
        self.xScaledMax = 800
        self.yScaledMin = 0
        self.yScaledMax = 650

        ##pygame.init()
        
##    def Print_File(self):
##        pickle_in = open(self.file, "rb")
##        gestureData = pickle.load(pickle_in)
##        print(gestureData)

    def Count_Gestures(self):
        path, dirs, files = next(os.walk('userData'))
        self.numGestures = len(files)

    def Print_Gestures(self):
        for i in range(self.numGestures):
            currentGestureFile = ("userData/gesture%s.p" % str(i))
            pickle_in = open(currentGestureFile, "rb")
            currentGestureData = pickle.load(pickle_in)
            # print(currentGestureData)

    def Draw_Each_Gesture_Once(self):
        for i in range(self.numGestures):
            self.pygameWindow.Prepare()
            self.Draw_Gesture(i)
            self.pygameWindow.Reveal()
            time.sleep(0.8)

    def Draw_Gesture(self, index):
        currentGestureFile = ("userData/gesture%s.p" % str(index))
        pickle_in = open(currentGestureFile, "rb")
        currentGestureData = pickle.load(pickle_in)
        for i in range(0, 5):
            for j in range(0, 4):
                currentBone = currentGestureData[i][j]
                xBaseNotYetScaled = currentBone[0]
                yBaseNotYetScaled = currentBone[1]
                xTipNotYetScaled = currentBone[3]
                yTipNotYetScaled = currentBone[4]

                #bone = finger.bone(b)
                #base = bone.prev_joint
                #tip = bone.next_joint
                #xBase, yBase = Handle_Vector_From_Leap(base)
                #xTip, yTip = Handle_Vector_From_Leap(tip)
                #pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, b, color)

                xBase = self.Scale(xBaseNotYetScaled, self.xRawMin, self.xRawMax, self.xScaledMin, self.xScaledMax)
                yBase = self.Scale(yBaseNotYetScaled, self.yRawMin, self.yRawMax, self.yScaledMin, self.yScaledMax)
                xTip = self.Scale(xTipNotYetScaled, self.xRawMin, self.xRawMax, self.xScaledMin, self.xScaledMax)
                yTip = self.Scale(yTipNotYetScaled, self.yRawMin, self.yRawMax, self.yScaledMin, self.yScaledMax)

                self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, 2, (0,0,255))
                

    def Scale(self, value, rawMin, rawMax, scaledMin, scaledMax):       
        rawFromLeft = value - rawMin
        ratio = float(float(rawFromLeft) / float(-rawMin + rawMax))
        scaledValue = int(ratio * scaledMax)
        return scaledValue

    def Draw_Gestures(self):
        while True:
            #self.pygameWindow.Prepare()
            self.Draw_Each_Gesture_Once()
            #self.pygameWindow.Reveal()
            

    def Prepare(self):
        pygame.event.get()
        self.pygameWindow.fill((255,255,255))

    def Reveal(self):
        pygame.display.update()
