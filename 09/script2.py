import re

ifile = open('input.txt', 'r')

lines = ifile.readlines()

target = 1212510616

int_lines = [int(i) for i in lines]

for rmin in range (0,len(lines)-1):
    for rmax in range (rmin+1,len(lines)):
        sums = sum(int_lines[rmin:rmax])
        mins = min(int_lines[rmin:rmax])
        maxs = max(int_lines[rmin:rmax])
        if(sums == target):
            print(maxs+mins)
            exit()
