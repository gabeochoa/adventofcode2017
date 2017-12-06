
with open('d5i.txt') as f:
    lines = f.readlines()

nums = [int(x) for x in "0 3 0 1 -3".split()]
nums= [int(line.strip()) for line in lines]
#  nums = nums[:10]

current=steps=0

#  print nums
while current < len(nums) or current < 0:
    # get the value
    val = nums[current]
    if val >= 3:
        nums[current]-=1
    else:
        nums[current]+=1

    current += val
    steps += 1
    #  print nums

print steps

#  print lines
