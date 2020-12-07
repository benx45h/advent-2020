
file = open('input.txt', 'r')

lines = file.readlines()

valid = 0

for line in lines:
    count = 0
    line = line.strip()
    minc = int(line.split('-')[0])
    line = line.split('-')[1]
    maxc = int(line.split(' ')[0])
    targetchar = line.split(' ')[1][0]
    passwd = line.split(' ')[2]
    for char in passwd:
        if(char == targetchar):
            count = count + 1
    if(count >= minc and count <= maxc):
        valid = valid + 1

print('part 1: ' + str(valid))

valid = 0

for line in lines:
    count = 0
    line = line.strip()
    idx1 = int(line.split('-')[0]) - 1
    line = line.split('-')[1]
    idx2 = int(line.split(' ')[0]) - 1
    targetchar = line.split(' ')[1][0]
    passwd = line.split(' ')[2]
    if((passwd[idx1] == targetchar) ^ (passwd[idx2] == targetchar)):
        valid = valid + 1

print('part 2: ' + str(valid))
