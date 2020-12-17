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
        space[x][y] = {0: {0: line[y]}}

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
    wmin = min(list(space[xmin][ymin][zmin].keys()))
    wmax = max(list(space[xmin][ymin][zmin].keys()))

    space[xmin-1] = {y: {z: {w: '.' for w in range(wmin,wmax+1)} for z in range(zmin,zmax+1)} for y in range(ymin,ymax+1)}
    space[xmax+1] = {y: {z: {w: '.' for w in range(wmin,wmax+1)} for z in range(zmin,zmax+1)} for y in range(ymin,ymax+1)}
    for x in space:
        space[x][ymin-1] = {z: {w: '.' for w in range(wmin,wmax+1)} for z in range(zmin,zmax+1)}
        space[x][ymax+1] = {z: {w: '.' for w in range(wmin,wmax+1)} for z in range(zmin,zmax+1)}
        for y in space[x]:
            space[x][y][zmin-1] = {w: '.' for w in range(wmin,wmax+1)}
            space[x][y][zmax+1] = {w: '.' for w in range(wmin,wmax+1)}
            for z in space[x][y]:
                space[x][y][z][wmin-1] = '.'
                space[x][y][z][wmax+1] = '.'
                    
                    

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
                for w in space[x][y][z]:
                    active = 0
                    for dy in [-1,0,1]:
                        for dx in [-1,0,1]:
                            for dz in [-1,0,1]:
                                for dw in [-1,0,1]:
                                    if(dy == dx == dz == dw  == 0):
                                        continue
                                    if(x+dx in space and y+dy in space[0] and z+dz in space[0][0] and w+dw in space[0][0][0]):
                                        if(space[x+dx][y+dy][z+dz][w+dw] == '#'):
                                            active = active + 1
                    
                    if(space[x][y][z][w] == '.' and active == 3):
                        nspace[x][y][z][w] = '#'
                    elif(space[x][y][z][w] == '#' and (active == 2 or active == 3)):
                        nspace[x][y][z][w] = '#'
                    else:
                        nspace[x][y][z][w] = '.'
                



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
            for w in space[x][y][z]:
                if space[x][y][z][w] == '#':
                    count=count+1

print(count)
