'''Exercício Python 036: Escreva um programa para aprovar o
empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o
empréstimo será negado.'''


casa = float(input('Valor da casa: R$ '))
salario = float(input('Qual o valor do seu salário? '))
anos = int(input('Quantos anos de financiamento?  '))
prestacao = casa / (anos * 12 )
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, '.format(casa,anos), end='')
print('prestação será de R${:.2f} emprestimo aprovado!'.format(prestacao))
if prestacao > minimo:
        print('Seu emprestimo não foi aprovado, a parcela é superior a 30% do seu salário')