'''
Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from time import sleep
itens = ('Pedra', 'Papel' ,'Tesoura')
computador = randint(0, 2)
print(''' Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
# print('O computador escolheu {}' .format(itens[computador]))
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador escolheu {itens[jogador]}')
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('Empate')

    elif jogador == 1:
        print('Jogador vence')

    elif jogador == 2:
        print('Computador vence')

    else:
        print('JOGADA INVÁLIDA')

elif computador ==1:
    if jogador == 0:
        print('Computador vence')

    elif jogador == 1:
        print('Empate')

    elif jogador == 2:
        prin('Jogador vence')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:
    if jogador == 0:
        print('Jogador vence')

    elif jogador == 1:
        print('Computador vence')

    elif jogador == 2:
        print('Empate')

    else:
        print('JOGADA INVÁLIDA')
