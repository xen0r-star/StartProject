from tkinter import *
from PIL import Image, ImageTk

from math import atan2, cos, sin, sqrt
from tkinter.colorchooser import askcolor

class CustomPicker(Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        color_systeme = "dark"

        if color_systeme == "dark":
            color_fond = "#16161C"
            color_text = "#ffffff"
            color_stext = "#82828B"
            color_line = "#ffffff"
        else:
            color_fond = "#EAEAF1"
            color_text = "#000000"
            color_stext = "#3C3C41"
            color_line = "#000000"

        # Titre
        self.titre_label = Label(self, text="Sélecteur de couleurs", font=("Arial", 22), bg=color_fond, fg=color_text)
        self.titre_label.pack(fill=X, anchor=CENTER, pady=(25,0))


        # Couleur selector
        self.selector_frame = Frame(self, bg=color_fond)
        self.selector_frame.pack(fill=X, anchor=CENTER, padx=60, pady=(25,0))

        self.circle_frame = Frame(self.selector_frame, bg=color_fond)
        self.circle_frame.pack(side=LEFT, anchor=W)

        self.circle_picture = ImageTk.PhotoImage(
            image=Image.open("Picture/App/color_picker.png").resize((180, 180), Image.LANCZOS)
        )
        self.circle_label = Label(self.circle_frame, bg=color_fond, image=self.circle_picture, bd=0)
        self.circle_label.image = self.circle_picture
        self.circle_label.pack()

        self.line_frame = Frame(self.selector_frame, bg=color_fond)
        self.line_frame.pack(side=RIGHT, anchor=E)

        self.line_picture = ImageTk.PhotoImage(
            image=Image.open("Picture/App/color_line.png").resize((20, 180), Image.LANCZOS)
        )
        self.line_label = Label(self.line_frame, bg="red", image=self.line_picture, bd=0)
        self.line_label.image = self.line_picture
        self.line_label.pack()


        # Couleur code
        self.code_frame = Frame(self, bg=color_fond)
        self.code_frame.pack(fill=X, anchor=CENTER, padx=60, pady=(25,15))

        self.titre_label = Label(self.code_frame, text="244", font=("Arial", 15), bg=color_fond, fg=color_stext)
        self.titre_label.pack(side=LEFT, expand=True, fill=X)
        
        self.titre_label = Label(self.code_frame, text="244", font=("Arial", 15), bg=color_fond, fg=color_stext)
        self.titre_label.pack(side=LEFT, expand=True, fill=X)
        
        self.titre_label = Label(self.code_frame, text="244", font=("Arial", 15), bg=color_fond, fg=color_stext)
        self.titre_label.pack(side=LEFT, expand=True, fill=X)


        # Line
        self.menu_line_frame = Frame(self, bg=color_line, height=2)
        self.menu_line_frame.pack(side=TOP, fill=X, padx=30)


        # couleur personnalisée
        # self.customcolor_frame = Frame(self, bg=color_fond)
        # self.customcolor_frame.pack(fill=X, anchor=CENTER, padx=20, pady=(25,15))

        # self.customcolor1_frame = Frame(self.customcolor_frame, bg=color_fond)
        # self.customcolor1_frame.pack(side=LEFT, fill=X, padx=5)

        # self.label_customcolor1 = Label(self.customcolor1_frame, width=5, height=3, bg="red")
        # self.label_customcolor1.pack(side=LEFT, padx=3)
        # self.label_customcolor2 = Label(self.customcolor1_frame, width=5, height=3, bg="green")
        # self.label_customcolor2.pack(side=LEFT, padx=3)
        # self.label_customcolor3 = Label(self.customcolor1_frame, width=5, height=3, bg="blue")
        # self.label_customcolor3.pack(side=LEFT, padx=3)


        # self.customcolor2_frame = Frame(self.customcolor_frame, bg=color_fond)
        # self.customcolor2_frame.pack(side=RIGHT, fill=X, padx=5)

        # self.label_customcolor1 = Label(self.customcolor2_frame, width=5, height=3, bg="red")
        # self.label_customcolor1.pack(side=LEFT, padx=3)
        # self.label_customcolor2 = Label(self.customcolor2_frame, width=5, height=3, bg="green")
        # self.label_customcolor2.pack(side=LEFT, padx=3)
        # self.label_customcolor3 = Label(self.customcolor2_frame, width=5, height=3, bg="blue")
        # self.label_customcolor3.pack(side=LEFT, padx=3)


        # self.customcolor3_frame = Frame(self, bg="blue")
        # self.customcolor3_frame.pack(side=TOP, fill=X, anchor=N)

        # self.label_customcolor1 = Label(self.customcolor3_frame, width=5, height=3, bg="red")
        # self.label_customcolor1.pack(side=LEFT, padx=3)
        # self.label_customcolor2 = Label(self.customcolor3_frame, width=5, height=3, bg="green")
        # self.label_customcolor2.pack(side=LEFT, padx=3)



# class ColorPicker(Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.title("Custom Color Picker")
#         self.geometry("300x300")

#         self.canvas = Canvas(self, width=300, height=300)
#         self.canvas.pack(ipadx=50, ipady=50)

#         self.color_picker = PhotoImage(file="color_picker.png")
#         self.canvas.create_image(150, 150, image=self.color_picker)

#         self.circle_radius = 10
#         self.circle = self.canvas.create_oval(150 - self.circle_radius, 150 - self.circle_radius,
#                                              150 + self.circle_radius, 150 + self.circle_radius,
#                                              outline="black", width=2, fill="white")

#         self.canvas.bind("<Button-1>", self.start_drag)
#         self.canvas.bind("<B1-Motion>", self.drag)
#         self.canvas.bind("<ButtonRelease-1>", self.stop_drag)

#         self.selected_color = None
#         self.dragging = False

#     def start_drag(self, event):
#         x, y = event.x, event.y
#         dist = sqrt((x - 150) ** 2 + (y - 150) ** 2)
#         if dist <= 150 - self.circle_radius:
#             self.dragging = True
#             self.drag_start = (event.x, event.y)

#     def drag(self, event):
#         if self.dragging:
#             dx = event.x - self.drag_start[0]
#             dy = event.y - self.drag_start[1]
#             self.canvas.move(self.circle, dx, dy)
#             self.drag_start = (event.x, event.y)
#             self.constrain_circle_position()

#     def stop_drag(self, event):
#         if self.dragging:
#             self.dragging = False
#             self.constrain_circle_position()
#             x_center = self.canvas.coords(self.circle)[0] + self.circle_radius
#             y_center = self.canvas.coords(self.circle)[1] + self.circle_radius
#             color_rgb = self.color_picker.get(int(x_center), int(y_center))
#             self.selected_color = f"#{color_rgb[0]:02X}{color_rgb[1]:02X}{color_rgb[2]:02X}"
#             self.destroy()

#     def constrain_circle_position(self):
#         x_center = self.canvas.coords(self.circle)[0] + self.circle_radius
#         y_center = self.canvas.coords(self.circle)[1] + self.circle_radius
#         dist = sqrt((x_center - 150) ** 2 + (y_center - 150) ** 2)
#         if dist > 150 - self.circle_radius:
#             angle = atan2(y_center - 150, x_center - 150)
#             new_x = 150 + (150 - self.circle_radius) * cos(angle) - self.circle_radius
#             new_y = 150 + (150 - self.circle_radius) * sin(angle) - self.circle_radius
#             self.canvas.coords(self.circle, new_x, new_y, new_x + 2 * self.circle_radius, new_y + 2 * self.circle_radius)


