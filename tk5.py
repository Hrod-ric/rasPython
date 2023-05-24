from calendar import c
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import sqlite3
con = sqlite3.connect("./Banco/disc.db")
cur = con.cursor()

win_principal = Tk()
win_principal.geometry("750x250")
win_principal.title("CRUD")
win_principal.configure(background="#CCFF66")

frm_caixa = Frame(win_principal, bg='#3EB21E')
frm_caixa.place(relx=0, rely=0, relwidth=1, relheight=0.25)

frm_botoes = Frame(win_principal, bg='#6cf5e7')
frm_botoes.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

titulo = Label(frm_caixa, bg='#3EB21E', text="Tabela", font=('Helvetica 10 bold')).pack(anchor=NW)
subTitulo = Label(frm_caixa, bg='#3EB21E', text="Qualquer uma", font=('Helvetica 10 bold')).pack(anchor=NW)

def visualizar():
    telaVisi = Tk()
    telaVisi.geometry("350x550")
    telaVisi.title("Visi")
    telaVisi.configure(background="#CCFF66")

    dados = cur.execute(f'SELECT "id_Professor", "nome", "CPF" FROM professor ORDER BY id_Professor ASC')
    babaouei = dados.fetchall()
    for i in babaouei:
        Label(telaVisi, bg='#CCFF66', text=f"RA:{i[0]}\tNome: {i[1]}\tCPF: {i[2]}", font=('Helvetica 10 bold')).pack(anchor=W)

def criar():
    telaCriar = Tk()
    telaCriar.geometry("225x75")
    telaCriar.title("Criar")
    telaCriar.configure(background="#CCFF66")
    telaCriar.resizable(width=False,height=False)

    telaCriar.columnconfigure(2, weight=3)

    #

    frm_caixa1 = Frame(telaCriar, bg='#CCFF66')
    frm_caixa1.grid(row=0,column=0, pady=5, padx=5)

    chave = 10000
    aus = cur.execute(f'SELECT "id_Professor" FROM professor ORDER BY id_Professor ASC')
    aust = aus.fetchall()
    chaves = []
    for i in aust:
        chaves += i
    while chave in chaves:
        chave = random.randrange(10000, 99999)
    cpf = 1
    aus = cur.execute(f'SELECT "CPF" FROM professor ORDER BY "CPF" ASC')
    aust = aus.fetchall()
    cpfs = []
    for i in aust:
        cpfs += i
    while cpf in cpfs:
        cpf = random.randrange(1, 99)

    Label(frm_caixa1, bg='#CCFF66', text=f"id_Professor: {chave}", font=('Helvetica 10 bold')).pack(anchor=NW)

    Label(frm_caixa1, bg='#CCFF66', text="Nome:", font=('Helvetica 10 bold')).pack(anchor=NW)
    nome = StringVar()
    e_nome = Entry(frm_caixa1, textvariable=nome)
    e_nome.pack(anchor=NW)
    

    frm_caixa2 = Frame(telaCriar, bg='#CCFF66')
    frm_caixa2.grid(row=0,column=1, pady=0, padx=5)

    
    def inserir():
        nome = e_nome.get()
        if(nome == ''):
            return
        campos = f"{chave},'{nome}','{cpf}'"
        try:
            cur.execute(f"""INSERT INTO professor VALUES ({campos})""")
        except:
            print("isso simplesmente não é possivel!")
        con.commit()
        telaCriar.destroy()

    Button(frm_caixa2, text="Confirmar", command=inserir, width=9, height=1).pack()
    

def editar():
    telaEditar = Tk()
    telaEditar.geometry("200x100")
    telaEditar.title("Remover")
    telaEditar.configure(background="#CCFF66")
    telaEditar.resizable(width=False,height=False)
    telaEditar.columnconfigure(2, weight=3)

    frm_caixa1 = Frame(telaEditar, bg='#CCFF66')
    frm_caixa1.grid(row=0,column=0, pady=5, padx=5)

    frm_caixa2 = Frame(telaEditar, bg='#CCFF66')
    frm_caixa2.grid(row=0,column=1, pady=5, padx=5)

    Label(frm_caixa1, bg='#CCFF66', text=f"id_Professor:", font=('Helvetica 10 bold')).pack(anchor=NW)
    id_Professor = StringVar()
    e_id_Professor = Entry(frm_caixa1, textvariable=id_Professor)
    e_id_Professor.pack(anchor=NW)

    def consultar():
        id_Professor = e_id_Professor.get()
        if(id_Professor == ''):
            return
        try:
            res = cur.execute(f"""SELECT * FROM professor WHERE id_Professor = '{id_Professor}'""")
            res = res.fetchall()
            nome = res[0][1]
            print(res)
            for i in frm_caixa1.winfo_children():
                i.destroy()
            Label(frm_caixa1, bg='#CCFF66', text=f"Nome Antigo: {nome}", font=('Helvetica 10 bold')).pack(anchor=NW)
            Label(frm_caixa1, bg='#CCFF66', text=f"Digite o novo nome", font=('Helvetica 10 bold')).pack(anchor=NW)
            nome = StringVar()
            e_nome = Entry(frm_caixa1, textvariable=id_Professor)
            e_nome.pack(anchor=NW)

            def alterar():
                nome = e_nome.get()
                cur.execute(f"""UPDATE professor SET "nome" = "{nome}" where "id_Professor" == {id_Professor}""")
                con.commit()
            Button(frm_caixa1, text="Alterar", command=lambda:[alterar(),telaEditar.destroy()], width=9, height=1).pack(pady=5)
        except:
            print("isso simplesmente não é possivel!")

    Button(frm_caixa1, text="Consultar", command=consultar, width=9, height=1).pack(pady=5)

def remover():
    telaRemover = Tk()
    telaRemover.geometry("150x100")
    telaRemover.title("Remover")
    telaRemover.configure(background="#CCFF66")
    telaRemover.resizable(width=False,height=False)
    telaRemover.columnconfigure(2, weight=3)

    frm_caixa1 = Frame(telaRemover, bg='#CCFF66')
    frm_caixa1.grid(row=0,column=0, pady=5, padx=5)
    Label(frm_caixa1, bg='#CCFF66', text=f"id_Professor:", font=('Helvetica 10 bold')).pack(anchor=NW)
    id_Professor = StringVar()
    e_id_Professor = Entry(frm_caixa1, textvariable=id_Professor)
    e_id_Professor.pack(anchor=NW)

    def consultar():
        id_Professor = e_id_Professor.get()
        if(id_Professor == ''):
            return
        try:
            res = cur.execute(f"""SELECT * FROM professor WHERE id_Professor = '{id_Professor}'""")
            res = res.fetchall()
            mat = res[0][0]
            nome = res[0][1]
            print(res)
            for i in frm_caixa1.winfo_children():
                i.destroy()
            id_Professor = Label(frm_caixa1, bg='#CCFF66', text=f"id_Professor: {mat}", font=('Helvetica 10 bold')).pack(anchor=NW)
            nome = Label(frm_caixa1, bg='#CCFF66', text=f"Nome: {nome}", font=('Helvetica 10 bold')).pack(anchor=NW)
            def remover():
                    try:
                        cur.execute(f"""DELETE FROM professor where id_Professor == {mat}""")
                    except:
                        print("isso simplesmente não é possivel!")
                    con.commit()
            Button(frm_caixa1, text="Remover", command=lambda:[remover(),telaRemover.destroy()], width=9, height=1).pack(pady=5)
        except:
            print("isso simplesmente não é possivel!")

    Button(frm_caixa1, text="Consultar", command=consultar, width=9, height=1).pack(pady=5)


Button(frm_caixa, text="Visualizar", command=visualizar, width=8, height=5).pack(anchor=NW)

frm_botoes.columnconfigure(1, weight=3)

Button(frm_botoes, text="Criar", command=criar, width=8, height=5).grid(row=0,column=0, pady=5, padx=5)
Button(frm_botoes, text="Editar", command=editar, width=8, height=5).grid(row=0,column=1, pady=5, padx=5)
Button(frm_botoes, text="Remover", command=remover, width=8, height=5).grid(row=0,column=2, pady=5, padx=5)
mainloop()