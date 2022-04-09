#!/usr/bin/python3

import sys


def read_mapper_output(file, separator):
    # output is a generator (better performance)
    for line in file:
        yield line.strip().split(separator, 1)


def main(separator='\t'):
    current_word = None
    current_count = 0
    word = None

    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    for word, count in data:
        try:
            count = int(count)
        except ValueError:
            continue

        if current_word == word:
            current_count += count
        else:
            if current_word:
                # write the result to STDOUT
                print(current_word, current_count, sep=separator)
            current_count = count
            current_word = word


if __name__ == "__main__":
    main()
