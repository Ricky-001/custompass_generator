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
    wordlist = []                                   # my, pass
    for word in words:                              # for each base word                    (pass)
        for separator in charsets.sep_charset:      # iterate through each separator        (_)
            wordlist.append(word + separator)       # add the separator to the end          (pass_) for pass_somethingelse
            wordlist.append(separator + word)       # add the separator at the beginning    (_pass) for my_pass

    base_separated = wordlist[:]

    for word in words:                                          # iterate through the baselist
        for separated_word in base_separated:                   # iterate over separated words
            if word not in separated_word:                      # if its a part of the separated word (pass and _pass should not combine)
                if separated_word[-1] in charsets.sep_charset:  # if separator appended to word, then add word to end
                    wordlist.append(separated_word + word)      # pass_ + 123 = pass_123
                elif separated_word[0] in charsets.sep_charset: # if separator prepended to word, add word to beginning
                    wordlist.append(word + separated_word)      # my + _pass = my_pass
    
    # remove words starting or ending with separators
    for word in wordlist:
        if word[0] in charsets.sep_charset or word[-1] in charsets.sep_charset:
            wordlist.remove(word)
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

