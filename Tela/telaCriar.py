from calendar import c
from this import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import telaInicial as tini
from cProfile import label


posi = 0
rest = ''
prem = ''
def tela(janela):
    global posi
    nProj = ''
    nReq = ''
    nGer = ''
    nTes = ''
    nCod = ''
    fr = Frame(janela, bg="#BA90C6")
    fr.place(relx=0, rely=0, relwidth=1, relheight=1)

    frm_caixa = Frame(fr, bg='#6cf5e7',highlightbackground= '#3EB21E',highlightthickness=4)
    frm_caixa.place(relx=0, rely=0, relwidth=1, relheight=1)

    def voltar():
        for i in janela.winfo_children():
            i.destroy()
        tini.tela(janela)

    frm_caixa.columnconfigure(2, weight=3)
    nomeProjeto = StringVar()
    nomeRequisitante = StringVar()
    nomeGerente = StringVar()
    nomeTestador = StringVar()
    nomeCodificador = StringVar()
        
    def equipe():
        conf()

        try:
            conf2()
        except:
            pass
        try:
            conf3()
        except:
            pass

        for i in frm_caixa.winfo_children():
            i.destroy()
        frm_caixaParcial1 = Frame(frm_caixa, bg='#6cf5e7',highlightbackground= '#6cf5e7',highlightthickness=4)
        frm_caixaParcial1.grid(row=0,column=0, pady=5, padx=5)

        Label(frm_caixaParcial1, bg='#6cf5e7', text="Nome do Requisitante:", font=('Helvetica 10 bold')).pack(anchor=N)
        e_nomeRequisitante = Entry(frm_caixaParcial1, textvariable=nomeRequisitante)
        e_nomeRequisitante.insert(0,nReq)
        e_nomeRequisitante.pack(anchor=N)

        ##

        frm_caixaParcial2 = Frame(frm_caixa, bg='#6cf5e7',highlightbackground= '#6cf5e7',highlightthickness=4)
        frm_caixaParcial2.grid(row=0,column=1, pady=5, padx=5)

        Label(frm_caixaParcial2, bg='#6cf5e7', text="Nome do Gerente:", font=('Helvetica 10 bold')).pack(anchor=N)
        e_nomeGerente = Entry(frm_caixaParcial2, textvariable=nomeGerente)
        e_nomeGerente.insert(0,nGer)
        e_nomeGerente.pack(anchor=N)

        ##

        frm_caixaParcial4 = Frame(frm_caixa, bg='#6cf5e7',highlightbackground= '#6cf5e7',highlightthickness=4)
        frm_caixaParcial4.grid(row=1,column=0, pady=5, padx=5)

        Label(frm_caixaParcial4, bg='#6cf5e7', text="Nome do Testador:", font=('Helvetica 10 bold')).pack(anchor=N)
        e_nomeTestador = Entry(frm_caixaParcial4, textvariable=nomeTestador)
        e_nomeTestador.insert(0,nTes)
        e_nomeTestador.pack(anchor=N)

        ##

        frm_caixaParcial5 = Frame(frm_caixa, bg='#6cf5e7',highlightbackground= '#6cf5e7',highlightthickness=4)
        frm_caixaParcial5.grid(row=1,column=1, pady=5, padx=5)

        Label(frm_caixaParcial5, bg='#6cf5e7', text="Nome do codificador:", font=('Helvetica 10 bold')).pack(anchor=N)
        e_nomeCodificador = Entry(frm_caixaParcial5, textvariable=nomeCodificador)
        e_nomeCodificador.insert(0,nCod)
        e_nomeCodificador.pack(anchor=N)
    def restricoes():
        conf()

        try:
            conf2()
        except:
            pass
        try:
            conf3()
        except:
            pass

        for i in frm_caixa.winfo_children():
            i.destroy()

        frm_desc = Frame(frm_caixa, bg='#3EB21E',highlightbackground= '#3EB21E',highlightthickness=4)
        frm_desc.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        Label(frm_desc, bg='#3EB21E', text="Descreva as suposições, fatores considerados verdadeiros para fins de planejamento do projeto de teste!", font=('Helvetica 10 bold')).pack(anchor=N)

        frm_caixaTexto = Frame(frm_caixa, bg='#3EB21E',highlightbackground= '#3EB21E',highlightthickness=4)
        frm_caixaTexto.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)

        global caixaTextoRest
        caixaTextoRest = Text(frm_caixaTexto)
        caixaTextoRest.pack(fill=BOTH)
        caixaTextoRest.insert(INSERT, rest)
    def premissas():
        conf()

        try:
            conf2()
        except:
            pass
        try:
            conf3()
        except:
            pass

        for i in frm_caixa.winfo_children():
            i.destroy()

        frm_desc = Frame(frm_caixa, bg='#3EB21E',highlightbackground= '#3EB21E',highlightthickness=4)
        frm_desc.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        Label(frm_desc, bg='#3EB21E', text="Descreva fatores limitadores do projeto!", font=('Helvetica 10 bold')).pack(anchor=N)

        frm_caixaTexto = Frame(frm_caixa, bg='#3EB21E',highlightbackground= '#3EB21E',highlightthickness=4)
        frm_caixaTexto.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)

        #Label(frm_caixa, bg='#6cf5e7', text="Premissas:", font=('Helvetica 10 bold')).pack(anchor=N)
        global caixaTextoPrem
        caixaTextoPrem = Text(frm_caixaTexto)
        caixaTextoPrem.pack(fill=BOTH)
        caixaTextoPrem.insert(INSERT, prem)
    def conf():
        global nReq, nGer, nTes, nCod, nProj
        nProj = nomeProjeto.get()
        nReq = nomeRequisitante.get()
        nGer = nomeGerente.get()
        nTes = nomeTestador.get()
        nCod = nomeCodificador.get()

    def conf2():
        global rest
        rest = caixaTextoRest.get('1.0','end-1c')

    def conf3():
        global prem
        prem = caixaTextoPrem.get("1.0",'end-1c')

    def projeto():
        conf()
        try:
            conf2()
        except:
            pass
        try:
            conf3()
        except:
            pass

        for i in frm_caixa.winfo_children():
            i.destroy()
        frm_caixaParcial1 = Frame(frm_caixa, bg='#6cf5e7',highlightbackground= '#6cf5e7',highlightthickness=4)
        frm_caixaParcial1.grid(row=0,column=0, pady=5, padx=5)

        Label(frm_caixaParcial1, bg='#6cf5e7', text="Nome do Projeto:", font=('Helvetica 10 bold')).pack(anchor=N)
        e_nomeProjeto = Entry(frm_caixaParcial1, textvariable=nomeProjeto)
        e_nomeProjeto.insert(0,nProj)
        e_nomeProjeto.pack(anchor=N)

    barra = Menu(janela)
    janela.config(menu=barra)
    barra.add_cascade(label='Voltar',command=voltar)
    barra.add_cascade(label='Projeto',command=projeto)
    barra.add_cascade(label='Equipe',command=equipe)
    barra.add_cascade(label='Premissas',command=premissas)
    barra.add_cascade(label='Restricoes',command=restricoes)
