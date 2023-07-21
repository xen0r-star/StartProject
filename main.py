import random
import json
from tkinter import *
from PIL import Image, ImageTk
import pystray
import webbrowser


icon = None
def run_icon():
    image = Image.open("Picture/App/logo.ico")

    def after_click(icon, query):
        if str(query) == "Github":
            webbrowser.open("https://github.com/xen0r-star/StartProject")
        elif str(query) == "Exit":
            closing()
        elif str(query) == "Python":
            webbrowser.open("https://www.python.org/")
        elif str(query) == "Freepik":
            webbrowser.open("https://fr.freepik.com/")

    Start_Project_submenu = pystray.MenuItem(
        "Start project",
        pystray.Menu(
            pystray.MenuItem("Web", after_click)
        ),
    )
    
    xen0r_star_submenu = pystray.MenuItem(
        "Xen0r-star",
        pystray.Menu(
            pystray.MenuItem("Github", after_click)
        ),
    )
    
    Source_submenu = pystray.MenuItem(
        "Source",
        pystray.Menu(
            pystray.MenuItem("Python", after_click),
            pystray.MenuItem("Freepik", after_click)
        ),
    )

    menu = (
        Start_Project_submenu,
        xen0r_star_submenu,
        Source_submenu,
        pystray.MenuItem("Exit", after_click)
    )

    global icon
    icon = pystray.Icon("GFG", image, "StartProject", menu)
    icon.run_detached()



win = None
content_frame = None
text_label_user_name = None
color_pseudo = ["#D20C0C", "#0C43D2", "#3B9206","#D29B0C", "#D20CCA", "#F26969", "#696FF2", "#9EF269", "#F0F269", "#F269D4"]


def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None

example_data = {
    "number_project": 0,
    "user_profil": 1,
    "user_name": None,
    "user_color": 1
}

data = load_data()
if data is None:
    data = example_data

save_data(data)

number_project = data["number_project"]
user_profil = data["user_profil"]
user_name = data["user_name"]
user_color = data["user_color"]

def run_mainloop():
    global win
    win = Tk()
    win.title("StartProject")
    win.iconbitmap("Picture/App/logo.ico")
    win.geometry("700x500")
    win.resizable(False, False)
    win.protocol("WM_DELETE_WINDOW", closing)
        


    def pseudo():
        p1 = ["Happy", "Crazy", "Lucky", "Silly", "Wild", "Brave", "Tiny", "Giant", "Glamorou", "Funky", "Gentle", "Sparklin", "Radiant", "Fierce", "Charming", "Dazzling", "Cheerful", "Elegant", "Enchanti", "Vibrant", "Giddy", "Glorious", "Marvelou", "Clever", "Graceful", "Splendid", "Energetic", "Creative", "Zealous", "Delightf", "Jovial", "Flamboya", "Chic", "Blazing", "Bubbly", "Dynamic", "Vivacious", "Exquisite", "Harmonio", "Ravishing", "Enthusia", "Sensatio", "Fantastic", "Enigmatic", "Gorgeous", "Mesmeriz", "Fantasti", "Spectacu", "Alluring", "Captivat", "Wondrous", "Thrillin", "Adventur", "Stunning", "Incredib", "Majestic", "Spellbin", "Graceful", "Resplend", "Magnific", "Fascinat", "Awesome", "Serene", "Brilliant", "Spirited", "Exhilara", "Spectacu", "Deliciou", "Charming", "Brilliant", "Glowing", "Lovely", "Glisteni", "Exotic", "Colorful", "Dynamic", "Fancy", "Elegant", "Talented", "Shimmeri", "Luminous", "Vibrant", "Intrigui", "Beautifu", "Delicate", "Whimsica", "Dramatic", "Enchanti", "Glamorou", "Sunny", "Spectacu", "Fantasti", "Dazzling", "Radiant", "Clever", "Gentle", "Blazing", "Sensatio", "Ravishing", "Harmonio", "Jovial", "Flamboya", "Zealous", "Bubbly", "Cheerful", "Vibrant", "Enchanti"]
        p2 = ["Ninja", "Panda", "Dragon", "Cookie", "Squirrel", "Penguin", "Robot", "Wizard", "Octopus", "Alien", "Superhero", "Star", "Moon", "Sun", "Flower", "Rainbow", "Dolphin", "Mermaid", "Unicorn", "Phoenix", "Phoenix", "Phoenix", "Phoenix", "Phoenix", "Phoenix", "Phoenix", "Phoenix", "Phoenix", "Phoenix", "Phoenix", "Butterfly", "Fairy", "Sparrow", "Jaguar", "Lion", "Tiger", "Eagle", "Hummingbi", "Firefly", "Swordfish", "Thunder", "Cheetah", "Gazelle", "Gorilla", "Lemur", "Leopard", "Zebra", "Kangaroo", "Koala", "Giraffe", "Elephant", "Puma", "Panther", "Seagull", "Seahorse", "Dove", "Albatross", "Snowflake", "Icicle", "Snowman", "Snowball", "Raindrop", "Tornado", "Hurricane", "Comet", "Meteor", "Galaxy", "Constell", "Stardust", "Galaxy", "Supernova", "Quasar", "Asteroid", "Cosmos", "Nebula", "Rocket", "Spaceship", "Astronaut", "Satellite", "Starship", "UFO", "Alien", "Andromeda", "Orion", "Draco", "Lyra", "Pegasus", "Taurus", "Leo", "Virgo", "Libra", "Scorpio", "Sagittas", "Capricorn", "Aquarius", "Pisces", "Jupiter", "Mars", "Neptune", "Venus", "Uranus", "Mercury", "Saturn", "Pluto", "Earth", "Moon", "Sun", "Comet", "Meteor", "Galaxy", "Constell", "Stardust"]

        p1 = random.choice(p1)
        p2 = random.choice(p2)
        pseudo = p1 + p2
        return pseudo



    color_first = "#363245"
    first_frame = Frame(win, bg=color_first)
    first_frame.pack(expand=1, fill=BOTH)

    color_menu = "#23212d"
    menu_frame = Frame(first_frame, bg=color_menu, width=200, bd=1)
    menu_frame.pack_propagate(False)
    menu_frame.pack(side=LEFT, fill=Y)

    color_content = "#363245"
    global content_frame
    content_frame = Frame(first_frame, bg=color_content, width=500)
    content_frame.pack_propagate(False)
    content_frame.pack(side=RIGHT, fill=BOTH)



    menu_profil_frame = Frame(menu_frame, bg=color_menu)
    menu_profil_frame.pack(side=TOP, fill=X, pady=20)

    photo_user = ImageTk.PhotoImage(
        image=Image.open("Picture/User/User-" + str(user_profil) + ".png").resize((125, 125), Image.LANCZOS)
    )
    label_photo_user = Label(menu_profil_frame, image=photo_user, bg=color_menu)
    label_photo_user.image = photo_user
    label_photo_user.pack(pady=5, fill=X)

    global user_name
    global text_label_user_name
    if user_name == None:
        user_name = pseudo()
        data["user_name"] = user_name
        save_data(data)

    text_label_user_name = Label(menu_profil_frame, text=user_name, font=("Arial", 15), bg=color_menu, fg=color_pseudo[user_color-1])
    text_label_user_name.pack(anchor=N, fill=X)



    menu_stat_frame = Frame(menu_frame, bg=color_menu)
    menu_stat_frame.pack(side=TOP, fill=X)

    text_label = Label(menu_stat_frame, text="Nombre projet", font=("Arial", 12), bg=color_menu, fg="#ffffff")
    text_label.pack(side=LEFT, padx=5)

    text_label = Label(menu_stat_frame, text=number_project, font=("Arial", 14), bg=color_menu)
    if number_project <= 0:
        text_label["fg"] = "#7d0404"
    else: 
        text_label["fg"] = "#047d16"
    text_label.pack(side=LEFT)



    menu_parametre_frame = Frame(menu_frame, bg=color_menu)
    menu_parametre_frame.pack(side=RIGHT, anchor=S, padx=5, pady=5)

    photo_setting = ImageTk.PhotoImage(
        image=Image.open("Picture/App/Settings.png").resize((25, 25), Image.LANCZOS)
    )
    button_parametre = Button(menu_parametre_frame, image=photo_setting, bg=color_menu, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_menu)
    button_parametre.pack(ipadx=2, ipady=2)



    def Frame_parametre(event):
        delete_frame_content()

        Parametre_user_frame = Frame(content_frame, bg=color_content)
        Parametre_user_frame.pack(side=LEFT, anchor=N, padx=35, pady=40)


        photo_user_parametre = ImageTk.PhotoImage(
            image=Image.open("Picture/User/User-" + str(user_profil) + ".png").resize((100, 100), Image.LANCZOS)
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


        def button_parametre_left(event):
            global user_profil
            user_profil -= 1
            if user_profil <= 0:
                user_profil = 9

            photo_user_parametre = ImageTk.PhotoImage(
                image=Image.open("Picture/User/User-" + str(user_profil) + ".png").resize((100, 100), Image.LANCZOS)
            )
            label_user_parametre.photo_parametre_on = photo_user_parametre
            label_user_parametre.config(image=photo_user_parametre)

        button_left.bind("<Button-1>", button_parametre_left)

        def button_parametre_right(event):
            global user_profil
            user_profil += 1
            if user_profil >= 10:
                user_profil = 1

            photo_user_parametre = ImageTk.PhotoImage(
                image=Image.open("Picture/User/User-" + str(user_profil) + ".png").resize((100, 100), Image.LANCZOS)
            )
            label_user_parametre.photo_parametre_on = photo_user_parametre
            label_user_parametre.config(image=photo_user_parametre)

        button_right.bind("<Button-1>", button_parametre_right)
        
        def button_parametre_save(event):
            photo_user = ImageTk.PhotoImage(
                image=Image.open("Picture/User/User-" + str(user_profil) + ".png").resize((125, 125), Image.LANCZOS)
            )
            label_photo_user.photo_parametre_on = photo_user
            label_photo_user.config(image=photo_user)

            data["user_profil"] = user_profil
            save_data(data)

        button_save.bind("<Button-1>", button_parametre_save)



        Parametre_NC_frame = Frame(content_frame, bg=color_content)
        Parametre_NC_frame.pack(padx=15, pady=45)


        Parametre_name_frame = Frame(Parametre_NC_frame, bg=color_content)
        Parametre_name_frame.pack(side=TOP, anchor=N, pady=15)

        text_label_parametre_name = Label(Parametre_name_frame, text=user_name, font=("Arial", 14), bg="#2a2933", fg="#ffffff", width=19)
        text_label_parametre_name.pack(fill=X, side=LEFT, anchor=W, ipadx=3, ipady=3)

        photo_alea = ImageTk.PhotoImage(
            image=Image.open("Picture/App/Alea.png").resize((30, 30), Image.LANCZOS)
        )
        button_alea = Button(Parametre_name_frame, image=photo_alea, bg=color_content, cursor="hand2", bd=0, highlightthickness=0, highlightbackground="white", activebackground=color_content)
        button_alea.image = photo_alea
        button_alea.pack(ipadx=2, ipady=2, padx=5, side=RIGHT, expand=True, fill=X)

        def button_parametre_alea(event):
            user_name = pseudo()
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
                photo_color_parametre = ImageTk.PhotoImage(
                    image=Image.open("Picture/App/Color-on" + str(i) + ".png").resize((30, 30), Image.LANCZOS)
                )
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
                photo_color_parametre = ImageTk.PhotoImage(
                    image=Image.open("Picture/App/Color-on" + str(i) + ".png").resize((30, 30), Image.LANCZOS)
                )
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

            new_image = ImageTk.PhotoImage(
                image=Image.open("Picture/App/Color-on" + str(color) + ".png").resize((30, 30), Image.LANCZOS)
            )
            button.config(image=new_image)
            button.image = new_image

            for other_button in color_button:
                if other_button != button:  # Évite de changer l'image du bouton cliqué une deuxième fois
                    original_image = ImageTk.PhotoImage(
                        image=Image.open("Picture/App/Color" + str(color_button.index(other_button) + 1) + ".png").resize((30, 30), Image.LANCZOS)
                    )
                    other_button.config(image=original_image)
                    other_button.image = original_image



    def delete_frame_content():
        for widget in content_frame.winfo_children():
            widget.destroy()



    button_parametre.bind("<Button-1>", Frame_parametre)

    win.mainloop()


def closing():
    save_data(data)
    icon.stop()
    win.destroy()


run_icon()
run_mainloop()
