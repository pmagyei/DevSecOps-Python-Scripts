def make_album(artist, album, songs_on_album=None):
    """Return artist, album made and songs on  the album"""

    if songs_on_album:
        info = {'artist':artist, 'album':album, 'songs_amount':songs_on_album }
        return info

    else:
        info  = {'artist':artist, 'album':album, }
        return info

while True:
    print("Enter details, press q to quit at nay stage")

    n_artist = input("Enter Artist")
    if n_artist == 'q':
        break
    n_album = input("Enter album: ")
    if n_album == 'q':
        break

    n_songs = input("Enter number of songs")
    # if n_songs == 0:
    #     continue
    # else:
    #     if n_songs == '':
    #         continue
    value = make_album(n_artist, n_album, songs_on_album=n_songs)
    print(value)