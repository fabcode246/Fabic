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
    def sigint_handler(signal, frame):
        queue.stop()
        sys.exit(0)
    signal.signal(signal.SIGINT, sigint_handler)