#!/usr/bin/python3
def write_file(filename="", text=""):
    file = open(filename, "w+")
    file.write(text)
    file.close
