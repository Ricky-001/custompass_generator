#!/usr/bin/python3

class color:

    GREY = u'\033[90m'
    RED = u'\033[91m'
    GREEN = u'\033[92m'
    YELLOW = u'\033[93m'
    BLUE = u'\033[94m'
    PURPLE = u'\033[95m'
    CYAN = u'\033[96m'    
    ORANGE = u'\033[33m'
    BOLD = u'\033[1m'
    UNDERLINE = u'\033[4m'
    CBLINK    = u'\033[5m'
    END = u'\033[0m'    

class charsets:

    leet_chars = 'aeiolsbtcgh'
    leet_charset = {'a':['4','@'], 'e':['3'], 'i':['1','!','¡'],
                    'l':['1'], 'o':['0'], 's':['$','5'], 'b':['8'], 
                    't':['7'], 'c':['('], 'g':['6'], 'h':['#'],}

    # long list of separators
    #sep_charset = "!#$%&+-/:@\^_~"
    # short list of separators
    sep_charset = " -_+"

    # to use an extensive list of prefixes and suffixes
    # just uncomment the lines and the code block below
    common_prefix_suffix = []    
    for i in range(10):
        common_prefix_suffix.append(str(i))
        #common_prefix_suffix.append(chr(i+65))
        #common_prefix_suffix.append(chr(i+97))
        common_prefix_suffix.append(str(i).zfill(2))
        common_prefix_suffix.append(str(i).zfill(3))
    common_prefix_suffix.extend(['123','12345','abc','abcd','abcde','987'])
