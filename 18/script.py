import re

ifile = open('input.txt','r')
lines = ifile.readlines()

lines = [line.strip() for line in lines]

problem = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'


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
    print(exprs)
    for expr in exprs:
        print(expr)
        if(expr[1] == 0):
            parsed.append(expr[0])
        else:
            parsed.append(parse(expr[0]))

    exprs = parsed
    print(exprs)
    queue = []

    problem = ''.join(exprs)
    
    print(problem)

    problem = problem.split(' ')
    result = int(problem[0])
    for c in range(len(problem)):
        op = problem[c]
        if(op == '+'):
            if(c+1 >= len(problem)):
                queue.append(op)
            else:
                result = result + int(problem[c+1])
        if(op == '*'):
            if(c+1 >= len(problem)):
                queue.append(op)
            else:
                result = result * int(problem[c+1])

    return str(result)

count = 0
for line in lines:
    print("Line: " + line)
    count = count + int(parse(line))

print(count)

