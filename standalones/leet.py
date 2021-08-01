#!/usr/bin/python3 

from statics import charsets

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
