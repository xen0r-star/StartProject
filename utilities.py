import random
import os, signal
from tkinter import *

def closing():
    print("Close programme")
    os.kill(os.getpid(), signal.SIGINT) # arreter le serveur

def pseudo(p1_pseudo, p2_pseudo):
    pseudo = random.choice(p1_pseudo) + random.choice(p2_pseudo)
    return pseudo

def files_list(folder_path):
    folder_path = "Picture/User/"
    files_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    full_paths = [os.path.join(folder_path, f) for f in files_list]
    full_paths.insert(0, "Picture/App/User.png")
    return full_paths

def content_folder(dossier):
    fichiers = os.listdir(dossier)
    for fichier in fichiers:
        if fichier.lower().endswith(('.png', '.jpg')):
            return True

    return False