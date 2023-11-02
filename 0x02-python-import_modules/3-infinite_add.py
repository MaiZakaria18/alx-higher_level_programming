#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = 0
    for x in sys.argv:
        if x != sys.argv[0]:
            num += int(x)
    print(num)
