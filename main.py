from choose_from import choose_from_menu_with_easteregg
from keyboard import KeyboardSusInputError, measure, is_valid_key

def comparison(word_parts1, word_parts2):
    _, _, keep1 = word_parts1
    _, _, keep2 = word_parts2
    length1, len_per_letter1 = single_word(*word_parts1)
    length2, len_per_letter2 = single_word(*word_parts2)

    if length1 > length2:
        print(f'\nThe first word: "{keep1}" had a longer typing distance than your second word: "{keep2}"!')
    else:
        print(f'\nYour second word: "{keep2}" had a longer typing distance than your first word: "{keep1}"!')

    if len_per_letter1 > len_per_letter2:
        print(f'The first word had a larger length per letter ({len_per_letter1:.4f}mm) than the second word ({len_per_letter2:.4f}mm)!')
    else:
        print(f'The second word had a larger length per letter ({len_per_letter2:.4f}mm) than the first word ({len_per_letter1:.4f}mm)!')

def single_word(word, discard, keep):
    try:
        length = measure(keep)
        len_per_letter = length / len(keep)
        print(f'\nThe characters "{discard}" from your input "{word}" were excluded, this was because they were invalid characters! ')
        print(f'Your word: "{keep}" has a length of {length:.4f}.')
        print(f'It consists of {len(keep)} letters, and on average has a length of {len_per_letter:.4f} mm per letter.')
        return (length, len_per_letter)
    except KeyboardSusInputError:
        print(f'Sorry, you must have entered an invalid character!')
        raise

def get_word(prompt):
    discard = []
    keep = []
    word = input(prompt).strip()
    for letter in word:
        if not is_valid_key(letter):
            discard.append(letter)
        else:
            keep.append(letter)
    return (word, ''.join(discard), ''.join(keep))

def easter_egg1():
    print('no')

def main():
    function = choose_from_menu_with_easteregg(
        ['length', 'compare'],
        'Would you like to determine the length of a word, or compare two different word lengths? ',
        'is this program right',
        easter_egg1
        )
    if function == 'compare':
        word_parts1 = get_word('What word would you like to compare the length of? (mm) ')
        word_parts2 = get_word('What other word would you like to compare the length of? (mm) ')
        comparison(word_parts1, word_parts2)
    elif function == 'length':
        word_parts = get_word('What word would you like to determine the length of? (mm) ')
        single_word(*word_parts)
    else:
        print('oops bad choice')

if __name__ == '__main__':
    main()


# create variable names for things being compared in ln 11