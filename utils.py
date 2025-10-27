import os, sys
from tkinter import messagebox

#when assets aren't loaded with this, they will not be found in the builded version.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def showerror(message:str):
    messagebox.showerror("Error", str(message))
