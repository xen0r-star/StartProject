from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

from data_app.data_json import load_info

from tkinter_app.Widgets.CustomEntry import CustomEntry
from tkinter_app.Widgets.CustomPath import CustomPath
from tkinter_app.Widgets.CustomCheckbutton import CustomCheckbutton
from tkinter_app.Widgets.CustomScrollbar import CustomScrollbar



info = load_info()
color_menu = info["color_menu"]
color_content = info["color_content"]

color_text = info["color_text"]
color_soustext = info["color_soustext"]
color_zone = info["color_zone"]
color_scroll = info["color_scroll"]

icon_type = info["icon_type"]



def delete_frame_content(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()



def color_selection(liste_button, project):
    for button in liste_button:
        if button["text"] == project:
            button["bg"] = color_content
        else:
            button["bg"] = color_menu



def general_part(frame, name):
    # Titre frame
    langage_frame = Frame(frame, bg=color_content)
    langage_frame.pack(side=TOP, anchor=W, fill=X)

    photo_langage = ImageTk.PhotoImage(
        image=Image.open("Picture/App/" + icon_type + "/" + name + ".png").resize((50, 50), Image.LANCZOS)
    )
    label_photo_langage = Label(langage_frame, image=photo_langage, bg=color_content)
    label_photo_langage.image = photo_langage
    label_photo_langage.pack(pady=10, side=LEFT)
    
    text_titre_label = Label(langage_frame, text=name, font=("Arial", 24), bg=color_content, fg=color_text)
    text_titre_label.pack(side=LEFT, padx=5)
    

    # Scrollbar
    scroll_canvas = Canvas(frame, bg="green", bd=0, highlightthickness=0) # crée canvas
    scroll_canvas.pack(side=LEFT, expand=True, fill=BOTH)

    scroll = CustomScrollbar(frame, orient=VERTICAL, command=scroll_canvas.yview, slidercolor=color_scroll, troughcolor=color_content, width=20) # crée scrollbar
    scroll.pack(side=RIGHT, fill=Y)

    frame.update_idletasks() # update pout taille
    scroll_frame = Frame(scroll_canvas, bg="red") # crée wrapper frame
    scroll_frame.pack(expand=True, fill=X)
    scroll_canvas.create_window(0, 0, window=scroll_frame, anchor="nw", width=scroll_canvas.winfo_width())
    scroll_canvas.config(yscrollcommand=scroll.set)

    def update_scroll(): # update pout taille scroll
        scroll_frame.update()
        scroll_canvas.config(scrollregion=scroll_canvas.bbox('all')) 


    # Titre projet
    title_frame = Frame(scroll_frame, bg=color_content)
    title_frame.pack(side=TOP, anchor=N, fill=X, pady=5, padx=10)
    title_ipadx_frame = Frame(title_frame, bg=color_zone, width=5)
    title_ipadx_frame.pack(side=LEFT, fill=Y)

    titre_texte = CustomEntry(title_frame, default_text="Titre", width=20, insertbackground=color_text, insertbackgroundoff=color_soustext, bg=color_zone)
    titre_texte.pack(side=LEFT, ipady=3)


    # Selectionner fichier 
    select_directory_frame = CustomPath(scroll_frame, icon_type, color_zone, color_soustext)
    select_directory_frame.pack(fill=X, pady=15, padx=10)


    # partie readme
    readme_checkbutton_frame = Frame(scroll_frame, bg=color_content)
    readme_checkbutton_frame.pack(side=TOP, anchor=N, fill=X, pady=5, padx=8)

    readme_frame = Frame(scroll_frame, bg=color_content)
    readme_frame.pack(side=TOP, anchor=N, fill=X, pady=5, padx=8)

    def readme_click_button(checked):
        if checked == True:
            text_label=Label(readme_frame, text="Image", font=("Arial", 15), bg=color_content, fg=color_text)
            text_label.pack(side=TOP, anchor=W, padx=5)

            image_button = []
            image1_frame = Frame(readme_frame, bg=color_content)
            image1_frame.pack(side=TOP, anchor=W, padx=(20,0))
            for i in range(1, 4):
                if i == 1: 
                    Picture1 = Image.open("Picture/App/Picture_readme"+str(i)+".png").resize((89, 50), Image.LANCZOS)
                    Picture2 = Image.open("Picture/App/" + icon_type + "/Picture_readme-on.png").resize((89, 50), Image.LANCZOS)
                    Picture1.paste(Picture2, (0, 0), Picture2)
                    photo_image = ImageTk.PhotoImage(Picture1)
                else:
                    photo_image = ImageTk.PhotoImage(
                        image=Image.open("Picture/App/Picture_readme"+str(i)+".png").resize((89, 50), Image.LANCZOS)
                    )
                button_image = Button(image1_frame, image=photo_image, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content)
                button_image.image = photo_image
                button_image.pack(ipadx=2, ipady=2, side=LEFT, expand=True, fill=X, padx=10, pady=5)
                button_image.config(command=lambda button=button_image: button_color_clicked(button))
                image_button.append(button_image)
                
            image2_frame = Frame(readme_frame, bg=color_content)
            image2_frame.pack(side=TOP, anchor=W, padx=(20,0))
            for i in range(4, 7):
                photo_image = ImageTk.PhotoImage(
                image=Image.open("Picture/App/Picture_readme.png").resize((89, 50), Image.LANCZOS)
                )
                button_image = Button(image2_frame, image=photo_image, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content)
                button_image.image = photo_image
                button_image.pack(ipadx=2, ipady=2, side=LEFT, expand=True, fill=X, padx=10, pady=5)
                button_image.config(command=lambda button=button_image: button_color_clicked(button))
                image_button.append(button_image)


            text_label=Label(readme_frame, text="Description", font=("Arial", 15), bg=color_content, fg=color_text)
            text_label.pack(side=TOP, anchor=W, padx=5, pady=(10,0))

            description_frame = Frame(readme_frame, bg=color_content)
            description_frame.pack(side=TOP, anchor=W)
            description_ipadx_frame = Frame(description_frame, bg=color_zone, width=5)
            description_ipadx_frame.pack(side=LEFT, fill=Y, padx=(30,0), pady=5)

            description_texte = Text(description_frame, width=35, height=7, insertbackground=color_soustext, insertofftime=500, insertontime=500, insertwidth=1.5, font=("Arial", 12), bg=color_zone, fg=color_soustext, bd=0, selectbackground="#e06161", selectforeground="#ffffff")
            description_texte.pack(side=LEFT, padx=(0,15), pady=5, ipady=3)


            text_label=Label(readme_frame, text="But", font=("Arial", 15), bg=color_content, fg=color_text)
            text_label.pack(side=TOP, anchor=W, padx=5, pady=(10,0))


            def button_color_clicked(button):
                Picture1 = Image.open("Picture/App/Picture_readme.png").resize((89, 50), Image.LANCZOS)
                Picture2 = Image.open("Picture/App/" + icon_type + "/Picture_readme-on.png").resize((89, 50), Image.LANCZOS)
                Picture1.paste(Picture2, (0, 0), Picture2)
                new_image = ImageTk.PhotoImage(Picture1)
                button.config(image=new_image)
                button.image = new_image

                for other_button in image_button:
                    if other_button != button:  # Évite de changer l'image du bouton cliqué une deuxième fois
                        original_image = ImageTk.PhotoImage(
                                image=Image.open("Picture/App/Picture_readme.png").resize((89, 50), Image.LANCZOS)
                        )
                        other_button.config(image=original_image)
                        other_button.image = original_image
            
            update_scroll()
        else:
            for widget in readme_frame.winfo_children():
                    widget.destroy()
                    readme_frame.update_idletasks()
            update_scroll()

    readme_checkbutton = CustomCheckbutton(readme_checkbutton_frame, icon_type, color_content, readme_click_button)
    readme_checkbutton.pack(side=LEFT)

    text_label=Label(readme_checkbutton_frame, text="Fichier Readme", font=("Arial", 12), bg=color_content, fg=color_text)
    text_label.pack(side=LEFT, fill=X, padx=3)


    update_scroll()


    # Event scroll
    def on_mouse_scroll(event):
        content_height = scroll_canvas.winfo_reqheight()  # Taille du contenu
        canvas_height = scroll_frame.winfo_height()  # Hauteur du canvas

        if content_height < canvas_height:
            scroll_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def mousewheel_all_nested_widgets(widget, function):
        widget.bind("<MouseWheel>", function)
        for child in widget.winfo_children():
            mousewheel_all_nested_widgets(child, function)

    def mousewheel_all_descendants(widget, function):
        mousewheel_all_nested_widgets(widget, function)
        for child in widget.winfo_children():
            mousewheel_all_descendants(child, function)

    mousewheel_all_descendants(scroll_frame, on_mouse_scroll)

    scroll_canvas.bind("<MouseWheel>", on_mouse_scroll)
    scroll.bind("<MouseWheel>", on_mouse_scroll)