import sys
from main import Player, Queue

def help():
    pass

if len(sys.argv) < 2:
    help()
else:
    plyr = Player()
    plyr.open_folder(sys.argv[1])
    queue = plyr.get_queue()
    if "-s" in sys.argv:
        queue.shuffled()
    queue.play()
    plyr.loop()