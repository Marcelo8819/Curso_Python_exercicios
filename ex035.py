'''Exercício Python 035: Desenvolva um programa que leia o
comprimento de três retas e diga ao usuário se elas podem ou
não formar um triângulo.'''
print('='*30)
print('Analisando Triângulos')
print('='*30)
reta1 = float(input(' primeiro segmento de reta: '))
reta2 = float(input('segundo segunda de reta: '))
reta3 = float(input('terceiro segmento de reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos não forma um triângulo')

