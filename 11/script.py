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

print(plines)
changed = True
while(changed == True):
    changed = False
    new = ['.'*(cbound)]
    for r in range(1,rbound+1):
        row = ['.']
        for c in range(1,cbound-1):
            count = 0
            for rt in range(r-1,r+2):
                for ct in range(c-1,c+2):
                    if(plines[rt][ct] == '#'):
                        count = count + 1
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

