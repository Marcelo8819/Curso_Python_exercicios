'''Exercício Python 039: Faça um programa que leia o ano de
 nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora
 exata de se alistar ou se já passou do tempo do alistamento.
  Seu programa também deverá mostrar o tempo que falta ou que
  passou do prazo.'''


from datetime import date


atual = date.today().year
print("----ALISTAMENTO MILITAR----")
print("----Genero----")
print("[1] MASCULINO")
print("[2] FEMININO")
genero = str(input("Qual seu gênero? "))
nasc = int(input("Digite o ano de nascimento: "))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}".format(nasc,idade,atual))
print("Alistamento para o sexo feminino não é obrigatório")
if idade == 18 and genero == 1:
    print("Você tem que se alistar imediatamente!")
elif idade < 18 and genero == 1:
    saldo = 18 - idade
    print("Ainda falta {} anos para o alistamento ".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será em {} ".format(ano))
elif idade > 18 and genero == 1 :
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos.".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))