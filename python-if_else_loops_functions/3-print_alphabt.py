#!/usr/bin/python3
skip = {113, 101}
i = 0

chars = [chr(i) for i in range(97, 123) if i not in skip]
print("{}".format(''.join(chars)))
