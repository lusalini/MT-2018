# Albina und Luca

import nltk

def open_and_tokenize(input):
    """Reads in file by its location and returns a list of the tokenized text."""

    out = []
    with open(input, 'r') as infile:
        for counter, line in enumerate(infile):
            out.append(nltk.word_tokenize(line))
    return out


def compute_ngram_precision(hypothesis, reference, ngram_nr=2):
    """Computes the ngram-precision of a hypothetical translation with the help of a reference sentence"""

    counter = 0

    if type(hypothesis) == str:
        hypothesis = nltk.word_tokenize(hypothesis)
    elif type(reference == str):
        reference = nltk.tokenize(reference)

    hypothesis = nltk.ngrams(hypothesis, ngram_nr)
    reference = nltk.ngrams(reference, ngram_nr)

    for gram in hypothesis:
        if gram in reference:
            counter += 1
            


if __name__ == '__main__':
    print(open_and_tokenize(r'C:\Users\salin\Google Drive\Uni Zurich\4 Semester\Maschinelle Übersetzung\Übungen\mt18_uebung1\artikel_zeit\text_de.txt'))
