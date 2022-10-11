# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
# Conceitos:
# 1 Tipos primitivos:  int, input;
# 2 Operadores aritiméticos: + , -
# 3 Variáveis: n= int(input()), a = n - 1 , s = n - 1 ,
# 4 Funções: int(input()), print()

n = int(input('Digite um número:'))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {} ' .format(n, a, s))

n = int(input('Digite um número:'))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}' .format(n, n-1, n+1))