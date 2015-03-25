from time import *

def lasfil(filnamn):
    songtable = {}
    with open(filnamn) as fil:
        for rad in fil:
            data = rad.split("<SEP>")
            artist = data[2].strip()
            song = data[3].strip()
            songtable[artist] = song
    return songtable

def hitta(artist, songtable):
    start = time()
    print(songtable[artist])
    stop = time()
    tidhash = stop - start
    return tidhash

songtable = lasfil("/info/tildav13/unique_tracks.txt")
artist = "Elude"
tidhash = hitta(artist, songtable)
print(tidhash)
