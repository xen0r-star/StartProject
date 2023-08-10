from tkinter import *

class CustomEntry(Entry):
    def __init__(self, master=None, default_text="", **kwargs):
        self.insertbackgroundoff = kwargs.pop("insertbackgroundoff", "grey")
        Entry.__init__(self, master, **kwargs)
        
        self.default_text = default_text
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
        self.insert(0, default_text)

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
