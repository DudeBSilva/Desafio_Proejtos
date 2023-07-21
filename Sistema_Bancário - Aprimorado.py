menu = '''

Escolha uma opção!

[1] Depósito:
[2] Saque:
[3] Extrato:
[4] Cadastrar Novo Usuário:
[5] Abrir Conta:
[6] Listar as Contas
[7] Sair:

=> '''

saldo = 0
limitepsaque = 500
extrato = ""
contSaque = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
clientes = []
contas = []

def deposito(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Falha na operação!! Valor informado é inválido!")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limitepsaque, contSaque):

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

    return saldo, extrato

def mostra_extrato(saldo, /, *, extrato):

    print("\n********** EXTRATO **********")
    print("Não foram realizadas operações!" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("*******************************")

def cad_usuario(clientes):
    cpf = input("Digite seu CPF - [Só números]: ")
    usuario = filtro_cpf(cpf, clientes) # filtrar cpf

    if usuario:
        print("CPF já cadastrado!!")
        return
    
    nome = input("Digite seu nome completo: ")
    nascimento = input("Digite sua data de nascimento - [dd-mm-aaaa]: ")
    endereco = input("Digite seu endereço completo: ")

    clientes.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!!")

def filtro_cpf(cpf, clientes):
    clientes_flitro = [usuario for usuario in clientes if usuario["cpf"] == cpf]
    return clientes_flitro[0] if clientes_flitro else None
  
def abrir_conta(agencia, numero_conta, clientes):
    cpf = input("Digite o CPF do cliente: ")
    usuario = filtro_cpf(cpf, clientes)

    if usuario:
        print("Conta aberta com sucesso!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, processo encerrado!!")

def mostrar_contas(contas):
    for conta in contas:
        print (f"""\
            Agência:\t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """)
        print("-" * 100)


while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Qual valor do depósito? "))

        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == 2:

        valor = float(input("Qual valor do saque? "))
    
        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limitepsaque=limitepsaque, contSaque=contSaque)

    elif opcao == 3:
        
        mostra_extrato(saldo, extrato=extrato)

    elif opcao == 4:
        cad_usuario(clientes)

    elif opcao == 5: 
        numero_conta = len(contas) + 1
        conta = abrir_conta(AGENCIA, numero_conta, clientes)

        if conta:
            contas.append(conta)

    elif opcao == 6:
        mostrar_contas(contas)

    elif opcao == 7:
        print("Obrigado por usar nosso serviço, Volte sempre!")
        break

    else:
        print("Operação inválida, favor selecionar a opção desejada! ")