import lyricsgenius
api_key = "srCsePtJkXYbCjydk8b6kxOPF2vyQGYcO176Aj6Ajz3GIudFt7g98lS7MyLsJQPX"
genius = lyricsgenius.Genius(api_key)
name = input("Enter Artist Name : ")
artist = genius.search_artist (name)
song = input("Type your song for Lyrics : ")
song = artist.song(song)
print(song.lyrics)