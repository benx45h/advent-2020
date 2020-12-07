import math
ifile = open('input.txt','r')
lines = ifile.readlines()

tcount = 0
gcount = 0

group = ""

new = True
for i in range(0,len(lines)):
    line = lines[i]
    if(new == True):
        tcount = tcount + len(group)
        group = line.strip()
        new = False
    if(line == "\n"):
        new = True
    else:
        line = line.strip()
        for c in group:
            if(not(c in line)):
                group = group.replace(c,'')
        print(line)
        print("group: " + group)

tcount = tcount + len(group)
print(tcount)
 


