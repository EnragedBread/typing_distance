import pytest
import keyboard

from pytest import approx

def test_key_distance():
    key1 = keyboard.key_coords['a']
    key2 = keyboard.key_coords['s']
    assert keyboard.key_distance(key1, key2) == 19.5

def test_key_distance_reversed_proof():
    key1 = keyboard.key_coords['s']
    key2 = keyboard.key_coords['a']
    assert keyboard.key_distance(key1, key2) == 19.5

def test_key_distance_in_a_diagonal_line():
    key1 = keyboard.key_coords['t']
    key2 = keyboard.key_coords['h']
    assert keyboard.key_distance(key1, key2) == approx(31.2156, abs=1e-3)

def test_same_letter_is_hit_twice_in_a_row():
    key1 = keyboard.key_coords['q']
    assert keyboard.key_distance(key1, key1) == 0

def test_no_letter_word():
    word = ''
    assert keyboard.measure(word) == 0

def test_3_letter_word():
    word = 'hat'
    assert keyboard.measure(word) == approx(173.1804, abs=1e-3)

def test_4_letter_word():
    word = 'hate'
    assert keyboard.measure(word) == approx(212.1804, abs=1e-3)

def test_4_letter_word_with_caps():
    word = 'Hate'
    assert keyboard.measure(word) == approx(212.1804, abs=1e-3)

def test_empty_word():
    word = ''
    assert keyboard.measure(word) == 0

def test_throws_an_error_with_bad_keys():
    word = 'at5gh'
    with pytest.raises(keyboard.KeyboardSusInputError):
        keyboard.measure(word)

def test_if_a_number_is_a_valid_key():
    letter = '5'
    assert keyboard.is_valid_key(letter) == False

def test_if_a_symbol_is_a_valid_key():
    letter = '&'
    assert keyboard.is_valid_key(letter) == False

def test_if_a_letter_is_a_valid_key():
    letter = 'a'
    assert keyboard.is_valid_key(letter) == True

def test_if_a_capital_is_a_valid_key():
    letter = 'A'
    assert keyboard.is_valid_key(letter) == False

def test_if_a_space_is_a_valid_key():
    letter = ' '
    assert keyboard.is_valid_key(letter) == False

def test_if_a_empty_string_is_valid():
    letter = ''
    assert keyboard.is_valid_key(letter) == True