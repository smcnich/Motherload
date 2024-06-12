from eyed3.mp3 import Mp3AudioFile

class Song():

    def __init__(self, path:str) -> None:

        self.audio = Mp3AudioFile(path)
        self.tag = self.audio.tag
        self.info = self.audio.info

        self.path = path

        self.title = self.tag.title
        self.artist = self.tag.artist
        self.album = self.tag.album
        self.track_num = self.tag.track_num[0]
        self.genre = self.tag.genre.name
        self.year = self.tag.getBestDate().year

        self.duration = self.info.time_secs

        self.play_count = 0



song = Song("/home/shane/motherload/songs/04 - Hurricane.mp3")
        
print(song.year)