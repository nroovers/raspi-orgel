import json


def openSong(path):
    with open(path) as json_file:
        song = json.load(json_file)
        return song


def getTempo(song):
    return song['tempo']


def getNotes(song):
    return song['notes']
