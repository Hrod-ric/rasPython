import sqlite3
con = sqlite3.connect(database="./Banco/disco.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS professores(
    "matricula"	integer NOT NULL UNIQUE,
    "nome"	text NOT NULL,
    PRIMARY KEY("matricula")
)""")
cur.execute("""
CREATE TABLE IF NOT EXISTS "alunos" (
    "matricula"	integer NOT NULL UNIQUE,
    "nome"	text NOT NULL,
    PRIMARY KEY("matricula")
)""")
cur.execute("""
CREATE TABLE IF NOT EXISTS "disciplinas" (
	"codigo"	text NOT NULL UNIQUE,
	"nome"	text NOT NULL,
	PRIMARY KEY("codigo"),
)""")

cur.execute("""
CREATE TABLE IF NOT EXISTS "prof_disc" (
	"prof_id"	integer NOT NULL,
	"disc_id"	text NOT NULL,
	PRIMARY KEY("prof_id","disc_id"),
	FOREIGN KEY("disc_id") REFERENCES "disciplinas"("codigo"),
	FOREIGN KEY("prof_id") REFERENCES "professores"("matricula")
)""")
cur.execute("""
CREATE TABLE IF NOT EXISTS "notas" (
	"disc_id"	text NOT NULL,
	"aluno_id"	integer NOT NULL,
	"nota"	real NOT NULL CHECK("nota" < 10),
	PRIMARY KEY("aluno_id","disc_id"),
	FOREIGN KEY("aluno_id") REFERENCES "alunos"("aluno_id"),
	FOREIGN KEY("disc_id") REFERENCES "disciplinas"("disc_id"),
	UNIQUE("aluno_id","disc_id")
)""")

#cur.execute('drop table notas')

cur.execute("""
INSERT INTO professores VALUES
    (12345, 'Manoel de Castro Almeida'),
    (52452, 'Ana Maria da Conceição'),
    (51421, 'Carlos Augusto')
""")
cur.execute("""
INSERT INTO disciplinas VALUES
    ('BD001', 'Banco de Dados I'),
    ('DS001', 'Des. de Sistemas I'),
    ('LP001', 'Lógica de Programação')
""")
cur.execute("""
INSERT INTO alunos VALUES
    (10001, 'Joaquim José da Silva Xavier'),
    (10002, 'Maria Paula de Souza'),
    (10003, 'Camila Machado Andrade')
""")
cur.execute("""
INSERT INTO notas VALUES
(12345,'BD001', 0.0),
(51421, 'DS001', 0.0),
(52452, 'LP001', 0.0)
""")
cur.execute("""
INSERT INTO notas VALUES
    ('BD001',1,0.0),
    ('BD001',3,0.0),
    ('DS001',2,0.0),
    ('LP001',1,0.0),
    ('LP001',3,0.0)
""")

con.commit()

res = cur.execute("SELECT * FROM professores")
res.fetchall()

#title, year = res.fetchone()
#data = [(10004,"Bruno"),(10005,"Lucas"),(10006,"Brian")]
#"INSERT INTO alunos VALUES(?, ?)", data
#'DELETE FROM table where column == column AND column == column')
#dic_prof_disciplina = {12345: ['BD001','DS001'],  12344: ['DS001','BD001', 'LP001'],  12333:[ 'LP001']}
#dic_notas = {'BD001': {1: [10.0, 8.8],2: [8.0, 8.0], 3:[5.0, 8.2]}, 'DS001':{1:[0.0,0.0],3:[0.0,0.0]}, 'LP001':{1:[0.0,0.0],2:[0.0,0.0]}}