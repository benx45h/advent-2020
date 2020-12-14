import re

ifile = open('input.txt','r')
lines = ifile.readlines()

lines = [line.strip() for line in lines]

lines = [line.split(' = ') for line in lines]

mem = [0]*100000

print(lines)
for line in lines:
    if(line[0] == 'mask'):
        mask = line[1]
        mask1s = int(mask.replace('X','0'),2)
        mask0s = int(mask.replace('X','1'),2)
    if(line[0][0:3] == 'mem'):
        address = int(re.search('[0-9]+',line[0])[0])
        data = int(line[1])
        data = data & mask0s
        data = data | mask1s
        mem[address] = data

print(sum(mem)) 
