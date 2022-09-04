# This is a simple solver for our famouse dice game with three dice and finding the closest solution
# using simple operations like + - * /
import random
import dicelib
# 
operations =["+","-","*","/"]
multiples = [1,1,1,10,10,10, 100, 100, 100,1000, 1000,1000,10000, 10000,10000]
targets = range(1,120)
dice_values =[1,2,3,4,5,6]

def print_dice_value(value):
    #generate a simple output of dice values
    if value == 1:
        print("   ")
        print(" 0 ")
        print("   ")
    elif value == 2:
        print("0  ")
        print("   ")
        print("  0")
    elif value == 3:
        print("0  ")
        print(" 0 ")
        print("  0")
    elif value == 4:
        print("0 0")
        print("   ")
        print("0 0")
    elif value == 5:
        print("0 0")
        print(" 0 ")
        print("0 0")
    elif value == 6:
        print("0 0")
        print("0 0")
        print("0 0")

answer = ""
while answer != "x":
    answer = input("Use own values [press o enter] else use proposal [press enter]")
    if answer == "o":
        target = int(input("What is the target value ? "))
        a = int(input("Dice 1: "))
        b = int(input("Dice 2: "))
        c = int(input("Dice 3: "))
    else:  
        answer = "n"
        while answer == "n":
            target = random.choice(targets)
            print("Proposed target value; ", target)
            answer = input("Choose new target value [press n enter]")
        a = random.choice(dice_values)
        b = random.choice(dice_values)
        c = random.choice(dice_values)
        print("---")
        print_dice_value(a)
        print("---")
        print_dice_value(b)
        print("---")
        print_dice_value(c)
        print("---")

    dice = [a,b,c]

    dice_combinations, operation_combinations, multiple_combinations = dicelib.generate_combinations(dice, operations, multiples)
    results = dicelib.calculate_all_solutions(target, dice_combinations, operation_combinations, multiple_combinations)
# sort result from smallest difference to largest
# output 20 best results
    print()
    print("Number of combinations evaluated", len(results))
    input("Want to see the the minimum distance found ? [press enter] ")
    print("Minimum distance found: ", results[0][9])
    input("Want to see the results ? [press enter] ")
    for i in range(len(results[:15])):
        solution = results[i]
        print(solution[9],":",solution[8],"=",solution[0]*solution[1], "", solution[2], "", solution[3]*solution[4], "", solution[5], "", solution[6]*solution[7])
    answer = input("Exit [press x enter] Continue [press enter]")