## TMNT Classes

This python script runs on a folder and lists all file names that can be sung to the TMNT theme song

### Why

For fun! Inspired by https://xkcd.com/1412/ and https://twitter.com/wiki_tmnt

### How

When it runs, it:
- Takes a full path to a directory on your machine
- Recursively gets all file names from all sub-directories
- Cleans up file names from '-' and '_' 
- Separates camel casing and pascal casing
- Uses catleeball's code to determine if the file name can be sung to the TMNT theme song

### Environment

This script requires the following:

- Python >= 3.7
  - Earlier may work, only tested on 3.7
- Via PyPi:
  - pronouncing
  - num2words

### Caveats

- I only have a vague understanding of what catleeball did here. But I can call isTMNT() and print the response...
- It's using The Carnegie Mellon University Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict