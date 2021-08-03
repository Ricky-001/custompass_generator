#!/usr/bin/python3

import requests as rq
from bs4 import BeautifulSoup as bs
import os, re
from modules.lyrics2pass import make_phrases

# reference : https://github.com/aakashbansal/Songs-Lyrics-Web-Scraper/

# website to query to find all songs based on artist name
# http://www.song-list.net/
base_artist = "http://www.song-list.net/{}/songs"
# website to query to extract lyrics of songs based on artist name and song name
# https://www.azlyrics.com/
base_song = "https://www.azlyrics.com/lyrics/{}/{}.html"
# HTTP header to specify User agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

# function to extract lyrics of a song
def lyrics_extractor(artist,song):
    artist = clean(artist)
    song = clean(song)
    song_url = base_song.format(artist,song)
    
    try:
        resp = rq.get(song_url, headers=headers)
        soup = bs(resp.text,'html.parser')
        
        # the div element containing the lyrics doesn't have any class or id
        # so we find the nearest div with a class 'ringtone' and find the next div element
        lyrics = soup.find('div', attrs={'class':'ringtone'}).find_next('div').text.strip()        
        return lyrics

    except Exception as e:
        #print(e)
        return None

# function to retrieve all songs of an artist
def song_search_by_artist(artist):
    songs=[]
    artist = clean(artist)
    artist_url = base_artist.format(artist)
    # pattern to search for in the <a href="LINK" /> containing the names of the songs
    song_url_pattern = re.compile('/{}/'.format(artist) + '.*/tracks')    

    try:
        resp = rq.get(artist_url, headers=headers)
        soup = bs(resp.text,'html.parser')
        links = soup.find_all('a')                  # all links

        for a in links:
            if song_url_pattern.search(a['href']):  # search for the particular pattern in link
                if a.text.strip():                  # strip off extra spaces and check if the string is valid (not empty)
                    songs.append(a.text.strip())  # append the contants of the string (song name) to songs list
        return songs

    except Exception as e:
        print(e)

# clean the song names to remove any special characters or spaces 
# (required in that format to add it to the URL)
# removes spaces(if any) in artist names and converts everything into lowercase
def clean(name):    
    name = ''.join(c for c in name if c.isalnum()).lower()
    return name


def run():
    lyricpasses=[]

    artist = input('[?] Enter Artist Name: ')
    song = input('[?] Enter Song Name: ')
    ch = int(input('(1) Extract Songs by Artist Name\t(2) Extract Lyrics by Song Name\n[?] Choice >>> '))

    if ch==1:
        songs = song_search_by_artist(artist)
        for song in songs:
            print(song)
    elif ch==2:
        lyrics = lyrics_extractor(artist,song)
        print('Song name : ',song)
        print(lyrics)

