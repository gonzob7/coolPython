import time
import sys

def printFlush(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.075)

printFlush("Welcome to python interactive! Today i'll be showing you the basics of my game.")
