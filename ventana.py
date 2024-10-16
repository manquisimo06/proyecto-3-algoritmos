from tkinter import ttk
import tkinter as tk
import tkinter as  messagebox
import sys
main_window=tk.Tk()
main_window.config(width=300, height=200)
mostrar=ttk.Combobox().place(x=50, y=50)
ttk.Entry().place(x=50, y=100,width=100, height=100)
ttk.Style.configure.pading=20
main_window.mainloop()