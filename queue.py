import pygame
from mutagen.mp3 import MP3

SONG_END = pygame.USEREVENT + 1

class Queue:
    def __init__(self, file_list):
        self.original = file_list
        self.ordered = self.original
        self.now = self.ordered
        self.index = 0
        self.song_now = ""
        self.duration = 0
        self.paused = True

    def shuffled(self):
        old_list = self.ordered
        new_list = []
        for i in self.ordered:
            choice = random.choice(old_list)
            new_list.append(choice)
            old_list.remove(choice)
        self.now = new_list

    def ordered(self):
        self.now = self.ordered

    def recover(self):
        self.ordered = self.original
        self.now = self.ordered

    def clear(self):
        pygame.mixer.music.stop()
        self.ordered = []
        self.now = []

    def add(self, item):
        self.now.append(item)

    def remove(self, item=None, index=None):
        if item:
            self.now.remove(item)
        if index:
            self.now.pop(index)

    def play(self, item=None, index=None, start=0):
        self.paused = False
        if item:
            self.index = self.now.index(item)
        if index:
            self.index = index
        file = self.now[self.index]
        self.song_now = file[file.rindex("/")+1:file.rindex(".")]
        audio = MP3(file)
        self.duration = audio.info.length
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(start=start)
        pygame.mixer.music.set_endevent(SONG_END)


    def vol(self, val):
        vol = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume((vol*100+val)/100)

    def pause(self):
        self.paused = True
        pygame.mixer.music.pause()

    def resume(self):
        self.paused = False
        pygame.mixer.music.unpause()

    def next(self):
        self.index = 0 if self.index == len(self.now)-1 else self.index+1
        self.play()

    def prev(self):
        self.index = len(self.now)-1 if self.index == 0 else self.index-1
        self.play()

    def stop(self):
        self.paused = True
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
    
    def get_pos(self):
        return pygame.mixer.music.get_pos() / 1000