# DiceGameSolver
A simple python based script the evaluates all possible compinations of 3 dice values 2 operators (+, -, *, /) and multiples of 10
in order to get to a target value as close as possible.

The script also has a simple user interface providing a random target value between 0 and 120 and
3 random dice values.

You can also put in your own choices of target value and dice values.
The script gives you the 15 combinations the come closest to the target value

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

Playing with more people: 
Each person tries to find a solution as fast as possible. 
The fist person announcing the difference to the target value they found locks in such difference and cannot change it anymore within this round.
The other have now time to find a smaller difference. By announcing a smaller difference the corresponding player locks again in its difference value for this round. The round ends if all players come to the conclusion that there is no better solution, solution with smaller difference to the target value.

Example:

target value:65

dice values 1, 2, 3


Playing with several players:
Maybe the first player announces a difference of 2 (without disclosing the solution!), because they found e.g. the solution 2*10 + 1 = 21 and 
21 *3 = 63 which is 2 lower than 65. 
Now the other player have time to think of better solutions, e.g. the difference 0 with the following solution.
calculating 1\*100 + 3\*10 = 130 and 130/2 = 65

The player that comes closest to 65 first wins the round.

