#!/usr/bin/python3

# transsforms various characters into uppercase - works with words
def cases_transform(word):
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
