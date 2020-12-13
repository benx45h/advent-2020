# I don't know the chinese remainder theorem

lines = open('input.txt','r').readlines()
lines = [line.strip() for line in lines]
ids = lines[1].split(',')
ids = [num for num in ids]
conds = []
for i in range(0,len(ids)):
    if(ids[i] != 'x'):
        conds.append([int(ids[i]),i % int(ids[i])])

conds.sort(key=lambda x: x[0])
conds.reverse()
print(conds)

last = conds[len(conds)-1]



guess = 0
inc = 1
layer = 0

done = False
while(not done):
    diff = guess % conds[layer][0]
    delay = conds[layer][0] - diff
    if(diff == 0):
        delay = 0
    if(delay == conds[layer][1]):
        inc = inc * conds[layer][0]
        layer = layer + 1
        if(layer >= len(conds)):
            done = True
    guess = guess + inc

print("done")
print(guess)


