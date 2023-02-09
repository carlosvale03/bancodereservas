import datetime


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        var = f'Data de Abertura: {self.data_abertura}\nTransações: \n'
        for t in self.transacoes:
            var += f'- {t}\n'

        return var


class Conta:
    total_contas = 0

    __slots__ = ['_usuario', '_senha', '_numero', '_titular',
                 '_saldo', '_limite', '_historico', '_confereTrans']

    def __init__(self, usuario, senha, numero, titular, saldo, limite=1000.00):
        self._usuario = usuario
        self._senha = senha
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        # conferir se a operação é uma transferencia para adicionar ao historico
        self._confereTrans = 0
        Conta.total_contas += 1

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @property
    def confereTrans(self):
        return self._confereTrans

    @confereTrans.setter
    def confereTrans(self, valor):
        self._confereTrans = valor

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, value):
        self._historico = value

    @staticmethod
    def get_total_contas():
        return Conta.total_contas

    # Função para fazer deposito de um valor na conta: Essa função retornará True se
    # a transação ocorrer ou False se der algum problema no deposito
    def depositar(self, valor):
        if valor >= 0.01 and (self.saldo + valor <= self.limite):
            self.saldo += valor
            if self.confereTrans == 0:
                self.historico.transacoes.append(
                    f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Deposito de R${valor}')
            else:
                self.confereTrans = 0
            return True
        else:
            if self.confereTrans == 0:
                self.historico.transacoes.append(
                    f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Falha no deposito')
            else:
                self.confereTrans = 0
            return False

    # Função para fazer saque de um valor na conta: Essa função retornará True se
    # a transação ocorrer ou False se der algum problema no saque
    def sacar(self, valor):
        if self.saldo < valor or valor < 0.01:
            if self.confereTrans == 0:
                self.historico.transacoes.append(
                    f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Falha no saque')
            else:
                self.confereTrans = 0
            return False
        else:
            self.saldo -= valor
            if self.confereTrans == 0:
                self.historico.transacoes.append(
                    f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Saque de R${valor}')
            else:
                self.confereTrans = 0
            return True

    # Função para fazer transferencia de uma conta para outra: Essa função retornará True se
    # a transação ocorrer ou False se der algum problema na transferencia
    def transfere(self, destino, valor):
        self.confereTrans = 1
        retirou = self.sacar(valor)
        if retirou == False:
            self.historico.transacoes.append(
                f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Falha na tranferencia de R${valor} para {destino._titular.nome}')
            return False
        else:
            destino.confereTrans = 1
            destino.depositar(valor)
            self._historico.transacoes.append(f'''{datetime.datetime.today().strftime(
                "DATA: %d/%m/%Y - HORA: %H:%M")}: Tranferencia de R${valor} para {destino.titular.nome}''')
            destino._historico.transacoes.append(f'''{datetime.datetime.today().strftime(
                "DATA: %d/%m/%Y - HORA: %H:%M")}: Transferencia recebida de {self.titular.nome} no valor de R${valor}''')
            return True

    # Função para retirar o extrato da conta
    def extrato(self):
        print(f'Número: {self.numero} \n Saldo: {self.saldo}')
        self.historico.transacoes.append(
            f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Tirou extrato - saldo R${self.saldo}')
