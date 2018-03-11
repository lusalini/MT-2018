# Albina und Luca

import nltk
from math import exp

def open_and_tokenize(input):
    """Reads in file by its location and returns a list of the tokenized text."""

    out = []
    with open(input, 'r') as infile:
        for counter, line in enumerate(infile):
            out.append(nltk.word_tokenize(line))
    return out


def compute_ngram_precision(hypothesis, reference, ngram_nr=2):
    """Computes one explicit ...gram-precision of a hypothetical translation with the help of a reference sentence"""

    counter = 0
    length = 0

    if type(hypothesis) is str:
        hypothesis = nltk.word_tokenize(hypothesis)
    if type(reference is str):
        reference = nltk.word_tokenize(reference)

    hypothesis = list(nltk.ngrams(hypothesis, ngram_nr))
    reference = list(nltk.ngrams(reference, ngram_nr))

    # print([i for i in reference])
    # print([i for i in hypothesis])
    for gram in hypothesis:
        length += 1
        if gram in reference:
            counter += 1

    #print(counter)
    #print(length, '\n\n')
    return counter/length

def compute_BLEU(hypothesis, reference, ngram_nr=2):
    """Computes the BLEU Score of a hypothetical translation with the help of a reference sentence"""
    product = 1
    N = ngram_nr

    while ngram_nr > 0:
        product = product * compute_ngram_precision(hypothesis, reference, ngram_nr)
        ngram_nr -= 1

    ngram_prec = product ** (1/N)
    # print(ngram_prec)

    brevity_penalty = min([1, exp(1 - (len(nltk.word_tokenize(reference)) / len(nltk.word_tokenize(hypothesis))))])
    # print(brevity_penalty)

    return brevity_penalty * ngram_prec


if __name__ == '__main__':
    hypo = 'airport security Israeli officials are responsible'
    ref = 'Israeli officials are responsible for airport security'

    #print(open_and_tokenize(r'C:\Users\salin\Google Drive\Uni Zurich\4 Semester\Maschinelle Übersetzung\Übungen\MT-2018\mt18_uebung1\artikel_zeit\text_de.txt'))
    print(compute_BLEU(hypo, ref, 4))