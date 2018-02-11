# A program to demonstrate the use of regular expressions in python
import re 

def checkMatching(mobj):
    if (mobj.group()):
        return 'matched'
    else:
        return 'Not matched'

pobj=re.compile('a*')

mobj=pobj.match('abcd')

print(checkMatching(mobj))
