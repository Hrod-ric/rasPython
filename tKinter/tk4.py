from cProfile import label
from tkinter import *
from tkinter import ttk

window = Tk()
barra = Menu(window)
a = Menu(barra, tearoff=0)
a.add_command(label='Incluir')
a.add_command(label='Atualizar')
a.add_command(label='Pesquisar')
a.add_separator()
a.add_command(label='Sair', command=window.quit)

t=Menu(a,tearoff=0)
t.add_command(label='Submenu')
barra.add_cascade(label='a',menu=a)

window.config(menu=barra)
mainloop()