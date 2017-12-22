
print "star"
with open('d22i.txt') as f:
	lines= f.readlines()

lines= '''..#
#..
...'''.split("\n")

grid = [] 
is_clean = False

from collections import defaultdict
grid = defaultdict(int)

print "building griod"
for i, line in enumerate(lines):
	for j, c in enumerate(line):
		grid[(j,i)] = c
print "done building grid"
print grid

mid = len(lines)//2
cur = (mid, mid)
facing = 0

def ne(d, cur):
	a = [(0,-1), (1,0), (0,1), (-1, 0)]
	x,y = a[d]
	return (cur[0] + x, cur[1] + y)

count = 0
for i in range(70):
	# steps # wake up # do work
	print cur, grid[cur]
	node = grid[cur]
	# if the current node is infected, turn to the right
	if node == '#':
		print "node is infected, turning right"
		facing = 1
	else: 
		print "node is not infected, turning left"
		facing = 3
	# if the current node is clean, it becomes infected
	if node != "#": 
		print "current node is clean"
		grid[cur] = '#'
		count += 1
	# else the node is infected clean it
	else:
		print "current node is infected so clkean"
		grid[cur] = '.'
	cur = ne(facing, cur)
	print "move"


print "count", count
su = 0
for line in grid:
	su += line.count("#")
print su
