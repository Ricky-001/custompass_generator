#!/usr/bin/python3 

from multiprocessing.dummy import Pool as ThreadPool
from .statics import charsets

##########################################################################################################################

# leet transform a word - only pass a word, doesn't check for blanks
def leet_transform(word):
    wordlist = []
    wordlist.append(word)
    size = len(wordlist)            # used to check whether new wordlist is modified

    #print('size',size)
    for word in wordlist:
        size = len(wordlist)                                    # needed to check whether the size changes (indicating list modified)
        #print('wordlist',wordlist)
        for character in word:
            #print('character',character)
            if character in charsets.leet_chars:                # if character is one of the 1337 transformable characters
                for leet in charsets.leet_charset[character]:   # retrive the list of 1337 transforms for that character
                    newword = word.replace(character, leet)     # replace character with its 1337 transform
                    #print('leet word',newword)
                    wordlist.append(newword)                    # append the new word to the wordlist
        
        if len(wordlist)==size:                                 # if wordlist size same as before (no new word added)
            break                                               # break condition for the infinite loop
    return list(set(wordlist))

##########################################################################################################################
############################ RECURSIVE LEET TRANSFORM DOESN'T WORK - RECURSION LIMIT EXCEEDED ############################
##########################################################################################################################

# leet transform a word - only pass a word, doesn't check for blanks
def leetit(word):
    wordlist = []    

    for character in word:
        if character in charsets.leet_chars:                # if character is one of the 1337 transformable characters
            for leet in charsets.leet_charset[character]:   # retrive the list of 1337 transforms for that character
                newword = word.replace(character, leet)     # replace character with its 1337 transform
                wordlist.append(newword)                    # append the new word to the wordlist
                #print(num,newword)

    # for each new word after leet transform,
    # pass it for any other possible leet characters
    for newword in wordlist:
        size = len(wordlist)            # used to check whether new wordlist is modified
        wordlist.extend(leetit(word))   # execute possible 1337 transforms
        if len(wordlist) == size:       # if new word is not added, stop recursion (no character remains for transformation)
            break

    return list(set(wordlist))

##########################################################################################################################
##########################################################################################################################

# transsforms various characters into uppercase - works with words
def case_transform(word):
    wordlist = []
    vowels = 'aeiou'

    # Make each character upper one by one
    i=0
    for char in word:
        new_word = word[:i] + char.upper() + word[i+1:]
        i+=1
        if new_word not in wordlist:
            wordlist.append(new_word)

    # Make even characters uppercase
    i=0
    new_word = ''
    for char in word:
        if not i%2:
            new_word += char.upper()
        else:
            new_word += char
        i+=1
    if new_word not in wordlist:
        wordlist.append(new_word)

    # Make odd characters uppercase
    i=0
    new_word = ''
    for char in word:
        if i%2:
            new_word += char.upper()
        else:
            new_word += char
        i += 1
    if new_word not in wordlist:
        wordlist.append(new_word)

    # Make consonants uppercase
    new_word = ''
    for char in word:
        if char.lower() not in vowels:
            new_word += char.upper()
        else:
            new_word += char
    if new_word not in wordlist:
        wordlist.append(new_word)

    # Make vowels uppercase
    new_word = ''
    for char in word:
        if char.lower() in vowels:
            new_word += char.upper()
        else:
            new_word += char
    if new_word not in wordlist:
        wordlist.append(new_word)

    return wordlist

##########################################################################################################################

# extract initials from given words
def take_initials(word):
    splitted = word.split(' ')
    initials = ''
    for char in splitted:
        try:
            initials += char[0]
        except IndexError:
            continue
    return initials

##########################################################################################################################

def append_prepend(final_wordlist):
    # include common prefixes/ suffixes
    wordlist=[]
    for pre_suf in charsets.common_prefix_suffix:        
        for passes in final_wordlist:            
            wordlist.append(passes+pre_suf)            
            #wordlist.append(pre_suf+passes)
    return wordlist

##########################################################################################################################

def multithread_transforms(transform_type, wordlist, proc_threads):
    # process each word in their own thread and return the results
    new_wordlists = []
    with ThreadPool(proc_threads) as pool:
        new_wordlists += pool.map(transform_type, wordlist)
    new_wordlist = []
    for nlist in new_wordlists:
         new_wordlist += nlist
    return new_wordlist
