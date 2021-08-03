#!/usr/bin/python3

from .statics import color
from .utilities import is_empty,is_valid_date,clear
from .transforms import take_initials
from modules import banner

class userinterface:

    def __init__(self):
        self.DEFAULT_MIN = 4
        self.DEFAULT_MAX = 12
        self.DEFAULT_N_WORDS = 2
        self.DEFAULT_OUTPUT_FILE = 'custompass.txt'
        self.DEFAULT_THREADS = 5        

##########################################################################################################################

    def ui(self):
        clear()
        banner.show()
        # MIN password length
        while True:
            min_length = input('{}[?]{} Minimum password length {}(default: {}){} >>> '.format(color.BLUE, color.END,color.YELLOW,self.DEFAULT_MIN,color.END))
            if is_empty(min_length):
                self.min_length = self.DEFAULT_MIN; break
            else:
                try:
                    self.min_length = int(min_length)
                    break
                except ValueError:
                    print('{}[!] Min length should be an integer{}'.format(color.RED, color.END))
        # MAX password length
        while True:
            max_length = input('{}[?]{} Maximum password length {}(default: {}){} >>> '.format(color.BLUE, color.END,color.YELLOW,self.DEFAULT_MAX,color.END))
            if is_empty(max_length):
                self.max_length = self.DEFAULT_MAX; break
            else:
                try:
                    max_length = int(max_length)
                    if max_length < self.min_length:
                        print('{}[!] Max length should be greater or equal to Min length{}'.format(color.RED, color.END))
                    else:
                        self.max_length = max_length
                        break
                except ValueError:
                    print('{}[!] Max length should be an integer{}'.format(color.RED, color.END))

##########################################################################################################################

        # name of target
        firstname = input('{}[?]{} First Name >>> '.format(color.BLUE, color.END))
        midname = input('{}[?]{} Middle Name >>> '.format(color.BLUE, color.END))
        lastname = input('{}[?]{} Last Name >>> '.format(color.BLUE, color.END))

        # generate fullname
        fullname = firstname+' '+midname+' '+lastname
        # extract name initials
        name_initials = take_initials(fullname)        

##########################################################################################################################

        # DOB of target
        while True:
            birth = input('{}[?]{} Date of Birth {}(DD/MM/YYYY){} >>> '.format(color.BLUE, color.END,color.BOLD,color.END))
            if not is_empty(birth) and not is_valid_date(birth):
                print('{}[!] Please enter date in {}DD/MM/YYYY format{}'.format(color.RED, color.BOLD, color.END))
            else:
                break
        
        # other important dates
        while True:
            flag=0
            dates = input('{}[?]{} Other important dates [comma separated] {}(DD/MM/YYYY){} >>> '.format(color.BLUE, color.END,color.BOLD,color.END))
            for date in dates.split(','):                
                if not is_empty(date) and not is_valid_date(date):
                    print('{}[!] Please enter date in {}DD/MM/YYYY format{}'.format(color.RED, color.BOLD, color.END))
                    flag=0
                else:
                    flag=1                    
            if flag:
                break

##########################################################################################################################

        # other significant names/ words/ info
        othernames = input('{}[?]{} Some other relevant words/names (comma-separated) >>> '.format(color.BLUE, color.END))

        # word generator options for the tool
        leet = input('{}[?]{} Do you want to produce 1337 7r4n5f0rms? [y/n] {}(default: False){} >>> '.format(color.BLUE, color.END,color.YELLOW,color.END))
        case = input('{}[?]{} Do you want to produce cAsE tRaNsFoRmS? [y/n] {}(default: False){} >>> '.format(color.BLUE, color.END,color.YELLOW,color.END))
        sep = input('{}[?]{} Do you want to use common_word-separators replacing spaces? [y/n] {}(default: False){} >>> '.format(color.BLUE, color.END,color.YELLOW,color.END))

        if leet and leet[0].lower() == 'y':
            self.leet = True
        else:
            self.leet = False

        if case and case[0].lower() == 'y':
            self.case = True
        else:
            self.case = False
        
        if sep and sep[0].lower() == 'y':
            self.sep = True
        else:
            self.sep = False

##########################################################################################################################

        # how many words to combine together
        while True:
            n_words = input('{}[?]{} How many words do you want to combine at most {}(default: {}){} >>> '.format(color.BLUE, color.END,color.YELLOW,self.DEFAULT_N_WORDS,color.END))
            if is_empty(n_words):
                self.n_words = self.DEFAULT_N_WORDS; break
            else:
                try:
                    n_words = int(n_words)
                    if n_words < 1:
                        print('{}[!] Number of words to combine should be greater than or equal to 1{}'.format(color.RED, color.END))
                    else:
                        self.n_words = n_words
                        break
                except ValueError:
                    print('{}[!] Number of words to combine should be an integer{}'.format(color.RED, color.END))

##########################################################################################################################

        # significant artists/ role model names
        self.artists = input('{}[?]{} Favourite Artist(s) names (comma-separated)>>> '.format(color.BLUE, color.END))        
        if is_empty(self.artists):
            self.artists = False
        else:
            self.artists = self.artists.split(',')
            print('[*] The script will attempt to search for relevant song lyrics (ensure internet connection)')

##########################################################################################################################

        # number of process threads for multiprocessing jobs
        self.proc_threads = input('{}[?]{} Number of threads to run concurrently {}(default: {}){} >>> '.format(color.BLUE, color.END,color.YELLOW,self.DEFAULT_THREADS,color.END))
        if is_empty(self.proc_threads):
            self.proc_threads = self.DEFAULT_THREADS
        else:
            try:
                self.proc_threads = int(self.proc_threads)
            except ValueError:
                print('{}[!] No. of threads should be an integer{}'.format(color.RED, color.END))        

##########################################################################################################################

        # output filename
        self.outfile = input('{}[?]{} Output file name {}(default: {}){} >>> '.format(color.BLUE, color.END,color.YELLOW,self.DEFAULT_OUTPUT_FILE,color.END))
        if is_empty(self.outfile):
            self.outfile = self.DEFAULT_OUTPUT_FILE

        print('')

##########################################################################################################################
    
        # generate the wordlist
        self.base_wordlist = []
        # adding the relevant information to our wordlist
        if not is_empty(firstname):
            firstname = firstname.lower()
            self.base_wordlist.append(firstname)

        if not is_empty(midname):
            midname = midname.lower()
            self.base_wordlist.append(midname)

        if not is_empty(lastname):
            lastname = lastname.lower()
            self.base_wordlist.append(lastname)
        
        if not is_empty(name_initials):
            initials = name_initials.lower()
            self.base_wordlist.append(initials)
        
        if not is_empty(birth):
            birth = birth.split('/')
            for i in birth:
                self.base_wordlist.append(i)
            self.base_wordlist.append((birth[2])[-2:])  # Also add two last digits of the year
        
        if not is_empty(dates):
            for date in dates.split(','):
                dt = date.split('/')
                for d in dt:
                    self.base_wordlist.append(d)
                self.base_wordlist.append((dt[2])[-2:])
        
        if not is_empty(othernames):
            others = othernames.split(',')            
            for i in others:
                if len(i.split(' ')) > 1:
                    initials = take_initials(i).lower()
                    self.base_wordlist.append(initials)
                self.base_wordlist.append(i.lower())
        
        if self.artists:
            for artist in self.artists:
                if len(artist.split(' ')) > 1:
                    initials = take_initials(artist).lower()
                    self.base_wordlist.append(initials)
                for a in artist.split(' '):                    
                    self.base_wordlist.append(a)
    
##########################################################################################################################

    def getList(self):
        return self.base_wordlist
