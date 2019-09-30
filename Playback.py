# deliverable 3 program
# 09/16/2019

import sys
sys.path.insert(0, '..')
import Leap
import numpy as np
import pickle
import os
import pygame
from pygameWindow_Del03 import PYGAME_WINDOW 
from Reader import READER

pygameWindow = PYGAME_WINDOW()

##pickle_in = open("userData/gesture.p", "rb")
##gestureData = pickle.load(pickle_in)
##print(gestureData)

reader = READER()
reader.Count_Gestures()
reader.Draw_Gestures()

controller = Leap.Controller()

##while True:
 ##   pygameWindow.Prepare()
##    
##    frame = controller.frame()
##
##    reader.Count_Gestures()
##    reader.Draw_Gestures()
##    
##    pygameWindow.Reveal()
