menu = '''

Digite 1 para Depósito:
Digite 2 para Saque:
Digite 3 para Extrato:
Digite 4 para Sair:

=> '''

saldo = 0
limitepsaque = 500
extrato = ""
contSaque = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Qual valor do depósito? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Falha na operação!! Valor informado é inválido!")

    elif opcao == 2:
        valor = float(input("Qual valor do saque? "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limitepsaque

        excedeu_saques = contSaque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação!! saldo insuficiente!")
        
        elif excedeu_limite:
            print("Falha na operação!! Valor do saque excede limite!")

        elif excedeu_saques:
            print("Falha na operação!! Saques diário excedidos!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            contSaque += 1

        else:
            print("Falha na operação!! Valor informado é inválido!")
        

    elif opcao == 3:
        print("\n********** EXTRATO **********")
        print("Não foram realizadas operações!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("*******************************")

    elif opcao == 4:
        print("Obrigado por usar nosso serviço, Volte sempre!")
        break

    else:
        print("Operação inválida, favor selecionar a opção desejada! ")