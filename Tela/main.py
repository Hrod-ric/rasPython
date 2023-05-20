from calendar import c
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import telaInicial as tini

win_principal = Tk()
win_principal.geometry("750x250")
win_principal.title("Gestão de Teste de Software")
win_principal.configure(background="#CCFF66")

tini.tela(win_principal)

mainloop()