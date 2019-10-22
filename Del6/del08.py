import sys
sys.path.insert(0, '../..')
import Leap
sys.path.insert(0, '..')
import numpy as np
import pickle
import os
import shutil
import matplotlib.pyplot as plt
import csv
import numpy as np
from knn import KNN

database = {}
print(database)

pickle.dump(database, open('userData/database.p','wb'))



