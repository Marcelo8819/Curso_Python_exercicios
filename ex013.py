#Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário, com 15% de aumento.#

s = float(input('Qual é o salário do funcionário? '))
n = s + (s * 15/100)
print('O  funcionário recebe um salário de R$ {:.2f} , com o aumento de 15% ficou passou a ser R$ {:.2f}'.format(s, n))