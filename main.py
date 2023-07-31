from tkinter import *
from PIL import Image, ImageTk
import os


from pystray_app.main_pystray import main_pystray

from tkinter_app.frame_c import Frame_c
from tkinter_app.frame_cpp import Frame_cpp
from tkinter_app.frame_csharp import Frame_csharp
from tkinter_app.frame_java import Frame_java
from tkinter_app.frame_nodejs import Frame_nodejs
from tkinter_app.frame_python import Frame_python
from tkinter_app.frame_web import Frame_web
from tkinter_app.frame_parametre import Frame_parametre
from tkinter_app.other_module import color_selection

from data_app.data_json import load_data, save_data, load_info, save_info

from utilities import closing, pseudo, files_list


# load les information du programme
info = load_info()
list_project = info["list_project"]

color_menu = info["color_menu"]
color_first = info["color_first"]
color_content = info["color_content"]

color_text = info["color_text"]
color_soustext = info["color_soustext"]
color_autretext = info["color_autretext"]

icon_type = info["icon_type"]

file_list = files_list("Picture/User/")
info["liste_profil"] = file_list
save_info(info)


# donner utilisateur
data_base = {
    "number_project": 0,
    "user_profil": "Picture/App/User.png",
    "user_name": None,
    "user_color": 1
}

data = load_data()
if data is None:
    data = data_base
save_data(data)

number_project = data["number_project"]
user_profil = data["user_profil"]
user_name = data["user_name"]
user_color = data["user_color"]

if not os.path.exists(user_profil):
    user_profil = "Picture/App/User.png"
    data["user_profil"] = user_profil
    save_data(data)



# crée la fenetre
win = Tk()
win.title("StartProject")
win.iconbitmap("Picture/App/logo.ico")
win.geometry("700x500")
win.resizable(False, False)
    


first_frame = Frame(win, bg=color_first)
first_frame.pack(expand=1, fill=BOTH)

menu_frame = Frame(first_frame, bg=color_menu, width=200, bd=1)
menu_frame.pack_propagate(False)
menu_frame.pack(side=LEFT, fill=Y)

content_frame = Frame(first_frame, bg=color_content, width=500)
content_frame.pack_propagate(False)
content_frame.pack(side=RIGHT, fill=BOTH)



menu_profil_frame = Frame(menu_frame, bg=color_menu)
menu_profil_frame.pack(side=TOP, fill=X, pady=10)

photo_user = ImageTk.PhotoImage(
    image=Image.open(user_profil).resize((125, 125), Image.LANCZOS)
)
label_photo_user = Label(menu_profil_frame, image=photo_user, bg=color_menu)
label_photo_user.image = photo_user
label_photo_user.pack(pady=10, fill=X)

if user_name == None:
    user_name = pseudo(info["p1_pseudo"], info["p2_pseudo"])
    data["user_name"] = user_name
    save_data(data)

text_label_user_name = Label(menu_profil_frame, text=user_name, font=("Arial", 15), bg=color_menu, fg=info["color_pseudo"][user_color-1])
text_label_user_name.pack(anchor=N, fill=X)



menu_line_frame = Frame(menu_frame, bg=color_autretext, height=1)
menu_line_frame.pack(side=TOP, fill=X, padx=15)



menu_stat_frame = Frame(menu_frame, bg=color_menu)
menu_stat_frame.pack(side=TOP, fill=X, pady=5)

text_label = Label(menu_stat_frame, text="Nombre projet", font=("Arial", 12), bg=color_menu, fg=color_soustext)
text_label.pack(side=LEFT, padx=5)

text_label = Label(menu_stat_frame, text=number_project, font=("Arial", 14), bg=color_menu)
if number_project <= 0:
    text_label["fg"] = "#7d0404"
else: 
    text_label["fg"] = "#047d16"
text_label.pack(side=LEFT)



menu_liste_frame = Frame(menu_frame, bg=color_menu)
menu_liste_frame.pack(padx=5, anchor=N, side=LEFT)

liste_button = []
for list_project in list_project:
    photo_list_project = ImageTk.PhotoImage(
        image=Image.open("Picture/App/" + icon_type + "/" + list_project + ".png").resize((20, 20), Image.LANCZOS)
    )
    
    button_list_project = Button(menu_liste_frame, text=list_project, image=photo_list_project, font=("Arial", 13), fg=color_text, bg=color_menu, cursor="hand2", relief="flat", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_menu, activeforeground="#ffffff", compound="left", padx=10, anchor="w")
    button_list_project.image = photo_list_project
    button_list_project.pack(ipadx=2, ipady=2, side=TOP, fill=X, padx=10, pady=2)
    button_list_project.config(command=lambda project=list_project: button_select_project(project))
    liste_button.append(button_list_project)


def button_select_project(project):
    if project == "C":
        Frame_c(content_frame)
    elif project == "C++":
        Frame_cpp(content_frame)
    elif project == "C#":
        Frame_csharp(content_frame)
    elif project == "Java":
        Frame_java(content_frame)
    elif project == "Nodejs":
        Frame_nodejs(content_frame)
    elif project == "Python":
        Frame_python(content_frame)
    elif project == "Web":
        Frame_web(content_frame)
    else:
        print("Erreur : Aucune fonction associée au projet.")

    color_selection(liste_button, project)

# scrollbar = Scrollbar(menu_liste_frame, orient="vertical", command=menu_liste_button_frame.yview) # barre de défilement
# scrollbar.pack(side="right", fill="y")
# menu_liste_button_frame.config(yscrollcommand=scrollbar.set)


menu_parametre_frame = Frame(menu_frame, bg=color_menu)
menu_parametre_frame.pack(side=RIGHT, anchor=S, padx=5, pady=5)

photo_setting = ImageTk.PhotoImage(
    image=Image.open("Picture/App/Settings.png").resize((25, 25), Image.LANCZOS)
)
button_parametre = Button(menu_parametre_frame, image=photo_setting, bg=color_menu, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_menu)
button_parametre.pack(ipadx=2, ipady=2)



global_event = None
def handle_parametre_button_click(event):
    color_selection(liste_button, "Parametre")
    global global_event
    global_event = event
    Frame_parametre(event, content_frame, label_photo_user, text_label_user_name)
button_parametre.bind("<Button-1>", handle_parametre_button_click)



button_select_project("C")



icon = main_pystray(win, global_event, content_frame, label_photo_user, text_label_user_name, liste_button)
win.protocol("WM_DELETE_WINDOW", lambda: closing(icon, win))

win.mainloop()