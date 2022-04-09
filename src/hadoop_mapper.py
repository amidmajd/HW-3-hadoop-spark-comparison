#!/usr/bin/python3

import sys
import string


def clean_word(word):
    for char in string.punctuation + '0123456789':
        word = word.replace(char, "")
    return word.lower().strip().replace('\n', ' ')


def read_input(file):
    # split the line into words
    # output is a generator (better performance)
    for line in file:
        yield line.split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for words in data:
        for word in words:
            token = clean_word(word)
            if token:
                print(token, 1, sep=separator)


if __name__ == "__main__":
    main()
