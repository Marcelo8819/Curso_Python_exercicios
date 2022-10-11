# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
#Conceitos:
# Ordem de precedência: r = n **(1/2)
# Orientação a objetos: .format(n,d,t,r)#


n = int(input('Digite um número:'))
d = n * 2
t = n * 3
r = n **(1/2)
print('Analisando o valor de {},\n seu dobro é {},\n o triplo é {} \n e  a raiz quadrada é {:.2f}' .format(n, d, t, r))

n = int(input('Digite um número'))
print('Analisando o valor de {}, \n seu dobro é {}, \n o triplo é {} \n e a raiz quadrada é {:.2f}' .format(n,(d),(t),(r)))
