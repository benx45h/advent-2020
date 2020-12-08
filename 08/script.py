import re

ifile = open('input.txt', 'r')

program = ifile.readlines()

acc = 0
pc = 0
npc = 0

pastpc = []

while(True):
    if(pc in pastpc):
        print("infinite loop detected!")
        print(pc)
        print(acc)
        exit()
    pastpc.append(pc)
    print(pc)
    line = program[pc].strip()
    print(line)
    inst = re.split(' ', line)[0]
    arg = re.split(' ', line)[1]
    iarg = int(arg)
    if(inst == 'jmp'):
        npc = pc + iarg
    if(inst == 'acc'):
        acc = acc + iarg
        npc = pc + 1
    if(inst == 'nop'):
        npc = pc + 1
    pc = npc
