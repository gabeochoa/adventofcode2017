
inp = [ord(x) for x in open('d10i.txt','r').read().rstrip()]
inp += [17, 31, 73, 47, 23]

from itertools import cycle, islice

nums = range(256)
#  inp = [3,4,1,5]
#  nums = [0,1,2,3,4]
cur_pos = 0
skip_size = 0
def rev(nums, cur, leng):
    total = len(nums)
    dist = cur+leng
    # grab the part to reverse, this can loop
    b = islice(cycle(nums), cur, dist)
    bl = list(reversed(list(b)))
    i = 0
    while cur < dist:
        nums[cur%total] = bl[i]
        cur += 1
        i += 1
    return nums

for it in range(64):
    for leng in inp:
        nums = rev(nums, cur_pos, leng)
        cur_pos += ((leng) + skip_size) % len(nums)
        skip_size +=1

print nums
print nums[0] * nums[1]

#dense hash
dh = []
for i in range(16):
    out = reduce(lambda a,b: a^b, nums[(16*i)+1:16*(i+1)], nums[16*i])
    toadd = hex(out)[2:]
    if len(toadd) == 1:
        toadd = '0'+toadd
    dh.append(toadd)

print ''.join(dh)










