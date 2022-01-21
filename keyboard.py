import math

from string import ascii_lowercase

class KeyboardSusInputError(Exception):
    pass

key_coords = {
    '~': (1, 4),
    '1': (2, 4),
    '2': (3, 4),
    '3': (4, 4),
    '4': (5, 4),
    '5': (6, 4),
    '6': (7, 4),
    '7': (8, 4),
    '8': (9, 4),
    '9': (10, 4),
    '0': (11, 4),
    '-': (12, 4),
    '=': (13, 4),
    'backspace': (15, 4),
    'tab': (1.5, 3),
    'q': (2.5, 3),
    'w': (3.5, 3),
    'e': (4.5, 3),
    'r': (5.5, 3),
    't': (6.5, 3),
    'y': (7.5, 3),
    'u': (8.5, 3),
    'i': (9.5, 3),
    'o': (10.5, 3),
    'p': (11.5, 3),
    '[': (12.5, 3),
    ']': (13.5, 3),
    '|': (15, 3),
    'caps': (1.75, 2),
    'a': (2.75, 2),
    's': (3.75, 2),
    'd': (4.75, 2),
    'f': (5.75, 2),
    'g': (6.75, 2),
    'h': (7.75, 2),
    'j': (8.75, 2),
    'k': (9.75, 2),
    'l': (10.75, 2),
    ';': (11.75, 2),
    '"': (12.75, 2),
    'enter': (15, 2),
    'l_shift': (2.25, 1),
    'z': (3.25, 1),
    'x': (4.25, 1),
    'c': (5.25, 1),
    'v': (6.25, 1),
    'b': (7.25, 1),
    'n': (8.25, 1),
    'm': (9.25, 1),
    ',': (10.25, 1),
    '.': (11.25, 1),
    '/': (12.25, 1),
    'r_shift': (15, 1),
    'l_ctrl': (1.5, 0),
    'windows': (2.75, 0),
    'l_alt': (4, 0),
    'space': (9.75, 0),
    'r_alt': (11, 0),
    'fn': (12.25, 0),
    'list': (13.5, 0),
    'r_ctrl': (15, 0)
}

key_pitch = 19.5

def is_valid_key(key):
    return key in ascii_lowercase

def key_distance(key1, key2):
    return (key_pitch * (math.sqrt((key2[0] - key1[0])**2 + (key2[1] - key1[1])**2)))

def measure(word):
    distance = 0
    if not word:
        return 0
    prev = word[0].lower()
    for letter in word.lower():
        if not is_valid_key(letter):
            raise KeyboardSusInputError
        distance += key_distance(key_coords[prev], key_coords[letter])
        prev = letter
    return distance