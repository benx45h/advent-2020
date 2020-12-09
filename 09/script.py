import re

ifile = open('input.txt', 'r')

lines = ifile.readlines()

last25 = []

for i in range (0,len(lines)):
    line = lines[i]
    num = int(line)
    possiblesums = []
    for x in last25:
        for y in last25:
            if(y != x):
                possiblesums.append(x+y)
    if(i >= 25 and num not in possiblesums):
        print(num)
        exit()
    if(i >= 25):
        last25 = last25[1:25] + [num]
    else:
        last25 = last25 + [num]
