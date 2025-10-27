import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox

from PIL.Image import Image
import os

import converter
from utils import resource_path



def open_png(betaflight:bool):
    filetypes = (
        ('PNG image file', '*.png'),
        ('All files', '*.*')
    )

    filepath = fd.askopenfilename(
        title="Open a file", filetypes=filetypes
    )

    if filepath == "":
        return

    if betaflight:
        img = converter.open_betaflight_png(filepath)
    else:
        img = converter.open_normal_png(filepath)

    if img == -1:
        return

    filename = os.path.splitext(os.path.basename(filepath))[0]
    savepath = os.path.join(os.path.dirname(filepath), filename+".mcm")

    result = converter.convert(img, savepath)
    if result == -1:
        return

    messagebox.showinfo("Succes", f"File succesfully converted! You can find it in the same folder as the source file ({os.path.dirname(filepath)})")


root = tk.Tk()
root.title("png2mcm")
root.geometry("600x400")
root.minsize(600, 400)

icon = tk.PhotoImage(file=resource_path("assets/icon.png"))
root.iconphoto(False, icon)

##betaflight
frame_betaflight = tk.Frame(root)

open_betaflight_png_btn = tk.Button(frame_betaflight, text="Open a Betaflight font .png", command=lambda: open_png(True))
open_betaflight_png_btn.pack(expand=True)

betaflight_label = tk.Label(frame_betaflight, text="Example of a betaflight-style font .png: ")
betaflight_label.pack()

betaflight_example = tk.PhotoImage(file=resource_path("assets/betaflight_example.png"))
betaflight_example_img = tk.Label(frame_betaflight, image=betaflight_example)
betaflight_example_img.pack(expand=True)

frame_betaflight.pack(side=tk.LEFT, expand=True)

##normal
frame_normal = tk.Frame(root)

open_normal_png_btn = tk.Button(frame_normal, text="Open a normal font .png", command=lambda: open_png(False))
open_normal_png_btn.pack(expand=True)

normal_label = tk.Label(frame_normal, text="Example of a normal font .png: ")
normal_label.pack()

normal_example = tk.PhotoImage(file=resource_path("assets/normal_example.png"))
normal_example_img = tk.Label(frame_normal, image=normal_example)
normal_example_img.pack(expand=True)

frame_normal.pack(side=tk.RIGHT, expand=True)

root.mainloop()
