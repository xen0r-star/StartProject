from tkinter import *

class CustomScrollbar(Canvas): #Scrollbar custom
    def __init__(self, parent, orient='vertical', hideable=False, **kwargs):
        self.command = kwargs.pop('command', None)
        self.slidercolor = kwargs.pop('slidercolor', 'grey')
        self.troughcolor = kwargs.pop('troughcolor', 'white')
        Canvas.__init__(self, parent, **kwargs)

        self.orient = orient
        self.hideable = hideable

        self.new_start_y = 0
        self.new_start_x = 0
        self.first_y = 0
        self.first_x = 0

        self.config(bg=self.troughcolor, bd=0, highlightthickness=0)

        self.create_rectangle(
            0, 0, 1, 1, 
            fill=self.slidercolor, 
            width=0, # c'est la largeur de la bordure
            outline='teal', 
            tags=('slider',)
            )
        
        self.bind('<ButtonPress-1>', self.move_on_click)
        self.bind('<ButtonPress-1>', self.start_scroll, add='+')
        self.bind('<B1-Motion>', self.move_on_scroll)
        self.bind('<ButtonRelease-1>', self.end_scroll)

    def set(self, lo, hi):
        lo = float(lo)
        hi = float(hi)

        if self.hideable is True:
            if lo <= 0.0 and hi >= 1.0:
                self.grid_remove()
                return
            else:
                self.grid()

        height = self.winfo_height()
        width = self.winfo_width()

        if self.orient == 'vertical':
            x0 = 2
            y0 = max(int(height * lo), 0)
            x1 = width - 2
            y1 = min(int(height * hi), height)
        elif self.orient == 'horizontal':
            x0 = max(int(width * lo), 0)
            y0 = 2
            x1 = min(int(width * hi), width)
            y1 = height

        self.coords('slider', x0, y0, x1, y1)
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def move_on_click(self, event):
        if self.orient == 'vertical':
            y = event.y / self.winfo_height()
            if event.y < self.y0 or event.y > self.y1:
                self.command('moveto', y)
            else:
                self.first_y = event.y
        elif self.orient == 'horizontal':
            x = event.x / self.winfo_width()
            if event.x < self.x0 or event.x > self.x1:
                self.command('moveto', x)
            else:
                self.first_x = event.x

    def start_scroll(self, event):
        if self.orient == 'vertical':
            self.last_y = event.y 
            self.y_move_on_click = int(event.y - self.coords('slider')[1])
        elif self.orient == 'horizontal':
            self.last_x = event.x 
            self.x_move_on_click = int(event.x - self.coords('slider')[0])

    def end_scroll(self, event):
        if self.orient == 'vertical':
            self.new_start_y = event.y
        elif self.orient == 'horizontal':
            self.new_start_x = event.x

    def move_on_scroll(self, event):
        jerkiness = 3

        if self.orient == 'vertical':
            if abs(event.y - self.last_y) < jerkiness:
                return
            delta = 1 if event.y > self.last_y else -1
            self.last_y = event.y
            self.command('scroll', delta, 'units')
            mouse_pos = event.y - self.first_y
            if self.new_start_y != 0:
                mouse_pos = event.y - self.y_move_on_click
            self.command('moveto', mouse_pos/self.winfo_height()) 
        elif self.orient == 'horizontal':
            if abs(event.x - self.last_x) < jerkiness:
                return
            delta = 1 if event.x > self.last_x else -1
            self.last_x = event.x
            self.command('scroll', delta, 'units')
            mouse_pos = event.x - self.first_x
            if self.new_start_x != 0:
                mouse_pos = event.x - self.x_move_on_click
            self.command('moveto', mouse_pos/self.winfo_width())
            