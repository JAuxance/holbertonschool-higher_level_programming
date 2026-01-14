#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    count = len(sys.argv) - 1
    for i in range(1, count + 1):
        total += int(sys.argv[i])
    print(total)
