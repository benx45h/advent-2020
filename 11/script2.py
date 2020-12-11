

ifile = open('input.txt', 'r')
lines = ifile.readlines()


rbound = len(lines)
cbound = len(lines[0])
# pad
rpad = "."*(cbound)

lines.append(rpad)
lines.insert(0,rpad)

plines = []

for line in lines:
    pline = "." + line.strip() + "."
    plines.append(pline)

cbound = len(plines[2])

print(cbound)
print(rbound)

changed = True
while(changed == True):
    changed = False
    new = ['.'*(cbound)]
    for r in range(1,rbound+1):
        row = ['.']
        for c in range(1,cbound):
            count = 0
            col = []
            dirmatch = [0,0,0,0,0,0,0,0]

            # Check horizontal up
            for rt in reversed(range(0, r)):
                if(plines[rt][c] == '#'):
                    dirmatch[0] = 1
                if(plines[rt][c] == 'L'):
                    break
            # Horizontal Down
            for rt in range(r+1, rbound+2):
                if(plines[rt][c] == '#'):
                    dirmatch[4] = 1
                if(plines[rt][c] == 'L'):
                    break
            # Diagonal Up Right
            for rt in reversed(range(0,r)):
                dr = r - rt
                if(c+dr < cbound):
                    if(plines[rt][c+dr] == '#'):
                        dirmatch[1] = 1
                    if(plines[rt][c+dr] == 'L'):
                        break
            # Diagonal Up left
            for rt in reversed(range(0,r)):
                dr = r - rt
                if(c-dr >= 0):
                    if(plines[rt][c-dr] == '#'):
                        dirmatch[7] = 1
                    if(plines[rt][c-dr] == 'L'):
                        break
            # Diagonal Down Right
            for rt in range (r+1,rbound+2):
                dr = rt - r
                if(c+dr < cbound):
                    if(plines[rt][c+dr] == '#'):
                        dirmatch[3] = 1
                    if(plines[rt][c+dr] == 'L'):
                        break
            # Diagonal Down Left
            for rt in range (r+1,rbound+2):
                dr = rt - r
                if(c-dr >= 0):
                    if(plines[rt][c-dr] == '#'):
                        dirmatch[5] = 1
                    if(plines[rt][c-dr] == 'L'):
                        break
            # Horizontal left
            for ct in reversed(range(0, c)):
                if(plines[r][ct] == '#'):
                    dirmatch[6] = 1
                if(plines[r][ct] == 'L'):
                    break
            # Horizontal right
            for ct in range(c+1, cbound):
                if(plines[r][ct] == '#'):
                    dirmatch[2] = 1
                if(plines[r][ct] == 'L'):
                    break

            count = dirmatch.count(1)

            if(plines[r][c] == '#'):
                if(count > 4):
                    row.append('L')
                    changed = True
                else:
                    row.append('#')
            elif(plines[r][c] == 'L'):
                if(count == 0):
                    row.append('#')
                    changed = True
                else:
                    row.append('L')
            else:
                row.append('.')

        row.append('.')
        row = ''.join(row)
        new.append(row)
    new.append('.'*cbound)
    plines = new


count = 0
for line in plines:
    count = count + line.count('#')

print(count)

