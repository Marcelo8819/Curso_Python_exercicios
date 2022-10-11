'''Exercício Python 033: Faça um programa que leia três
números e mostre qual é o maior e qual é o menor.'''

a = int(input('Primeiro número:'))
b = int(input('Segundo número:'))
c = int(input('Terceiro número:'))
#Verificando o menor número
menor = a
if b<a and b<c:
    menor = b
if c<a and c<a:
    menor = c
#Verificando o maior número
maior = a
if b>a and b>c:
    maior =  b
if c>a and c>b:
    maior = c
print('O menor valor digitado é: {}'.format(menor))
print('O maior valor digitado é: {}'.format(maior))