lines = open('input.txt','r').readlines()
tests = [line.strip() for line in lines[137:]]
rules = [line.strip().split(': ') for line in lines[0:136]]

#lines = open('test2.txt','r').readlines()
#tests = [line.strip() for line in lines[32:]]
#rules = [line.strip().split(': ') for line in lines[0:31]]

rlist = {line[0]: line[1] for line in rules}

def check(string, rule, rlist):
    if (string == ''):
        return string, False
    remainder = string
    match = True
    oldstring = string
#    print("checking string " + string + " against " + str(rule))
    rules = rlist[rule].split()
#   print(rules)
    if(len(rules) == 3 and rules[1] == '|'):
        remainder, match = check(string, rules[0], rlist)
        if(match):
            return remainder, True
        remainder, match = check(string, rules[2], rlist)
        if(match):
            return remainder, True
        return string, False

    elif(len(rules) == 5 and rules[2] == '|'):
        remainder, match = check(string, rules[0], rlist)
        if(remainder == ''):
            return string, False
        if(match):
            remainder, match = check(remainder, rules[1], rlist)
  #          print(remainder)
            if(match):
                return remainder, True
        remainder, match = check(string, rules[3], rlist)
        if(match):
            remainder, match = check(remainder, rules[4], rlist)
   #         print(remainder)
            if(match):
                return remainder, True
        return string, False
    
    elif(rules[0] == '"a"' or rules[0] == '"b"'):
        char = rules[0][1]
        if(string[0] == char):
            return string[1:], True
        else:
            return string[1:], False
    else:
        for rule in rules:
            if(remainder == ''):
                return string, False
            remainder, match = check(remainder, rule, rlist)
            if not match:
                #print(string)
                return string, False
    return remainder, match


count = 0
for test in tests:
    totallyDone = False
    extMatch = False
    count42 = 2
    count31 = 0

    while(not totallyDone):
        done = False
        remainder = test
        for i in range(count42):
            remainder, match = check(remainder, '42', rlist)
            if not match:
                totallyDone = True
                extMatch = False
                done = True
                break
        
        count31 = 0
        
        while not done:
            remainder, match = check(remainder, '31', rlist)
            if(match):
                count31 += 1
                if(remainder == ''):
                    done = True
                    if(count31 < count42):
                        totallyDone = True
                        extMatch = True
                    else:
                        count42 = count42 + 1
            else: 
                count42 = count42 + 1
                done = True
                break

    if(extMatch):
#        print("match at " + str(count42) + " 42s and " + str(count31) + " 31s: " + test)
        count += 1
    else:
        print("failed match: " + test + " after " + str(len(test)/8) + " | " + str(count42) + " | " + str(count31))

print(count)
