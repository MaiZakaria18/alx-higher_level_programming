#!/usr/bin/python3
if __name__ != "__main__":
    import sys
    arg_n = len(sys.argv) - 1
    if arg_n == 0:
        print("{} arguments".format(arg_n))
    elif arg_n == 1:
        print("{} argument".format(arg_n))
    elif arg_n > 1:
        print("{} arguments".format(arg_n))
    for i in range(arg_n):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
