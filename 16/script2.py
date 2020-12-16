import re

ifile = open('input.txt','r')
lines = ifile.readlines()

lines = [line.strip() for line in lines]

pre_rules = [line for line in lines if re.search(" or ", line)]
ytick = lines[lines.index('your ticket:')+1]
ytick = [int(num) for num in ytick.split(',')]
rules = {}
for rule in pre_rules:
    rule = rule.split(':')
    key = rule[0]
    rule = rule[1].split(' or ')
    min1 = int(rule[0].split('-')[0])
    max1 = int(rule[0].split('-')[1])
    min2 = int(rule[1].split('-')[0])
    max2 = int(rule[1].split('-')[1])
    rules[key] = [(min1,max1),(min2,max2),[i for i in range(0,len(ytick))]]

oof = lines.index('nearby tickets:')+1

pre_tickets = []
for i in range(oof, len(lines)):
    pre_tickets.append(lines[i])

tickets = []
for ticket in pre_tickets:
    error = False
    ticket = ticket.split(',')
    for num in ticket:
        num = int(num)
        found = False
        for rule in rules:
            zones = rules[rule]
            for i in range(2):
                if(num >= zones[i][0] and num <= zones[i][1]):
                        found = True
                        break
        if(not found):
            error = True
    if(not error):
        tickets.append(ticket)

for ticket in tickets:
    for i in range(0,len(ticket)):
        num = int(ticket[i])
        for rule in rules:
            match = False
            zones = rules[rule]
            for k in range(2):
                if(num >= zones[k][0] and num <= zones[k][1]):
                    match = True
                    break
            if(not match):
                rules[rule][2].remove(i)

done = False
solved = []
for i in range(0,30):
    for rule in rules:
        possibilities = rules[rule][2]
        if(len(possibilities)==1):
            if(possibilities[0] not in solved):
                solved.append(possibilities[0])
        if(len(possibilities) != 1):
            for possibility in possibilities:
                if(possibility in solved):
                    rules[rule][2].remove(possibility)

prod = 1
for rule in rules:
    if(re.search("departure", rule)):
        prod = prod * ytick[rules[rule][2][0]]
print(prod)
