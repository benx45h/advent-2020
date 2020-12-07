import math
import re
ifile = open('test2.txt','r')
lines = ifile.readlines()


# bags per bag
def find_layer(target, lines):
    total = 1
    for line in lines:
        tmp = re.split(" bags contain ", line)
        linecolor = tmp[0]
        if(linecolor == target):
            tmprule = tmp[1].strip()
            if(tmprule == "no other bags."):
                return total;
            else:
                rules = re.split(', ', tmprule)
                for rule in rules:
                    print(rule) 
                    print(re.findall('[0-9]', rule))
                    rcount = int(re.findall('[0-9]', rule)[0])
                    rcolor = re.findall('[0-9] (\S+ \S+)', rule)[0]
                    rtotal = rcount * find_layer(rcolor, lines)
                    total = total + rtotal
    return total;

total = find_layer("shiny gold", lines)

print(total - 1)
