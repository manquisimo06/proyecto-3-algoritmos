import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter as  messagebox
import re
main_window=tk.Tk()
main_window.config(width=900, height=950)
logo_umg=tk.PhotoImage(file="logo2.png")
lavel=ttk.Label(image=logo_umg).place(x=50, y=50, width=250, height=251)
menu_formuario=tk.Menu()
opciones_menu=tk.Menu(menu_formuario, tearoff=False)
opciones_menu.add_command(
    label="Abrir",
    accelerator="Ctrl+O"
)
opciones_menu.add_command(
    label="Guardar",
    accelerator="Ctrl+G"
)
opciones_menu.add_command(
    label="Guardar como",
    accelerator="Alt+F,A"
)
opciones_menu.add_command(
    label="Buscar",
    accelerator="Ctrl+B"
)
menu_formuario.add_cascade(menu=opciones_menu, label="Archivo")
editar_menu=tk.Menu(menu_formuario, tearoff=False)
editar_menu.add_command(
    label="Deshcer",
    accelerator="Ctrl+Z"
)
editar_menu.add_command(
    label="Rehacer",
    accelerator="Ctrl+Y"
)
menu_formuario.add_cascade(menu=editar_menu, label="Editar")
ayuda_menu=tk.Menu(menu_formuario, tearoff=False)
ayuda_menu.add_command(
    label="Informacion"
)
ayuda_menu.add_command(
    label="Manuel de usuario"
)
ayuda_menu.add_command(
    label="Integrantes"
)
menu_formuario.add_cascade(menu=ayuda_menu, label="Ayuda")
mostrar=ttk.Combobox().place(x=50, y=150, width=600, height=25)
texto1=tk.Text().place(x=50, y=200,width=600, height=700)
ttk.Style.configure.pading=20
boton_salida=ttk.Button(text="Salir", command=main_window.destroy).place(x=700, y=600, width=150,height=75)
boton_guardar=ttk.Button(text="Guardar").place(x=700, y=700, width=150,height=75)
boton_deshacer=ttk.Button(text="deshacer").place(x=700, y=500,width=150,height=75)
boton_guardar_como=ttk.Button(text="Guardar como").place(x=700, y=800, width=150,height=75)
boton_buscar=ttk.Button(text="Buscar").place(x=700, y=140, width=150,height=40)
def abrir_texto():
    filetypes=(
        ('text file','*.txt'),
        ('all file', '*.*')
    )
    f=fd.askopenfile(filetypes=filetypes)
    extraccion_de_texto=tk.Text.insert('1.0',f.readlines())
boton_abrir=ttk.Button(main_window,text="Abrir", command=abrir_texto).place(x=700, y=200, width=150,height=40)
main_window.config(menu=menu_formuario)
main_window.mainloop()