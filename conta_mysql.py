import datetime
# import mysql.connector
from banco_mysql import Banco


# class Historico:
#     def __init__(self):
#         self.data_abertura = datetime.datetime.today()
#         self.conexao = self.criar_conexao(
#             "127.0.0.1", "root", "Ch,123,carlao", "db_banco")
#         self.cursor = self.conexao.cursor()
#         self.cria_tabela()

#     def cria_tabela(self):
#         sql = """CREATE TABLE IF NOT EXISTS transacoes (
#                     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#                     conta_numero INT NOT NULL,
#                     descricao VARCHAR(255) NOT NULL,
#                     FOREIGN KEY (conta_numero) REFERENCES contas(numero));"""
#         self.cursor.execute(sql)
#         self.conexao.commit()

#     def criar_conexao(self, host, usuario, senha, banco):
#         return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

#     def fechar_conexao(self, con):
#         return con.close()

#     def retorna_descricao(self, numero):
#         sql = f"""SELECT descricao from transacoes WHERE id={numero}"""
#         self.cursor.execute(sql)
#         return self.cursor

#     def adiciona_transacao(self, conta_numero, descricao):
#         desc = self.retorna_descricao(conta_numero)
#         desc.append(descricao)
#         sql = "INSERT INTO transacoes (conta_numero, descricao) VALUES (%s, %s)"
#         valores = (conta_numero, desc)
#         self.cursor.execute(sql, valores)
#         self.conexao.commit()
#         self.fechar_conexao(self.conexao)
#         return True

#     def imprime(self, numero):
#         var = f'Data de Abertura: {self.data_abertura}\nTransações: \n'
#         self.cursor.execute(self.sql)
#         self.cursor.execute(f"SELECT * FROM transacoes WHERE conta_numero={numero}")
#         for t in self.cursor:
#             var += f'- {t}\n'

#         return var


class Conta:
    total_contas = 0

    __slots__ = ['conexao', 'cursor', 'sql', '_usuario', '_senha', '_numero', '_titular',
                 '_saldo', '_limite', '_historico', '_confereTrans']

    def __init__(self, usuario, senha, numero, titular, saldo, limite=1000.00):
        self._usuario = usuario
        self._senha = senha
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        # self._historico = Historico()
        self._banco = Banco()
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

    # @property
    # def historico(self):
    #     return self._historico

    # @historico.setter
    # def historico(self, value):
    #     self._historico = value
        
    @property
    def banco(self):
        return self._banco

    @banco.setter
    def banco(self, valor):
        self._banco = valor

    @staticmethod
    def get_total_contas():
        return Conta.total_contas


    # Função para fazer deposito de um valor na conta: Essa função retornará True se
    # a transação ocorrer ou False se der algum problema no deposito
    def depositar(self, numero, valor, senha):
        print("ENTROU NO DEPOSITAR")
        saldo = self.banco.pega_saldo(numero) # a variavel saldo vai conter o saldo atual e o limite da conta
        if valor >= 0.01 and (saldo[0][0] + valor <= saldo[0][1]):
            if self.banco.verificaSenha(senha, numero):
                self.banco.atualiza_saldo(numero, valor)
                if self.confereTrans == 0:
                    if saldo:
                        his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Deposito de R${valor}'
                        self.banco.atualiza_hist(numero, his)
                else:
                    self.confereTrans = 0
                return True, "Deposito realizado com sucesso."
            return False, "Senha invalida."
        else:
            if self.confereTrans == 0:
                his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Falha no deposito'
                self.banco.atualiza_hist(numero, his)
            else:
                self.confereTrans = 0
            return False, "Não foi possível fazer o deposito."

    # Função para fazer saque de um valor na conta: Essa função retornará True se
    # a transação ocorrer ou False se der algum problema no saque
    def sacar(self, numero, valor, senha):
        saldo = self.banco.pega_saldo(numero)
        if saldo[0][0] < valor or valor < 0.01:
            if self.confereTrans == 0:
                his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Falha no saque'
                self.banco.atualiza_hist(numero, his)
            else:
                self.confereTrans = 0
            return False, "Valor maior que o saldo ou valor menor que 0."
        else:
            if self.banco.verificaSenha(senha, numero):
                self.banco.atualiza_saldo(numero, valor, False)
                if self.confereTrans == 0:
                    if saldo:
                        his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Saque de R${valor}'
                        self.banco.atualiza_hist(numero, his)
                else:
                    self.confereTrans = 0
                return True, "Saque realizado com sucesso."
            return False, "Senha invalida."

    # Função para fazer transferencia de uma conta para outra: Essa função retornará True se
    # a transação ocorrer ou False se der algum problema na transferencia
    def transfere(self, numero, senha, destino, valor):
        self.confereTrans = 1
        retirou = self.sacar(numero, valor, senha)
        if retirou[0] == False:
            his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Falha na tranferencia de R${valor} para {destino}'
            self.banco.atualiza_hist(numero, his)
            return False, "Não foi possivel finalizar a transferencia."
        else:
            self.confereTrans = 1
            self.depositar(destino, valor)

            his = f'''{datetime.datetime.today().strftime(
                "DATA: %d/%m/%Y - HORA: %H:%M")}: Tranferencia de R${valor} para {destino}'''
            self.banco.atualiza_hist(numero, his)
            his = f'''{datetime.datetime.today().strftime(
                "DATA: %d/%m/%Y - HORA: %H:%M")}: Transferencia recebida de {numero} no valor de R${valor}'''
            self.banco.atualiza_hist(destino, his)
            return True, "Transferencia realizada com sucesso."

    # Função para retirar o extrato da conta
    def extrato(self, numero):
        saldo = self.banco.pega_saldo(numero)
        print(f'Número: {numero} \n Saldo: {saldo}')
        his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Tirou extrato - saldo R${saldo}'
        self.banco.atualiza_hist(numero, his)