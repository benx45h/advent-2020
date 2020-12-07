import re

mapfile = open('input.txt','r')

lines = mapfile.readlines()

valid = 0
new = True
for i in range(0,len(lines)):
    line = lines[i]

    if(line == '\n'):
        new = True
    else:
        pairs = line.split(' ')
        if(new):
            byrv = False
            iyrv = False
            eyrv = False
            hgtv = False
            hclv = False
            eclv = False
            pidv = False
            cidv = False
            keys = []
            vals = []
            new = False
        for pair in pairs:
            tmp = pair.split(':')
            key=tmp[0]
            val=tmp[1]
            if(key == 'byr'):
                if(int(val) >= 1920 and int(val) <= 2002):
                    byrv = True
            if(key == 'iyr'):
                if(int(val) >=2010 and int(val) <=2020):
                    iyrv = True
            if(key == 'eyr'):
                if(int(val) >= 2020 and int(val) <= 2030):
                    eyrv = True
            if(key == 'hgt'):
                num = int(val)
                if(num >= 150 and num <= 193):
                    if(val[3] == 'c' and val[4] == 'm'):
                        hgtv = True
                if(num >= 59 and num <= 76):
                    if(val[2] == 'i' and val[3] == 'n'):
                        hgtv = True
            if(key == 'hcl'):
                if(val[0] == '#'):
                    tmp = val.strip('#')
                    tmp = tmp.strip()
                    if(len(tmp) == 6):
                        if(all(c in 'abcdef0123456789' for c in tmp)):
                            hclv = True
            if(key == 'ecl'):
                if(val=='amb' or val=='blu' or val=='brn' or val=='gry' or val=='hzl' or val=='oth'):
                    eclv = True
            if(key == 'pid'):
                if(len(val) == 9 or (len(val) == 10 and val[9] == '#')):
                    tmp = val.strip()
                    if(all(c in '0123456789' for c in tmp)):
                        pidv = True
            if(key == 'cid'):
                cidv = True
        

        if(byrv and iyrv and eyrv and hgtv and hclv and eclv and pidv):
            valid = valid + 1
            new = True

print(valid)

