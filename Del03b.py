# deliverable 3 program
# 09/16/2019

import numpy as np
import pickle
from Reader import READER

##pickle_in = open("userData/gesture.p", "rb")
##gestureData = pickle.load(pickle_in)
##print(gestureData)

reader = READER("userData/gesture10.p")
reader.printFile()

reader = READER("userData/gesture11.p")
reader.printFile()

reader = READER("userData/gesture12.p")
reader.printFile()
