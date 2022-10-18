'''Tipos Primitivos
Nessa aula, vamos aprender como funcionam os tipos primitivos no Python
e as peculiaridades do int() float() bool() e str(). Além disso,
veremos como fazer as primeiras operações com a função print() do Python.'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = int(input('Escolha a operação: '))
print('----Menu----')
print('Escolha a operação')
print('[1] soma')
print('[2] subtração')
print('[3] multiplicação')
print('[4] divisão')

if op == 1:
   print('A soma é: ', n1 + n2)
elif op == 2:
    print('A subtração é:',n1 - n2)
elif op == 3:
    print('A multiplicação é: ',n1 * n2)
elif op == 4:
    print('A divisão é: ',n1 / n2)
else:
    print('Digite uma opção válida.')

