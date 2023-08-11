from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class CustomPath(Frame):
    def __init__(self, parent, icon_type, color_zone, color_soustext, **kwargs):
        super().__init__(parent, **kwargs)

        self.icon_type = icon_type
        self.color_zone = color_zone
        self.color_soustext = color_soustext

        self.select_directory_frame = Frame(self, bg=self.color_zone)
        self.select_directory_frame.pack(side=TOP, fill=X, ipadx=1, ipady=3)

        self.path_label = Label(self.select_directory_frame, text="Chemin vers le dossier", font=("Arial", 10), fg=self.color_soustext, bg=self.color_zone, anchor='w')
        self.path_label.pack(side=LEFT, padx=(3, 0), fill=X)

        self.photo_directory = ImageTk.PhotoImage(image=Image.open("Picture/App/" + self.icon_type + "/Folder.png").resize((23, 18), Image.LANCZOS))
        self.directory_button = Button(self.select_directory_frame, image=self.photo_directory, command=self.directory, bg=self.color_zone, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=self.color_zone)
        self.directory_button.image = self.photo_directory
        self.directory_button.pack(side=RIGHT, padx=5, ipadx=2, ipady=2)

    def directory(self):
        filepath = filedialog.askdirectory()
        if len(filepath) >= 60:
            shortened_filepath = "... " + filepath[-55:]
        elif filepath == "":
            shortened_filepath = "Chemin vers le dossier"
        else:
            shortened_filepath = filepath
        self.path_label["text"] = shortened_filepath
