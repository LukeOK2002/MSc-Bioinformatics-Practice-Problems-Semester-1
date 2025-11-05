def pig_latin(s):
    s_list = s.split()
    new_string = ""
    for item in s_list:
        if item[0] in "aeiouAEIOU": #Checks whether word begins with a vowel or not and applies transformation depending on which case applies
            for index, char in enumerate(item):
                if index != len(item)-1 and char not in "!£$%^&*()?~#'@}][{-_.,|/":
                    new_string += char
                elif index == len(item)-1 and char not in "!£$%^&*()?~#'@}][{-_.,|/":
                    new_string += char + "way "
                elif index == len(item)-1 and char in "!£$%^&*()?~#'@}][{-_.,|/":
                    new_string += "way" + char
        else:
            ending_append = ""
            vowel_index = 0
            starting_capitalisation = False
            if item[0].isupper():
                starting_capitalisation = True
            for index, char in enumerate(item): #Checks whether letter is a vowel or not, and if it is, records its position and stores previous letters in 'ending_append'
                if char.lower() in "aeiou":
                    vowel_index = index
                    break
                else:
                    ending_append += char.lower()
            for index, char in enumerate(item): #Interprets character positions as either: before the vowel, at the vowel, after the vowel, or after the vowel and at the end
                if index < vowel_index:
                    continue
                elif char in "!£$%^&*()?~#'@}][{-_.,|/": #Punctuation comes at the end of the word, so ending sequence can be executed here too
                    new_string += ending_append + "ay" + char + " "
                elif index == vowel_index and starting_capitalisation:
                    new_string += char.upper()
                elif index == vowel_index and index == len(item) - 1: #For cases where first vowel is at the end of the word
                    new_string += char.lower() + ending_append + "ay "
                elif index >= vowel_index and index < len(item) - 1: #For positions after the first vowel but before the end of the string
                    new_string += char.lower()
                elif index != vowel_index and index == len(item) - 1: #For the position at the end of the string
                    new_string += char + ending_append + "ay "
    print(new_string)
    return new_string

