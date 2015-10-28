#!/usr/bin/python
#
#JulioGomez
#
#this program will be reading maroon 5 lyrics from a file
#

Lyrics = open("Lyrics.txt", "r")

read_lyrics = Lyrics.readlines()

for lyrics in read_lyrics:
    print lyrics