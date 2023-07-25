menu = """
---------------------------
    [1] Depositar.
    [2] Sacar.
    [3] Extrato
    [4] Sair
---------------------------    
"""
saldo = 0
extrato = ''
numero_saques = 0

while True:
    opcao = int(input(menu))
    if opcao == 1: #aqui sera feito a parte do deposito            
        valor = 0
        valor = float(input('Quanto você deseja depositar? \n'))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
    
    if opcao == 2: #valor a ser sacado
        print(f'Você tem em sua conta {saldo}')
        print('Deseja sacar?')
        decisao = str(input('Digite [S] para SIM. Digite [N] para NÃO\n')).upper()
        
        if decisao == 'S':
            if numero_saques < 3:
                valor_saque = float(input('Qual o valor de que você deseja sacar? \n'))
                if valor_saque <= 500:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += f'Saque: R$ {valor_saque:.2f}\n'
                    print(f'Agora você tem {saldo} de saldo.')
                    print(f'Você já realizou {numero_saques} no dia.')
                else:
                    print('Valor máximo para o saque é R$500,00.')
            else:
                print('VOCÊ JÁ REALIZOU O LIMITE DE 3 SAQUES DIÁRIOS!!!!')
        else: 
            menu

    if opcao == 3:#extrato da conta
        print('-='*9, 'EXTRATO', '-='*9,)
        print('Não forma realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('-='*23)

    if opcao == 4:
        break
print("FIM")