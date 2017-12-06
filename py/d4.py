

with open('d4i.txt') as f:
    lines = f.readlines()

def valid(words):
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if sorted(word1) == sorted(word2):
                return False
    return True
sumw = 0
for line in lines:
    words = line.split()
    if valid(words):
        sumw += 1

print sumw
