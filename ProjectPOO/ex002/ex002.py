
class Conta_bancaria:
    contador = 1
    def __init__(self, nome = '', saldo = 0):
        self.id = Conta_bancaria.contador
        Conta_bancaria.contador += 1
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f'A conta numero: {self.id} de {self.titular} possui R${self.saldo:,.2f}'

    def depositar(self, valor):
        self.saldo += valor
        return f'Depósito de {valor:.2f} realizado com sucesso, novo saldo: {self.saldo:,.2f}'

    def sacar(self, valor):
        if valor > self.saldo:
            return 'Saldo insuficiente'
        else:
            self.saldo -= valor
            return f'Saque de {valor:,.2f} autorizado com sucesso, novo saldo: {self.saldo:,.2f}'

contas = []

def criarContas():
    nome = input('Digite o nome do conta: ')
    saldo = float(input('Digite o saldo do conta: '))

    conta = Conta_bancaria(nome,saldo)
    contas.append(conta)
    print(f'Conta criada com ID: {conta.id}')

def buscar_conta(numero):
    for conta in contas:
        if conta.id == numero:
            return conta
    return None

def ver_saldo():
    numero = int(input('Digite o número da conta: '))
    conta = buscar_conta(numero)

    if conta:
        print(f'Saldo atual: R${conta.saldo:,.2f}')
    else:
        print('Conta não encontrada')

criarContas()
ver_saldo()