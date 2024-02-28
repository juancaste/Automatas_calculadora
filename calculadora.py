import tkinter as tk
from tkinter import messagebox
from Alfabetos.MenuAlfabetos import operacionAlfabetos
from Cadenas.MenuCadenas import operacionCadenas
from Lenguajes.MenuLenguajes import operacionLenguajes
from colorama import init, Fore, Style

def exit_program():
    if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
        root.destroy()

def open_alfabetos():
    operacionAlfabetos()

def open_cadenas():
    operacionCadenas()

def open_lenguajes():
    operacionLenguajes()

root = tk.Tk()
root.title("Calculadora de Lenguajes Automatas")

init(autoreset=True)  # Iniciar colorama

label = tk.Label(root, text='BIENVENIDOS A NUESTRA CALCULADORA DE LENGUAJES AUTOMATAS', fg="blue")
label.pack()

menu_button = tk.Button(root, text="Mostrar Menú", command=lambda: show_menu(), fg="black", bg="blue")
menu_button.pack()

exit_button = tk.Button(root, text="Salir", command=exit_program, fg="black", bg="red")
exit_button.pack()

def show_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menú de Operaciones")

    label1 = tk.Label(menu_window, text="QUE OPERACION DESEAS REALIZAR?", fg="blue")
    label1.pack()

    button_alfabetos = tk.Button(menu_window, text="OPERACION DE ALFABETOS", command=open_alfabetos, fg="green", bg="black")
    button_alfabetos.pack()

    button_cadenas = tk.Button(menu_window, text="OPERACION DE CADENAS O PALABRAS", command=open_cadenas, fg="green", bg="black")
    button_cadenas.pack()

    button_lenguajes = tk.Button(menu_window, text="OPERACION DE LENGUAJES", command=open_lenguajes, fg="green", bg="black")
    button_lenguajes.pack()

    button_salir = tk.Button(menu_window, text="SALIR", command=exit_program, fg="black", bg="red")
    button_salir.pack()

root.mainloop()


        

        


           

           