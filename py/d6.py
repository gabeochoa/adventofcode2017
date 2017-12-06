

with open('d6i.txt') as f:
    lines = f.readlines()

lines = lines[0]
print lines
blocks = [int(x.strip()) for x in lines.split()]
print blocks
#  blocks = [0,2,7,0]

states = set()

def redir(index, blocks):
    left = blocks[index]
    blocks[index] = 0
    while left > 0:
        index = (index+1) % len(blocks)
        blocks[index] += 1
        left -=1
    return blocks
i = 0
saved = None
while True:
    i+=1
    ind = blocks.index(max(blocks))
    out = tuple(redir(ind, blocks))
    if saved is not None and saved == out:
        print "final", i
        break
    if out in states:
        print "duplicate", i, len(states)
        if saved is None:
            saved = out
            print 'saved', out
            i = 0
    else:
        states.add(out)
    blocks = list(out)
    #  print blocks, len(states)

