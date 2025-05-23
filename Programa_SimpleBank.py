## Programa SimpleBank #### 

import time

user = input("Olá, me diga seu nome de usuário do SimpleBank : ")
print(f'Bem vindo {user}, vamos iniciar nosso sistema para você!')
print("Carregando...")

for numeros_enfeite in range(10):
    print(f"Subindo o sistema {numeros_enfeite}...", end="\r")
    time.sleep(0.2)
    if numeros_enfeite == 10:
        break


print("=" * 50)
print("PRONTO!".center(50))
print("VEJA AS SUAS OPÇÕES!".center(50))
print("=" * 50)

########################################

menu = """
[d] Depositar
[s] Saque 
[e] Extrato
[q] Sair 
"""

saldo = 1000
limite = 500
extrato = []
numero_de_saques = ""
LIMITE_SAQUES = 3

saldo = 1000
limite = 500
extrato_list = [] 
numero_de_saques = 0
LIMITE_SAQUES = 3

menu = """
======= MENU =======
[d] - Depósito
[s] - Saque
[e] - Extrato
[q] - Sair
====================
Escolha uma opção: """


def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato_list.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")


def sacar(valor):
    global saldo
    global numero_de_saques
    if valor <= 0:
        print("Valor inválido para saque.")
        return
    if valor > saldo:
        print("Operação não pode ser realizada, saldo insuficiente.")
    elif numero_de_saques >= LIMITE_SAQUES:
        print("Número máximo de saques diários atingido.")
    elif valor > limite:
        print(f"O valor excede o limite de saque diário de R$ {limite:.2f}")
    else:
        saldo -= valor
        numero_de_saques += 1
        extrato_list.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")


def mostrar_extrato():
    print("\n=== EXTRATO ===")
    if not extrato_list:
        print("Nenhuma operação realizada.")
    else:
        for registro in extrato_list:
            print(registro)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===============")


while True:
    opcao = input(menu).lower()

    if opcao == "d":
        try:
            valor = float(input("Digite o valor do depósito: "))
            depositar(valor)
        except ValueError:
            print("Valor inválido. Digite um número.")

    elif opcao == "s":
        try:
            valor = float(input("Digite o valor do saque: "))
            sacar(valor)
        except ValueError:
            print("Valor inválido. Digite um número.")

    elif opcao == "e":
        mostrar_extrato()

    elif opcao == "q":
        print("Você escolheu SAIR")
        print("Obrigado, volte sempre!")
        for numeros_enfeite in range(10):
            print(f"Fechando o sistema {numeros_enfeite}...", end="\r")
            time.sleep(0.2)
        break  

    else:
        print("Selecione uma das opções disponíveis, por favor...")
