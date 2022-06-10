import matplotlib.pyplot as plt
import itertools
import random

##Checks if roll busts
def Check(num,num2,num3,array):
    global result, bust

    ##num check
    if array[0]+array[1]==num or array[2]+array[3]==num:
        result+=1
        return True
    elif array[0]+array[2]==num or array[1]+array[3]==num:
        result+=1
        return True
    elif array[0]+array[3]==num or array[1]+array[2]==num:
        result+=1
        return True

    ##num2 check
    elif array[0]+array[1]==num2 or array[2]+array[3]==num2:
        result+=1
        return True
    elif array[0]+array[2]==num2 or array[1]+array[3]==num2:
        result+=1
        return True
    elif array[0]+array[3]==num2 or array[1]+array[2]==num2:
        result+=1
        return True

    ##num3 check
    elif array[0]+array[1]==num3 or array[2]+array[3]==num3:
        result+=1
        return True
    elif array[0]+array[2]==num3 or array[1]+array[3]==num3:
        result+=1
        return True
    elif array[0]+array[3]==num3 or array[1]+array[2]==num3:
        result+=1
        return True

    else:
        bust+=1
        return False

##Simulates game
def Simulate(turns,num,num2,num3):
    bust_turn=[0,0,0,0]
    for i in range(0,turns):
        for i in range(0,4):
            choice=random.randint(0,1295)
            turn=all_rolls[choice]
            if Check(num,num2,num3,turn)==False:
                bust_turn[i]+=1
                break
    for i in range(0,4):
        bust_turn[i]=str((bust_turn[i]/turns)*100)+"%"
    return bust_turn

##Init vars
bust=0
result=0
sim_times=1000000
##makes all_rolls an array that hold all possible dice rolls for 4 thrown dice (Cartesian product)
x = [1, 2, 3, 4, 5, 6]
all_rolls=[p for p in itertools.product(x, repeat=4)]
##finds how many rolls there are in all_rolls
total_rolls=len(all_rolls)

##Print statments below here

print('\n################################################################\n')

print("Part 1 Problem 1 columns 3,8,11\n")
for i in list(all_rolls):
    Check(3,8,11,i)

print("Chance of Busting: ",(bust/total_rolls)*100)
print("Chance of Advancing: ",(result/total_rolls)*100)
bust=0
result=0

print('\n################################################################\n')

print("Part 1 Problem 2 columns 2,4,11\n")
for i in list(all_rolls):
    Check(2,4,11,i)

print("Chance of Busting: ",(bust/total_rolls)*100)
print("Chance of Advancing: ",(result/total_rolls)*100)

print('\n################################################################\n')

print("Part 2 Simulate Game",sim_times,"times from columns 3,8,11\n")
print("Bust Chance for Turn 1, Turn 2, Turn 3, Turn 4")
print(Simulate(sim_times,3,8,11))

print('\n################################################################\n')

print("Part 2 Simulate Game",sim_times,"times from columns 2,4,11\n")
print("Bust Chance for Turn 1, Turn 2, Turn 3, Turn 4")
print(Simulate(sim_times,2,4,11))

print('\n################################################################\n')

##matplot graphs below here

