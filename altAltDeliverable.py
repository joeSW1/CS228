import Leap
from pygameWindow_Del03 import PYGAME_WINDOW
from constants import pygameWindowWidth
from constants import pygameWindowDepth

class DELIVERABLE:
    def __init__(self):
        global Leap
        global PYGAME_WINDOW
        self.controller = Leap.Controller()
        self.pygameWindow = PYGAME_WINDOW()
        self.x = (pygameWindowWidth/2)
        self.y = (pygameWindowDepth/2)
        self.xRawMin = -70
        self.xRawMax = 244
        self.yRawMin = -120
        self.yRawMax = 204
        self.xScaledMin = 0
        self.xScaledMax = 800
        self.yScaledMin = 0
        self.yScaledMax = 650
        pass
