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
saldo = 2000.0
valor_saque = 0


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
                    print('       Saque realizado com sucesso')
                    print(f'Saques restantes: {qtd_limite_saque}')
                    print(f'Saldo restante: R${saldo:.2f}')
                else:
                    print('                  ERRO!')
                    print('      Valor indisponível para saque')
            else:
                print('                  ERRO!')
                print('       Valor de saque indisponível')
        else:
            print('                  ERRO!')
            print('        Limite de saques atingido')
        
        print()
        print('Retornando ao menu...')
            
        # Lógica registro no extrato
        

    elif opcao == 'D':
        print('Você escolheu depositar')
    
    elif opcao == 'E':
        print('Você escolheu consultar extrato')
    
    elif opcao == 'Q':
        print('      O GNB agradece a preferência!')
        print()
        break
    
    else:
        print('   Operação inválida. Tente novamente')
        print()