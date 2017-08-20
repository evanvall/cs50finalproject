import sys
import cs50

def main():
    if (len(sys.argv) != 2):
        print ("Correct usage: python fizzbuzz.py n")
        return 1
    n = int(sys.argv[1])
    fizzbuzz(n)

def fizzbuzz(n):
    for i in range(n):
        if ((i%3 == 0) and (i%5 == 0)):
            print("Fizz Buzz")
        elif (i%5 == 0):
            print("Buzz")
        elif (i%3 == 0):
            print("Fizz")
        else:
            print(i)
    return 0

if __name__ == "__main__":
    main()