import sys

def greet_me():
    if len(sys.argv) == 2:
        print("Hello " + sys.argv[1] + "!")
    else:
        print("Hello World!")
greet_me()