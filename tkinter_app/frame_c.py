from tkinter import *
from PIL import Image, ImageTk
from tkinter_app.other_module import delete_frame_content, general_part
from data_app.data_json import load_info

def Frame_c(content_frame):
    delete_frame_content(content_frame)
    
    info = load_info()
    color_content = info["color_content"]

    frame = Frame(content_frame, bg=color_content)
    frame.pack(side=LEFT, anchor=N, padx=35, pady=20, fill=BOTH, expand=True)

    general_part(frame, "C")

    