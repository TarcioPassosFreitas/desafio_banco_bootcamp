from conta_bancaria import ContaBancaria

def main():
    minha_conta = ContaBancaria('1234', '56789')

    while True:
        print('1 - Depósito')
        print('2 - Saque')
        print('3 - Extrato')
        print('4 - Sair')

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            valor = float(input('Digite o valor para depósito: '))
            minha_conta.depositar(valor)
        elif opcao == 2:
            valor = float(input('Digite o valor para saque: '))
            minha_conta.sacar(valor)
        elif opcao == 3:
            minha_conta.extrato()
        elif opcao == 4:
            break
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    main()