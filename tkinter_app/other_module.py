from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

from data_app.data_json import load_info


info = load_info()
color_menu = info["color_menu"]
color_content = info["color_content"]

color_text = info["color_text"]
color_soustext = info["color_soustext"]
color_zone = info["color_zone"]

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
    langage_frame = Frame(frame, bg=color_content)
    langage_frame.pack(side=TOP, anchor=W)

    photo_langage = ImageTk.PhotoImage(
        image=Image.open("Picture/App/" + icon_type + "/" + name + ".png").resize((50, 50), Image.LANCZOS)
    )
    label_photo_langage = Label(langage_frame, image=photo_langage, bg=color_content)
    label_photo_langage.image = photo_langage
    label_photo_langage.pack(pady=10, side=LEFT)
    
    text_titre_label = Label(langage_frame, text=name, font=("Arial", 24), bg=color_content, fg=color_text)
    text_titre_label.pack(side=LEFT, padx=5)


    title_frame = Frame(frame, bg=color_content)
    title_frame.pack(side=TOP, anchor=N, fill=X, pady=5, padx=10)

    default_text = "Titre"
    path_texte = Entry(title_frame, insertbackground=color_soustext, insertofftime=500, insertontime=500, insertwidth=1.5, font=("Arial", 12), bg=color_zone, fg=color_soustext, bd=0, selectbackground="#e06161", selectforeground="#ffffff")
    path_texte.pack(side=LEFT, ipady=3)
    path_texte.insert(0, default_text)
    
    def on_entry_click(event): # Lorsque la zone de saisie obtient le focus, le texte par défaut disparaît
        if path_texte.get() == default_text:
            path_texte.delete(0, END)
            path_texte.config(fg=color_text)

    def on_entry_focusout(event): # Lorsque la zone de saisie perd le focus, si aucun texte n'a été saisi, le texte par défaut est réaffiché
        if path_texte.get() == "":
            path_texte.insert(0, default_text)
            path_texte.config(fg=color_soustext)

    path_texte.bind("<FocusIn>", on_entry_click)
    path_texte.bind("<FocusOut>", on_entry_focusout)


    readme_frame = Frame(frame, bg=color_content)
    readme_frame.pack(side=TOP, anchor=N, fill=X, pady=8, padx=8)

    button_check_statut = False
    def button_check():
        nonlocal button_check_statut
        if button_check_statut == False:
            photo_check = ImageTk.PhotoImage(
                image=Image.open("Picture/App/" + icon_type + "/Checked-1.png").resize((25, 25), Image.LANCZOS)
            )
            button_check_statut = True
        else : 
            photo_check = ImageTk.PhotoImage(
                image=Image.open("Picture/App/" + icon_type + "/Checked-0.png").resize((25, 25), Image.LANCZOS)
            )
            button_check_statut = False

        check_button.config(image=photo_check)
        check_button.image = photo_check

    photo_check = ImageTk.PhotoImage(
        image=Image.open("Picture/App/" + icon_type + "/Checked-0.png").resize((25, 25), Image.LANCZOS)
    )
    check_button = Button(readme_frame, image=photo_check, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content, command=button_check)
    check_button.image = photo_check
    check_button.pack(side=LEFT, ipadx=2, ipady=2)

    text_label=Label(readme_frame, text="Fichier Readme", font=("Arial", 12), bg=color_content, fg=color_text)
    text_label.pack(side=LEFT, anchor=W, fill=X, padx=5)


    select_directory_frame = Frame(frame, bg=color_zone)
    select_directory_frame.pack(side=TOP, fill=X, pady=15, ipadx=1, ipady=4, padx=10)

    def directory():
        filepath=filedialog.askdirectory()
        if len(filepath) >= 55:
            shortened_filepath = "... " + filepath[-50:]
        else:
            shortened_filepath = filepath
        path_label["text"] = shortened_filepath

    path_label = Label(select_directory_frame, text="Chemin vers le dossier", font=("Arial", 10), fg=color_soustext, width=40, bg=color_zone, anchor='w')
    path_label.pack(side=LEFT, padx=(3, 0))  # padx ajoute un espacement à gauche pour l'alignement

    photo_directory = ImageTk.PhotoImage(
        image=Image.open("Picture/App/" + icon_type + "/Folder.png").resize((25, 20), Image.LANCZOS)
    )
    directory_button = Button(select_directory_frame, image=photo_directory, command = directory, bg=color_zone, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground="#777777")
    directory_button.image = photo_directory
    directory_button.pack(side=LEFT, padx=5) 