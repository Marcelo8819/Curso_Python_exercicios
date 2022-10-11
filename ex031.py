'''Exercício Python 031: Desenvolva um programa que pergunte
 a distância de uma viagem em Km. Calcule o preço da passagem,
 cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta
  viagens mais longas.'''

distancia = float(input("Qual a distância de sua viagem: "))
preco1 = distancia * 0.50
preco2 = distancia * 0.45
if distancia <= 200:
    print("Sua viagem custará R$ {:.2f}" .format(preco1))
else:
    print("Sua viagem custa R$ {:.2f} ".format(preco2))

print("=" *30)

distancia = float(input("Qual a distância de sua viagem: "))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("O preço da sua passagem será de R$ {:.2f}".format(preco))

