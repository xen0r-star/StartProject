import random
from tkinter import *

def closing(icon, win):
    icon.stop()
    win.destroy()

def pseudo(p1_pseudo, p2_pseudo):
    pseudo = random.choice(p1_pseudo) + random.choice(p2_pseudo)
    return pseudo