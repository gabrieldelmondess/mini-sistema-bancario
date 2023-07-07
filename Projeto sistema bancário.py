menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques: int = 0
limite_saques: int = 3

while True:

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Insira o valor que deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += "Depósito efetuado no valor de R$: {valor:.2f}"
            print ("Depósito efetuado com sucesso!")
        else: 
            print("Operação falho: Valor inválido para depósito")


    elif opcao == "s":
        valor = float(input("Insira o valor que deseja sacar: "))

        sem_saldo = valor > saldo

        sem_limite = valor > limite

        sem_saque = numero_saques >= limite_saques

        if sem_saldo:
            print("Operalçao falhou: Sem saldo disponível")
        
        elif sem_limite:
            print("Operação falhou: Sem limite diponivel")
        
        elif sem_saque: 
            print("Operação falhou: O usuário excedeu o limite de saque")
        
        elif valor > 0:
            saldo -= valor
            extrato += "Saque efetuado no valor de R$: {valor:.2f}"
            numero_saques += 1
            print("Saque efetuado com sucesso")

        else:
            print("Operação falho: Valor inválido para saque")

    elif opcao == "e":
        print("\n============= EXTRATO =============")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "q":
        break

else:
    print("Operação inválida: Por favor selecione novamente a operação desejada")
