import re

ifile = open('input.txt', 'r')

program = ifile.readlines()

for i in range(0,len(program)):
    testprog = program.copy()
    testline = testprog[i]

    if(testprog[i][0:3] == 'nop'):
        print("match")
        testprog[i] = testprog[i].replace('nop', 'jmp')
    elif(testprog[i][0:3] == 'jmp'):
        testprog[i] = testprog[i].replace('jmp', 'nop')

    print("replacing line " + str(i-1))
    print(program[i])
    print(testline)
    print(testprog[i])
    cont = True
    
    acc = 0
    pc = 0
    npc = 0
    
    pastpc = []

    while(cont):
        if(pc == len(testprog)):
            print("success!")
            print(acc)
            print(i)
            exit()
        if(pc in pastpc):
            cont = False
            break
        if(pc > len(testprog)):
            cont = False
            break
        pastpc.append(pc)
        line = testprog[pc].strip()
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
