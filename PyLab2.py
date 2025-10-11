import math

'''
def odd_or_even():
    n = int(input("Enter a number"))
    if n % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

odd_or_even()


def d_to_h():
    human_years = int(input("Enter human years"))
    dog_years = 0
    for year in range(0, human_years):
        if year <= 2:
            dog_years += 10.5
        else:
            dog_years += 4
    print(dog_years)

d_to_h()

def quadratic():
    a = int(input("Input a value for a"))
    b = int(input("Input a value for b"))
    c = int(input("Input a value for c"))

    root_count = 0

    discriminant = (b**2) - (4*a*c)

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f'The equation has two roots, which have values of {root1} and {root2}')
    elif discriminant == 0:
        root = -b / (2*a)
        print(f'The equation has one root, which has a value of {root1}')

    else:
        print(f'The equation has no real roots')

quadratic()



def factorial():
    n = int(input("Input number"))
    result = 1

    for number in range(1, n+1):
        result *= number

    print(result)


factorial()


def non_trivial():

    for number in range(2, 100):
        number_string = str(number) + " : "
        for factor in range(2, number):
            if number % factor == 0:
                number_string += str(factor) + " "
            else:
                continue
        print(number_string)

non_trivial()

'''

def ex():
    n = int(input("Enter a real number"))

