'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''


print('='*30)
print('Analisando Triângulos')
print('='*30)
reta1 = float(input(' primeiro segmento de reta: '))
reta2 = float(input('segundo segunda de reta: '))
reta3 = float(input('terceiro segmento de reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print("Equilatero")
    if reta1 != reta2 != reta3 != reta1:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print('Os segmentos não forma um triângulo')