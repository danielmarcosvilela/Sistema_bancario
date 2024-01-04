

menu = """
########## MENU ##########

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

##########################
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor invalido")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Saque ultrapassa o limite!")
        elif excedeu_saques:
            print("Ultrapassou limite de saques!")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1 
        else:
            print("Valor informado invalido!")
            
    elif opcao == "e":
        print("\n########## EXTRATO ##########")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###############################")
        
    elif opcao == "q":
        break
    
    else:
        print("Por favor selecione a operação desejada")