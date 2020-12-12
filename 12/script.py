ifile = open('input.txt','r')
lines = ifile.readlines()
lines = [line.strip() for line in lines]


pos = [0,0,0]
for line in lines:
    cmd = line[0]
    num = int(line[1:])
    if(cmd == 'F'):
        bearing = pos[2] % 360
        if(bearing == 0):
            cmd = 'E'
        if(bearing == 90):
            cmd = 'N'
        if(bearing == 180):
            cmd = 'W'
        if(bearing == 270):
            cmd = 'S'
    
    if(cmd == 'N'):
        pos[1] = pos[1] + num
    if(cmd == 'S'):
        pos[1] = pos[1] - num
    if(cmd == 'E'):
        pos[0] = pos[0] + num
    if(cmd == 'W'):
        pos[0] = pos[0] - num
    if(cmd == 'R'):
        pos[2] = pos[2] - num
    if(cmd == 'L'):
        pos[2] = pos[2] + num

print(pos)

man = abs(pos[0])+abs(pos[1])

print(man)
