# irsa.py
# The International Radiotelephony Spelling Alphabet, commonly known as the military alphabet

import string

def military_alphabet_key() -> dict:
    code = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 
        'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 
        'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 
        'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-Ray', 'Yankee', 'Zulu']
    alphabet = string.ascii_uppercase
    military_alphabet_key = {key:value for key, value in zip(alphabet, code)}
    return military_alphabet_key

def letter_to_code(letter: str, codex: dict) -> str:
    coded_letter = codex[letter]
    return coded_letter

def word_to_code(word: str, codex: dict) -> str:
    coded_word = ''
    for letter in word:
        coded_word += letter_to_code(letter.upper(), codex)
    return coded_word

if __name__ == '__main__':
    x = military_alphabet_key()
    print(x)
    y = letter_to_code('M', x)
    print(y)
    z = word_to_code('Daniel', x)
    print(z)
