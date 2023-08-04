import pystray
from PIL import Image
import webbrowser
from utilities import closing

from tkinter_app.frame_c import Frame_c
from tkinter_app.frame_cpp import Frame_cpp
from tkinter_app.frame_csharp import Frame_csharp
from tkinter_app.frame_java import Frame_java
from tkinter_app.frame_nodejs import Frame_nodejs
from tkinter_app.frame_python import Frame_python
from tkinter_app.frame_web import Frame_web
from tkinter_app.frame_parametre import Frame_parametre
from tkinter_app.other_module import color_selection


def main_pystray(win, event, content_frame, label_photo_user, text_label_user_name, liste_button):
    image = Image.open("Picture/App/logo.ico")

    def after_click(icon, query):
        if str(query) == "Github":
            webbrowser.open("https://github.com/xen0r-star/StartProject")

        elif str(query) == "Aide":
            webbrowser.open("index.html")
            
        elif str(query) == "Exit":
            closing(icon, win)

        elif str(query) == "C":
            win.deiconify()
            Frame_c(content_frame)
            color_selection(liste_button, "C")

        elif str(query) == "C++":
            win.deiconify()
            Frame_cpp(content_frame)
            color_selection(liste_button, "C++")

        elif str(query) == "C#":
            win.deiconify()
            Frame_csharp(content_frame)
            color_selection(liste_button, "C#")

        elif str(query) == "Java":
            win.deiconify()
            Frame_java(content_frame)
            color_selection(liste_button, "Java")

        elif str(query) == "Nodejs":
            win.deiconify()
            Frame_nodejs(content_frame)
            color_selection(liste_button, "Nodejs")

        elif str(query) == "Python":
            win.deiconify()
            Frame_python(content_frame)
            color_selection(liste_button, "Python")

        elif str(query) == "Web":
            win.deiconify()
            Frame_web(content_frame)
            color_selection(liste_button, "Web")

        elif str(query) == "Parametre":
            win.deiconify()
            Frame_parametre(event, content_frame, label_photo_user, text_label_user_name)
            color_selection(liste_button, "Prametre")

    Start_Project_submenu = pystray.MenuItem(
        "Start project",
        pystray.Menu(
            pystray.MenuItem("C", after_click),
            pystray.MenuItem("C++", after_click),
            pystray.MenuItem("C#", after_click),
            pystray.MenuItem("Java", after_click),
            pystray.MenuItem("Nodejs", after_click),
            pystray.MenuItem("Python", after_click),
            pystray.MenuItem("Web", after_click),
        ),
    )

    xen0r_star_submenu = pystray.MenuItem(
        "Xen0r-star",
        pystray.Menu(
            pystray.MenuItem("Github", after_click)
        ),
    )

    menu = (
        Start_Project_submenu,
        pystray.MenuItem("Parametre", after_click),
        pystray.MenuItem("Aide", after_click),
        xen0r_star_submenu,
        pystray.MenuItem("Exit", after_click)
    )

    icon = pystray.Icon("GFG", image, "StartProject", menu)
    icon.run_detached()

    return icon