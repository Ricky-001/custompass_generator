#!/usr/bin/python3

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
