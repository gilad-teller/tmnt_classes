#!/usr/bin/env python3
from lib import words
from lib import files


def main():
    # sentence = input("Sentence to check: ")
    # isTmnt = words.isTMNT(sentence)
    # print("Yes" if isTmnt else "No")

    directory = input("Directory: ")
    onlyFiles = files.getFiles(directory)
    for f in onlyFiles:
        sentence = files.sentenceFromFile(f)
        isTmnt = words.isTMNT(sentence)
        if isTmnt:
            print(sentence)


if __name__ == "__main__":
    main()
