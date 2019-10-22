import sys
sys.path.insert(0, '..')
import Leap
import pygame

from random import randint
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowWidth
from constants import pygameWindowDepth
from constants import pygameWindowHalfWidth
from constants import pygameWindowHalfDepth


class state():
    def __init__(self, pygameWindow, programState):
        self.pygameWindow = pygameWindow
        self.programState = programState

def HandleState():
    if programState == 0:
        #HandleState0()
        pygameWindow.screen.blit(image0resize, (pygameWindowHalfWidth + 60, 30 ))
    if programState == 1:
        HandleState1()

def HandleState0():
    DrawImageToHelpUserPutTheirHandOverTheDevice()

def HandleState1():
    pass
    

def DrawImageToHelpUserPutTheirHandOverTheDevice():
    global image0resize
    global pygameWindowHalfWidth
    global pygameWindow
    pygameWindow = pygameWindow
    print(pygameWindow)
    pygameWindow.screen.blit(image0resize, (pygameWindowHalfWidth + 60, 30))
    
