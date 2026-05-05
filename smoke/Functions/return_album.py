def make_album(artist_name, album_tile, songs_on_album=None):
    """Returns information about artists and an album they made"""
    great_artist = {'artist':artist_name, 'album': album_tile, 'songs_on_album': songs_on_album}


    return great_artist



artist_album = make_album('Dante', 'Renaissance', songs_on_album=14)
print(artist_album)
artist_album = make_album('MJ', 'Thriller')
print(artist_album)
artist_album = make_album('Tory Lanez', 'Peterson')
print(artist_album)
