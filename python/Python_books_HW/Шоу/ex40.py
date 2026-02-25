class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    def make_lyrics_upper(self):
        self.lyrics = [line.upper() for line in self.lyrics]
text1 = ['This birthday i cannot',
        'Give you costly gifts', 
        'But at least this spring nights']
happy_bday = Song(text1)
happy_bday.make_lyrics_upper()
happy_bday.sing_me_a_song()
