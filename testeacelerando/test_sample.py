def imc(peso, altura):
    imc = peso / (altura*altura)
    #print(imc)
    if imc > 40:
        return 'Obesidade grau III'

    elif imc >= 35 and imc < 40:
        return 'Obesidade grau II'
    
    elif imc >= 30 and imc < 35:
        return 'Obesidade grau I'

    elif imc >= 25 and imc < 30:
        return 'Sobrepeso'
    
    elif imc >= 18.5 and imc < 25:
        return 'Peso normal'
    
    elif imc < 18.5:
        return 'Abaixo do peso'

def test(escolha):
    lista = {}
    for peso in range(20,500):
        for altura in range(9,25,1):
            if(imc(peso,(altura/10)) == escolha):
                try:
                    lista[peso] += [altura]
                except:
                    lista[peso] = [altura]
    
    return lista

def test2(escolha):
    lista = test(escolha)
    lista2 = list(lista)
    print(escolha)
    for peso in lista2:
        print('\nPeso:',peso,)
        for altura in lista[peso]:
            print('Altura:',altura/10)

#test2('Abaixo do peso')
test2('Peso normal')
#test2('Sobrepeso')
#test2('Obesidade grau I')