#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_n = len(sys.argv) - 1
    if arg_n == 0:
        print("0 arguments.")
    elif arg_n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_n))
    for i in range(arg_n):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
