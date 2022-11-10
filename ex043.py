'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de 
uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''


peso = float(input('Digite seu peso: '))
print(peso)

altura = float(input('Digite sua altura: '))
print(altura)

imc = peso/ (altura **2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('A pessoa está a baixo do peso')

elif imc >= 18.5 and imc <= 25: # 18.5 <= imc < 25:   códico simplificado 
    print('Seu peso é ideal')

elif imc >= 25 and imc <= 30: # 25 <= imc < 30: códico simplificado
    print('Você está em condição de sobrepeso')

elif imc >=30 and imc <=40: # 30 <= imc < 40:
    print('Você está em condição de obsedidade')

else:
    print('Você está em condição de obsedidade mórbida')


