# irsa.py
# The International Radiotelephony Spelling Alphabet, commonly known as the military alphabet

import string

def military_alphabet() -> dict:
    code = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 
        'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 
        'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 
        'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-Ray', 'Yankee', 'Zulu']
    alphabet = string.ascii_uppercase
    military_alphabet = {key:value for key, value in zip(alphabet, code)}
    return military_alphabet

def letter_to_code(letter: str) -> str:
    military_code = military_alphabet()
    return military_code[letter]

def word_to_code(word: str, codex: dict) -> str:
    coded_word = ''
    for letter in word:
        coded_word += letter_to_code(letter.upper())
    return coded_word

if __name__ == '__main__':
    x = military_alphabet()
    print(x)
    y = letter_to_code('M')
    print(y)
    z = word_to_code('Daniel', x)
    print(z)
