'''O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando
não sabemos o número exato de vezes que nosso bloco de código deve ser executado.''' 


# while 

# i = 0 

#   while(i <=10):
#       print(i)
#       i = i + 1

# i = 0 

# while(i <=10):
#     print('O loop está rodando...')
#     # i = i +1
#     i+=1


# Receba um número do teclado e exiba os 2 números seguntes

opcao = -1

while opcao != 0:
    opcao = int(input(' [1] Saldo \n [2] Sacar \n [3] Extrato \n [0] Sair \n: '))

    if opcao == 1:
        print('Verificando saldo...')
    elif opcao == 2:
        print('Sacando...')
    elif opcao == 3:
        print('Exibindo o extrato...')
