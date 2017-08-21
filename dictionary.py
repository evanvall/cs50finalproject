import sys
import cs50

class Dictionary():
    def __init__(self):
        self.words = set()
        
    def load(self, dictionary):
        file = open(dictionary, "r")
        for line in file:
            self.words.add(line.rstrip("\n"))
        file.close()
        return True
