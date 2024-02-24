from tkinter import *
from PIL import Image, ImageTk
import threading
import webbrowser
import math
# import queue

from data_app.data_json import save_data, load_data, load_info
from tkinter_app.other_module import delete_frame_content
from tkinter_app.Widgets.CustomPicker import CustomPicker
from utilities import pseudo, content_folder
# import flask_app.main_flask

from tkinter_app.Widgets.CustomImageButton import CustomImageButton

exit_thread = False  # Variable de contrôle partagée entre les threads
def Frame_parametre(event, win, content_frame, label_photo_user, text_label_user_name):
    delete_frame_content(content_frame) 

    data = load_data()
    user_profil = data["user_profil"]
    user_name = data["user_name"]
    user_color = data["user_color"]

    info = load_info()
    color_menu = info["color_menu"]
    color_content = info["color_content"]
    color_text = info["color_text"]
    color_soustext = info["color_soustext"]
    color_autretext = info["color_autretext"]
    color_zone = info["color_zone"]
    color_scroll = info["color_scroll"]
    color_icon_type = "#ffffff" if info["icon_type"] == "Light" else "#000000"

    color_pseudo = info["color_pseudo"]

    icon_type = info["icon_type"]
    p1_pseudo = info["p1_pseudo"]
    p2_pseudo = info["p2_pseudo"]




    # Paramettre profil utilisateur
    Parametre_top_frame = Frame(content_frame, bg=color_content)
    Parametre_top_frame.pack(pady=(30,0), padx=40, fill=X)

    Parametre_user_frame = Frame(Parametre_top_frame, bg=color_content)
    Parametre_user_frame.pack(side=LEFT, anchor=W)

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


    Parametre_NC_frame = Frame(Parametre_top_frame, bg=color_content)
    Parametre_NC_frame.pack(side=RIGHT, anchor=E)

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


    def save_color(color):
        global user_color
        user_color = color

        data["user_color"] = user_color
        save_data(data)
        text_label_user_name["fg"] = color_pseudo[user_color-1]

    Parametre_color_frame = CustomImageButton(Parametre_NC_frame, color_content, image="Color", imageOn=f"{icon_type}/Color-on.png", repeat=[(1, 6), (6, 11)], size=(30, 30), first_img=user_color, callback=save_color)
    Parametre_color_frame.pack(side=TOP)




    # line
    menu_line_frame = Frame(content_frame, bg=color_soustext, height=1)
    menu_line_frame.pack(side=TOP, fill=X, padx=15, pady=17)




    # palette de couleur de l'application
    text_label=Label(content_frame, text="Couleur application", font=("Arial", 17), bg=color_content, fg=color_text)
    text_label.pack(side=TOP, anchor=W, padx=30)


    def Frame_colorpicker():
        win_colorpicker = Toplevel(win)
        win_colorpicker.title("Sélecteur de couleurs")
        win_colorpicker.iconbitmap("Picture/App/logo.ico")
        win_colorpicker.geometry("350x600")
        win_colorpicker.resizable(False, False)

        selected_color_frame = CustomPicker(win_colorpicker)
        selected_color_frame.pack(fill=BOTH, expand=True)

        win_colorpicker.mainloop()


    square_size = 34
    # color 1
    canvas = Canvas(content_frame, height=(square_size + 10), bd=0, bg=color_content, highlightthickness=0)
    canvas.pack(side=TOP, fill=X, anchor=CENTER, padx=20, pady=5)

    colors = [color_menu, color_content, color_zone, color_text, color_soustext, color_autretext, color_scroll, color_icon_type]
    split = [(1,4), (4,7), (7, 9)]
    split_size = 15
    padx_size = 5

    for frame_range in split:
        for i in range(frame_range[0], frame_range[1]):
            x1 = (i * square_size) + ((i - 1) * padx_size) + (math.floor((i-1) / 3) * split_size)
            y1 = 5
            x2 = x1 + square_size
            y2 = square_size + y1
            canvas.create_rectangle(x1, y1, x2, y2, fill=colors[i-1], outline=color_icon_type)
    
    photo_palette = ImageTk.PhotoImage(
        image=Image.open("Picture/App/" + icon_type + "/Palette.png").resize((square_size, square_size), Image.LANCZOS)
    )
    button_palette = Button(canvas, image=photo_palette, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content, command=Frame_colorpicker)
    button_palette.image = photo_palette
    button_palette.pack(ipadx=5, ipady=2)
    canvas.create_window(((9 * square_size) + (8 * padx_size) + (2 * split_size) + square_size), 23, window=button_palette)

    
    # color 2
    canvas = Canvas(content_frame, height=(square_size + 10), bd=0, bg=color_content, highlightthickness=0)
    canvas.pack(side=TOP, fill=X, anchor=CENTER, padx=20, pady=5)

    colors = [color_menu, color_content, color_zone, color_text, color_soustext, color_autretext, color_scroll, color_icon_type]
    split = [(1,4), (4,7), (7, 9)]
    split_size = 15
    padx_size = 5

    for frame_range in split:
        for i in range(frame_range[0], frame_range[1]):
            x1 = (i * square_size) + ((i - 1) * padx_size) + (math.floor((i-1) / 3) * split_size)
            y1 = 44
            x2 = x1 + square_size
            y2 = square_size + y1
            canvas.create_rectangle(x1, y1, x2, y2, fill=colors[i-1], outline=color_icon_type)

    photo_palette = ImageTk.PhotoImage(
        image=Image.open("Picture/App/" + icon_type + "/Palette.png").resize((square_size, square_size), Image.LANCZOS)
    )
    button_palette = Button(canvas, image=photo_palette, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content, command=Frame_colorpicker)
    button_palette.image = photo_palette
    button_palette.pack(ipadx=5, ipady=2)
    canvas.create_window(((9 * square_size) + (8 * padx_size) + (2 * split_size) + square_size), 63, window=button_palette)


    # bouton connexion
    Parametre_bottom_frame = Frame(content_frame, bg=color_content)
    Parametre_bottom_frame.pack(anchor=CENTER, side=BOTTOM, pady=25, padx=30)  

    link_github_frame = Frame(Parametre_bottom_frame, bg=color_content)
    link_github_frame.pack(side=LEFT, anchor=W)    

    photo_link_github = ImageTk.PhotoImage(
        image=Image.open("Picture/App/" + icon_type + "/Github_link.png").resize((193, 31), Image.LANCZOS)
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
            # flask_app.main_flask.app.run(debug=False, use_debugger=False, use_reloader=False)
            pass

    button_link_github.bind("<Button-1>", link_github)


    link_2_frame = Frame(Parametre_bottom_frame, bg=color_content)
    link_2_frame.pack(side=RIGHT, anchor=E)    

    photo_link_2 = ImageTk.PhotoImage(
        image=Image.open("Picture/App/" + icon_type + "/Link_2.png").resize((193, 31), Image.LANCZOS)
    )
    button_link_2 = Button(link_2_frame, image=photo_link_2, bg=color_content, cursor="hand2", relief="flat", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content, activeforeground="#ffffff", compound="left")
    button_link_2.image = photo_link_2
    button_link_2.pack(ipadx=2, ipady=2, side=TOP, fill=X, padx=10, pady=2)
    
    def link_2(event):
        print("link 2")

    button_link_2.bind("<Button-1>", link_2)