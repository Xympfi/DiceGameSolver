# This is a simple solver for our famouse dice game with three dice and finding the closest solution
# using simple operations like + - * /
from csv import DictReader
import random
from itertools import permutations
#this is a
operations =["+","-","*","/"]
multiples = [1,1,1,10,10,10, 100, 100, 100,1000, 1000,1000,10000, 10000,10000]
targets = range(1,120)
dice_values =[1,2,3,4,5,6]

def operation(a, operator, b):
    if operator == "+":
        return a+b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a/b
    elif operator =="-":
        return a - b

def calculate_all_solutions(dice_combinations, operation_combinations, multiple_combinations):
    results = []
    i = 0
    for dc in dice_combinations:
        for op in operation_combinations:
            for mlt in multiple_combinations:
                if i % 100 == 0:
                    print("-", end="")
    #calulate result
                first_part = operation(dc[0]*mlt[0],op[0],dc[1]*mlt[1])
                if first_part >= 0: # make sure that not negative partial results occur 
                    result =  operation(first_part , op[1],dc[2]*mlt[2])
    #check validity of result if result is a whole number
                    if result >= 0. and  result - int(result) < 0.000001: # make sure that result is positive and whole number
                        results.append([dc[0], mlt[0], op[0], dc[1],mlt[1], op[1],dc[2],mlt[2], int(result), int(abs(target - result))])
                i=i+1
    return results
def print_dice_value(value):
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
        print("---")
        c = random.choice(dice_values)
        print_dice_value(a)
        print("---")
        print_dice_value(b)
        print("---")
        print_dice_value(c)
        print("---")

    dice = [a,b,c]


#generate all possible combinations of dice order, operator order and multiple
    dc_comb = list(permutations(dice, 3))
# remove duplicates
    dice_combinations = []
    for dc in dc_comb:
        if dc not in dice_combinations:
            dice_combinations.append(dc)

    operation_combinations = list(permutations(operations,2))
    mlt_comb = list(permutations(multiples,3))
#remove duplicates
    multiple_combinations = []
    for mlt in mlt_comb:
        if mlt not in multiple_combinations:
            multiple_combinations.append(mlt)

    results = calculate_all_solutions(dice_combinations, operation_combinations, multiple_combinations)
# sort result from smalles difference to largest^
    results.sort(key=lambda row: (row[9]), reverse=False)
# output 20 best results
    print()
    print("Number of iterations", len(results))
    input("Want to see the the minimum distance found ? [press enter] ")
    print("Minimum distance found: ", results[0][9])
    input("Want to see the results ? [press enter] ")
    for i in range(len(results[:20])):
        solution = results[i]
        print(solution[9],":",solution[8],"=",solution[0],"*",solution[1], "", solution[2], "", solution[3], "*", solution[4], "", solution[5], "", solution[6], "*", solution[7])
    answer = input("Exit [press x enter] Continue [press enter]")