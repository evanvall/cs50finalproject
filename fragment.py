import os
import sys
import cs50
from dictionary import Dictionary 

def main():
    if (len(sys.argv) != 2):
        print ("Correct usage: fragment.py 'string'")
        return 1
    
    file = os.path.join(sys.path[0], "dictionary.txt")
    dictionary.load(file)
    string = sys.argv[1]
    finder(string)
    
def finder(string):
    i=0
    for line in dictionary.words:
        if (i == 5):
            break
        if line.startswith(string) == True:
            print(line)
            i += 1
    return 0

if __name__ == "__main__":
    dictionary = Dictionary()
    main()