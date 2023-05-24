import sqlite3
con = sqlite3.connect(database="./Banco/disc.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS professor(
    "id_Professor"	    integer NOT NULL UNIQUE,
    "Nome"          	text NOT NULL,
    "CPF"	            integer NOT NULL UNIQUE,
    PRIMARY KEY("id_Professor")
)""")
cur.execute("""
CREATE TABLE IF NOT EXISTS "alunos" (
    "nr_Matricula"	    integer NOT NULL UNIQUE,
    "nome_Aluno"	    text NOT NULL,
    "CPF"	integer     NOT NULL UNIQUE,
    "endereco_Aluno"	text NOT NULL,
    PRIMARY KEY("nr_Matricula")
)""")
cur.execute("""
CREATE TABLE IF NOT EXISTS "disciplinas" (
	"id_Disciplina"     text NOT NULL UNIQUE,
	"nome_Disciplina"	text NOT NULL,
    "id_Curso"	        text NOT NULL UNIQUE,
	PRIMARY KEY("id_Disciplina")
)""")

cur.execute("""
CREATE TABLE IF NOT EXISTS "Professor_Disciplina" (
	"id_Professor"	    integer NOT NULL,
	"id_Disciplina"	    text NOT NULL,
    "data_Disciplina"	integer NOT NULL,
	PRIMARY KEY("id_Professor","id_Disciplina"),
	FOREIGN KEY("id_Disciplina") REFERENCES "disciplinas"("id_Disciplina"),
	FOREIGN KEY("id_Professor") REFERENCES "professor"("id_Professor")
)""")

cur.execute("""
CREATE TABLE IF NOT EXISTS "curso" (
	"id_Curso"          text NOT NULL UNIQUE,
	"nome_Curso"        text NOT NULL,
    "id_Coordenador"	text NOT NULL UNIQUE,
	PRIMARY KEY("id_curso")
)""")

cur.execute("""
CREATE TABLE IF NOT EXISTS "turma" (
	"id_Turma"	    text NOT NULL,
    "nr_Matricula"	integer NOT NULL,
	"id_Curso"	    text NOT NULL,
    "data_Turma"	integer NOT NULL,
	PRIMARY KEY("id_Turma","nr_Matricula"),
	FOREIGN KEY("id_Curso") REFERENCES "curso"("id_Curso")
)""")

cur.execute("""
CREATE TABLE IF NOT EXISTS "cronograma" (
	"id_Professor"	    integer NOT NULL,
	"id_Disciplina"	    text NOT NULL,
    "data_Disciplina"	integer NOT NULL,
    "id_Turma"	    text NOT NULL,
	PRIMARY KEY("id_Professor","id_Disciplina","id_Turma"),
	FOREIGN KEY("id_Disciplina") REFERENCES "disciplinas"("id_Disciplina"),
	FOREIGN KEY("id_Professor") REFERENCES "professor"("id_Professor"),
    FOREIGN KEY("id_Turma") REFERENCES "turma"("id_Turma")
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
con.commit()