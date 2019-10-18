# lucas' first root calculator
# 18th of October 2019

import math

x = -100
answer = input("Please input the eqn you want to find the first root of (** = exponent, * = multiplication, / = divide, - = subtraction, + = addition): ")
# (x**5-5*x**4+7*x**3-7*x**3+6*x-2)
# example equation
while x != 3:
    x = float(x + 0.5)
    print(x)
    eqn = eval(answer)
    print(x, eqn)
    if eqn == 0:
        break
    print(x, eqn)
