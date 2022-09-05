from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse
import random
#import json
import dicelib

#uvicorn web server needs to be running in local environment


app = FastAPI()

#app.mount("/", StaticFiles(directory="static",html = True), name="static")
# return the contents of intex.htlm file in folder static when the https://host/ is called in a browser
@app.get("/")
async def homepage():
    file = open("./static/index.html","r")
    html_content =str(file.read())
    file.close()
    return HTMLResponse(content = html_content, status_code = 200)


# return the target value, dice values and first 15 solutions in JSON format when the https://host/dicegame is called in a browser
@app.get("/dicegame", response_class=JSONResponse)
def read_root():
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
    rslts =[]
    for r in results:
        rslts.append(str(r[9])+":"+str(r[8])+"="+"("+str(r[0]*r[1])+r[2]+str(r[3]*r[4])+")"+r[5]+str(r[6]*r[7]))
    return {"Target": target, "dice": dice, "Results": rslts[0:15]} 
