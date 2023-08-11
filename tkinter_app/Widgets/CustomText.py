from tkinter import *

class CustomText(Frame):
    def __init__(self, parent, **kwargs):
        self.fg = kwargs.pop("fg", "white")
        self.placeholder = kwargs.pop("placeholder", "Cliquez spour écrire...")
        self.placeholder_color = kwargs.pop("placeholder_color", "grey")
        self.width = kwargs.pop("width", 40)
        self.height = kwargs.pop("height", 7)
        super().__init__(parent, **kwargs)

        self.bg = kwargs.get("bg", "black")
        self.insertofftime = kwargs.get("insertofftime", 500)
        self.insertontime = kwargs.get("insertontime", 500)
        self.insertwidth = kwargs.get("insertwidth", 1.5)


        self.Text_frame = Frame(self, bg=self.bg)
        self.Text_frame.pack()

        self.text_ipadx_left = Frame(self.Text_frame, bg=self.bg, width=5)
        self.text_ipadx_left.pack(side=LEFT, fill=Y)

        self.text = Text(self.Text_frame, width=self.width, height=self.height, placeholder=self.placeholder, placeholder_color=self.placeholder_color, fg=self.fg, bg=self.bg, insertbackground=self.placeholder_color, insertofftime=self.insertofftime, insertontime=self.insertontime, insertwidth=self.insertwidth, font=("Arial", 11), bd=0, selectbackground="#e06161", selectforeground="#ffffff")
        self.text.pack(side=LEFT, ipady=5)

        self.text_ipadx_right = Frame(self.Text_frame, bg=self.bg, width=5)
        self.text_ipadx_right.pack(side=LEFT, fill=Y)

class Text(Text):
    def __init__(self, master=None, placeholder="", placeholder_color="grey", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.tag_configure("placeholder", foreground=placeholder_color)
        
        self.insert("1.0", self.placeholder, "placeholder")  # Use the "placeholder" tag
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.on_focus_out(None)  # Call on_focus_out initially

    def on_focus_in(self, event):
        if self.get("1.0", "end-1c") == self.placeholder:
            self.delete("1.0", "end-1c")
            self.tag_remove("placeholder", "1.0", "end")

    def on_focus_out(self, event):
        if not self.get("1.0", "end-1c"):
            self.insert("1.0", self.placeholder, "placeholder")  # Use the "placeholder" tag
            self.tag_add("placeholder", "1.0", "end")
    
        
