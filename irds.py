# irsa.py
# The International Radiotelephony Spelling Alphabet, commonly known as the military alphabet

import string

def irsa_key() -> dict:
    code = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 
        'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 
        'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 
        'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-Ray', 'Yankee', 'Zulu']
    alphabet = string.ascii_uppercase
    irsa_key = {key:value for key, value in zip(alphabet, code)}
    return irsa_key

def letter_to_code(letter: str) -> str:
    military_code = irsa_key()
    return military_code[letter]

def word_to_code(word: str, codex: dict) -> str:
    coded_word = ''
    for letter in word:
        coded_word += letter_to_code(letter.upper())
    return coded_word

if __name__ == '__main__':
    x = irsa_key()
    print(x)
    y = letter_to_code('M')
    print(y)
    z = word_to_code('Daniel', x)
    print(z)
