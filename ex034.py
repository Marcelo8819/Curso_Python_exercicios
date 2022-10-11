'''Exercício Python 034: Escreva um programa que pergunte o
 salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%.
  Para os inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Qual o seu salário atual? R$'))
if salario <= 1.250:
    aumento = salario + (salario * 15/100)
else:
    aumento = salario + (salario * 10/100)
print('Quem ganha R$ {:.2f} passa a ganhar R${:.2f} agora'.format(salario,aumento))