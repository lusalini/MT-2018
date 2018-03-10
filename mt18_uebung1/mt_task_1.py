#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MT, FS 18
# Übung 1 Aufgabe 1
# Albina Kudoyarova , Matr.Num.: 15-703-390
# Luca Salini, Matrikel Nr.: 16-732-505


import nltk
from nltk.util import ngrams
import numpy as np


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
    ref_length = len(ngrams_ref)
    correct = 0
    for item in ngrams_hyp:
        if item in ngrams_ref:
            correct += 1
            ngrams_ref.remove(item)
    p = correct / hyp_length
    #print(p)
    return p


def compute_bleu_score(hyp, ref, ngram_nr):
    """Computes the BLEU Score of a hypothetical translation with the help of a reference sentence"""
    product = 1
    N = ngram_nr

    while ngram_nr > 0:
        product = product * compute_ngram_precision(hyp, ref, ngram_nr)
        ngram_nr -= 1


    P = product ** (1 / N)
    #print(P)
    brevity_penalty = min(1.0, np.exp(1 - (len(ref)/len(hyp))))
    bleu = P * brevity_penalty
    print('%.3f' % bleu)


if __name__ == '__main__':
    ref = tokenize_file('test_reference.txt')
    hyp = tokenize_file('test_hypothesis.txt')
    precision = compute_ngram_precision(hyp, ref, 1)
    bleu = compute_bleu_score(hyp,ref, 4)



