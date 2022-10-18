'''Exercício Python 040: Crie um programa
 que leia duas notas de um aluno e calcule
  sua média, mostrando uma mensagem no final,
  de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2 # Precedencia de operação
if media < 5.0:
    print('REPROVADO sua media foi : {}'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO sua media foi : {}'.format(media))
else:
    print('APROVADO sua media foi : {}'.format(media))

# FORMA MAIS SIMPLES

# if 7 > media >= 5:
#     print('Aluno em RECUPERAÇÃO')
# elif < 5:
#     print('O aluno está REPROVADO')
# elif media >=7:
#     print('O aluno está APROVADO')
