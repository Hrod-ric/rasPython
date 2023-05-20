from calendar import c
from this import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import telaCriar as tcri

def tela(janela):
    frm = Frame(janela, bg="#CCFF66")
    frm.place(relx=0, rely=0, relwidth=1, relheight=1)

    frm_planoteste = Frame(frm, bg='#6cf5e7',highlightbackground= '#3EB21E',highlightthickness=4)
    frm_planoteste.place(relx=0.01, rely=0.01, relwidth=0.30, relheight=0.55)

    frm_lista_planoteste = Frame(frm, bg='#DFE3EE', highlightbackground='#3eb21e', highlightthickness=4)
    frm_lista_planoteste.place(relx=0.32,rely=0.01,relwidth=0.67,relheight=0.55)

    texto = ""
    caixaTexto = Text(frm_lista_planoteste)
    caixaTexto.pack(fill=BOTH)
    caixaTexto.insert(INSERT, texto)

    #telaCriar(janela)


    #frm_lista_planoteste.update()
    def textoFerramenta():
        caixaTexto.delete('1.0', END)
        texto = "Texto referente a Ferramenta"
        caixaTexto.insert(INSERT, texto)
    def textoBanco():
        caixaTexto.delete('1.0', END)
        texto = "Informações do Banco"
        caixaTexto.insert(INSERT, texto)
    Button(frm_planoteste, text="Ferramenta", command=textoFerramenta, width=15, height=1).pack(side = TOP)
    Button(frm_planoteste, text="Banco", command=textoBanco, width=15, height=1).pack(side = BOTTOM)
    #Button(frm_planoteste, text="c", command=None, width=3, height=10).pack(side = LEFT)
    #Button(frm_planoteste, text="d", command=None, width=3, height=10).pack(side = RIGHT)
    ttk.Button(frm, text="Novo Projeto", command=lambda: [frm.destroy(),tcri.tela(janela)]).pack(side=LEFT, anchor=S)
    ttk.Button(frm, text="Fechar", command=janela.destroy).pack(side=RIGHT, anchor=S)