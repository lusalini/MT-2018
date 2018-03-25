#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MT, FS 18
# Übung 2 Aufgabe 2
# Albina Kudoyarova , Matr.Num.: 15-703-390
# Luca Salini, Matrikel Nr.: 16-732-505


import nltk
from nltk.util import ngrams
from collections import Counter
import sys


def read_file(input):
    with open(input, 'r') as infile:
        char_list = []
        for line in infile:
            striped_line = line.strip()
            words = striped_line.split(' ')
            for word in words:
                word_list = []
                for char in word:
                    word_list.append(char)
                word_list[-1] += '</w>'
                char_list.append(word_list)

        # print(char_list)
        return char_list


def get_starts(char_list):
    bigrams = []
    for l in char_list:
        bigrams += list(nltk.bigrams(l))

    # print(bigrams)
    freq_counter = Counter(bigrams)
    print(sorted(freq_counter.items(), key=lambda x: (-x[1], x[0][0], x[0][1]))[0][0])


def merge_units(list, freq_bigram):
    modified_list = []
    for word in list:
        modified_word = []
        for index, unit in enumerate(word):
            if unit == freq_bigram[0] and word[index+1] == freq_bigram[1]:
                modified_word.append(str(freq_bigram[0]) + str(freq_bigram[1]))
            else:
                modified_word.append(unit)
        modified_list.append(modified_word)

    return modified_list


def find_merges():
    pass


def main():
    if len(sys.argv) != 2:
        print('Please give an agrument: text')
        sys.exit()
    char_list = read_file(sys.argv[1])
    freq_bigram = get_starts(char_list)
    # merge_units(list,freq_bigram)


if __name__ == '__main__':
    main()
