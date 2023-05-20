import random
import sqlite3
con = sqlite3.connect("./Banco/dismo.db")
cur = con.cursor()

def criar(table, campos):
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {table}({campos})""")
    con.commit()

def retirar(table, primaryKey, parametro):
    try:
        cur.execute(f"""DELETE FROM {table} where {primaryKey} == {parametro}""")
    except:
        print("isso simplesmente não é possivel!")
    con.commit()

def consulta(tabela):
    dados = cur.execute(f'SELECT "matricula", "nome" FROM {tabela} ORDER BY matricula ASC')
    babaouei = dados.fetchall()
    for i in babaouei:
        print("Matricula:", i[0], "Nome", i[1])

def inserir(tabela, campos):
    try:
        cur.execute(f"""INSERT INTO {tabela} VALUES {campos}""")
    except:
        print("isso simplesmente não é possivel!")
    con.commit()

def alterar(tabela, chavePrimaria, valor):
    try:
        cur.execute(f"""UPDATE {tabela} SET "nome" = "{valor}" where "matricula" == {chavePrimaria}""")
    except:
        print("isso simplesmente não é possivel!")
    con.commit()

teste1 = """
"matricula"	integer NOT NULL UNIQUE,
"nome"	text NOT NULL,
PRIMARY KEY("matricula")
"""
criar('jair',teste1)

Professor = { 
1:{ "nome": "matricula", "tipo": "INTEGER", "obrigatorio":True, "PK":True },
2:{ "nome": "nome", "tipo": "TEXT", "obrigatorio":True, "PK":False },
}

#inserir('jair', '(7,"Jorge")')
alterar('jair', 1, 'Mendes')
consulta('jair')
