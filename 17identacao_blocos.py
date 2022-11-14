def sacar (valor):
    saldo = 500 - valor

    if saldo >= valor:
        print('Valor de saque aprovado!')
        print('Retire seu dinheiro na boca do caixa')
        print(f'O saldo restante é {saldo}')

print('Obrigado por ser nosso cliente, bom dia!')

def depositat(valor):
    saldo = 500
    saldo += valor


sacar(1000)
