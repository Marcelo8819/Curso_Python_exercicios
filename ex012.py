'''Exercício Python 012: Faça um algoritmo que leia o preço de
um produto e mostre seu novo preço, com 5% de desconto.'''

preco1 = float(input('Qual o preço do produto? '))
preco2 = preco1 - (preco1 * 5/100)
print('O preço inicial do produto é R${}, com o desconte de 5% fica por R%{}'.format(preco1,preco2))