from modules import Memory
from threading import Thread

from modules.senses.keyinputs import Getcmd

__author__ = 'piper'

Memory.initialize()

cmd = Thread(target=Getcmd)
cmd.start()
cmd.join()
