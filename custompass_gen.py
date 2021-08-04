#!/usr/bin/python3

import sys, os, datetime
from time import sleep
from modules.ui import userinterface
from modules.transforms import *
from modules.statics import color,charsets
from modules.separators import *
from modules.utilities import remove_by_lengths
from modules.song_lyrics_extractor import song_search_by_artist,lyrics_extractor
from modules.lyrics2pass import make_phrases

def run():

    try:
        # Get initial timestamp
        start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        # initialise UI object and call UI function
        UI = userinterface()
        UI.ui()
        # retrive base wordlist based on user provided details
        base_wordlist = UI.getList()

##########################################################################################################################

        # copying words from base list to the final wordlist
        print('{}[+]{} Appending words based on provided data {}(base wordlist length: {}){}'.format(color.GREEN, color.END,color.CYAN,len(base_wordlist),color.END))
        final_wordlist = base_wordlist[:]  # Copy to preserve the original

        # case transforms enabled
        if UI.case:
            # send the base wordlist for case transformations
            print('{}[+]{} Applying case transformations to {}{} words{} of the base wordlist'.format(color.GREEN, color.END,color.CYAN,len(base_wordlist),color.END))
            temp_wordlist = []
            temp_wordlist += multithread_transforms(case_transform, base_wordlist, UI.proc_threads)
            final_wordlist += temp_wordlist
        
        # words to combine is greater than 1
        if UI.n_words > 1:
            # combines words from base list
            print('{}[+]{} Creating all posible combinations between {}{} words{}'.format(color.GREEN, color.END,color.CYAN, UI.n_words,color.END))
            i = 1       # combine 1 to n number of words together
            while ((i < UI.n_words) and (len(final_wordlist) > i)):
                i += 1
                final_wordlist += combinator(final_wordlist,i)
                print('{}[*]{} Combining upto {} words using {} words {}(words produced: {}){}'.format(color.CYAN,color.END,i,len(base_wordlist),color.CYAN,len(final_wordlist),color.END))

        # create extra combinations using special separators instead of space
        if UI.sep:
            # separates combined words from base list using separators
            print('{}[+]{} Creating extra combinations using space transformations'.format(color.GREEN,color.END))            
            final_wordlist += separator(base_wordlist)
            #print(separator(wl))
        
        # Remove words by min-max length range established
        final_wordlist = remove_by_lengths(final_wordlist, UI.min_length, UI.max_length)
        # remove any possible duplicates at this point
        final_wordlist = list(set((final_wordlist)))        
        
        
##########################################################################################################################
# MULTITHREADED TRANSFORMS 
##########################################################################################################################

        # leet transforms enabled
        if UI.leet:
            # send the final wordlist for leet transformations
            print('{}[+]{} Applying leet transformations to {}{} words{}'.format(color.GREEN, color.END, color.CYAN, len(final_wordlist),color.END))
            print('{}[!] This operation may take several minutes!{}'.format(color.ORANGE, color.END))
            temp_wordlist = []            
            temp_wordlist += multithread_transforms(leet_transform, final_wordlist, UI.proc_threads)
            final_wordlist += temp_wordlist

        # case transforms enabled
        if UI.case:
            # send the final wordlist for case transformations
            print('{}[+]{} Applying case transformations to {}{} words{}'.format(color.GREEN, color.END,color.CYAN,len(final_wordlist),color.END))
            print('{}[!] This operation may take several minutes!{}'.format(color.ORANGE, color.END))
            temp_wordlist = []
            temp_wordlist += multithread_transforms(case_transform, final_wordlist, UI.proc_threads)
            final_wordlist += temp_wordlist

##########################################################################################################################

        if UI.presuf:
            # include common prefixes/ suffixes
            print('{}[+]{} Adding common prefixes and suffixes to {}{} generated words{}'.format(color.GREEN,color.END,color.CYAN,len(final_wordlist),color.END))        
            print('{}[!] This operation may take several minutes!{}'.format(color.ORANGE, color.END))
            temp_wordlist = append_prepend(final_wordlist)
            final_wordlist += temp_wordlist

##########################################################################################################################

        # search for song names based on favourite artists
        # extract their lyrics and use them as passphrases
        if UI.artists:
            for artist in UI.artists:
                phrases=[]            
                songs = song_search_by_artist(artist)                
                if len(songs)>5:
                    print('{}[!] This operation may take several minutes!{}'.format(color.ORANGE, color.END))
                if songs:
                    temp_wordlist = []
                    print('{}[+]{} Applying case transforms to {}{}{} song names found for artist: {}{}{}'.format(color.GREEN,color.END,color.YELLOW,len(songs),color.END,color.YELLOW,artist,color.END))
                    temp_wordlist += multithread_transforms(case_transform, songs, UI.proc_threads)
                    final_wordlist += temp_wordlist

                    for song in songs:
                        size = len(phrases)
                        if song:
                            lyrics = lyrics_extractor(artist, song)
                        if lyrics:                        
                            for line in lyrics.split('\n'):        
                                phrases.extend(make_phrases(line, UI.min_length, UI.max_length))
                            print('{}[+]{} Song: {}{}{} => {}{} new words/ phrases{} added'.format(color.GREEN,color.END,color.YELLOW,song,color.END,color.CYAN,len(phrases)-size,color.END))                    
                        sleep(2)
                    final_wordlist += list(set(phrases))


##########################################################################################################################

        # re-check for duplicates
        final_wordlist = list(set((final_wordlist)))

#        for word in final_wordlist:
#            if word[0] in charsets.sep_charset or word[-1] in charsets.sep_charset:
#                final_wordlist.remove(word)

        # SAVE WORDLIST TO FILE        
        with open(UI.outfile, 'w') as of:
            for word in final_wordlist:
                of.write(word + '\n')

##########################################################################################################################

        # Get final timestamps and calculate time elapsed
        end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        total_time = (datetime.datetime.strptime(end_time, '%H:%M:%S') - datetime.datetime.strptime(start_time, '%H:%M:%S'))

##########################################################################################################################

        # overview of final results
        ############################################################################
        print('\n{}[+]{} Time elapsed\t:\t{}{}'.format(color.GREEN, color.BOLD, total_time, color.END))
        print('{}[+]{} Output file\t\t:\t{}{}{}{}'.format(color.GREEN, color.END, color.BOLD, color.BLUE, UI.outfile, color.END))
        print('{}[+]{} Words generated\t:\t{}{} words{}\n'.format(color.GREEN, color.END, color.RED, len(final_wordlist), color.END))
        sys.exit(0)

        print('min_length',UI.min_length)
        print('max_length',UI.max_length)
        print('1337',UI.leet)
        print('case',UI.case)
        print('case',UI.sep)
        print('combine',UI.n_words)
        print('outfile',UI.outfile)

        #print(baselist)

    except KeyboardInterrupt:
        print('\n\n{}[!] Exiting...{}\n'.format(color.RED, color.END))
        sys.exit(3)

    #except Exception as e:
    #    print(e)

run()