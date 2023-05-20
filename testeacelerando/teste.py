from typing import List


dic_Alunos = {
    321:['Lucas','07155'],
    123:['Matheus'],
    213:['Junior']
} # = dict()
dic_Disciplinas = {
    'BD001': 'Banco de Dados',
    'LP001': 'Logica de programação'
}
dic_Notas = {
    321:{
        'BD001':[8.0,8.0],
        'LP001':[7.5,6.5]
    },
    123:{
        'LP001':[0.0,0.0]
    },
    213:{
        'BD001':[7.0,6.9]
    }
}
dic_Notas[123]['BD001'] = [0.0,0.0]
print(dic_Notas[123])

def imprimir():
    alunos = list(dic_Alunos)
    for aluno in alunos:
        print(dic_Alunos[aluno][0])

while True:
    escolha = input('Menu:\n1-Imprimir\n2-Sair\nEscolha uma das opções: ')
    if(escolha == '1'):
        imprimir()
    elif(escolha == '2'):
        break