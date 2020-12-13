lines = open('input.txt','r').readlines()
lines = [line.strip() for line in lines]
time = int(lines[0])

ids = lines[1].split(',')
ids = [int(num) for num in ids if num != 'x']

mid = 0
mwait = 99999
for num in ids:
    diff = time % num
    wait = num - diff
    if(wait < mwait):
        mwait = wait
        mid = num

print(mid*mwait)
