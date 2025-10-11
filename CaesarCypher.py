import string

def caesar():
    alphabet = string.ascii_lowercase
    hi = "abc"

    code = "ghofhlpmlrfmwbulmcifldiadywblhvwglaomlgssalkswfrlpihlwhlwglhvslcbzmlkomlhvsgslqccywsglkwzzlpoysldfcdsfzmlobrlbchlhifblcihlqoysmlgdfsorlmcifldiadywblcbloldzohslobrldzoqsloldodsflhckszlcjsflhvslhcdlzwuvhzmldfsgglhclopgcfplhvslzweiwrlfsdsohlhvslghsdlohlzsoghltciflacfslhwasglgshlogwrslwblolgaozzlpckzlkvwgylhcushvsflhvsltzcifldiadywbldwslgdwqslpoywbulgcrolpoywbuldckrsflobrlgozhlgshlogwrslwblolzofuslpckzlqfsoalhvslgcthsbsrlpihhsflobrlpfckblgiuoflhcushvsflkwhvloblszsqhfwqlawlsflorrlwblhvslsuulmczyglobrljobwzzolobrlawlltcflcbslawbihslibhwzldozslobrltzittmlorrlwblhvsldiadywblobrlqcapwbslawllwblhvslrfmlwbufsrwsbhglgqccdlhvslrciuvlwbhclswuvhssblpozzglobrlfczzlhvsalwblhvslgdwqsrlgiuoflpoyslhvslqccywsglobrlhvsblzshlqcczlgzwuvhzmlpstcfslsbxcmwbu"
    for alpha_rotation in range(len(alphabet)):
        trial_string = ""
        cleaned_string = ""
        for letter in code:
            index_of_letter = alphabet.index(letter)
            trial_string += alphabet[(index_of_letter + alpha_rotation) % len(alphabet)]
        if "pumpkin" in trial_string:
            print(f'Found the rotation {alpha_rotation}!')
            for char in trial_string:
                if char == "x":
                    cleaned_string += " "
                else:
                    cleaned_string += char
            print(cleaned_string)


caesar()