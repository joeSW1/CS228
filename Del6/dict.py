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

database = pickle.load(open('userData/database.p','rb'))
userName = ""

def start():
    global database, userName
    userName = raw_input('Please enter your name: ')
    if userName in database:
        database[userName]["logins"] += 1
        print('welcome back ' + userName + '.')
    else:
        database[userName] = {}
        database[userName]["logins"] = 1
        print('welcome ' + userName + '.')

    print(database)

    pickle.dump(database, open('userData/database.p','wb'))

def attempt(randomNumber):
    global database, userName
    keyName = (str(randomNumber) + "timesAttempted")
    if keyName in database[userName]:
        database[userName][keyName] += 1
    else:
        database[userName][keyName] = 1
    print("Attempting %s for the %s time" % (str(randomNumber), str(database[userName][keyName])))
    pickle.dump(database, open('userData/database.p','wb'))
    return (database[userName][keyName])

def complete(randomNumber):
    global database, userName
    keyName = (str(randomNumber) + "timesCompleted")
    if keyName in database[userName]:
        database[userName][keyName] += 1
    else:
        database[userName][keyName] = 1
    print("Completed %s for the %s time" % (str(randomNumber), str(database[userName][keyName])))
    pickle.dump(database, open('userData/database.p','wb'))
    return (database[userName][keyName])

