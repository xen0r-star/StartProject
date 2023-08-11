from tkinter import *

class CustomEntry(Frame):
    def __init__(self, parent, **kwargs):
        self.placeholder = kwargs.pop("placeholder", "Text")
        self.insertbackground = kwargs.pop("insertbackground", "white")
        self.insertbackgroundoff = kwargs.pop("insertbackgroundoff", "white")
        self.width = kwargs.pop("width", 20)
        super().__init__(parent, **kwargs)
        self.bg = kwargs.get("bg", "grey")


        self.entry_frame = Frame(self, bg=self.bg)
        self.entry_frame.pack(ipady=4)

        self.entry_ipadx_left = Frame(self.entry_frame, bg=self.bg, width=5)
        self.entry_ipadx_left.pack(side=LEFT, fill=Y)

        self.entry = widget_Entry(self.entry_frame, width=self.width, default_text=self.placeholder, insertbackground=self.insertbackground, insertbackgroundoff=self.insertbackgroundoff, bg=self.bg)
        self.entry.pack(side=LEFT, ipady=2)

        self.entry_ipadx_right = Frame(self.entry_frame, bg=self.bg, width=5)
        self.entry_ipadx_right.pack(side=LEFT, fill=Y)



class widget_Entry(Entry):
    def __init__(self, master=None, **kwargs):
        self.insertbackgroundoff = kwargs.pop("insertbackgroundoff", "grey")
        self.default_text = kwargs.pop("default_text", "Text")
        Entry.__init__(self, master, **kwargs)
        
        self.insertbackground = kwargs.get("insertbackground", "black")
        self.insertofftime = kwargs.get("insertofftime", 500)
        self.insertontime = kwargs.get("insertontime", 500)
        self.insertwidth = kwargs.get("insertwidth", 1.5)
        self.config(
            font=("Arial", 12),
            bd=0,
            selectbackground="#e06161",
            selectforeground="#ffffff",
            fg=self.insertbackgroundoff
        )
        self.insert(0, self.default_text)

        self.bind("<FocusIn>", self.on_entry_click)
        self.bind("<FocusOut>", self.on_entry_focusout)

    def on_entry_click(self, event):
        if self.get() == self.default_text:
            self.delete(0, END)
            self.config(fg=self.insertbackground)

    def on_entry_focusout(self, event):
        if self.get() == "":
            self.insert(0, self.default_text)
            self.config(fg=self.insertbackgroundoff)
