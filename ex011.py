'''Exercício Python 011: Faça um programa que leia a largura
e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta
uma área de 2 metros quadrados.'''

larg = float(input('Qual é a largura da sua parede? '))
alt = float(input('Qual a altura da sua parede? '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².' .format(larg,alt,area))
tinta = area / 2
print('Para pintar {} m² de parede , você precisará de {} litros de tinta' .format(area,tinta))