from tkinter import *
from PIL import Image, ImageTk
from tkinter_app.other_module import delete_frame_content
from data_app.data_json import load_info

def Frame_nodejs(content_frame):
    delete_frame_content(content_frame)

    info = load_info()
    color_menu = info["color_menu"]
    color_content = info["color_content"]

    frame = Frame(content_frame, bg=color_content)
    frame.pack(side=LEFT, anchor=N, padx=35, pady=30)

    text_label = Label(frame, text="Frame nodejs", font=("Arial", 12), bg=color_menu, fg="#bebebe")
    text_label.pack(side=LEFT, padx=5)