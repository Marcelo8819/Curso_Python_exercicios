
print('='*20 ,"Banco do Celo", "=" *20)
saldo = 500 

while True:
    opcao = int(input('Informe a opção: \n [1] Saldo \n [2] Sacar \n [3] Extrato \n [0] Sair >>> '))

    if opcao == 0:
        break
    
    if opcao == 1: 
        print(f'Seu saldo é de R${saldo}')
        
    elif  opcao == 2:
        saque = float(input('Informe o valor de saque: '))
        if saque <= saldo:
            print('Valor de saque aprovado!')
            print('Retire seu dinheiro na boca do caixa')
            print(f'O saldo restante é {saldo - saque}')
        elif saldo < saque: 
            print(f'Saldo insuficiente! O valor de  saque {saque} é superior a seu saldo')
    else:
     print('Exibindo o extrato...')

   






