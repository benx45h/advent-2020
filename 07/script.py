import math
import re
ifile = open('input.txt','r')
lines = ifile.readlines()


def find_layer(target, lines, excludes):
    targets = []
    for line in lines:
        tmp = re.split(" bags contain ", line)
        linecolor = tmp[0]
        tmprule = tmp[1]
        if(len(re.findall(target,tmprule))):
            targets.append(linecolor)

    excludes.append(target)
    for t in targets:
        if not(t in excludes):
            print(t)
            tmp1, tmp2 = find_layer(t, lines, excludes)
            for fuck in tmp2:
                if not fuck in excludes:
                    excludes.append(fuck)
            for fuck in tmp1:
                if not fuck in targets:
                    targets.append(fuck)
    return targets, excludes;

excludes = []
targets, excludes = find_layer("shiny gold", lines, excludes)

print(len(targets))
