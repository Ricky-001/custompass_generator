#!/usr/bin/python3

import re

# Cleans raw lyrics into usable passphrases
def make_phrases(line, min_len, max_len):
    clean_lines = []
    final_lines = []

    # Allow only letters, numbers, spaces, and some punctuation
    allowed_chars = re.compile("[^a-zA-Z0-9 '&]")

    # lowercase the line
    line = line.lower()
    
    # remove word separators by space
    line = re.sub(r'[-_]', ' ', line)

    # Remove special characters
    line = allowed_chars.sub('', line)

    # Remove multiple spaces
    line = re.sub(r'\s\s+', ' ', line)

    # remove all spaces from the line and make a phrase
    clean_lines.append(line.replace(' ',''))
    
    # If line has an apostrophe make a duplicate without
    if "'" in line:
        clean_lines.append(re.sub("'", "", line))

    # Making duplicate phrases including and / &
    if ' and ' in line:
        clean_lines.append(re.sub(' and ', ' & ', line))
    if '&' in line:
        newline = re.sub('&', ' and ', line)
        newline = re.sub(r'\s+', ' ', newline).strip()
        clean_lines.append(newline)

    # Add what is left to the list
    clean_lines.append(line)

    # remove lines not measuring within the given length
    for item in clean_lines:
        #print(len(item))
        if len(item) in range(min_len,max_len+1):
            final_lines.append(item)

    return final_lines