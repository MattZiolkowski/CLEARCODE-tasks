#! python3

'''
Hack_power calculator deciphers a code written using strings and assign values
to given letters and phrases.
Power value is assigned to code letters and phrases as following:
Letters: {'a':1,'b':2, 'c':3}; Phrases: {'ba':10, 'baa':20}
Additionally, each letter in the code is multiplied by number of occurrences of that letter.
Example: Code 'abca' has power(i.e. equals to)=(1*1)+(2*1)+(1*3)+(2*1)=8
Example(with phrases): Code 'abaa' has power=(1*1)+(1*2)+(1*2)+(2*1)+(3*1)+(20)=28

Code letters and phrases can be dynamically typed (i.e. changed, added or removed in dictionaries)
'''

import re

# Creating dictionaries for accessing hack code values for code letters and phrases
# Dynamic version - keys and values can be changed or added
hackDict_letters = {'a': 1, 'b': 2, 'c': 3}
hackDict_phrases = {'ba': 10, 'baa': 10}


# Creting function
def hack_calculator(hack: str):
    # Assign input from console into variable userInput. Change to lower case
    userInput = hack.lower()

    # Initial power state
    power = 0

    # Calculating power of letters
    for letter in hackDict_letters.keys():
        pattern = re.compile(letter)
        search = pattern.findall(userInput)
        for j in range(len(search)):
            power += hackDict_letters[letter] * (j + 1)

    # Calculating power of phrases
    for phrase in hackDict_phrases.keys():
        pattern = re.compile(phrase)
        search = pattern.findall(userInput)
        for j in range(len(search)):
            power += hackDict_phrases[phrase]

    # Message in case of typing errors
    for letter in userInput:
        if letter not in hackDict_letters.keys():
            print("Code letter: " + letter + " not found.")
            power *= 0

    # Final result with a message
    print("The power of the '" + hack + "' hack code is: " + str(power))

# Example:
hack_calculator('baaca')
hack_calculator('babacaba')
hack_calculator('aabacabaaaca')
hack_calculator('abc')
hack_calculator('bad')
