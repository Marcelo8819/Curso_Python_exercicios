'''Exercício Python 030: Crie um programa que
leia um número inteiro e mostre na tela se ele é PAR ou
ÍMPAR.'''

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O núemero {} é par '.format(numero))
else:
    print('O número {} é impar:'.format(numero))
