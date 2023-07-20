banco = 'Goliath National Bank (GNB)'
slogan = 'The world leader in credit and banking'
menu ='''         Seja bem-vindo ao GNB!
[S] Sacar
[D] Depositar
[E] Consultar extrato
[Q] Sair

Selecione uma operação: '''

opcao = 'Início'
qtd_limite_saque = 3
VALOR_LIMITE_SAQUE = 500.0
saldo = 1500.0
valor_saque = valor_deposito = 0
historico_depositos = []
historico_saques = []
historico_saldos = [saldo]

# Dando início ao menu
while True:
    print('-'*41)
    print(f'{banco:^41}'.upper())
    print(f'{slogan:^41}')
    print('-'*41)
    opcao = str(input(menu)).upper()
    print('-'*41)
    
    if opcao == 'S':
        # Lógica de realização do saque
        valor_saque = int(input('Valor do saque: R$ '))
        print()
        
        if qtd_limite_saque > 0:
            if valor_saque <= VALOR_LIMITE_SAQUE:
                if valor_saque <= saldo:
                    qtd_limite_saque -= 1
                    saldo -= valor_saque
                    print('                SUCESSO!')
                    print(f'       Saque de R$ {valor_saque:.2f} realizado')
                    
                    # Lógica registro no extrato
                    historico_saques.append(valor_saque)
                       
                else:
                    print('                  ERRO!')
                    print('      Valor indisponível para saque')
            else:
                print('                  ERRO!')
                print('       Valor de saque indisponível')
        else:
            print('                  ERRO!')
            print('        Limite de saques atingido')
        
        print('\nRetornando ao menu...')
        

    elif opcao == 'D':
        # Lógica de realização do depósito
        valor_deposito = int(input('Valor do depósito: R$ '))
        if valor_deposito > 0:
            saldo += valor_deposito
            print('\n                SUCESSO!')
            print(f'      Depósito de R$ {valor_deposito:.2f} realizado')
        else:
            print('\nValor de depósito inválido')
            
        print('\nRetornando ao menu...')
        
        # Lógica registro no extrato
        historico_depositos.append(valor_deposito)
    
    elif opcao == 'E':
        print(f'\n{banco:^41}'.upper())
        print(f'{slogan:^41}')
        print('-' * 41)
        print('\n            Extrato da conta\n')
        if len(historico_depositos) == 0 and len(historico_saques) == 0:
            print('       Nenhuma operação realizada')
            print('-' * 41)
        else:
            print(f'Saldo inicial: R$ {historico_saldos[0]:.2f}\n')
        if len(historico_depositos) > 0:
            print('depósitos'.upper())
            for deposito in historico_depositos:
                print(f'R$ {deposito:.2f}')
            print('-' * 41)
        if len(historico_saques) > 0:
            print('saques'.upper())
            for saque in historico_saques:
                print(f'R$ {saque:.2f}')
            print('-' * 41)
        print(f'Saldo atual da conta: R$ {saldo:.2f}')
        print(f'Saques diários restantes: {qtd_limite_saque}\n')
    
    elif opcao == 'Q':
        print('      O GNB agradece a preferência!')
        print()
        break
    
    else:
        print('   Operação inválida. Tente novamente')
        print()