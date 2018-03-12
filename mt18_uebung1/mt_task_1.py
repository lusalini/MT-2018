#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MT, FS 18
# Übung 1 Aufgabe 1
# Albina Kudoyarova , Matr.Num.: 15-703-390
# Luca Salini, Matrikel Nr.: 16-732-505


import nltk
from nltk.util import ngrams
import numpy as np
import sys


def tokenize_file(input:str) -> list:
    """ Opens the input file for reading and makes a list of tokenized input"""

    with open(input, 'r') as infile:
        tokenized = nltk.word_tokenize(infile.read())

        return tokenized


def compute_ngram_precision(hypothesis, reference, ngram_nr):
    """Computes n-gram precision"""

    ngrams_hyp = list(ngrams(hypothesis, ngram_nr))
    ngrams_ref = list(ngrams(reference, ngram_nr))
    hyp_length = len(ngrams_hyp)
    correct = 0

    for item in ngrams_hyp:
        if item in ngrams_ref:
            correct += 1
            ngrams_ref.remove(item)

    p = correct / hyp_length

    return p


def compute_bleu_score(hyp, ref, ngram_nr):
    """Computes the BLEU Score of a hypothetical translation with the help of a reference sentence"""

    product = 1
    N = ngram_nr

    while ngram_nr > 0:
        product = product * compute_ngram_precision(hyp, ref, ngram_nr)
        ngram_nr -= 1

    P = product ** (1 / N)
    brevity_penalty = min(1.0, np.exp(1 - (len(ref)/len(hyp))))
    bleu = P * brevity_penalty

    return bleu


def main():
    """First type in the hypothesis filename, then the reference filename."""

    if len(sys.argv) != 3:
        print('Please give two agruments: hypothesis and reference')
        sys.exit()

    hyp = tokenize_file(sys.argv[1])
    ref = tokenize_file(sys.argv[2])
    precision = compute_ngram_precision(hyp, ref, 1)
    bleu = compute_bleu_score(hyp, ref, 4)

    print('%.3f' % bleu)


if __name__ == '__main__':
    main()
