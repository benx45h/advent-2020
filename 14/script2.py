import re

ifile = open('input.txt','r')
lines = ifile.readlines()

lines = [line.strip() for line in lines]

lines = [line.split(' = ') for line in lines]

addys = []
vals = []

# dumpster fire
def recurse(mask,addy):
    targets = []
    x = mask.find('X')
    if(x != -1):
        mlist = list(mask)
        alist = list(bin(addy)[2:].zfill(36))
        mlist[x] = '0'
        alist[x] = '0'
        t0 = "".join(mlist)
        a0 = "".join(alist)
        a0 = int(a0,2)
        mlist[x] = '1'
        t1 = "".join(mlist)
        r0 = recurse(t0,a0)
        r1 = recurse(t1,addy)
        if type(r0) is list:
            for r in r0:
                targets.append(r)
            for r in r1:
                targets.append(r)
        else:
            targets.append(r0)
            targets.append(r1)
        return targets
    else:
        return (mask,addy)
    
mask = '000000000000000000000000000000X1001X'

print(recurse(mask, 42))

mask = []
for line in lines:
    if(line[0] == 'mask'):
        mask = line[1]
    if(line[0][0:3] == 'mem'):
        data = int(line[1])
        address = int(re.search('[0-9]+',line[0])[0])
        targets = recurse(mask,address)
        targets = [(int(target[0],2),target[1]) for target in targets]
        for target in targets:
            addy = target[0] | target[1]
            if(addy not in addys):
                addys.append(addy)
                vals.append(-1)
            idx = addys.index(addy)            
            vals[idx] = data


print(sum(vals)) 
