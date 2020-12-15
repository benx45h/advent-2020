import re

nums = [8,13,1,0,18]
hist = [1,2,3,4,5]

last = 9

timer = 0
goal = 10000
for i in range(7,30000001):
    if(timer == goal):
        print(timer)
        goal = goal + 10000
    if(last not in nums):
        num = 0
        nums.append(last)
        hist.append(i-1)
    else:
        num = i - 1 - hist[nums.index(last)]
        hist[nums.index(last)] = i - 1
    last = num
    timer = timer + 1

print(num)
