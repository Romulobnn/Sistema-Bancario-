


menu = """
    ======Menu======
    |              |
    |[a] Depositar |
    |[s] Sacar     |
    |[d] Extrato   |
    |[f] Sair      |
    ================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "a":
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:                                  # verificando se o calor informado é maior que 0
            saldo += valor                             # soma o valor com o saldo em conta
            extrato += f"Depósito: R$ {valor:.2f}\n"   # concateno a str com valor formatodo com 2 casas decimais

        else:
            print("OPERAÇÂO FALHOU! Verifique o valor informado.") # caso n seja maior que 0, recebera essa mensagem

    elif opcao == "s":                                           # Condicionais para falhas
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("OPERAÇÂO FALHOU! você não tem saldo suficiente.")

        elif excedeu_limite:
            print("OPERAÇÃO FALHOU! o valor do saque excede o limite.")

        elif excedeu_saques:
            print("OPERAÇÂO FALOU! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("OPERAÇÂO FALHOU!  Verifique o valor informado.")

    elif opcao == "d":
        print("\n =====extrato=====")
        print("Não foram realizados movimentações."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================")

    elif opcao =="f":
         break
    else:
        print("OPERAÇÂO INVÁLIDA, POR FAVOR SELECIONE NOVAMENTE A OPERAÇÂO DESEJADA.")