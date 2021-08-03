# custompass_generator
A Python utility to generate a custom wordlist based on the details provided about the target (interactively), along with some common password creating practices like p@$$w0rd or password123 and so on.

The script takes into account all the basic target details that one may include in their password like:-
* Name (first name, middle name, last name)
* Important dates like DoB or anniversary
* Other important words related to that person (ex: 2C,Flipper)
* Artists/ significant figures for the target
* Initials of the names (target's, artists', others, etc)

It then generates various combinations of these details along with the following transformations often found in passwords:
* CaSe tRaNsFoRmAtIoN
* 1337 7r4n$f0rm@7!0n
* Space_separators-between~words

The script also adds common prefixes and suffixes one may use in their passwords such as:
* password123
* 12345admin

Finally, the script scrapes the internet for songs and their lyrics to be added as passphrases
(based on the names provided in the Artists/ Role Models section)
- Fetches list of Songs based on Artist name from https://www.song-list.net/
- Extracts the Lyrics of fetched Songs from https://www.azlyrics.com/

