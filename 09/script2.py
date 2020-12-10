import re

ifile = open('input.txt', 'r')

lines = ifile.readlines()

target = 1212510616

int_lines = [int(i) for i in lines]

for rmin in range (0,len(lines)-1):
    for rmax in range (rmin+1,len(lines)):
        yeet = int_lines[rmin:rmax])
        sums = sum(yeet)
        mins = min(yeet)
        maxs = max(yeet)
        if(sums == target):
            print(maxs+mins)
            exit()
