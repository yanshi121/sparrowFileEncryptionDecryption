import tkinter as tk
from tkinter import messagebox


class Tools(object):
    @staticmethod
    def show_message_box(title, message):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(title, message)
