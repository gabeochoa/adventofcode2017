output = None
from collections import defaultdict

with open('d9i.txt') as f:
    linesr = f.readlines()

inp = linesr[0]

import sys
sys.setrecursionlimit = 20000
def remgarb(some):
    if len(some) < 1:
        return ""
    out = ""
    i = 0
    x = 0
    inga = False
    while i < len(some):
        char = some[i]

        if char == "!": # need to skip next one
            i += 1
        elif inga:
            if char == ">":
                inga = False
            else:
                x += 1
        elif char == "<":
            inga = True

        if not inga:
            out += char

        i+=1
        #  return char + remgarb(some[1:])
    return out, x

def countgroups(some):
    cur = level = i = 0
    while i < len(some):
        if some[i] == "!":
            i += 2
            continue
        if some[i] == "{":
            level += 1
        elif some[i] == "}":
            cur += level; level -=1
        else: # just continue
            pass
        i+=1
    return cur

def test(inpt):
    #  print inpt
    import re
    #  inpt = re.sub('<>', '', inpt)
    #  inpt = re.sub('!!', '', inpt)
    #  inpt = re.sub('[a-z{},]+!>', '', inpt)
    nogarb, x = remgarb(inpt)
    #  print inpt
    #  print nogarb
    print countgroups(nogarb), x
#
test("{}")
test("{{{}}}")
test("{{},{}}")
test("{{{},{},{{}}}}")
test("{<a>,<a>,<a>,<a>}")
test("{{<ab>},{<ab>},{<ab>},{<ab>}}")
test("{{<!!>},{<!!>},{<!!>},{<!!>}}")
test("{{<a!>},{<a!>},{<a!>},{<ab>}}")
test("<{!>}>")
test(inp)
