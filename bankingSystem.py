saldo = 0
saqueLimite = 500
extrato = "Extrato da Conta XX\n"
saquesRealizados = 0
dailySaqueLimit = 3

while True:
    selectedChoice = input("Seja bem vindo ao Banco Morningstar. Qual operação deseja realizar?\na- Depósito\nb- Saque\nc- Extrato\nd-Nenhuma, sair.\n")

    if selectedChoice == "a":
        depositValue = float(input("Quanto deseja depositar? "))
        if depositValue >= 0:
            saldo += depositValue ## saldo = saldo + depositValue
            extrato += f"Déposito realizado no valor de R$ {depositValue:.2f}.\n"
            print(f"Depósito realizado com sucesso no valor de {depositValue:.2f}. Seu saldo é de: R${saldo:.2f}\n")
        else:
            print("Valor impossível de ser depositado. Redirecionando ao menu anterior.\n")

    elif selectedChoice == "b":
        if saquesRealizados < dailySaqueLimit:
            saqueRequested = float(input("Quanto você deseja sacar? "))
            if saqueRequested <= saldo:
                saldo -= saqueRequested ## saldo = saldo - saqueRequested
                extrato += f"Saque realizado no valor de R$ {saqueRequested:.2f}. Saldo restante: {saldo:.2f}.\n"
                saquesRealizados += 1
                print(f"Saque realizado com sucesso no valor de {saqueRequested:.2f}. Saldo restante: {saldo:.2f}.\n")
            else:
                print("Seu saldo não é suficiente para realizar o saque. Retornando ao menu anterior.\n")
        else:
            print("Você não possui saques remanescentes, retornando ao menu anterior.\n")
    
    elif selectedChoice == "c":
        print(extrato)
    
    elif selectedChoice == "d":
        print("Obrigado por fazer negócios com Morningstar, tenha um ótimo dia! :)")
        break

    else:
        print("Opção inválida. Retornando ao menu anterior.\n")