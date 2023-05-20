import random
import sqlite3
con = sqlite3.connect("./Banco/disco.db")
cur = con.cursor()

def cad(tabela):
    try:
        chave = random.randrange(10000, 99999)
        nome = input('Nome: ')
        data = (chave,nome)
        cur.execute(f"INSERT INTO {tabela} VALUES(?,?)",data)
        #for i in cur.execute("SELECT * from professores"):
        #    print(i)
        con.commit()
    except:
        chave = ''
        print('chave invalida!')
    print('\n')

def mostrar(li,string, string2):
    contador = 1
    lista = [0]
    print(f'\n****** {string} ******')
    for i in li:
        #str(contador) + ' - Matricula: ' + str(i)
        print(str(contador) + f' - {string2}:\t' + str(i[0]) + '\tNome:\t' + i[1])
        lista += [i[0]]
        contador += 1
    return lista

def alocarProfDisc():
    try:
        lista = mostrar(cur.execute("SELECT * from professores"), 'Professor','Matricula')
        prof = int(input('\nEscolha o numero correspondente ao professor '))
        profEscolhido = lista[prof]

        lista = mostrar(cur.execute("SELECT * from disciplinas"), 'Disciplina','Codigo')
        disc = int(input('\nEscolha o numero correspondente a disciplina '))
        discEscolhida = lista[disc]

        rr = cur.execute(f"select disc_id from prof_disc where prof_id == {profEscolhido}")
        rr.fetchall()
        for i in rr:
            print(i[0])
            print(discEscolhida)
            if i[0] == discEscolhida: 
                print('Disciplina já alocada')
                return i

        data = (profEscolhido, discEscolhida)
        cur.execute("INSERT INTO prof_disc VALUES(?,?)",data)
        con.commit()
    except:
        print('Erro!')

def alocarAlunDisc():
    try:
        lista = mostrar(cur.execute("SELECT * from alunos"), 'Aluno','Matricula')
        alun = int(input('\nEscolha o numero correspondente ao aluno '))
        alunEscolhido = lista[alun]

        lista = mostrar(cur.execute("SELECT * from disciplinas"), 'Disciplina','Codigo')
        disc = int(input('\nEscolha o numero correspondente a disciplina '))
        discEscolhida = lista[disc]

        troca = True
        rr = cur.execute(f"SELECT disc_id, aluno_id from notas where aluno_id == {alunEscolhido}")
        rr.fetchall()
        for i in rr:
            if i[0] == discEscolhida:
                print('Disciplina já alocada\n')
                res = input("A disciplina " + str(i[1]) + " já foi alocada para esse aluno, deseja remover? ")
                print('\n')
                if res == 's':
                    cur.execute(f'DELETE FROM notas where disc_id == "{i[0]}" AND aluno_id == {i[1]}')
                    con.commit()
                    troca = False
                    break

        if troca:
            data = (discEscolhida,alunEscolhido,0.0)
            cur.execute('INSERT INTO notas VALUES(?,?,?)',data)
            con.commit()
            print('Disciplina alocada\n')
    except:
        pass

def notas():
    try:
        lista = mostrar(cur.execute("SELECT * from professores"), 'Professor','Matricula')
        prof = int(input('\nEscolha o numero correspondente ao professor '))
        profEscolhido = lista[prof]

        res = cur.execute(f"SELECT codigo, nome from prof_disc INNER JOIN disciplinas ON prof_disc.disc_id = disciplinas.codigo WHERE prof_id == '{profEscolhido}'")
        disciplinas = res.fetchall()
        #print(disciplinas)

        lista = mostrar(disciplinas, 'Disciplina','Codigo')
        disc = int(input('\nEscolha o numero correspondente a disciplina '))
        discEscolhida = lista[disc]
        #print(discEscolhida)


        res = cur.execute(f"SELECT aluno_id, nome from notas INNER JOIN alunos ON notas.aluno_id = alunos.matricula where disc_id == '{discEscolhida}'")
        alunos = res.fetchall()
        #print(alunos)

        lista = mostrar(alunos, 'Aluno','Matricula')
        alun = int(input('\nEscolha o numero correspondente ao aluno '))
        alunEscolhido = lista[alun]

        nota1 = float(input('Qual a nota da primeira avaliação? '))
        #nota2 = float(input('Qual a nota da segunda avaliação? '))

        try:
            data = (discEscolhida, alunEscolhido, nota1)
            cur.execute("INSERT or replace INTO notas VALUES(?,?,?)",data)
            con.commit()
            print('Nota inserida!')
        except:
            print("Nota invalida!")
    except:
        pass

def imprimirBoletim():
    print('\n***Boletim***')
    res = cur.execute('select matricula, nome from alunos')
    alunos = res.fetchall()
    #print(alunos)

    res = cur.execute('select disc_id, aluno_id, nota from notas ORDER BY disc_id')
    notas = res.fetchall()
    #print(notas)

    res = cur.execute('select codigo, nome from disciplinas')
    disciplinas = res.fetchall()
    #print(disciplinas)

    for i in alunos:
        print('***************************************************************************************************************')
        print('Matrícula: ' + str(i[0]) + '\tNome: ' + i[1])
        print('\nCódigo\t–\tNome da disciplina\t–\tAV-1\t–\tAV-2\t–\tMédia\t–\tResultado Final')
        for u in notas:

            if not u[1] == i[0]:continue
            for a in disciplinas:
                if u[0] == a[0]:
                    nomeDisciplina = a[1]
            #print(nomeDisciplina)
            nota1 = u[2]
            nota2 = u[2]
            media = (float(nota1) + float(nota2))/2
            resultado = ''
            if (media >= 7): 
                resultado = 'Aprovado'
            elif (media > 0): 
                resultado = 'Reprovado'
            else: 
                nota1 = 'N/A'
                nota2 = 'N/A'
                media = 'N/A'
                resultado = 'Indefinido'
            print(u[0] + '\t–\t' + nomeDisciplina + '\t–\t' + str(nota1) + '\t–\t' + str(nota2) + '\t–\t'+ str(media) +'\t–\t' + resultado)


while True:
  #try:
    e1 = input('\nGestão Escolar:\n1 – Cadastro de professores\n2 – Alocação a disciplinas\n3 – Lançamento de Notas\n4 – Impressão de Boletim\n5 – Sair\nDigite a opção desejada: ')
    if(e1 == '1'):
                    e2 = input('\n1 – Cadastro de professores\n2 – Cadastro de disciplinas\n3 – Cadastro de Alunos\nDigite a opção desejada: ')
                    if(e2 == '1'):cad('professores')
                    elif(e2 == '2'):cad('disciplinas')
                    elif(e2 == '3'):cad('alunos')
      
    elif(e1 == '2'):
                    e3 = input('\n1 - Alocação de professores a disciplinas\n2 - Alocação de Alunos a disciplinas\nDigite a opção desejada: ')
                    if(e3 == '1'):alocarProfDisc()
                    elif(e3 == '2'):alocarAlunDisc()

    elif(e1 == '3'):notas()
    elif(e1 == '4'):imprimirBoletim()
    elif(e1 == '5'): break
  #except:
    #print('programa encerrado!')
    #break