## Programa SimpleBank ##

import time

user = input("Olá, me diga seu nome de usuário do SimpleBank : ")
print(f'Bem-vindo {user}, vamos iniciar nosso sistema para você!')
print("Carregando...")

for numeros_enfeite in range(11):
    print(f"Subindo o sistema {numeros_enfeite}...", end="\r")
    time.sleep(0.2)

print("=" * 50)
print("PRONTO!".center(50))
print("VEJA AS SUAS OPÇÕES!".center(50))
print("=" * 50)

########################################

menu = """
======= MENU =======
[d] - Depósito
[s] - Saque
[e] - Extrato
[c] - Criar Conta
[u] - Criar Usuário
[q] - Sair
====================
Escolha uma opção: """

# Dados iniciais
LIMITE_SAQUES = 3
limite = 500

usuarios = []
contas = []


def buscar_usuario(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None


def criar_usuario():
    print("\nVamos criar seu usuário...")
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite seu CPF: ")
    endereco = input("Digite seu endereço (logradouro - bairro - cidade/sigla estado): ")

    if buscar_usuario(cpf):
        print("CPF já cadastrado. Tente novamente.")
        return

    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário cadastrado com sucesso!")


def criar_conta():
    print("\nVamos criar sua conta...")
    cpf = input("Digite seu CPF: ")

    if not buscar_usuario(cpf):
        print("CPF não encontrado. Cadastre o usuário primeiro.")
        return

    numero_conta = len(contas) + 1

    print("""
Escolha o tipo de conta:
[1] Conta Corrente
[2] Conta Poupança
[3] Conta Salário
""")
    tipo_opcao = input("Digite o número correspondente ao tipo de conta: ")

    tipos_conta = {
        '1': 'Conta Corrente',
        '2': 'Conta Poupança',
        '3': 'Conta Salário'
    }

    tipo_conta = tipos_conta.get(tipo_opcao)

    if not tipo_conta:
        print("Opção inválida. A conta não foi criada.")
        return

    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'cpf': cpf,
        'tipo_conta': tipo_conta,
        'saldo': 0,
        'extrato': [],
        'numero_saques': 0
    }
    contas.append(conta)
    print(f"\nConta criada com sucesso!")
    print(f"Agência: 0001  Conta: {numero_conta}")
    print(f"Tipo de conta: {tipo_conta}")


def buscar_contas_por_cpf(cpf):
    contas_do_cpf = []
    for conta in contas:
        if conta['cpf'] == cpf:
            contas_do_cpf.append(conta)
    return contas_do_cpf


def selecionar_conta(cpf):
    contas_do_cpf = buscar_contas_por_cpf(cpf)
    if not contas_do_cpf:
        print("Nenhuma conta vinculada a este CPF.")
        return None

    print("\nContas encontradas:")
    for i, conta in enumerate(contas_do_cpf, 1):
        print(f"[{i}] Conta {conta['numero_conta']} - {conta['tipo_conta']} - Saldo: R$ {conta['saldo']:.2f}")

    try:
        opcao = int(input("Escolha o número da conta: "))
        if 1 <= opcao <= len(contas_do_cpf):
            return contas_do_cpf[opcao - 1]
        else:
            print("Opção inválida.")
            return None
    except ValueError:
        print("Entrada inválida.")
        return None


def depositar():
    cpf = input("Digite seu CPF: ")

    if not buscar_usuario(cpf):
        print("CPF não encontrado. Operação cancelada.")
        return

    conta = selecionar_conta(cpf)
    if not conta:
        return

    try:
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            conta['saldo'] += valor
            conta['extrato'].append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    except ValueError:
        print("Valor inválido. Digite um número.")


def sacar():
    cpf = input("Digite seu CPF: ")

    if not buscar_usuario(cpf):
        print("CPF não encontrado. Operação cancelada.")
        return

    conta = selecionar_conta(cpf)
    if not conta:
        return

    try:
        valor = float(input("Digite o valor do saque: "))
        if valor <= 0:
            print("Valor inválido para saque.")
        elif valor > conta['saldo']:
            print("Saldo insuficiente.")
        elif conta['numero_saques'] >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")
        elif valor > limite:
            print(f"O valor excede o limite de saque diário de R$ {limite:.2f}")
        else:
            conta['saldo'] -= valor
            conta['numero_saques'] += 1
            conta['extrato'].append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Valor inválido. Digite um número.")


def mostrar_extrato():
    cpf = input("Digite seu CPF: ")

    if not buscar_usuario(cpf):
        print("CPF não encontrado. Operação cancelada.")
        return

    conta = selecionar_conta(cpf)
    if not conta:
        return

    print("\n=== EXTRATO ===")
    if not conta['extrato']:
        print("Nenhuma operação realizada.")
    else:
        for registro in conta['extrato']:
            print(registro)
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    print("================")


while True:
    opcao = input(menu).lower()

    if opcao == "d":
        depositar()

    elif opcao == "s":
        sacar()

    elif opcao == "e":
        mostrar_extrato()

    elif opcao == "u":
        criar_usuario()

    elif opcao == "c":
        criar_conta()

    elif opcao == "q":
        print("Você escolheu SAIR")
        print("Obrigado, volte sempre!")
        for numeros_enfeite in range(11):
            print(f"Fechando o sistema {numeros_enfeite}...", end="\r")
            time.sleep(0.2)
        break

    else:
        print("Selecione uma das opções disponíveis, por favor...")
