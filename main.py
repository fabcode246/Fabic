import os
import pygame
import random
from mutagen.mp3 import MP3
import time
import sys

def help():
    pass

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

class Player:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((300,300))
        self.queue = None
        font1 = pygame.font.SysFont("Sans Serif", 20)
        textsurface = font1.render('Some Text', False, (255, 255, 255))
        self.screen.blit(textsurface,(0,0))

    def open_folder(self, path):
        files = []
        for i in os.listdir(path):
            files.append(path+i)
        self.queue = Queue(files)

    def get_queue(self):
        return self.queue

    def loop(self):
        while True:
            self.event_handler()
            loading = ""
            for i in range(int((self.queue.get_pos()/self.queue.duration) * 50)):
                loading += "-"
            for i in range(int(((self.queue.duration - self.queue.get_pos())/self.queue.duration) * 50)):
                loading += " "
            def progress(val):   
                mins = int(val / 60)
                secs = int(val - mins * 60)
                return f"{mins}:{secs}"
            print(f"Now playing[{self.queue.index+1}]: " + self.queue.song_now + f" ({progress(self.queue.get_pos())}/{progress(self.queue.duration)}) " + loading, end="\r")
            time.sleep(0.05)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == SONG_END:
                self.queue.next()
            if event.type == pygame.QUIT:
                self.queue.stop()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.queue.stop()
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    if self.queue.paused:
                        self.queue.resume()
                    else:
                        self.queue.pause()
                if event.key == pygame.K_RIGHT:
                    self.queue.next()
                if  event.key == pygame.K_LEFT:
                    self.queue.prev()
                if event.key == pygame.K_UP:
                    self.queue.vol(5)
                if event.key == pygame.K_DOWN:
                    self.queue.vol(-5)
                if event.key == pygame.K_l:
                    text = ""
                    index = 0
                    max_len = max(self.queue.now, key=len)
                    for i in self.queue.now:
                        index += 1
                        text += f"{index} - {i}\n"
                    print(text)
                    inp = input("select song by number: ")
                    self.queue.play(index=int(inp)-1)

plyr = Player()

if len(sys.argv) < 2:
    help()
else:
    plyr.open_folder(sys.argv[1])
    queue = plyr.get_queue()
    if "-s" in sys.argv:
        queue.shuffled()
    queue.play()
    plyr.loop()