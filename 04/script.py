import re
ifile = open('input.txt','r')
lines = ifile.readlines()
valid = 0
fields = 0
for i in range(0,len(lines)):
    line = lines[i]
    if(line == '\n'):
        fields = 0
    matches = re.findall("(byr:1[9][[2-9][0-9]|byr:200[0-2])|(pid:[0-9]{9}\s)|(iyr:20(1[0-9]|20))|(eyr:20(2[0-9]|30))|(hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in))|(hcl:#[a-f0-9]{6}\s)|(ecl:(amb|blu|brn|gry|grn|hzl|oth))",line)
    fields = fields + len(matches)
    if(fields == 7):
        valid = valid + 1
        fields = 0
print(valid)

