from data_app.data_json import load_info

info = load_info()
color_menu = info["color_menu"]
color_content = info["color_content"]

def delete_frame_content(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

def color_selection(liste_button, project):
    for button in liste_button:
        if button["text"] == project:
            button["bg"] = color_content
        else:
            button["bg"] = color_menu