import re

ifile = open('input.txt','r')
lines = ifile.readlines()

lines = [line.strip() for line in lines]

problem = '2 * 3 + (4 * 5)'


def parse(problem):
    print("Parsing " + problem)
    exprs = []
    deep = True
    count = 0
    result = 0
    idx = 0
    jf = True
    for i in range(len(problem)):
        c = problem[i]
        if(c == '('):
            deep = False
            if(not count):
                idx = i
            count = count + 1
        elif(c == ')'):
            count = count - 1
            if(count == 0):
                exprs.append((problem[idx+1:i],1))
                jf = True
        elif(count == 0):
            if(jf):
                exprs.append(([],0))
                jf = False
            exprs[-1][0].append(c)
    
    exprs = [(''.join(expr[0]),expr[1]) for expr in exprs]
    
    parsed = []
    for expr in exprs:
        if(expr[1] == 0):
            parsed.append(expr[0])
        else:
            parsed.append(parse(expr[0]))

    exprs = parsed
    queue = []

    problem = ''.join(exprs)
    
    problem = problem.split(' ')
    
    idx = 0
    length = len(problem)
    while idx < length:
        op = problem[idx]
        if(op == '+'):
            problem[idx-1] = str(int(problem[idx-1]) + int(problem[idx+1]))
            del problem[idx:idx+2]
            length = len(problem)
            idx = 0
        idx = idx + 1


    result = int(problem[0])
    for c in range(len(problem)):
        op = problem[c]
        if(op == '*'):
            result = result * int(problem[c+1])

    print("Parse result: " + str(result))
    return str(result)

print(parse(problem))


count = 0
for line in lines:
    print("Line: " + line)
    count = count + int(parse(line))


print(count)
