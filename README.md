## Sobre

Esse projeto é um dos desafios de código propostos no Bootcamp DIO, Potência Tech powered by iFood - Ciências de Dados com Python.


### Módulo

O desafio 'Criando um Sistema Bancário com Python' é o 1º de 2 desafios propostos no módulo 2: Dominando o Python para Ciência de Dados, sob a responsabilidade do professor Guilherme Arthur de Carvalho.


## Tecnologias

- Python 3


## Objetivo

O objetivo desse desafio é criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.


## Proposta

Fomos contratados por um grande banco para desenvolver seu novo sistema. Esse banco deseja modernizar suas operações e, para isso, escolheu a linguagem Python. 

Para a primeira versão do sistema, devemos implementar apenas 3 operações: depósito, saque e extrato.

### Operação de depósito
Deve ser possível depositar valores positivos para uma conta bancária. A v1 do projeto trabalha com apenas 1 usuário, então não é necessário se preocupar com a identificação do número da agência e nem da conta bancária.

Todos os depósitos devem ser armazenados numa variável e exibidos na operação de extrato.

### Operação de saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00/saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar dinheiro por falta de saldo.

Todos os saques devem ser armazenados numa variável e exibidos na operação de extrato.

### Operação de extrato
Deve listar todos os depósitos e saques realizados na conta. No fim da lista, deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx.

## Versão 2.0

Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato.

Além disso, para a versão 2 do nosso sistema, precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).


### Módulo

O desafio 'Otimizando o Sistema Bancário com funções Python' é o 2º de 2 desafios propostos no módulo 2: Dominando o Python para Ciência de Dados, sob a responsabilidade do professor Guilherme Arthur de Carvalho.

## Objetivo

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

## Separação em funções
Devemos criar funções para todas as operações do sistema.
Cada função terá uma regra na passagem de argumentos, visando exercitar tudo o que aprendemos. 
O retorno e a forma como serão chamadas pode ser definida da forma que achar melhor.

### Operação saque
A função saque deve receber os argumentos apenas por nome (kwd only).
**Sugestão de argumentos:** saldo, valor, extrato, limite, numero_saques, limite_saques.
**Sugestão de retorno:** saldo e extrato.

### Operação depósito
A função depósito deve receber os argumentos apenas por posição (positional only).
**Sugestão de argumentos:** saldo, valor, extrato.
**Sugestão de retorno:** saldo e extrato.

### Operação extrato
A função extrato deve receber os argumentos por posição e nome (positional e keyword only).
**Argumentos posicionais:** saldo.
**Argumentos nominais:** extrato.

### Operação cadastrar usuário
O programa deve armazenar os usuários numa lista.
Um usuário é composto por nome, data de nascimento, CPF (apenas números) e endereço (string no formato: logradouro, nº - bairro - cidade/sigla estado).
Não deve ser possível cadastrar dois usuários com o mesmo CPF.

### Operação cadastrar conta bancária
O programa deve armazenar contas numa lista. Uma conta é formada por agência, número da conta e usuário.
O número da conta é sequencial, iniciando em 1.
O número da agência é fixo: ‘0001’.
O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.