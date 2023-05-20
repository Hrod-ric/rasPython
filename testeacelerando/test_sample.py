def imc(peso, altura):
    imc = peso / (altura*altura)
    print(imc)
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

