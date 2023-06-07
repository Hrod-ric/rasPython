def imc(peso, altura):
    imc = peso / (altura*altura)
    texto = ''
    if imc > 40:
        texto = 'Obesidade grau III'

    elif imc >= 35 and imc < 40:
        texto = 'Obesidade grau II'
    
    elif imc >= 30 and imc < 35:
        texto = 'Obesidade grau I'

    elif imc >= 25 and imc < 30:
        texto = 'Sobrepeso'
    
    elif imc >= 18.5 and imc < 25:
        texto = 'Peso normal'
    
    elif imc < 18.5:
        texto = 'Abaixo do peso'
        
    return texto

print(imc(80,1.80))