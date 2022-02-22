import tkinter as tk
from Persona import Persona
import pickle


def insertData(list, Tdni, Tnom):
    Tdni.configure(state='normal')
    Tnom.configure(state='normal')
    for i in list:
        Tdni.insert(tk.END, i.dni + "\n")
        Tnom.insert(tk.END, i.nombre + "\n")
    Tdni.configure(state='disabled')
    Tnom.configure(state='disabled')


def deleteData(Tdni, Tnom):
    Tdni.configure(state='normal')
    Tnom.configure(state='normal')
    Tdni.delete("1.0", "end")
    Tnom.delete("1.0", "end")
    Tdni.configure(state='disabled')
    Tnom.configure(state='disabled')


def borrar(txtDNI, list, Tdni, Tnom):
    for i in list:
        if i.dni == txtDNI.get():
            list.remove(i)
    deleteData(Tdni, Tnom)
    insertData(list, Tdni, Tnom)


def anadir(txtDNI, txtNom, list, Tdni, Tnom):
    if txtDNI.get() != "":
        if txtNom.get() != "":
            a = txtDNI.get()
            b = txtNom.get()
            anadir = True
            for i in list:
                if i.dni == a:
                    anadir = False

            if anadir is True:
                list.append(Persona(a, b))
                deleteData(Tdni, Tnom)
                insertData(list, Tdni, Tnom)


def listar(lista, Tdni, Tnom):
    with open("Persona.pickle", "rb") as f:
        lista = pickle.load(f)
    deleteData(Tdni, Tnom)
    insertData(lista, Tdni, Tnom)


def modificar(txtDNI, txtNom, list, Tdni, Tnom):
    if txtDNI.get() != "":
        if txtNom.get() != "":
            a = txtDNI.get()
            b = txtNom.get()
            anadir = False
            for i in list:
                if i.dni == a:
                    anadir = True

            if anadir is True:
                list.remove(i)
                list.append(Persona(a, b))
                deleteData(Tdni, Tnom)
                insertData(list, Tdni, Tnom)


def exportar(lista):
    with open("Persona.pickle", "wb") as f:
        pickle.dump(lista, f)


listaPersonas = []

root = tk.Tk()
root.state("zoomed")

tk.Label(root, text="Nombre").grid(row=0, column=1)
tk.Label(root, text="DNI").grid(row=0, column=0)
tk.Label(root, text="Nombre:").grid(row=1, column=2)
tk.Label(root, text="DNI:").grid(row=0, column=2)
txtDNI = tk.StringVar()
txtNom = tk.StringVar()
tk.Entry(root, textvariable=txtDNI).grid(row=0, column=3)
tk.Entry(root, textvariable=txtNom).grid(row=1, column=3)

tk.Button(root, text="Listar", command=lambda: listar(listaPersonas, Tdni, Tnom)).grid(row=3, column=0)
tk.Button(root, text="Añadir", command=lambda: anadir(txtDNI, txtNom, listaPersonas, Tdni, Tnom)).grid(row=3, column=1)
tk.Button(root, text="Borrar", command=lambda: borrar(txtDNI, listaPersonas, Tdni, Tnom)).grid(row=3, column=2)
tk.Button(root, text="Modificar", command=lambda: modificar(txtDNI, txtNom, listaPersonas, Tdni, Tnom)).grid(row=3,column=3)
tk.Button(root, text="Exportar", command=lambda: exportar(listaPersonas)).grid(row=3, column=4)

Tdni = tk.Text(root, height=40, width=50)
Tnom = tk.Text(root, height=40, width=50)

Tdni.grid(row=1, column=0)
Tnom.grid(row=1, column=1)

insertData(listaPersonas, Tdni, Tnom)

tk.mainloop()
