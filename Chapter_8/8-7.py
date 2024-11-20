def make_album(artist,album):
    music = {
        'artist': artist,
        'album': album,
    }
    return music

album = make_album('abc','123')
print(album)

album = make_album('abcd','1234')
print(album)

album = make_album('abcde','12345')
print(album)