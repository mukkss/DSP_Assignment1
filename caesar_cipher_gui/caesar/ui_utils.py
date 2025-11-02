import tkinter as tk
from tkinter import filedialog, messagebox


def ask_open_file(master: tk.Tk) -> str | None:
    path = filedialog.askopenfilename(parent=master, title="Open text file", filetypes=[("Text files", "*.txt"), ("All files", "*")])
    return path or None


def ask_save_file(master: tk.Tk, suggested_name: str = "output.txt") -> str | None:
    path = filedialog.asksaveasfilename(parent=master, title="Save as", defaultextension=".txt", initialfile=suggested_name, filetypes=[("Text files", "*.txt"), ("All files", "*")])
    return path or None


def show_error(master: tk.Tk, title: str, message: str) -> None:
    messagebox.showerror(title, message, parent=master)


def show_info(master: tk.Tk, title: str, message: str) -> None:
    messagebox.showinfo(title, message, parent=master)