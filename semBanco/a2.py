from enum import auto
import random
dic_autores = {
    451: 'Paulo Freire',
    765: 'Machado de Assis'
}
dic_livros = {
    787: 'Pedagogia do Oprimido' ,
    889: 'Educação como Prática da Liberdade',
    898: 'Pedagogia da Autonomia: Saberes Necessários à Prática Educativa', 
    859: 'Dom Casmurro',
    623: 'Memórias Póstumas de Brás Cubas'
}
dic_autor_livro = {
    451: [787,889,898], 
    765: [859,623]
}
def cadAut():
    autores = list(dic_autores)
    chave = 100
    while chave in autores:
        chave = random.randrange(100, 999)
    
    nome = input('\nDigite o nome do autor: ')
    if nome.lower() == 'n': return

    concordar = input(f'o autor {str(chave)} {nome} sera adicionado ao banco de dados com a chave {chave}, confirma? ')
    if concordar.lower() == 's':
        dic_autores[chave] = nome
        dic_autor_livro[chave] = []
    
    concordar = input('Deseja continuar? S/N ')
    if concordar.lower() == 's': cadAut()
    else: return

def cadLiv():
    livros = list(dic_livros)
    chave = 100
    while chave in livros:
        chave = random.randrange(100, 999)
    
    nome = input('\nDigite o nome do livro: ')
    if nome.lower() == 'n': return

    autores = list(dic_autores)
    for i in autores:
        print('O autor ' + str(i) + ' ' + dic_autores[i])
    autor = input('Digite o Id do autor: ')
    autor = int(autor)

    concordar = input(f'o livro {nome} sera adicionado ao banco de dados com a chave {chave}, confirma? ')
    if concordar.lower() == 's':
        dic_livros[chave] = nome
        dic_autor_livro[autor] += [chave]

    concordar = input('Deseja continuar? S/N ')
    if concordar.lower() == 's': cadLiv()
    else: return

def consulta():
    escolha = input('\n1 - Pesquisar por Autor\n2 - Mostrar todos\n3 - Sair\n- Digite a opção desejada: ')
    if escolha == 'n': return
    if escolha == '1':
        escolha2 = input('\n1 - Id\n2 - Nome\nPesquisar por: ')
        autores = list(dic_autores)
        if escolha2 == 'n': return
        if escolha2 == '1':
            print('\n')
            for i in autores:
                print('Id: ' + str(i) + '\tNome: ' + dic_autores[i])
            autor = input('Digite o Id do autor: ')
            if autor == 'n': return
            autor = int(autor)
            livros = dic_autor_livro[autor]
            if len(livros) == 0:
                print('\nO autor ' + str(i) + ' ' + dic_autores[i] + ', nao possui livros')
            else:
                print('\nO autor ' + str(autor) + ' ' + dic_autores[i] + ', possui cadastrados os seguintes livros:')
                contador = 1
                for i in livros:
                    print(str(contador) + '. ' + dic_livros[i])
                    contador += 1

        if escolha2 == '2':
            print('\n')
            for i in autores:
                print('Nome: ' + dic_autores[i])
            autor = input('Digite o nome do autor ')
            if autor == 'n': return
            autor = autor.lower()
            for i in autores:
                nome = dic_autores[i]
                if(autor == nome.lower()):
                    livros = dic_autor_livro[i]
                    if len(livros) == 0:
                        print('\nO autor ' + str(i) + ' ' + dic_autores[i] + ', nao possui livros')
                    else:
                        print('\nO autor ' + str(i) + ' ' + dic_autores[i] + ', possui cadastrados os seguintes livros:')
                        contador = 1
                        for u in livros:
                            print(str(contador) + '. ' + dic_livros[u])
                            contador += 1
                    return
    if escolha == '2':
        autores = list(dic_autores)
        for i in autores:
            livros = dic_autor_livro[i]
            if len(livros) == 0:
                print('\nO autor ' + str(i) + ' ' + dic_autores[i] + ', nao possui livros')
            else:
                print('\nO autor ' + str(i) + ' ' + dic_autores[i] + ', possui cadastrados os seguintes livros:')
                contador = 1
                for u in livros:
                    print(str(contador) + '. ' + dic_livros[u])
                    contador += 1


    if escolha == '3':return

while True:
    escolha = input('\n1 - Cadastro de AUTORES\n2 - Cadastro de LIVROS\n3 - Consulta de LIVROS por AUTOR\n4 - Sair\n- Digite a opção desejada: ')
    if escolha == '1':cadAut()
    if escolha == '2':cadLiv()
    if escolha == '3':consulta()
    if escolha == '4':break