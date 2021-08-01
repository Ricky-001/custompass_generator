#!/usr/bin/python3

from .statics import charsets
import itertools

# replaces spaces between words by different special characters often used as separators
def separate(msg):

    wordlist = []
    for sep in charsets.sep_charset:
        #print(*msg.split(' '), sep=sep)
        #print(sep.join(msg.split(' ')))
        word = sep.join(msg.split(' '))
        wordlist.append(word)
    return list(set(wordlist))

# takes in a wordlist and separates the different words of the list based on separator characters
def separator(baselist):

    words = baselist[:]
    wordlist = []
    for word in words:
        for separator in charsets.sep_charset:
            wordlist.append(word + separator)
            wordlist.append(separator + word)

    base_separated = wordlist[:]

    for word in words:
        for separated_word in base_separated:
            if word not in separated_word:
                wordlist.append(separated_word + word)
                wordlist.append(word + separated_word)
    
    return list(set((wordlist)))

# combines different words together
def combinator(baselist, nWords):
    wordlist = baselist[:]
    combined_wordlist = itertools.permutations(wordlist, nWords)
    for combination in combined_wordlist:
        word = ''
        for i in combination:
            word += i
        if word not in wordlist:
            wordlist.append(word)

    return list(set((wordlist)))

