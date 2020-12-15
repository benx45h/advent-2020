last = 9

timer = 0
goal = 1000000
table = {8:1,13:2,1:3,0:4,18:5}

last = 9;
for i in range(7,30000001):
#    print("Turn: " + str(i))
#    if(timer == goal):
 #       print("Percent Complete: " + str(100*timer/30000000)+ "%")
  #      goal = goal + 1000000
    if(last not in table):
        num = 0
    else:
        num = (i-1) - table[last]
    table[last] = i-1
    last = num
 #   timer = timer + 1

print(num)
