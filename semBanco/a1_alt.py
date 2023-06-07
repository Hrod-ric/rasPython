import random

dic_alunos = { 
    #Matricula  : ['nome',                          'telefone']
    25877      : ['Simone de Castro Albuquerque',  '71-91552-9999']#,
    #19614      : ['Manoel de Souza Santos',        '71-98599-9999'],
    #25355      : ['Keila Soares da Silva',         '71-95863-9995']
}
dic_disciplinas = {
    #'Codigo'   : 'Nome da disciplina'
    'BD001'    : 'BANCO DE DADOS',
    'LP001'    : 'LINGUAGEM DE PROGRAMAÇÃO I'#,
    #'IHM'      : 'INTERFACE HOMEM-MÁQUINA'
}
dic_notas = {
    #Matricula  : {'Codigo' : [Notas]}
    25877      : {'BD001'  : [75.5,80.0], 'LP001': [80.5,75.0]}#,
    #19614      : {'BD001'  : [90.5,85.0], 'LP001': [85.5,10.0]}
}

def cadAlunos():
#-
    while True:
                nome = input('Nome do Aluno: ')
                telefone = input('Telefone do Aluno: ')
                while True:
                            chave = random.randrange(10000, 99999)
                            try:
                                k = dic_alunos[chave]
                            except:
                                k = input(f'O Aluno {nome} será adicionado com a matricula {chave}, Confirma? s/n\n')
                                if k == 's': 
                                    break

                dic_alunos[chave] = [nome,telefone]
                disciplinas = list(dic_disciplinas)
                dic_notas[chave] = {}
                for i in disciplinas:
                    dic_notas[chave][i] = [0.0,0.0]

                k = input('Deseja continuar? s/n\n')
                if k == 's':
                    cadAlunos()
                return

def cadDisciplinas():
#-
    while True:
        codigo = input('Codigo da Disciplina: ')
        nomeDisciplina = input('Nome da Disciplina: ')
        try:
            k = dic_alunos[codigo]
            print('Codigo de disciplina já cadastrado!')
        except:
            k = input(f'A Disciplina {nomeDisciplina} será adicionada com o codigo {codigo}, Confirma? s/n\n')
            if k == 's': 
                dic_disciplinas[codigo] = nomeDisciplina
            k = input('Deseja continuar? s/n')
            if k == 's':
                cadDisciplinas()
            else:
                return


def controleNotas():
    if dic_alunos == {}:
        print('Não há alunos cadastrados!')
        return
    if dic_disciplinas == {}:
        print('Não há disciplinas cadastradas!')
        return
    while True:
        #--
        alunos = list(dic_alunos)
        print('escolha uma matricula!')
        contador = 1
        for i in alunos:
            print(f'{contador} Matricula: {i}\tNome do aluno: {dic_alunos[i][0]}')
            contador+=1
        matricula = alunos[int(input(''))-1]
        #--
        disciplinas = list(dic_notas[matricula])
        print('escolha uma disciplina!')
        contador = 1
        for i in disciplinas:
            print(f'{contador} Codigo: {i}\tNome da disciplina: {dic_disciplinas[i]}')
            contador+=1
        codigo = disciplinas[int(input(''))-1]
        #--
        nota1 = input('Digite a nota do primeiro bimestre: ')
        nota2 = input('Digite a nota do segundo bimestre: ')

        k = input(f'As notas do primeiro bimestre {nota1} e o segundo bimestre {nota2} serão adicionados a Disciplina {dic_disciplinas[codigo]}, Confirma? s/n\n')
        if k == 's':
            dic_notas[matricula][codigo]=[nota1,nota2]

        k = input('Deseja continuar? s/n\n')
        if k == 'n':
            return

def imprimirNotas():
    if dic_alunos == {}:
        print('Não há alunos cadastrados!')
        return
    alunos = list(dic_alunos)
    for matricula in alunos:
        print('\nMatrícula: ' + str(matricula) + '\tNome: ' + dic_alunos[matricula][0])
        Disciplinas = list(dic_notas[matricula])
        print('Código\t–\tBim-1\t–\tBim-2\t–\tNome da disciplina')
        for i in Disciplinas:
            print(f'{i}\t–\t{dic_notas[matricula][i][0]}\t–\t{dic_notas[matricula][i][1]}\t–\t{dic_disciplinas[i]}')
    print("\n")



while True:
    e1 = input("'ESCOLA DESSA VEZ EU APRENDO':\n\n1-Cadastro de ALUNOS\n2-Cadastro de Disciplinas\n3-Controle de Notas\n4-Imprimir Notas\n5-Sair\n-Digite a opção desejada: ")
    if e1 == '1':cadAlunos()
    elif e1 == '2':cadDisciplinas()
    elif e1 == '3':controleNotas()
    elif e1 == '4':imprimirNotas()
    elif e1 == '5':break