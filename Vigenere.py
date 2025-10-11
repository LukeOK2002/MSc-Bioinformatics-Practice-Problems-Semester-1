import string
import random

def vigenere_encrypt(message, key):
    alphabet = string.ascii_lowercase
    message = str(message.lower())
    key = str(key.lower())

    encrypted_string = ""
    while len(encrypted_string) < len(message):
        for letter in message:
            code_letter = key[(len(encrypted_string) % len(key))]
            index_of_letter = alphabet.index(letter)
            index_of_code_letter = alphabet.index(code_letter)
            #Adding the index of the letter to the index of the code letter, and using it to find
            #the position of the new character in the alphabet
            encrypted_string += alphabet[(index_of_letter + index_of_code_letter) % len(alphabet)]
    print(encrypted_string)
    #Output is rmwlqb, just as in the example
vigenere_encrypt("python", "code")

def vigenere_decrypt():
    alphabet = string.ascii_lowercase
    message = "kbokzzrbisolqkchwgzxilrhjoenzazhgfolgokhdikdgfoltcnxzglqcfokprowqzrcusjhwbksnlwvwtwizosywhodycowkbldggokfrooiuokprofcbzvnookprolgokhwbksnltyopzxgrosplrhosuswaolqkchyvzcmlwvqiihudzmggolcyzxiljyfookprocczkhwbksnlyopzxgrogkhyhvvvhowootlfxzzfgzuikfirvnmokfrontmospuiofwvxvgodqlnovlzxifvnksedulrczkvvnlrcztiouvoqkbxotlrxflfbcbxoznvcvllxvwchfclqjlaeuhomqavczhfqghyotlusxwuozrfeivosplykntokpromtsrdglkgqlusuqjhyfrzzsrmjlzxzdckuhzmzkikrlrxfltrkzchwbksnlwstaokdcldzhnyzhfhvvioglyywfjhrfvrgokhqjvxzhfhqbvhjientsuhcbuhgwxrvmokprovkbvhvkfhnoiqglskmweqzgyoghjhywkrzdrbevdophozcdvbzdckesoypsonkgthqtonqixrzcehclcsivkvalwvqiiofljettrmglrxfliynzoephzvzvrvhlrhesedkavdtsodjwtuzqldzcldzuzxisiltsrnztzqwfvczkzdjlrhusmopltophzwghiozkzngltevhvbzoenzhikpgwotlkyzprukbxhuvvovgolcyvhwbksnljvkuydnmozwtwoflrxfljovlespsodqlkopldspikouluorsenkbxhqbodjsocknvhqtoiqiihecfuksomwhkotgovghomqcchqbolcyzxiljrgskcztfbztzfgldspikoulsohciozhikpgwotfzxilkyzoomqccspuobcqbhvcomqcchecdznskonm"


    string_solved = False
    while not string_solved:
        letters = string.ascii_lowercase
        trial_string = ''.join(random.choice(letters) for i in range(4))
        trial_translation = ""
        clean_translation = ""
        for letter in message:
            trial_string_letter = trial_string[len(trial_translation) % len(trial_string)]
            index_of_letter = alphabet.index(letter)
            index_of_trial_string_letter = alphabet.index(trial_string_letter)
            trial_translation += alphabet[(index_of_letter + index_of_trial_string_letter) % len(alphabet)]
        if "gingerbread" in trial_translation:
            string_solved = True
            for char in trial_translation:
                if char == "x":
                    clean_translation += " "
                else:
                    clean_translation += char
            print(f'Completed translation: {clean_translation}')
            print(f'Encoded with the string: {trial_string}')



vigenere_decrypt()

