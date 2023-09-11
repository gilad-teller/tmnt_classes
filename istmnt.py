#!/usr/bin/env python3
from lib import words
import sys

def main():
    if len(sys.argv) > 1:
        phrase = sys.argv[1]
    else:
        phrase = input("Phrase: ")
    isTmnt = words.isTMNT(phrase)
    if isTmnt:
        print(f"{phrase} - is TMNT")
    else:
        print(f"{phrase} - is not TMNT")


if __name__ == "__main__":
    main()
