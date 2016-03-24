import sys
import os.path
from multiprocessing import Process

usage = '''\
Usage:
  python uniqifier.py InFileA InFileB OutOnlyFileA OutOnlyFileB
'''

def Letters (str):
  return sum(1 for c in str if c.isalpha())

def GetLines (filePath):
  entireFile = [line for line in open(filePath)]
  threePlus  = [word for word in entireFile if Letters(word) > 5]
  return threePlus

def GetAllowed ():
  dictPath   = os.path.join(os.path.dirname(__file__), "dict.txt")
  words      = [line.lower().strip() for line in open(dictPath) if len(line) > 3]
  substrings = set()
  for str in words:
    substring = ""
    for c in str:
      substring += c
      if substring in substrings:
        break
    if substring == str:
      substrings.add(substring)
  return substrings
        
def ContainsAllowed (test, allowed):
  for allowedLine in allowed:
    if allowedLine in test.lower():
      return True
  return False
  
def ValidateArgs (argv):
  if (len(argv) != 4):
    return False
  if not os.path.isfile(argv[0]) or not os.path.isfile(argv[1]):
    return False
  return True
  
def FillDiff (filePath, lines, only, allowed):
  open(filePath, 'w').writelines(line for line in lines if line in only and ContainsAllowed(line, allowed))
  
def main(argv):
  if not ValidateArgs(argv):
    print(usage)
    return

  allowed = GetAllowed()
  
  linesA = GetLines(argv[0])
  linesB = GetLines(argv[1])
  setA   = set(linesA)
  setB   = set(linesB)
  onlyA  = setA - setB
  onlyB  = setB - setA
  
  processA = Process(target = FillDiff, args = (argv[2], linesA, onlyA, allowed))
  processB = Process(target = FillDiff, args = (argv[3], linesB, onlyB, allowed))
  processA.start()
  processB.start()
  processA.join()
  processB.join()  
  
if __name__ == "__main__":
  main(sys.argv[1:])