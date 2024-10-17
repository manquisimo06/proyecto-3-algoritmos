import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter as  messagebox
import re
main_window=tk.Tk()
main_window.config(width=900, height=950)
mostrar=ttk.Combobox().place(x=50, y=150, width=600, height=25)
texto1=tk.Text().place(x=50, y=200,width=600, height=700)
ttk.Style.configure.pading=20
boton_salida=ttk.Button(text="Salir", command=main_window.destroy).place(x=700, y=600, width=150,height=75)
boton_guardar=ttk.Button(text="Guardar").place(x=700, y=700, width=150,height=75)
boton_guardar_como=ttk.Button(text="Guardar como").place(x=700, y=800, width=150,height=75)
boton_buscar=ttk.Button(text="Buscar").place(x=700, y=140, width=150,height=40)
def abrir_texto():
    filetypes=(
        ('text file','*.txt'),
        ('all file', '*.*')
    )
    f=fd.askopenfile(filetypes=filetypes)
    texto1.insert('1.0',f.readlines())
boton_abrir=ttk.Button(main_window,text="Abrir", command=abrir_texto).place(x=700, y=200, width=150,height=40)
#imagen_logo =tk.Image(open('C:\Users\Oficina\Desktop\proyecto3\logo2.png'))
#ttk.Label( imagen=imagen_logo).pack()

main_window.mainloop()