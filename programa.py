import tkinter as tk
from tkinter import messagebox
from tkinter import *

root = tk.Tk()

root.geometry("1980x1080")

root.title("Si")


elemento= Label(root, text ="Number One")
elemento.pack()

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "Eminem")
    
elemento = tk.Button(root, command=mostrar_mensaje)
elemento.pack()

elemento=Button(
    root,
    text ="The Goat",
    fg="darkorange",
    bg="lightgreen",
    font=("Arial", 22),
    width=20,
    height=5,
    padx=10,
    pady=10,
    anchor="center",
    relief="raised",
    borderwidth=5,
    cursor="hand2"
    )
elemento.pack()

root.mainloop() 