from tkinter import *
from PIL import Image, ImageTk

class CustomCheckbutton(Checkbutton):
    def __init__(self, parent, icon_type, color_content, callback, **kwargs):
        super().__init__(parent, **kwargs)

        self.icon_type = icon_type
        self.color_content = color_content
        self.callback = callback
        self.button_check_statut = False

        self.photo_check = ImageTk.PhotoImage(image=Image.open("Picture/App/" + self.icon_type + "/Checked-0.png").resize((25, 25), Image.LANCZOS))
        self.config(image=self.photo_check, bg=self.color_content, cursor="hand2", bd=0, highlightthickness=0, activebackground=self.color_content, command=self.button_check, indicatoron=False, selectcolor=color_content)
        self.image = self.photo_check
        self.pack(side=LEFT, ipadx=2, ipady=2)

    def button_check(self):
        new_picture_path = "Picture/App/" + self.icon_type + ("/Checked-1.png" if not self.button_check_statut else "/Checked-0.png")
        new_picture = ImageTk.PhotoImage(image=Image.open(new_picture_path).resize((25, 25), Image.LANCZOS))
        self.button_check_statut = not self.button_check_statut
        self.callback(self.button_check_statut)

        self.config(image=new_picture, cursor="hand2", activebackground=self.color_content, selectimage=new_picture, command=self.button_check)
        self.image = new_picture