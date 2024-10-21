import tkinter as tk
import sys
import os


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller. """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = tk.Tk()
icon_path = resource_path('logo.ico')

try:
    root.wm_iconbitmap(icon_path)
except Exception as e:
    print(f"Error setting icon: {e}")

root.mainloop()
