from tkinter import *
from tkinter import ttk
from PIL import Image
import pystray
import webbrowser
import threading


def run_icon():
    image = Image.open("logo.png")

    def after_click(icon, item):
        if item == "Github":
            webbrowser.open("https://github.com/xen0r-star/StartProject")
        elif item == "Exit":
            icon.stop()
            win.destroy

    icon = pystray.Icon("GFG", image, "StartProject",
                    menu=pystray.Menu(
    pystray.MenuItem("Github", after_click),
    pystray.MenuItem("Exit", after_click)))
    icon.run()




def run_mainloop():
    win = Tk()
    win.title("StartProject")
    win.iconbitmap("logo.ico")
    win.geometry("500x500")
    win.overrideredirect(1)
    win.taskbar_icon("logo.ico")
    win.iconbitmap("logo.ico")

    def start_drag(e):
        win.x = e.x
        win.y = e.y

    def drag_app(e):
        deltax = e.x - win.x
        deltay = e.y - win.y
        win.geometry(f"+{win.winfo_x() + deltax}+{win.winfo_y() + deltay}")

    title_bar = Frame(win, bg="#15131a", bd=1)
    title_bar.pack(fill=X)
    title_bar.bind("<ButtonPress-1>", start_drag)
    title_bar.bind("<B1-Motion>", drag_app)

    close_button = Button(title_bar, text="X", bg="#15131a", fg="white", bd=0, command=win.destroy, cursor="hand2")
    close_button.pack(side=RIGHT, padx=5)

    content_frame = Frame(win, bg="#363245")
    content_frame.pack(expand=1, fill=BOTH)

    win.mainloop()



# Créez et démarrez les threads
icon_thread = threading.Thread(target=run_icon)
icon_thread.start()

mainloop_thread = threading.Thread(target=run_mainloop)
mainloop_thread.start()




# frm = ttk.Frame(win)
# frm.grid()

# style = ttk.Style()
# style.configure("BW.TLabel", foreground="black", background="white")
# l1 = ttk.Label(frm, text="Test", style="BW.TLabel").grid(column=0, row=0)
# l2 = ttk.Label(frm, text="Test", style="BW.TLabel").grid(column=1, row=0)

# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

# button_color = ttk.Button(frm, text="Change")
# button_color.grid(column=0, row=1)

# Image de <a href="https://fr.freepik.com/vecteurs-libre/fond-fusee-dans-style-plat_2838939.htm#query=fusee&position=0&from_view=keyword&track=sph">Freepik</a>