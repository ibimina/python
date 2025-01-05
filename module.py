from math import pi # import pi from math
import sys # imports the whole module
import random as rdm # import module as an alias name
from enum import Enum
import kansas
from rps7 import rock_paper_scissors
print(pi)
print(dir(rdm))


for item in dir(rdm):
    print(item)


nessong = kansas.song
print(nessong)

kansas.randomfunfacts()

print(__name__)

print(kansas.__name__)

rock_paper_scissors()