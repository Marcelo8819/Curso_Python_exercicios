'''Exercício Python 016: Crie um programa que leia um número
Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

real = float(input('Digite um número real: '))
print('Esse número real {} convertido para intereiro fica {:.0f}'.format(real,real))