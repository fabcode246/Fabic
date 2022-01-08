import os
import pygame
import random
import time
from queue import Queue

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
            files.append(path+"/"+i)
        self.queue = Queue(files)

    def get_queue(self):
        return self.queue

    def get_loading_str(self):
        loading = ""
        for i in range(int((self.queue.get_pos()/self.queue.duration) * 50)):
            loading += "-"
        for i in range(int(((self.queue.duration - self.queue.get_pos())/self.queue.duration) * 50)):
            loading += " "
        return loading

    def get_progress_str(self):
        def progress(val):   
            mins = int(val / 60)
            secs = int(val - mins * 60)
            return f"{mins}:{secs}"
        return f"({progress(self.queue.get_pos())}/{progress(self.queue.duration)})"

    def get_nowplaying_str(self):
        return f"Now playing[{self.queue.index+1}/{len(self.queue.now)}]"

    def get_name_str(self):
        return self.queue.song_now

    def event_handler(self):
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