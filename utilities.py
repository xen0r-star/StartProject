import random
import ctypes
import os
from tkinter import *

def closing(icon, win):
    icon.stop()
    # nid = (icon._data.hWnd, 0)
    # ctypes.windll.shell32.Shell_NotifyIconW(2, ctypes.byref(nid)) # Supprimer l'icône de la barre des tâches en utilisant ctypes
    win.destroy()

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
