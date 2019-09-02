# RealTimeDraw.py
# deliverable 1 program
# 9/1/2019
from random import randint
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowWidth
from constants import pygameWindowDepth

x = (pygameWindowWidth/2)
y = (pygameWindowDepth/2)

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

while True:
    pygameWindow.Prepare()
    Perturb_Circle_Position()
    pygameWindow.Draw_Black_Circle(x,y)
    pygameWindow.Reveal()
