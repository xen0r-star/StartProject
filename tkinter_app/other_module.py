from tkinter import *
from PIL import Image, ImageTk

from data_app.data_json import load_info

from tkinter_app.Widgets.CustomEntry import CustomEntry
from tkinter_app.Widgets.CustomPath import CustomPath
from tkinter_app.Widgets.CustomCheckbutton import CustomCheckbutton
from tkinter_app.Widgets.CustomScrollbar import CustomScrollbar
from tkinter_app.Widgets.CustomText import CustomText
from tkinter_app.Widgets.CustomImageButton import CustomImageButton



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
    scroll_canvas = Canvas(frame, bg=color_content, bd=0, highlightthickness=0) # crée canvas
    scroll_canvas.pack(side=LEFT, expand=True, fill=BOTH)

    scroll = CustomScrollbar(frame, orient=VERTICAL, command=scroll_canvas.yview, slidercolor=color_scroll, troughcolor=color_content, width=20) # crée scrollbar
    scroll.pack(side=RIGHT, fill=Y)

    frame.update_idletasks() # update pout taille
    scroll_frame = Frame(scroll_canvas, bg=color_content) # crée wrapper frame
    scroll_frame.pack(expand=True, fill=X)
    scroll_canvas.create_window(0, 0, window=scroll_frame, anchor="nw", width=scroll_canvas.winfo_width())
    scroll_canvas.config(yscrollcommand=scroll.set)

    def update_scroll(): # update pout taille scroll
        scroll_frame.update()
        scroll_canvas.config(scrollregion=scroll_canvas.bbox('all')) 


    # Titre projet
    titre_entry = CustomEntry(scroll_frame, width=20, bg=color_zone, insertbackground=color_text, insertbackgroundoff=color_soustext, placeholder="Titre du projet")
    titre_entry.pack(side=TOP, anchor=W, padx=10)

    # Selectionner fichier 
    select_directory_frame = CustomPath(scroll_frame, icon_type, color_zone, color_soustext)
    select_directory_frame.pack(fill=X, pady=15, padx=10)


    # line
    menu_line_frame = Frame(scroll_frame, bg=color_soustext, height=1)
    menu_line_frame.pack(side=TOP, fill=X, padx=15, pady=10)


    # partie readme
    readme_checkbutton_frame = Frame(scroll_frame, bg=color_content)
    readme_checkbutton_frame.pack(side=TOP, anchor=N, fill=X, pady=5, padx=8)

    readme_element = Frame(scroll_frame, bg=color_content)
    readme_element.pack(side=TOP, anchor=N, fill=X, pady=5, padx=8)
    
    readme_frame = None
    def readme_click_button(checked):
        nonlocal readme_frame

        if checked == True:
            readme_frame = Frame(readme_element, bg=color_content)
            readme_frame.pack()

            # Image
            text_label=Label(readme_frame, text="Image", font=("Arial", 15), bg=color_content, fg=color_text)
            text_label.pack(side=TOP, anchor=W, padx=5)

            def Image_fonction_readme(number):
                print(f"Image {number}")

            image_readme_frame = CustomImageButton(readme_frame, color_content, image="Picture_readme", imageOn=f"{icon_type}/Picture_readme-on.png", repeat=[(1, 4), (4, 7)], size=(89, 50), callback=Image_fonction_readme)
            image_readme_frame.pack(side=TOP, anchor=W, padx=(20,0))

            # Description
            text_label=Label(readme_frame, text="Description", font=("Arial", 15), bg=color_content, fg=color_text)
            text_label.pack(side=TOP, anchor=W, padx=5, pady=(10,0))

            description_frame = CustomText(readme_frame, bg=color_zone, fg=color_text, placeholder="La description générale du projet ...", placeholder_color=color_soustext)
            description_frame.pack(side=TOP, anchor=W, padx=(30,0), pady=5)

            # But
            text_label=Label(readme_frame, text="But", font=("Arial", 15), bg=color_content, fg=color_text)
            text_label.pack(side=TOP, anchor=W, padx=5, pady=(10,0))

            but_frame = CustomText(readme_frame, bg=color_zone, fg=color_text, placeholder="Le but du projet ...", placeholder_color=color_soustext)
            but_frame.pack(side=TOP, anchor=W, padx=(30,0), pady=5)

            # Licence
            text_label=Label(readme_frame, text="Licence", font=("Arial", 15), bg=color_content, fg=color_text)
            text_label.pack(side=TOP, anchor=W, padx=5, pady=(10,0))

            # Auteur
            text_label=Label(readme_frame, text="Auteur", font=("Arial", 15), bg=color_content, fg=color_text)
            text_label.pack(side=TOP, anchor=W, padx=5, pady=(10,0))

            auteur_texte = CustomEntry(readme_frame, placeholder="Auteur du projet", width=20, bg=color_zone, insertbackground=color_text, insertbackgroundoff=color_soustext)
            auteur_texte.pack(side=TOP, anchor=W, padx=(30,0), pady=5)

            mousewheel_all_widgets(readme_frame, on_mouse_scroll)
        else:
            readme_frame.destroy()
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

    def mousewheel_all_widgets(widget, function):
        widget.bind("<MouseWheel>", function)
        for child in widget.winfo_children():
            mousewheel_all_widgets(child, function)

    mousewheel_all_widgets(scroll_frame, on_mouse_scroll)

    scroll_canvas.bind("<MouseWheel>", on_mouse_scroll)
    scroll.bind("<MouseWheel>", on_mouse_scroll)