from .modules import Memory
from .modules.senses.keyinputs import Getcmd

from threading import Thread

__author__ = 'piper'

Memory.initialize()

cmd = Thread(target=Getcmd)
cmd.start()
cmd.join()
