#!/usr/bin/env python3
from lib import words
from lib import files
import sys

def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("Directory: ")
    onlyFiles = files.getFiles(directory)
    for f in onlyFiles:
        sentence = files.sentenceFromFile(f)
        isTmnt = words.isTMNT(sentence)
        if isTmnt:
            print(f"{sentence} - {f}")


if __name__ == "__main__":
    main()
