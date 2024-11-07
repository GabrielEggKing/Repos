import tkinter as tk
from tkinter import *

ventana = tk.Tk()

ventana.title("Soy un título")

ventana.geometry("800x600")

menu_bar = Menu(ventana)
ventana.config(menu=menu_bar)
archivo_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Archivo", menu=menu_bar)


ventana.mainloop()
