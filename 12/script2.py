ifile = open('input.txt','r')
lines = ifile.readlines()
lines = [line.strip() for line in lines]


wpos = [10,1]
dpos = [0,0]
for line in lines:
    cmd = line[0]
    num = int(line[1:])

    if(cmd == 'F'):
        dpos[0] = dpos[0] + num * wpos[0]
        dpos[1] = dpos[1] + num * wpos[1]
    if(cmd == 'N'):
        wpos[1] = wpos[1] + num
    if(cmd == 'S'):
        wpos[1] = wpos[1] - num
    if(cmd == 'E'):
        wpos[0] = wpos[0] + num
    if(cmd == 'W'):
        wpos[0] = wpos[0] - num
    if(cmd == 'R'):
        for i in range(int(num/90)):
            x = wpos[0]
            wpos[0] = wpos[1]
            wpos[1] = -x
    if(cmd == 'L'):
        for i in range(int(num/90)):
            x = wpos[0]
            wpos[0] = -wpos[1]
            wpos[1] = x

man = abs(dpos[0])+abs(dpos[1])
print(man)
