from calendar import c
from this import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import telaInicial as tini

posi = 0
nReq = ''
nProj = ''
nGer = ''
ntes = ''
ncod = ''
nExt = ''

def tela(janela):
    global posi
    fr = Frame(janela, bg="#BA90C6")
    fr.place(relx=0, rely=0, relwidth=1, relheight=1)

    frm_botoes = Frame(fr, bg='#3EB21E',highlightbackground= '#3EB21E',highlightthickness=4)
    frm_botoes.place(relx=0, rely=0, relwidth=1, relheight=0.25)

    frm_caixa = Frame(fr, bg='#6cf5e7',highlightbackground= '#3EB21E',highlightthickness=4)
    frm_caixa.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)
    def caixa1():
        global posi
        def confirmar():
            global nReq, nProj, nGer, nTes, nCod, nExt
            nReq = e_nomeRequisitante.get()
            nProj = e_nomeProjeto.get()
            nGer = e_nomeGerente.get()
            nTes = e_nomeTestador.get()
            nCod = e_nomecodificador.get()
            nExt = e_nomeExtra.get()
            global posi
            for i in frm_caixa.winfo_children():
                i.destroy()
            for i in frm_botoes.winfo_children():
                i.destroy()
            posi = caixa1()
        def voltar():
            global posi
            if(posi == 1):
                posi = 0
                fr.destroy()
                tini.tela(janela)
            else:
                for i in frm_caixa.winfo_children():
                    i.destroy()
                for i in frm_botoes.winfo_children():
                    i.destroy()
                posi -= 2
                posi = caixa1()

        Button(frm_botoes, text="Voltar", command=voltar, width=8, height=5).pack(side = LEFT)
        Button(frm_botoes, text="Avançar", command=confirmar, width=8, height=5).pack(side = RIGHT)
        print(posi)
        if(posi == 0):
            frm_caixa.columnconfigure(2, weight=3)

            frm_caixaParcial1 = Frame(frm_caixa, bg='#6cf5e7',highlightbackground= '#6cf5e7',highlightthickness=4)
            frm_caixaParcial1.grid(row=0,column=1, pady=5, padx=5)

            Label(frm_caixaParcial1, bg='#6cf5e7', text="Nome do Projeto:", font=('Helvetica 10 bold')).pack(anchor=N)
            nomeProjeto = StringVar()
            e_nomeProjeto = Entry(frm_caixaParcial1, textvariable=nomeProjeto)
            e_nomeProjeto.pack(anchor=N)

            ##

            frm_caixaParcial4 = Frame(frm_caixa, bg='#6cf5e7',highlightbackground= '#6cf5e7',highlightthickness=4)
            frm_caixaParcial4.grid(row=1,column=1, pady=5, padx=5)

            Label(frm_caixaParcial4, bg='#6cf5e7', text="Nome do Requisitante:", font=('Helvetica 10 bold')).pack(anchor=N)
            nomeRequisitante = StringVar()
            e_nomeRequisitante = Entry(frm_caixaParcial4, textvariable=nomeRequisitante)
            e_nomeRequisitante.pack(anchor=N)

            ##

            frm_caixaParcial2 = Frame(frm_caixa, bg='#6cf5e7',highlightbackground= '#6cf5e7',highlightthickness=4)
            frm_caixaParcial2.grid(row=0,column=2, pady=5, padx=5)

            Label(frm_caixaParcial2, bg='#6cf5e7', text="Nome do Gerente:", font=('Helvetica 10 bold')).pack(anchor=N)
            nomeGerente = StringVar()
            e_nomeGerente = Entry(frm_caixaParcial2, textvariable=nomeGerente)
            e_nomeGerente.pack(anchor=N)

            ##

            frm_caixaParcial5 = Frame(frm_caixa, bg='#6cf5e7',highlightbackground= '#6cf5e7',highlightthickness=4)
            frm_caixaParcial5.grid(row=1,column=2, pady=5, padx=5)

            Label(frm_caixaParcial5, bg='#6cf5e7', text="Nome do Testador:", font=('Helvetica 10 bold')).pack(anchor=N)
            nomeTestador = StringVar()
            e_nomeTestador = Entry(frm_caixaParcial5, textvariable=nomeTestador)
            e_nomeTestador.pack(anchor=N)

            ##

            frm_caixaParcial3 = Frame(frm_caixa, bg='#6cf5e7',highlightbackground= '#6cf5e7',highlightthickness=4)
            frm_caixaParcial3.grid(row=0,column=3, pady=5, padx=5)

            Label(frm_caixaParcial3, bg='#6cf5e7', text="Nome do codificador:", font=('Helvetica 10 bold')).pack(anchor=N)
            nomecodificador = StringVar()
            e_nomecodificador = Entry(frm_caixaParcial3, textvariable=nomecodificador)
            e_nomecodificador.pack(anchor=N)

            ##

            frm_caixaParcial6 = Frame(frm_caixa, bg='#6cf5e7',highlightbackground= '#6cf5e7',highlightthickness=4)
            frm_caixaParcial6.grid(row=1,column=3, pady=5, padx=5)

            Label(frm_caixaParcial6, bg='#6cf5e7', text="Nome do Extra:", font=('Helvetica 10 bold')).pack(anchor=N)
            nomeExtra = StringVar()
            e_nomeExtra = Entry(frm_caixaParcial6, textvariable=nomeExtra)
            e_nomeExtra.pack(anchor=N)
        
            

            return 1
        elif(posi == 1):
            Label(frm_caixa, bg='#6cf5e7', text="Nome do Extra:", font=('Helvetica 10 bold')).pack()
            return 2
        elif(posi == 2):
            Label(frm_caixa, bg='#6cf5e7', text="Nome do sla:", font=('Helvetica 10 bold')).pack()
            return 3
        else:
            return posi + 1

    posi = caixa1()
    
