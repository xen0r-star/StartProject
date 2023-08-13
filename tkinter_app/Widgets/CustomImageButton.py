from tkinter import *
from PIL import Image, ImageTk

class CustomImageButton(Frame):
    def __init__(self, parent, color_content, image, imageOn, repeat, size, callback, first_img=1, **kwargs):
        super().__init__(parent, bg=color_content, **kwargs)
        self.image_button = []
        self.callback = callback
        self.create_buttons(color_content, image, imageOn, repeat, size, first_img)

    def create_buttons(self, color_content, image, imageOn, repeat, size, first_img):
        def button_image_clicked(number, button, image):
            Picture1 = Image.open("Picture/App/" + str(image) + str(number) + ".png").resize(size, Image.LANCZOS)
            Picture2 = Image.open("Picture/App/" + str(imageOn)).resize(size, Image.LANCZOS)
            Picture1.paste(Picture2, (0, 0), Picture2)
            new_image = ImageTk.PhotoImage(Picture1)
            button.config(image=new_image)
            button.image = new_image

            for other_button in self.image_button:
                if other_button != button:
                    original_image = ImageTk.PhotoImage(
                            image=Image.open("Picture/App/" + str(image) + str(self.image_button.index(other_button) + 1) + ".png").resize(size, Image.LANCZOS)
                    )
                    other_button.config(image=original_image)
                    other_button.image = original_image

            if self.callback and callable(self.callback):
                self.callback(number)

        for frame_range in repeat:
            image_frame = Frame(self, bg=color_content)
            image_frame.pack(side=TOP, anchor=W)
            for i in range(frame_range[0], frame_range[1]):
                print
                if i == first_img: 
                    Picture1 = Image.open("Picture/App/" + str(image) + str(i) + ".png").resize(size, Image.LANCZOS)
                    Picture2 = Image.open("Picture/App/" + str(imageOn)).resize(size, Image.LANCZOS)
                    Picture1.paste(Picture2, (0, 0), Picture2)
                    photo_image = ImageTk.PhotoImage(Picture1)
                else:
                    photo_image = ImageTk.PhotoImage(
                        image=Image.open("Picture/App/" + str(image) + str(i) + ".png").resize(size, Image.LANCZOS)
                    )
                button_image = Button(image_frame, image=photo_image, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content)
                button_image.image = photo_image
                button_image.pack(ipadx=2, ipady=2, side=LEFT, expand=True, fill=X, padx=10, pady=5)
                button_image.config(command=lambda number=i, button=button_image, image=image: button_image_clicked(number, button, image))
                self.image_button.append(button_image)