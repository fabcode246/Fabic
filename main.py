import os
import pygame
import random
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

    def play(self, item=None, index=None):
        file = self.now[self.now.index(item) if item else index if index else self.index]
        self.song_now = file[file.rindex("/")+1:file.rindex(".")]
        audio = MP3(file)
        self.duration = audio.info.length
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(SONG_END)
        while True:
            loading = ""
            for i in range(int((self.get_pos()/self.duration) * 100)):
                loading += "-"
            for i in range(int(((self.duration - self.get_pos())/self.duration) * 100)):
                loading += " "
            def progress(val):   
                var1 = str(val / 60).split(".")
                try:
                    var2 = var1[0] + ":" + var1[1][:2]
                    return var2
                except:
                    return ""
            print("Now playing: " + self.song_now + " (" + progress(self.get_pos()) + "/" + progress(self.duration) + ") " + loading, end="\r")
            for event in pygame.event.get():
                if event.type == SONG_END:
                    self.next()
    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def next(self):
        pygame.mixer.music.stop()
        self.index += 1
        self.play()

    def prev(self):
        pygame.mixer.music.stop()
        self.index -= 1
        self.play()

    def stop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
    
    def get_pos(self):
        return pygame.mixer.music.get_pos() / 1000

class Player:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.queue = None

    def open_folder(self, path):
        files = []
        for i in os.listdir(path):
            files.append(path+i)
        self.queue = Queue(files)

    def get_queue(self):
        return self.queue

plyr = Player()