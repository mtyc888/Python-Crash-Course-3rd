def make_album(artist,album, num_songs=0):
    music = {
        'artist': artist,
        'album': album,
    }
    if num_songs:
        music['num_songs']=num_songs
    return music

title_prompt = "\n What album are you thinking of?"
artist_prompt = "Who's the artist?"
print("Entr 'quit' to exit")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    album = make_album(artist, title)
    print(album)
