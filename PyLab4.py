import string
#Write a function to remove all the vowels from a string. The function should take
#a single string parameter and return a modified copy of the string containing all the
#consonants but none of the vowels. For example, the string ‘vowels’ should yield ‘vwls’
#and ‘consonants’ should yield ‘cnsnnts’

def anti_vowel(string):
    new_string = ""

    for char in string:
        if char not in "aeiou":
            new_string += char
        else:
            continue

    print(new_string)

#Write a Python function that takes as string and that prints out the individual words
#each on a separate line with their first letter capitalised. Assume the the string contains
#letters only (no digits or punctuation) and that words are separated from one one
#another by means of a single space. Hint: you can detect the first letter of each word
#by checking if the previous character is a space

#First iteration, without split method
def complicated_word_separator(sentence):
    space_list = []
    word_list = []

    #Getting positions of spaces
    for index, char in enumerate(sentence):
        if char == " ":
            space_list.append(index)

    for space in range(len(space_list)):
        if space == 0:
            word_list.append(sentence[0: space_list[space]])
        else:
            word_list.append(sentence[(space_list[(space - 1)]) + 1: space_list[space]])

    word_list.append(sentence[space_list[-1] + 1:len(sentence)])

    for word in word_list:
        new_word = ""
        for char_index, char in enumerate(word):
            if char_index == 0:
                new_word += char.upper()
            else:
                new_word += char.lower()
        print(new_word)

#Second iteration, with split method, much simpler!
def simple_word_separator(sentence):
    x = sentence.split()
    for word in x:
        capitalised_word = ""
        for index, char in enumerate(word):
            if index == 0:
                capitalised_word += char.upper()
            else:
                capitalised_word += char.lower()
        print(capitalised_word)

#In the game of Scrabble, each letter has a number of points associated with it. The total
#score for a word is the total of the points/score of its constituent letters. The points for
#each letter are as shown below:
#Write a function that takes a string parameter and that determines and returns the
#Scrabble score for that string. Your function should ignore capitalization. Any string
#that contains any non-letters (including spaces) should result in a score of zero. Lists,
#strings and ifs should suffice to solve this.
def scrabble(word):
    score = 0
    one_point = "aeilnorstu"
    two_points = "dg"
    three_points = "bcmp"
    four_points = "fhvwy"
    five_points = "k"
    eight_points = "jx"
    ten_points = "qz"

    for char in word.lower():
        if char in string.digits or char in string.punctuation:
            print(f'Invalid input, 0 points')
            return
        else:
            if char in one_point:
                score += 1
            elif char in two_points:
                score += 2
            elif char in three_points:
                score += 3
            elif char in four_points:
                score += 4
            elif char in five_points:
                score += 5
            elif char in eight_points:
                score += 8
            elif char in ten_points:
                score += 10

    print(f'Total score is {score}')

#Write a function that that takes a list of integer values and a non-negative integer n as
#its parameters. The function should create a new copy of the list with the n smallest
#and the n largest elements removed. It should return the new copy of the list as the
#function’s result. It may be easier to start with a function that strips out the single
#largest and smallest and use that n times.

def list_janitor(input_list, n):
    list = input_list.copy()

    #n must be non-negative
    if n < 0:
        raise "Invalid input"

    n_lower_count = 0
    n_upper_count = 0

    while n_lower_count != n:
        for list_element in list:
            if list_element == min(list):
                list.remove(list_element)
                n_lower_count += 1

    while n_upper_count != n:
        for list_element in list:
            if list_element == max(list):
                list.remove(list_element)
                n_upper_count += 1

    print(list)

#Halved in length!
def list_janitor_simple(input_list, n):
    list = input_list.copy()
    list.sort()
    for list_element in range(0, n):
        list.remove(list[list_element])
    for list_element in range(n, 0, -1):
        list.remove(list[list_element])
    print(list)

list_janitor_simple([3, 5, 6, 3, 2, 4, 1], 2)

#A integer, n, is said to be perfect when the sum of all the proper divisors of n is equal
#to n. For example, 28 is perfect because its proper divisors are 1, 2, 4, 7 and 14 and
#1 + 2 + 4 + 7 + 14 = 28. Write a function that determines whether a positive integer is
#perfect. Your function should take the positive integer as its sole parameter and that
#returns True or False to indicate whether it is perfect or not.

def perfect_number(n):
    divisor_sum = 0
    for potential_divisor in range(1, (n-1)):
        if n % potential_divisor == 0:
            divisor_sum += potential_divisor
    if divisor_sum == n:
        return True
    else:
        return False
