#!/usr/bin/env python
import os, datetime

# clear screen
def clear():    
    os.system(['clear', 'cls'][os.name == 'nt'])

# check if a string variable is empty
def is_empty(var):    
    empty = False
    if len(str(var)) == 0:
        empty = True
    return empty

# check if the given string is 
# in the valid date format DD/MM/YYYY
def is_valid_date(date_str):    
    try:
        datetime.datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# takes a list as argument and returns a new list 
# with the values between min and max length provided
def remove_by_lengths(wordlist, min_length, max_length):    
    new_wordlist = []
    for word in wordlist:
        #if (len(str(word)) < min_length) or (len(str(word)) > max_length): wordlist.remove(word)
        if (len(str(word)) >= min_length) and (len(str(word)) <= max_length): new_wordlist.append(str(word))
    return new_wordlist