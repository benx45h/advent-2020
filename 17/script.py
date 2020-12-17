import re
import copy
ifile = open('input.txt','r')
lines = ifile.readlines()

lines = [line.strip() for line in lines]


space = {}

for x in range(0,len(lines)):
    line = lines[x]
    space[x] = {}
    for y in range(0,len(line)):
        space[x][y] = {0: line[y]}

for x in space:
        print(space[x])

for n in range(6):

    # Expand space
    xmin = min(list(space.keys()))
    xmax = max(list(space.keys()))
    ymin = min(list(space[xmin].keys()))
    ymax = max(list(space[xmin].keys()))
    zmin = min(list(space[xmin][ymin].keys()))
    zmax = max(list(space[xmin][ymin].keys()))
    xlen = len(space.keys())
    ylen = len(space[xmin].keys())
    zlen = len(space[xmin][ymin].keys())

    space[xmin-1] = {y: {z: '.' for z in range(zmin,zmax+1)} for y in range(ymin,ymax+1)}
    space[xmax+1] = {y: {z: '.' for z in range(zmin,zmax+1)} for y in range(ymin,ymax+1)}
    for x in space:
        space[x][ymin-1] = {z: '.' for z in range(zmin,zmax+1)}
        space[x][ymax+1] = {z: '.' for z in range(zmin,zmax+1)}
        for y in space[x]:
            space[x][y][zmin-1] = '.'
            space[x][y][zmax+1] = '.'

    nspace = copy.deepcopy(space)
    print(space)
    for z in space[0][0]:
        print("z = " + str(z))
        for x in range(xmin-1,xmax+2):
            for y in range(ymin-1,ymax+2):
                print(space[x][y][z],end="")
            print()

    for x in space:
        for y in space[x]:
            for z in space[x][y]:
                active = 0
                for dy in [-1,0,1]:
                    for dx in [-1,0,1]:
                        for dz in [-1,0,1]:
                            if(dy == dx == dz == 0):
                                continue
                            if(x+dx in space and y+dy in space[0] and z+dz in space[0][0]):
                                if(space[x+dx][y+dy][z+dz] == '#'):
                                    active = active + 1
                
                if(space[x][y][z] == '.' and active == 3):
                    nspace[x][y][z] = '#'
                elif(space[x][y][z] == '#' and (active == 2 or active == 3)):
                    nspace[x][y][z] = '#'
                else:
                    nspace[x][y][z] = '.'
                



    space = nspace
    for z in space[0][0]:
        print("z = " + str(z))
        for x in range(xmin-1,xmax+2):
            for y in range(ymin-1,ymax+2):
                print(space[x][y][z],end="")
            print()

count = 0
for x in space:
    for y in space[x]:
        for z in space[x][y]:
            if space[x][y][z] == '#':
                count=count+1

print(count)
