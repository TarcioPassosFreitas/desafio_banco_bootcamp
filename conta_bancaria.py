class ContaBancaria:
    def __init__(self, numero_agencia, numero_conta):
        self.numero_agencia = numero_agencia
        self.numero_conta = numero_conta
        self.saldo = 0.0
        self.transacoes = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(('Depósito', valor))
            print(f"Depósito de R$: {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saques_diarios >= 3:
            print("Limite de saques diários atingido.")
            return
        if valor > 500:
            print("O limite máximo por saque é de R$: 500,00.")
            return
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append(('Saque', valor))
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para o saque.")

    def extrato(self):
        print(f"\nExtrato - Ag: {self.numero_agencia} Conta: {self.numero_conta}")
        for operacao, valor in self.transacoes:
            print(f"{operacao}: R$: {valor:.2f}")
        print(f"Saldo atual: R$: {self.saldo:.2f}")
        print(f"Total de operações: {len(self.transacoes)}\n")