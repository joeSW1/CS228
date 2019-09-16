import pickle

class READER:
    def __init__(self, file):
        self.file = file
    
    def printFile(self):
        pickle_in = open(self.file, "rb")
        gestureData = pickle.load(pickle_in)
        print(gestureData)


        
