from os import listdir
from os.path import isfile, join


def getFiles(directory):
    listDirectory = listdir(directory)
    onlyFiles = []
    for i in listDirectory:
        if isfile(join(directory, i)):
            onlyFiles.append(i)
        else:
            innerDirectoryFiles = getFiles(join(directory, i))
            onlyFiles.extend(innerDirectoryFiles)
    return onlyFiles


def sentenceFromFile(fileName):
    fileName = fileName.split(".")[0]
    sentence = ""
    for c in fileName:
        if c == "_" or c == "-":
            sentence += " "
            continue
        if c.isupper() and (sentence
                            and sentence[len(sentence) - 1].islower()):
            sentence += " "
        sentence += c
    return sentence.strip()