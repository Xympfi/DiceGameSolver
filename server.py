from fastapi import FastAPI
import json
import dicelib

operations =["+","-","*","/"]
multiples = [1,1,1,10,10,10, 100, 100, 100,1000, 1000,1000,10000, 10000,10000]
targets = range(1,120)
dice_values =[1,2,3,4,5,6]

target = random.choice(targets)

a = random.choice(dice_values)
b = random.choice(dice_values)
c = random.choice(dice_values)

dice = [a,b,c]

dice_combinations, operation_combinations, multiple_combinations = dicelib.generate_combinations(dice, operations, multiples)
results = dicelib.calculate_all_solutions(target, dice_combinations, operation_combinations, multiple_combinations)

target_dump = json.dumps([target])
dice_json = json.dumps(dice)
results_json = json.dumps(result[:15])

app = FastAPI()


@app.get("/")
def read_root():
    return dice_json
