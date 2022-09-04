from itertools import permutations

def operation(a, operator, b):
    # calulates a operator b depending on the value of operator
    if operator == "+":
        return a+b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a/b
    elif operator =="-":
        return a - b

def calculate_all_solutions(target, dice_combinations, operation_combinations, multiple_combinations):
    # calculates all allowed solutions 
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
    results.sort(key=lambda row: (row[9]), reverse=False)
    return results

def generate_combinations(dice,operations, multiples):
#generate all possible combinations of dice order, operator order and multiple without duplicates
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
    return dice_combinations, operation_combinations, multiple_combinations