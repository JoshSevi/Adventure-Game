import sys
import time


def typewriter(i):
    for char in i:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(1)
            