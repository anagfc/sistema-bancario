def realizar_saque(*, saldo_em_conta, quantidade_saques, extrato):
    VALOR_LIMITE_SAQUE = 500.0
    acrescimo_extrato = ''
    realização_operacao = bool
    valor_saque = int(input('Valor do saque: R$ '))
    if quantidade_saques > 0:
        if valor_saque <= VALOR_LIMITE_SAQUE:
            if valor_saque <= saldo_em_conta:
                saldo_em_conta -= valor_saque
                quantidade_saques -= 1
                print('                SUCESSO!')
                print(' '* 7, acrescimo_extrato)
                acrescimo_extrato = f'Saque de R$ {valor_saque:.2f} realizado'
                if 'Nenhuma' in extrato[0]:
                    extrato[0] = acrescimo_extrato
                else:
                    extrato.append(acrescimo_extrato)
                return saldo_em_conta, quantidade_saques, extrato 
            else:
                realização_operacao = False
                print('                  ERRO!')
                print('      Valor indisponível para saque')
                return realização_operacao   
        else:
            realização_operacao = False
            print('                  ERRO!')
            print('       Valor de saque indisponível')
            return realização_operacao   
    else:
        realização_operacao = False
        print('                  ERRO!')
        print('        Limite de saques atingido')
        return realização_operacao

banco = 'Goliath National Bank (GNB)'
slogan = 'The world leader in credit and banking'
menu ='''         Seja bem-vindo ao GNB!
[S] Sacar
[D] Depositar
[E] Consultar extrato
[Q] Sair

Selecione uma operação: '''

opcao = 'Início'
saques_restantes = 3
saldo = 1500.0
historico_movimentacoes = []

# Dando início ao menu
while True:
    print('-'*41)
    print(f'{banco:^41}'.upper())
    print(f'{slogan:^41}')
    print('-'*41)
    opcao = str(input(menu)).upper()
    print('-'*41)
    
    if opcao == 'S':
        operacao = realizar_saque(saldo_em_conta= saldo, quantidade_saques= saques_restantes, extrato= historico_movimentacoes)
        if operacao == False:
            print('\nRetornando ao menu...')
        elif len(operacao) > 1:
            saldo = operacao[0]
            saques_restantes = operacao[1]
            historico_movimentacoes = operacao[2]
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