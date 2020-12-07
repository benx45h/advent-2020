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
        tcount = tcount + len(set(group))
        group = ""
        new = False
    if(line == "\n"):
        new = True
    line = line.strip()
    group = group + line

tcount = tcount + len(set(group))
print(tcount)
 


