def realizar_saque(*, saldo_em_conta, quantidade_saques, extrato):
    VALOR_LIMITE_SAQUE = 500.0
    acrescimo_extrato = ''
    realizacao_operacao = bool
    valor_saque = int(input('Valor do saque: R$ '))
    if quantidade_saques > 0:
        if valor_saque <= VALOR_LIMITE_SAQUE:
            if valor_saque <= saldo_em_conta:
                saldo_em_conta -= valor_saque
                quantidade_saques -= 1
                acrescimo_extrato = f'Saque de R$ {valor_saque:.2f} realizado'
                print('\n                SUCESSO!')
                print(' '* 5, acrescimo_extrato)
                
                if 'Nenhuma' in extrato[0]:
                    extrato[0] = acrescimo_extrato
                else:
                    extrato.append(acrescimo_extrato)
                return saldo_em_conta, quantidade_saques, extrato 
            else:
                realização_operacao = False
                print('\n                  ERRO!')
                print('      Valor indisponível para saque')
                return realização_operacao   
        else:
            realização_operacao = False
            print('\n                  ERRO!')
            print('       Valor de saque indisponível')
            return realização_operacao   
    else:
        realização_operacao = False
        print('\n                  ERRO!')
        print('        Limite de saques atingido')
        return realização_operacao

def realizar_depósito(saldo_em_conta, extrato , /):
    acrescimo_extrato = ''
    realizacao_operacao = bool
    valor_deposito = int(input('Valor do depósito: R$ '))
    if valor_deposito > 0:
        saldo_em_conta += valor_deposito
        acrescimo_extrato = f'Depósito de R$ {valor_deposito:.2f} realizado'
        print('\n                SUCESSO!')
        print(' ' * 4, acrescimo_extrato)
        if 'Nenhuma' in extrato[0]:
            extrato[0] = acrescimo_extrato
        else:
            extrato.append(acrescimo_extrato)
        print('\nRetornando ao menu...')
        return saldo_em_conta, extrato        
    else:
        print('\n                  ERRO!')
        print('       Valor de depósito inválido')
        realizacao_operacao = False
        return realizacao_operacao

def visualizar_extrato(saldo_em_conta, saldo_de_inicio, /, nome_banco, slogan_banco, quantidade_saques, *, extrato):
    print(f'\n{nome_banco:^41}'.upper())
    print(f'{slogan_banco:^41}')
    print('-' * 41)
    print('\n            Extrato da conta\n')
    print(f'Saldo inicial: R$ {saldo_de_inicio:.2f}\n')
    for transacao in extrato:
        print(f'{transacao}')
    print('-' * 41)
    print(f'Saldo atual da conta: R$ {saldo_em_conta:.2f}')
    print(f'Saques diários restantes: {quantidade_saques}\n')

def cadastrar_usuario(lista_clientes):
    usuario = {}
    cpf_cadastro = int(input('Insira seu CPF (somente números): '))
    if f'{cpf_cadastro}' in lista_clientes:
        print('Cliente já existente.')
    else:
        nome_cadastro = str(input('Nome completo: '))
        nascimento_cadastro = str(input('Data de nascimento (xx/xx/xxxx): '))
        logradouro_cadastro = str(input('Endereço - Rua/Avenida: '))
        numero_cadastro = str(input('Endereço - Nº: '))
        bairro_cadastro = str(input('Endereço - Bairro: '))
        cidade_cadastro = str(input('Endereço - Cidade: '))
        uf_cadastro = str(input('Endereço - UF: '))
        endereco_cadastro = logradouro_cadastro + ', ' + numero_cadastro + ' - ' + bairro_cadastro + ' - ' + cidade_cadastro + '/' + uf_cadastro

        usuario['CPF'] = cpf_cadastro
        usuario['nome'] = nome_cadastro
        usuario['nascimento'] = nascimento_cadastro
        usuario['endereco'] = endereco_cadastro

        chave_principal = usuario['CPF']
        lista_clientes[f'{chave_principal}'] = usuario

        return lista_clientes

banco = 'Goliath National Bank (GNB)'
slogan = 'The world leader in credit and banking'
menu ='''         Seja bem-vindo ao GNB!

Novo no GNB? ----------------------------
[N] Cadastrar novo cliente
[C] Cadastrar conta

Já é nosso cliente? --------------------- 
[S] Sacar
[D] Depositar
[E] Consultar extrato
[Q] Sair

Selecione uma operação: '''

clientes = {}
opcao = 'Início'
saques_restantes = 3
saldo = 1500.0
saldo_inicial = saldo
historico_movimentacoes = ['Nenhuma operação realizada']

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
        operacao = realizar_depósito(saldo, historico_movimentacoes)
        if operacao == False:
            print('\nRetornando ao menu...')
        elif len(operacao) > 1:
            saldo = operacao[0]
            historico_movimentacoes = operacao[1]
        
    elif opcao == 'E':
        visualizar_extrato(saldo, saldo_inicial, banco, slogan, saques_restantes, extrato= historico_movimentacoes)
    
    elif opcao == 'Q':
        print('      O GNB agradece a preferência!\n')
        break
    
    elif opcao == 'N':
        clientes = cadastrar_usuario(clientes)
        print(clientes)
    
    else:
        print('   Operação inválida. Tente novamente\n')