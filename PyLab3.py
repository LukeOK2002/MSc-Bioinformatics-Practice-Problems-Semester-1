import random

#Write a function that takes the lengths of the two shorter sides of a right-angled triangle
#as parameters. Return the length of the hypotenuse of the triangle, computed using the
#Pythogorean theorem, as the function’s result. Test your function on a range of inputs
#to check its correctness.
def hypotenuse(adj, opp):
    adj = float(adj)
    opp = float(opp)
    hyp = ((adj**2) + (opp**2))**0.5
    print(hyp)

#Write a function that takes three numbers as parameters and that returns the median
#of those parameters as the result. Do not use Python’s sorting capabilities
def median(a, b, c):
    if b > a and b < c:
        median = b
    elif c > a and c < b:
        median = c
    else:
        median = a
    print(f'Median is {median}')

#Write a function doughnut(n) that displays an n × n “doughnut” pattern
def doughnut(n):
    third = round(n/3)
    print(third)
    hole = ""
    ring = ""
    for char_number in range(n):
        if char_number >= (n - (2*third)) and char_number < (n - third):
            hole += " "
        else:
            hole += "_"
    for char_number in range(n):
        ring += "_"
    for line in range(n):
        if line >= (n - (2*third)) and line < (n - third):
            print(hole)
        else:
            print(ring)

#Write a function that takes a string of characters as its first parameter and the width
#of the screen as its second parameter. Your function should return a new string that
#consists of the original string and the correct number of leading spaces so that the the
#original string will appear centered within the provided width when it is printed. Do
#not add characters at the end of the string.
def stringy(string=str, screenwidth=int):
    string_vs_width = round((screenwidth / 2)) - len(string)
    spaces = string_vs_width*" "
    spaces += string
    print(spaces)

#Write a function that simulates a sequence of coin flips and returns the number of flips
#performed until the first occurrence of two consecutive heads. Use the randint function
#from Python’s random module to simulate a single coin flip. Perform a maximum of
#1000 flips; if two consecutive heads have not appeared by sthat stage return 1000 as the
#result. Note a return statement can appear anywhere with the body of a function. It
#will cause the function’s execution to cease (even from the middle of a loop say) and
#for the indicated value to be returned.
def flipper():
    prev_flip = None
    for flip in range(1, 1001):
        current = "H" if random.randint(0, 1) == 1 else "T"

        if prev_flip == "H" and current == "H":
            return flip
        prev_flip = current
    return 1000

#Write a function that takes a non-negative real number as its parameter and that returns
#an approximation of the square root of that number using the approach sketched below.
#(Do no use the ∗∗ or any of Python’s functions such as sqrt or pow etc.).
#Calculate the root by a generating a sequence of successively better approximations
#(“guesses”) for the true value. For parameter x, take x/2 as your initial guess. At
#each step update guess by replacing it by the average of the current value of guess and
#x/guess. Terminate the process after 100 iterations and return the value of guess.
def square_guess(n):
    ceiling = 0
    floor = n/2
    for guess_number in range(100):
        guess = (ceiling + floor) / 2
        if (n / guess) > guess:
            ceiling = guess
        else:
            floor = guess
