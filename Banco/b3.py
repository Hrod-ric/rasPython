import sqlite3
con = sqlite3.connect(database="./Banco/disco.db")
cur = con.cursor()

data=cur.execute('''SELECT * FROM alunos''')
print(data.description)

def criarTabela(nomeTabela, lista):
    estrutura = ''
    for campo in lista:
        estrutura += campo[0], campo[1], campo[2], campo[3] + ','
        if campo[4] == 'PK':
            chavePrimaria = campo[0]

    campoRevisado = estrutura, 'PRIMARY KEY(' + chavePrimaria + ')'

    sql = f'''CREATE TABLE {nomeTabela}({campoRevisado})'''
    cur.execute(sql)

campos = [
    ['matricula', 'INTEGER', 5, 'NOT NULL', 'PK'],
    ['nome', 'VARCHAR', 100, 'NOT NULL', ""]
]
criarTabela('alunos', campos)