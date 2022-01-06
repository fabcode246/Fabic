import os
import pygame
import random
from mutagen.mp3 import MP3
import time
import sys

def help():
    pass

SONG_END = pygame.USEREVENT + 1


class Player:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        '''
        pygame.font.init()
        self.screen = pygame.display.set_mode((300,300))
        self.queue = None
        font1 = pygame.font.SysFont("Sans Serif", 20)
        textsurface = font1.render('Some Text', False, (255, 255, 255))
        self.screen.blit(textsurface,(0,0))
'''

    def open_folder(self, path):
        files = []
        for i in os.listdir(path):
            files.append(path+i)
        self.queue = Queue(files)

    def get_queue(self):
        return self.queue

    def loop(self):
        while True:
            #self.event_handler()
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
            for event in pygame.event.get():
                if event.type == SONG_END:
                    self.queue.next()
'''
    def event_handler(self):
        
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
'''