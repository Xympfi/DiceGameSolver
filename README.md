# DiceGameSolver
A simple python based script the evaluates all possible compinations of 3 dice values 2 operators (+, -, *, /) and multiples of 10
in order to get to a target value as close as possible.
The script also has a simple user interface providing a random target value between 0 and 120 and
3 random dice values.
You can also put in your own choices of target value and dice values.
The script gives you the 15 combination the come closest to the target value

# Game rules
Given a target value as a whole number and three dice:
You try to get as close as possible to the target value by combining the three dice values with the operations +, -, *, /
with following rules
1. each dice can only be used once
2. all dice have to be used
3. you can multiply the value of a dice with any factor 10^n
4. operations +, -, *, / can only be used once
5. calculation of the result follow the order of operation (no priority of * or / and no brackets allowed)
6. all results, also the interim results, need to be whole numbers and greater or equal to zero.

Example:

target value:65

dice values 1, 2, 3
Minimum difference 0: 1*100 + 3*10 = 130 and 130/2 = 65
