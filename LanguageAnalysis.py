import os, sys
from collections import defaultdict


POSITIVEWORDDICT = { # k: word, v: word score
   'LOVE'      : 1,
   'FUN'       : 1,
   'WITH'      : 1,
   'ADORE'     : 1,
   'LIKE'      : 1,
   'HEART'     : 1,
   'BEAUTIFUL' : 1,
   'GOOD'      : 1,
   'BEST'      : 1,

}

NEGATIVEWORDDICT = { # k: word, v: word score
   'HATE'   : -1,
   'WITHOUT': -1,
   'DON\'T' : -1,
   'WON\'T' : -1,
   'EVIL'   : -1,

}


class LanguageAnalyzer:
   def __init__(self):
      """
      This module will read in a text string given a filename and analyze for positivity in the language. Each individual sentence is analyzed and assigned a point value.
      Values <=0 are overall negative, while numbers >0 are positive overall
      """

      pass

   def run(self, filename):
      with open(filename, 'rb') as analysisFile:
         lines = analysisFile.readlines()

      fileString = ''.join(lines)
      fileString = fileString.split('.')
      loveScore = defaultdict(int) # k: sentence number, v: sentence score

      for sentenceNum, sentence in enumerate(fileString):
         for word in sentence.split(' '):
            if word.upper() in POSITIVEWORDDICT:
               loveScore[sentenceNum] += POSITIVEWORDDICT.get(word.upper())
            elif word.upper() in NEGATIVEWORDDICT:
               loveScore[sentenceNum] += NEGATIVEWORDDICT.get(word.upper())
               loveScore[sentenceNum] *= -1

      print loveScore


def __main__():
   mainClass = LanguageAnalyzer()
   mainClass.run('test.txt')


if __name__ == '__main__': __main__()