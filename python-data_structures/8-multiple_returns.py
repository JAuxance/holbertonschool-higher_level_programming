#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        fisrtchar = None
        size = len(sentence)
    else:
        size = len(sentence)
        fisrtchar = sentence[0]
    return size, fisrtchar

