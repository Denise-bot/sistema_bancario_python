LIMITE_SAQUE = 500
LIMITE_SAQUES_DIARIOS = 3
SENHA_CORRETA = "1234"

def menu():
    print("\n=== Sistema Bancário ===")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

def autenticar():
    senha = input("Digite sua senha: ")
    return senha == SENHA_CORRETA

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: R$ "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: +R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    if numero_saques >= LIMITE_SAQUES_DIARIOS:
        print("Limite de saques diários atingido.")
        return saldo, extrato, numero_saques

    valor = float(input("Informe o valor do saque: R$ "))
    
    if valor <= 0:
        print("Valor inválido para saque.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > LIMITE_SAQUE:
        print(f"Limite máximo por saque é R$ {LIMITE_SAQUE:.2f}.")
    else:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
        
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n=== Extrato ===")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")

def main():
    saldo = 0.0
    extrato = []
    numero_saques = 0

    print("Bem-vindo ao Banco Digital!")

    if not autenticar():
        print("Senha incorreta. Encerrando...")
        return

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
        elif opcao == "3":
            mostrar_extrato(saldo, extrato)
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
