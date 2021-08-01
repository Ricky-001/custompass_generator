#!/usr/bin/python3

from statics import charsets

#msg = input('text: ')
#newmsg = ''
#m = msg


def cases(word):
    new_wordlist = []

    # Make each one upper (hello => Hello, hEllo, heLlo, helLo, hellO)
    i=0
    for char in word:
        new_word = word[:i] + char.upper() + word[i+1:]
        i += 1
        if new_word not in new_wordlist: new_wordlist.append(new_word)

    # Make pairs upper (hello => HeLlO)
    i=0
    new_word = ''
    for char in word:
        if i % 2 == 0: new_word += char.upper()
        else: new_word += char
        i += 1
    if new_word not in new_wordlist: new_wordlist.append(new_word)

    # Make odds upper (hello => hElLo)
    i=0
    new_word = ''
    for char in word:
        if i % 2 != 0: new_word += char.upper()
        else: new_word += char
        i += 1
    if new_word not in new_wordlist: new_wordlist.append(new_word)

    # Make consonants upper (hello => HeLLo)
    vowels = 'aeiou'
    new_word = ''
    for char in word:
        if char.lower() not in vowels: new_word += char.upper()
        else: new_word += char
    if new_word not in new_wordlist: new_wordlist.append(new_word)

    # Make vowels upper (hello => hEllO)
    new_word = ''
    for char in word:
        if char.lower() in vowels: new_word += char.upper()
        else: new_word += char
    if new_word not in new_wordlist: new_wordlist.append(new_word)

    return new_wordlist

# test for cases
#wl = cases('message')
#print(wl)



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

    return wordlist

# test for leet
#wl = leetit('message')
#print(wl)



def separator(msg):

    wordlist = []
    for sep in charsets.sep_charset:
        #print(*msg.split(' '), sep=sep)
        #print(sep.join(msg.split(' ')))
        word = sep.join(msg.split(' '))
        wordlist.append(word)
    return wordlist

# test for separator
#wl = separator('message is cool')
#print(wl)

def take_initials(word):
    splitted = word.split(' ')
    initials = ''
    for char in splitted:
        try:
            initials += char[0]
        except IndexError:
            continue
    return initials

# test for initials
#wl = take_initials('message is cool')
#print(wl)

def presuf(final_wordlist):
    # include common prefixes/ suffixes
    wordlist=[]
    for pre_suf in charsets.common_prefix_suffix:        
        for passes in final_wordlist:            
            wordlist.append(passes+pre_suf)
            #print(wordlist)
        #final_wordlist.append(pre_suf+passes)
    return wordlist

# test for presuf
#wl = presuf(['raktim','saha'])
#print(wl)

import itertools
def combine(baselist,nWords):
    wordlist = baselist[:]
    combined_wordlist = itertools.permutations(wordlist, nWords)
    
    for combination in combined_wordlist:
        word = ''
        for i in combination:
            word += i
            print(word)
        if word not in wordlist:
            wordlist.append(word)

    return list(set((wordlist)))

# test for itertools combinator
#wl = combine(['raktim', 'saha', 'rs', 'Raktim', 'rAktim', 'raKtim', 'rakTim', 'raktIm', 'raktiM', 'RaKtIm', 'rAkTiM', 'RaKTiM', 'rAktIm', 'Saha', 'sAha', 'saHa', 'sahA', 'SaHa', 'sAhA', 'Rs', 'rS', 'RS', 'rs'],2)
#print('\n\n',wl)

def leet_transform(word):
    wordlist = []
    wordlist.append(word)
    size = len(wordlist)            # used to check whether new wordlist is modified
    #print('size',size)
    for word in wordlist:
        size = len(wordlist)
        #print('wordlist',wordlist)
        for character in word:
            #print('character',character)
            if character in charsets.leet_chars:                # if character is one of the 1337 transformable characters
                for leet in charsets.leet_charset[character]:   # retrive the list of 1337 transforms for that character
                    newword = word.replace(character, leet)     # replace character with its 1337 transform
                    #print('leet word',newword)
                    wordlist.append(newword)                    # append the new word to the wordlist
        if len(wordlist)==size:
            break
    return wordlist

wl = leet_transform('raktim')
print(wl)