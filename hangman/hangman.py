import math
import os
import random
from unicodedata import normalize
import re
import importlib
constants = importlib.import_module('constants', './constants.py')

HANGMAN_PICS= constants.HANGMAN_PICS


def clear_console():
    os.system('clear')


def normalize_word(word):

    # -> NFD y eliminar diacríticos
    word = re.sub(
    r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
    normalize("NFD", word), 0, re.I
    )

    # -> NFC
    word = normalize('NFC', word)

    return word


def hangman(word):
    word = list(normalize_word(word).upper())
    blank = list('_'*len(word))

    attempts = 0
    fails = 0

    clear_console()

    while word != blank:
        hanged = HANGMAN_PICS[fails]

        print(hanged)

        letter = input('Ingresa una letra: ').upper()

        if letter in word and not letter in blank:
            for i in range(0, len(word)):
                if letter == word[i]:
                    blank[i] = letter
        else:
            print('Esta letra no está en la palabra, inténtalo de nuevo')
            fails += 1

        attempts += 1

        print(' '.join(blank))

        if fails == 6 and word != blank:
            print('Has perdido!')
            print(f'La palabra era {"".join(word)}')
            break
        
        if word == blank:
            print('GANASTE!!!')


def choose_word():
    words = []

    with open('./files/data.txt', 'r', encoding='utf-8') as f:
        words = [word.replace('\n', '') for word in f]

    random_word = words[random.randint(0, len(words)-1)]

    return random_word


def run():
    word = choose_word()
    hangman(word)


if __name__ == '__main__':
    run()
