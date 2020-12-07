import math
ifile = open('input.txt','r')
lines = ifile.readlines()
valid = 0
maxid = 0
fields = 0
sids = []
for i in range(0,len(lines)):
    line = lines[i]
    rowmin = 0
    rowmax = 127
    colmin = 0
    colmax = 7
    for c in line:
        if(c == 'F'):
            rowmax = int((rowmin+rowmax)/2)
        if(c == 'B'):
            rowmin = math.ceil((rowmin+rowmax)/2)
        if(c == 'L'):
            colmax = int((colmin+colmax)/2)
        if(c == 'R'):
            colmin = math.ceil((colmin+colmax)/2)

    col = colmin
    row = rowmin

    sid = row * 8 + col
    sids.append(sid)
    if(sid > maxid):
        maxid = sid

for i in range(0,801):
    if((not (i in sids)) and ((i+1) in sids) and ((i-1) in sids)):
        print(i)
        

print(maxid)

