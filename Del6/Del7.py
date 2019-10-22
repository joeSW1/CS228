# RealTimeDraw.py
# deliverable 2 program for Del7
# 9/8/2019

import sys
sys.path.insert(0, '../..')
import Leap
sys.path.insert(0, '..')
import pygame
from random import randint
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowWidth
from constants import pygameWindowDepth
from constants import pygameWindowHalfWidth
from constants import pygameWindowHalfDepth
import numpy as np
import pickle
from dict import start
from dict import attempt
from dict import complete

clf = pickle.load( open('userData/classifier.p','rb') )
testData = np.zeros( (1,30), dtype='f')

pygame.font.init()

x = (pygameWindowWidth/2)
y = (pygameWindowDepth/2)

last10Guesses = range(10)
counter = 0
attemptNumber = 0
k = 0

xTracker = -1000
yTracker = -1000
xCentered = False
yCentered = False

randomNumber = randint(0,9)

pygameWindow = PYGAME_WINDOW()


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

#loading image0
image0 = pygame.image.load('image0.jpg')
image0resize = pygame.transform.scale(image0, (250,250))

greenMark = pygame.image.load('greenMark.png')
greenMarkResize = pygame.transform.scale(greenMark, (250,250))

tooLeft = pygame.image.load('tooLeft.png')
tooLeftResize = pygame.transform.scale(tooLeft, (100,80))

tooRight = pygame.image.load('tooRight.png')
tooRightResize = pygame.transform.scale(tooRight, (100,80))

tooFar = pygame.image.load('tooFar.png')
tooFarResize = pygame.transform.scale(tooFar, (80,100))

tooClose = pygame.image.load('tooClose.png')
tooCloseResize = pygame.transform.scale(tooClose, (80,100))

rows, cols = (10, 2)
digits = [[0 for i in range(cols)] for j in range(rows)] 

gesture0 = pygame.image.load('gesture0.png')
gesture0Resize = pygame.transform.scale(gesture0, (200,200))
digits[0][0] = gesture0Resize
digits[0][1] = 0

gesture1 = pygame.image.load('gesture1.png')
gesture1Resize = pygame.transform.scale(gesture1, (200,200))
digits[1][0] = gesture1Resize
digits[1][1] = 1

gesture2 = pygame.image.load('gesture2.png')
gesture2Resize = pygame.transform.scale(gesture2, (200,200))
digits[2][0] = gesture2Resize
digits[2][1] = 2

gesture3 = pygame.image.load('gesture3.png')
gesture3Resize = pygame.transform.scale(gesture3, (200,200))
digits[3][0] = gesture3Resize
digits[3][1] = 3

gesture4 = pygame.image.load('gesture4.png')
gesture4Resize = pygame.transform.scale(gesture4, (200,200))
digits[4][0] = gesture4Resize
digits[4][1] = 4

gesture5 = pygame.image.load('gesture5.png')
gesture5Resize = pygame.transform.scale(gesture5, (200,200))
digits[5][0] = gesture5Resize
digits[5][1] = 5

gesture6 = pygame.image.load('gesture6.png')
gesture6Resize = pygame.transform.scale(gesture6, (200,200))
digits[6][0] = gesture6Resize
digits[6][1] = 6

gesture7 = pygame.image.load('gesture7.png')
gesture7Resize = pygame.transform.scale(gesture7, (200,200))
digits[7][0] = gesture7Resize
digits[7][1] = 7

gesture8 = pygame.image.load('gesture8.png')
gesture8Resize = pygame.transform.scale(gesture8, (200,200))
digits[8][0] = gesture8Resize
digits[8][1] = 8

gesture9 = pygame.image.load('gesture9.png')
gesture9Resize = pygame.transform.scale(gesture9, (200,200))
digits[9][0] = gesture9Resize
digits[9][1] = 9
print(digits)
display_width = 485
display_height = 485



def Handle_Frame(frame):
    global x, y, xMin, xMax, yMin, yMax, testData, last10Guesses, counter
    hand = frame.hands[0]
    fingers = hand.fingers
    for finger in fingers:
        Handle_Finger(finger)
    testData = CenterData(testData)
    predictedClass = clf.Predict(testData)

    last10Guesses[counter] = predictedClass[0]
    #print(last10Guesses)
    if counter < 9:
        counter += 1
    else:
        counter = 0

    #Used for testing
    #print(predictedClass)
    #print(last10Guesses)

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
    global xRawMin, xRawMax, yRawMin, yRawMax, xScaledMin, xScaledMax, yScaledMin, yScaledMax
    
    scaledX = Scale(v[0], xRawMin, xRawMax, xScaledMin, xScaledMax) / 2
    scaledY = Scale(v[2], yRawMin, yRawMax, yScaledMin, yScaledMax) / 2
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

def HandleState(state):
    if state == 0:
        HandleState0()
    if state == 1:
        HandleState1()
    if state == 2:
        HandleState2()
    if state == 3:
        HandleState3()

def HandleState0():
    global programState
    DrawImageToHelpUserPutTheirHandOverTheDevice()

def DrawImageToHelpUserPutTheirHandOverTheDevice():
    global image0resize
    global pygameWindowHalfWidth
    global pygameWindow
    pygameWindow.screen.blit(image0resize, (pygameWindowHalfWidth + 60, 30))


def isHandCentered():
    global xTracker, yTracker, xCentered, yCentered, k
    k = 0
    Handle_Frame(frame)
    hand = frame.hands[0]
    fingers = hand.fingers
    indexFingerList = fingers.finger_type(1)
    indexFinger = indexFingerList[0]
    distalPhalanx = indexFinger.bone(3)
    tip = distalPhalanx.next_joint
    xTracker = int(tip[0])
    yTracker = int(tip[2])

    if xTracker < -90:
        xCentered = False
    elif xTracker > 90:
        xCentered = False
    else:
        xCentered = True
        
    if yTracker < -130:
        yCentered = False
    elif yTracker > 20:
        yCentered = False
    else:
        yCentered = True

    if xCentered and yCentered:
        return True
    else:
        return False


def HandleState1():
    global xTracker, yTracker, xCentered, yCentered, programState, k, randomNumber
    k = 0
    Handle_Frame(frame)
    hand = frame.hands[0]
    fingers = hand.fingers
    indexFingerList = fingers.finger_type(1)
    indexFinger = indexFingerList[0]
    distalPhalanx = indexFinger.bone(3)
    tip = distalPhalanx.next_joint
    xTracker = int(tip[0])
    yTracker = int(tip[2])
    #print(xTracker, yTracker)
    
    if xTracker < -90:
        pygameWindow.screen.blit(tooLeftResize, (pygameWindowHalfWidth + 50, pygameWindowHalfDepth / 3.2))
        xCentered = False
    elif xTracker > 90:
        pygameWindow.screen.blit(tooRightResize, (pygameWindowWidth - 150, pygameWindowHalfDepth / 3.2))
        xCentered = False
    else:
        xCentered = True
        
    if yTracker < -130:
        pygameWindow.screen.blit(tooFarResize, (pygameWindowHalfWidth + (pygameWindowHalfWidth / 2.5) , 5))
        yCentered = False
    elif yTracker > 20:
        pygameWindow.screen.blit(tooCloseResize, (pygameWindowHalfWidth + (pygameWindowHalfWidth / 2.5) , pygameWindowHalfDepth - 150))
        yCentered = False
    else:
        yCentered = True

def HandleState2():
    global xTracker, yTracker, xCentered, yCentered, programState, k, last10Guesses
    k = 0
    Handle_Frame(frame)

    checkForCompletion()

    pygameWindow.screen.blit(digits[randomNumber][0], ((pygameWindowHalfWidth / 2) * 2.5, (pygameWindowHalfDepth /2) * 2.5))
    goal_display()
    attempt_display("black")
    
    if xTracker < -90:
        pygameWindow.screen.blit(tooLeftResize, (pygameWindowHalfWidth + 50, pygameWindowHalfDepth / 3.2))
        xCentered = False
    elif xTracker > 90:
        pygameWindow.screen.blit(tooRightResize, (pygameWindowWidth - 150, pygameWindowHalfDepth / 3.2))
        xCentered = False
    else:
        xCentered = True
        
    if yTracker < -130:
        pygameWindow.screen.blit(tooFarResize, (pygameWindowHalfWidth + (pygameWindowHalfWidth / 2.5) , 5))
        yCentered = False
    elif yTracker > 20:
        pygameWindow.screen.blit(tooCloseResize, (pygameWindowHalfWidth + (pygameWindowHalfWidth / 2.5) , pygameWindowHalfDepth - 150))
        yCentered = False
    else:
        yCentered = True
        
def goal_display():
    global pygameWindow, randomNumber
    myfont = pygame.font.SysFont('Comic Sans MS', 100)
    textSurface = myfont.render(str(randomNumber), False, (0,0,0))
    pygameWindow.screen.blit(textSurface, ((pygameWindowHalfWidth / 2) * 3.1, (pygameWindowHalfDepth / 2.4 )))

def attempt_display(blackOrGreen):
    global pygameWindow, attemptNumber
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    if blackOrGreen == "black":
        color = (0,0,0)
    if blackOrGreen == "green":
        color = (0,255,0)
    textSurface = myfont.render("(" + str(attemptNumber) + ")", False, color)
    pygameWindow.screen.blit(textSurface, ((5), (5)))   

def checkForCompletion():
    global last10Guesses, randomNumber, programState
    all10AreTheSame = (len(set(last10Guesses)) == 1)
    #print(all10AreTheSame)
    if (all10AreTheSame):
        if (last10Guesses[0] == randomNumber):
            pygameWindow.screen.blit(greenMarkResize, (pygameWindowHalfWidth + 60, 30))
            programState = 3
            HandleState(programState)
            #print("COMPLETE!!")

def HandleState3():
    global randomNumber, pygameWindow, greenMarkResize, pygameWindowHalfWidth, attemptNumber
    attempt_display("green")
    #pygameWindow.screen.blit(greenMarkResize, (pygameWindowHalfWidth + 60, 30))
    complete(randomNumber)
    randomNumber = randint(0,9)
    attemptNumber = attempt(randomNumber)
    
    displayCheck()
    #pygame.time.wait(1000)

def displayCheck():
    global randomNumber, pygameWindow, greenMarkResize, pygameWindowHalfWidth
    start_time = pygame.time.get_ticks()
    while (pygame.time.get_ticks() - start_time) < 1000:
        pygameWindow.screen.blit(greenMarkResize, (pygameWindowHalfWidth + 60, 30))


start()
attemptNumber = attempt(randomNumber)
while True:
    pygameWindow.Prepare()
  
    frame = controller.frame()
    handlist = frame.hands
    
    if not (handlist):
        programState = 0
        #HandleState0()
    
    else:
        if(isHandCentered()):
            
            programState = 2
        else:
            programState = 1
        #HandleState1()
        #while xCentered and yCentered:
         #   HandleState2()
        #if xCentered and yCentered:
         #    programState = 2

    HandleState(programState)
    
    pygameWindow.Reveal()
