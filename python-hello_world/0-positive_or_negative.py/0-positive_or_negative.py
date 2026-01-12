#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < -10:
    print(f"-{number} is negative ")
else: 
    print(f"{number} is positive")
