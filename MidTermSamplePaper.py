
#Write a Python program that begins by reading in a number of seconds
#from the user. Then your program should display the equivalent amount of time
#expressed in hours, minutes and seconds. Thus 5000 seconds would be displayed as
#1 hour, 23 minutes and 20 seconds.

def time_converter(n):
    seconds = int(n)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds_remaining = seconds % 60
    return str(hours) + ":" + str(minutes) + ":" + str(seconds_remaining)

#Write a Python program that calculates and prints an approximation to the value
#of π based on the first 100 items in the above product, where each () is considered
#an item
#pi/ 2 = (2/1 * 2/3) * (4/3 * 4/5) ... etc
def pi_approx():
    lower_1 = 1
    prev_result = None

    for iteration in range(1,100):
        first_fraction = iteration*2 / lower_1
        lower_1 += 2 #Should increase by 2 before second fraction calculated
        second_fraction = iteration*2 / lower_1
        product = first_fraction * second_fraction #Gets the product of the two fractions
        if prev_result is None:
            prev_result = product #If its the first result, product takes the place of prev_result
        else:
            prev_result *= product # Multiplies by previous result, e.g 2nd term multiplied by 1st term

#Write a function trim(lst) that takes a single parameter representing a
#list of integer values and that returns a list containing all the values of the original
#except the largest and the smallest. The remaining values should appear the same
#order in the result as they appear in the original. If the smallest value appears
#more than once in lst then all copies should be removed from the returned result;
#similarly for the largest.

def trim(lst):

    minimum = min(lst)
    maximum = max(lst)
    for item in lst:
        if item == minimum:
            lst.remove(item)
        elif item == maximum:
            lst.remove(item)
    print(lst)
#Question 4 A Pythagorean triple consists of three positive integers a, b and c with the
#property that a2 + b2 = c2. For example 3, 4, 5 is such a triple. Write a Python
#program that prints out all the Pythagorean triple where a, b, c ≤ 100. For full
#marks, print only distinct triples in the form a, b, c, where a ≤ b ≤ c to avoid
#duplicates such as 3, 4, 5 and 4, 3, 5.
def triples():
    limit = 100
    triple_list = []
    for a in range(1, limit+1):
        for b in range(a, limit+1):
            for c in range(b, limit+1):
                if a**2 + b**2 == c**2:
                    triple_list.append([a, b, c])
    print(triple_list)
