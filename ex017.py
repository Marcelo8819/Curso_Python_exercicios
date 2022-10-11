'''Exercício Python 017: Faça um programa que leia o comprimento do cateto
 oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre
 o comprimento da hipotenusa.'''

catOpost = float(input('Comprimento do cateto oposto: '))
catAdj = float(input('Comprimento do cateto adjacente: '))
hip = (catOpost ** 2 + catAdj **2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))


from math import hypot
catOpost = float(input('Comprimento do cateto oposto: '))
catAdj = float(input('Comprimento do cateto adjacente: '))
hip = hypot(catOpost,catAdj)
print('A hipotenusa vai medir {:.2f}'.format(hip))