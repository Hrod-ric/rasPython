from calendar import c
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win_principal = Tk()
win_principal.geometry("750x250")

#win_telaInicial = ttk.Frame
win_principal.title("Gestão de Teste de Software")
win_principal.configure(background="#CCFF66")



#texto = Label(text=frase)
#caixaTexto.grid(column=0,row=0)
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(win_principal)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()

#.place(relx=0.93,rely=0.94,relwidth=0.07,relheight=0.05)


#t_tipo_conta = StringVar()
#lst_tipo_contas = carrega_tipo_contas()
#cb_tipo_conta = ttk.Combobox(frm_conta, values=lst_tipo_contas, textvaraible=t_tipo_conta,state='reandonly)

#nome = StringVar()
#e_nome = Entry(frm_planoteste, textvariable=nome)

#def pri():
#    print(nome.get())

#Button(win_principal, text='mostrar', command=pri).pack(side=BOTTOM)

#e_nome.place(relx=0.5, rely=0.5, anchor=CENTER)


#def visualiza():
#    pass


mainloop()