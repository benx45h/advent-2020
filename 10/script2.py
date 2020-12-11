ifile = open('test2.txt', 'r')
lines = ifile.readlines()
jlist = [int(i) for i in lines]
jlist.append(0)
jlist.sort()

options = []
options.append(1)

# Array of number of branches
for i in jlist:
    a1 = ((i+1) in jlist)
    a2 = ((i+2) in jlist)
    a3 = ((i+3) in jlist)
    total = a1 + a2 + a3
    if(i == max(jlist)):
        total = 1
    options.append(fuck)

def sum_branch(options, idx):
    s = 0
    pos = options[idx]
    if(pos == 1):
        return 1
    for i in range(1, pos+1):
        count = sum_branch(options, (idx + i))
        s = s + count
    return s

yeet = 1
for i in range(1,len(options)):
    if(options[i] > 1) and options[i-1] <= 1:
       count = sum_branch(options, i)
       yeet = yeet * count

print(options)

print(yeet)
