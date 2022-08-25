#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        end = "s" if len(sys.argv) > 2 else ""
        print("{} argument{}:".format(len(sys.argv) - 1, end))
        for i in range(len(sys.argv) - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
