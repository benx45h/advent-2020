ifile = open('input.txt', 'r')
lines = ifile.readlines()
jlist = [int(i) for i in lines]

jlist.sort()

for i in range(0, len(jlist)):
    if(i == 0):
        diff = 1
    if(i > 0):
        diff = jlist[i] - jlist[i-1]
    if(diff == 1):
        d1 = d1 + 1
    if(diff == 3):
        d3 = d3 + 1

d3 = d3 + 1

print(d3*d1)
