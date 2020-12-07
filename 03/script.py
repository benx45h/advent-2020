mapfile = open('input.txt','r')

lines = mapfile.readlines()

for line in lines:
    line.strip()

trees = 0

length = len(lines[0])-1

pos = 0


tslope = []
for dr in [1,3,5,7]:
    pos = 0
    trees = 0
    for line in lines:
        if(line[pos] == '#'):
            trees = trees + 1
        pos = pos + dr
        pos = pos % length
    tslope.append(trees)

pos = 0
trees = 0
skip = False
dr = 1
for line in lines:
    if(not skip):
        if(line[pos] == '#'):
            trees = trees + 1
        pos = pos + dr
        pos = pos % length
    skip = not skip
tslope.append(trees)

print(tslope)
