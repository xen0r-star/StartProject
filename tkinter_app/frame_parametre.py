from tkinter import *
from PIL import Image, ImageTk
import threading
import webbrowser
import queue

from data_app.data_json import save_data, load_data, load_info
from tkinter_app.other_module import delete_frame_content
from utilities import pseudo, content_folder
import flask_app.main_flask

exit_thread = False  # Variable de contrôle partagée entre les threads
def Frame_parametre(event, content_frame, label_photo_user, text_label_user_name):
    delete_frame_content(content_frame) 

    data = load_data()
    user_profil = data["user_profil"]
    user_name = data["user_name"]
    user_color = data["user_color"]

    info = load_info()
    color_content = info["color_content"]
    color_pseudo = info["color_pseudo"]
    color_text = info["color_text"]
    color_zone = info["color_zone"]

    icon_type = info["icon_type"]
    p1_pseudo = info["p1_pseudo"]
    p2_pseudo = info["p2_pseudo"]



    Parametre_user_frame = Frame(content_frame, bg=color_content)
    Parametre_user_frame.pack(side=LEFT, anchor=N, padx=35, pady=30)


    photo_user_parametre = ImageTk.PhotoImage(
        image=Image.open(user_profil if content_folder("Picture/User/") == True else "Picture/App/Empty.png").resize((100, 100), Image.LANCZOS)
    )
    label_user_parametre = Label(Parametre_user_frame, image=photo_user_parametre, bg=color_content)
    label_user_parametre.image = photo_user_parametre
    label_user_parametre.pack(pady=5)

    parametre_button_frame = Frame(Parametre_user_frame, bg=color_content)
    parametre_button_frame.pack(anchor=S, fill=X)

    photo_left = ImageTk.PhotoImage(
        image=Image.open("Picture/App/Left.png").resize((30, 30), Image.LANCZOS)
    )
    button_left = Button(parametre_button_frame, image=photo_left, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content)
    button_left.image = photo_left
    button_left.pack(ipadx=2, ipady=2, side=LEFT, expand=True, fill=X)

    photo_save = ImageTk.PhotoImage(
        image=Image.open("Picture/App/Save.png").resize((30, 30), Image.LANCZOS)
    )
    button_save = Button(parametre_button_frame, image=photo_save, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content)
    button_save.image = photo_save
    button_save.pack(ipadx=2, ipady=2, side=LEFT, expand=True, fill=X)

    photo_right = ImageTk.PhotoImage(
        image=Image.open("Picture/App/Right.png").resize((30, 30), Image.LANCZOS)
    )
    button_right = Button(parametre_button_frame, image=photo_right, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content)
    button_right.image = photo_right
    button_right.pack(ipadx=2, ipady=2, side=LEFT, expand=True, fill=X)


    if content_folder("Picture/User/") == True:
        number_liste = info["liste_profil"].index(user_profil)
    else:
        number_liste = None

    def button_parametre_left(event):
        nonlocal number_liste
        if number_liste != None:
            number_liste -= 1
            if number_liste < 0:
                number_liste = len(info["liste_profil"])-1

            photo_user_parametre = ImageTk.PhotoImage(
                image=Image.open(info["liste_profil"][number_liste]).resize((100, 100), Image.LANCZOS)
            )
            label_user_parametre.photo_parametre_on = photo_user_parametre
            label_user_parametre.config(image=photo_user_parametre)

    button_left.bind("<Button-1>", button_parametre_left)

    def button_parametre_right(event):
        nonlocal number_liste
        if number_liste != None:
            number_liste += 1
            if number_liste >= len(info["liste_profil"]):
                number_liste = 0

            photo_user_parametre = ImageTk.PhotoImage(
                image=Image.open(info["liste_profil"][number_liste]).resize((100, 100), Image.LANCZOS)
            )
            label_user_parametre.photo_parametre_on = photo_user_parametre
            label_user_parametre.config(image=photo_user_parametre)

    button_right.bind("<Button-1>", button_parametre_right)
    
    def button_parametre_save(event):
        nonlocal number_liste
        if number_liste != None:
            photo_user = ImageTk.PhotoImage(
                image=Image.open(info["liste_profil"][number_liste]).resize((125, 125), Image.LANCZOS)
            )
            label_photo_user.photo_parametre_on = photo_user
            label_photo_user.config(image=photo_user)

            data["user_profil"] = info["liste_profil"][number_liste]
            save_data(data)

    button_save.bind("<Button-1>", button_parametre_save)



    Parametre_NC_frame = Frame(content_frame, bg=color_content)
    Parametre_NC_frame.pack(pady=30)

    Parametre_name_frame = Frame(Parametre_NC_frame, bg=color_content)
    Parametre_name_frame.pack(side=TOP, anchor=N, pady=15)

    text_label_parametre_name = Label(Parametre_name_frame, text=user_name, font=("Arial", 14), bg=color_zone, fg=color_text, width=19)
    text_label_parametre_name.pack(fill=X, side=LEFT, anchor=W, ipadx=3, ipady=3)

    photo_alea = ImageTk.PhotoImage(
        image=Image.open("Picture/App/Alea.png").resize((30, 30), Image.LANCZOS)
    )
    button_alea = Button(Parametre_name_frame, image=photo_alea, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content)
    button_alea.image = photo_alea
    button_alea.pack(ipadx=2, ipady=2, padx=5, side=RIGHT, expand=True, fill=X)

    def button_parametre_alea(event):
        user_name = pseudo(p1_pseudo, p2_pseudo)
        text_label_parametre_name.config(text=user_name)
        text_label_user_name.config(text=user_name)

        data["user_name"] = user_name
        save_data(data)

    button_alea.bind("<Button-1>", button_parametre_alea)


    color_button = []
    Parametre_color1_frame = Frame(Parametre_NC_frame, bg=color_content)
    Parametre_color1_frame.pack(side=TOP)
    for i in range(1, 6):
        if user_color == i: 
            Picture1 = Image.open("Picture/App/Color" + str(i) + ".png").resize((30, 30), Image.LANCZOS)
            Picture2 = Image.open("Picture/App/" + icon_type + "/Color-on.png").resize((30, 30), Image.LANCZOS)
            Picture1.paste(Picture2, (0, 0), Picture2)
            photo_color_parametre = ImageTk.PhotoImage(Picture1)
        else:
            photo_color_parametre = ImageTk.PhotoImage(
                image=Image.open("Picture/App/Color" + str(i) + ".png").resize((30, 30), Image.LANCZOS)
            )
        button_color_parametre = Button(Parametre_color1_frame, image=photo_color_parametre, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content)
        button_color_parametre.image = photo_color_parametre
        button_color_parametre.pack(ipadx=2, ipady=2, side=LEFT, expand=True, fill=X, padx=10, pady=5)
        button_color_parametre.config(command=lambda color=i, button=button_color_parametre: button_color_clicked(color, button))
        color_button.append(button_color_parametre)
        
    Parametre_color2_frame = Frame(Parametre_NC_frame, bg=color_content)
    Parametre_color2_frame.pack(side=TOP)
    for i in range(6, 11):
        if user_color == i: 
            Picture1 = Image.open("Picture/App/Color" + str(i) + ".png").resize((30, 30), Image.LANCZOS)
            Picture2 = Image.open("Picture/App/" + icon_type + "/Color-on.png").resize((30, 30), Image.LANCZOS)
            Picture1.paste(Picture2, (0, 0), Picture2)
            photo_color_parametre = ImageTk.PhotoImage(Picture1)
        else:
            photo_color_parametre = ImageTk.PhotoImage(
                image=Image.open("Picture/App/Color" + str(i) + ".png").resize((30, 30), Image.LANCZOS)
            )
        button_color_parametre = Button(Parametre_color2_frame, image=photo_color_parametre, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content)
        button_color_parametre.image = photo_color_parametre
        button_color_parametre.pack(ipadx=2, ipady=2, side=LEFT, expand=True, fill=X, padx=10, pady=5)
        button_color_parametre.config(command=lambda color=i, button=button_color_parametre: button_color_clicked(color, button))
        color_button.append(button_color_parametre)

    def button_color_clicked(color, button):
        global user_color
        user_color = color

        data["user_color"] = user_color
        save_data(data)

        text_label_user_name["fg"] = color_pseudo[user_color-1]

        Picture1 = Image.open("Picture/App/Color" + str(color) + ".png").resize((30, 30), Image.LANCZOS)
        Picture2 = Image.open("Picture/App/" + icon_type + "/Color-on.png").resize((30, 30), Image.LANCZOS)
        Picture1.paste(Picture2, (0, 0), Picture2)
        new_image = ImageTk.PhotoImage(Picture1)

        button.config(image=new_image)
        button.image = new_image

        for other_button in color_button:
            if other_button != button:  # Évite de changer l'image du bouton cliqué une deuxième fois
                original_image = ImageTk.PhotoImage(
                    image=Image.open("Picture/App/Color" + str(color_button.index(other_button) + 1) + ".png").resize((30, 30), Image.LANCZOS)
                )
                other_button.config(image=original_image)
                other_button.image = original_image


    link_github_frame = Frame(content_frame, bg=color_content)
    link_github_frame.pack(anchor=W, side=TOP)    

    photo_link_github = ImageTk.PhotoImage(
        image=Image.open("Picture/App/" + icon_type + "/Github_link.png").resize((218, 35), Image.LANCZOS)
    )
    button_link_github = Button(link_github_frame, image=photo_link_github, bg=color_content, cursor="hand2", relief="flat", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content, activeforeground="#ffffff", compound="left")
    button_link_github.image = photo_link_github
    button_link_github.pack(ipadx=2, ipady=2, side=TOP, fill=X, padx=10, pady=2)
    
    def link_github(event):
        print("link github compte")
        webbrowser.open("http://localhost:5000")
        thread = threading.Thread(target=run_flask_link)
        thread.start()

    def run_flask_link():
        global exit_thread
        print("lancer ok")
        while not exit_thread:
            flask_app.main_flask.app.run(debug=False, use_debugger=False, use_reloader=False)
            pass


    button_link_github.bind("<Button-1>", link_github)