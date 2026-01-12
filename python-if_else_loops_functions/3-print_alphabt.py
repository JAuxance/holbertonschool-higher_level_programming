#!/usr/bin/python3
skip = {113, 101}
print("{}".format(''.join(chr(i) for i in range(97, 123) if i not in skip)), end='')
