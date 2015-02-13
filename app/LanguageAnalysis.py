import os, sys
from collections import defaultdict


POSITIVEWORDDICT = { # k: word, v: word score
   'LOVE'      : 1,
   'FUN'       : 1,
   'WITH'      : 1,
   'ADORE'     : 1.5,
   'LIKE'      : 0.5,
   'HEART'     : 1.5,
   'BEAUTIFUL' : 1,
   'GOOD'      : 1,
   'BEST'      : 1,

}

NEGATIVEWORDDICT = { # k: word, v: word score
   'HATE'   : -1,
   'WITHOUT': -1,
   'DON\'T' : -1,
   'WON\'T' : -1,
   'CAN\'T' : -1,
   'EVIL'   : -1,

}


class LanguageAnalyzer:
   def __init__(self):
      """
      This module will read in a text string given a filename and analyze for positivity in the language. Each individual sentence is analyzed and assigned a point value.
      Values <=0 are overall negative, while numbers >0 are positive overall
      """

      pass

   def run_from_file(self, filename):
      with open(filename, 'rb') as analysisFile:
         fileString = analysisFile.read()
      self.analyze(fileString)

   def analyze(self, message):
      message = message.split('.')
      loveScore = defaultdict(int) # k: sentence number, v: sentence score

      for sentenceNum, sentence in enumerate(message):
         for word in sentence.split(' '):
            if word.upper() in POSITIVEWORDDICT:
               loveScore[sentenceNum] += POSITIVEWORDDICT.get(word.upper())
            elif word.upper() in NEGATIVEWORDDICT:
               if loveScore[sentenceNum] < 0:
                  loveScore[sentenceNum] *= -1
                  loveScore[sentenceNum]+= abs(NEGATIVEWORDDICT.get(word.upper()))
               else:
                  loveScore[sentenceNum] += NEGATIVEWORDDICT.get(word.upper())

      return loveScore


def __main__():
    mainClass = LanguageAnalyzer()
    score = mainClass.run_from_file('test.txt')
    print score


if __name__ == '__main__': __main__()
