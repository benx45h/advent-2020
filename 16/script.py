import re

ifile = open('input.txt','r')
lines = ifile.readlines()

lines = [line.strip() for line in lines]

pre_rules = [line for line in lines if re.search(" or ", line)]

rules = []
for rule in pre_rules:
    rule = rule.split(':')
    key = rule[0]
    rule = rule[1].split(' or ')
    min1 = int(rule[0].split('-')[0])
    max1 = int(rule[0].split('-')[1])
    min2 = int(rule[1].split('-')[0])
    max2 = int(rule[1].split('-')[1])

    rules.append((min1,max1))
    rules.append((min2,max2))

oof = lines.index('nearby tickets:')+1

tickets = []
for i in range(oof, len(lines)):
    tickets.append(lines[i])

error = 0
for ticket in tickets:
    ticket = ticket.split(',')
    for num in ticket:
        num = int(num)
        found = False
        for rule in rules:
            if(num >= rule[0] and num <= rule[1]):
                found = True
                break
        if(not found):
            error = error + num

print(error)
