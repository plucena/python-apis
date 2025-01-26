import simplejson
from sqlite3 import dbapi2 as sqlite3
import os
from sqlobject import *

# Replace this with the URI for your actual database

class Song(SQLObject):
    name = StringCol()
    artist = StringCol()
    album = StringCol()

# Create fake data for demo - this is not needed for the real thing
def __init__(self, con):
    connection  = con
    sqlhub.processConnection = connection


def SelectAll():
    # This is an iterable, not a list
    all_songs = Song.select().orderBy(Song.q.name)

    songs_as_dict = []

    for song in all_songs:
        song_as_dict = {
            'name' : song.name,
            'artist' : song.artist,
            'album' : song.album}
        songs_as_dict.append(song_as_dict)

    return simplejson.dumps(songs_as_dict)
