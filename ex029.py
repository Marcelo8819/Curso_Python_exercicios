'''Exercício Python 029: Escreva um programa que leia a
velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
 uma mensagem dizendo que ele foi multado. A multa vai
 custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input("Informe sua velocidade: "))
multa = (velocidade-80) * 7
if velocidade >= 80:
    print("Você foi multado no valor de R$ {:.2f} por ultrapassar a velocidade máxima de 80km/h".format(multa))
else:
    print("Parabéns você está dentro do limite de velocidade permitido")


