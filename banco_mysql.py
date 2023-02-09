import mysql.connector
import datetime
from random import randint
import threading

# from conta_mysql import Conta
# from cliente import Cliente


class Banco:
    def __init__(self):
        # self.conexao = self.criar_conexao(
        #     "127.0.0.1", "root", "Ch,123,carlao", "db_banco")
        self.conexao = mysql.connector.connect(
            host='127.0.0.1', db='db_banco', user='root', password='Ch,123,carlao', autocommit=True)
        self.cursor = self.conexao.cursor()
        self.sql = """CREATE TABLE IF NOT EXISTS usuarios(cpf char(15) PRIMARY KEY,
        titular text NOT NULL, usuario text NOT NULL, senha text NOT NULL, numero integer UNIQUE NOT NULL,
        saldo float NOT NULL, limite float NOT NULL, historico text NOT NULL);"""
        self._confereTrans = 0
        self.sincroniza = threading.Lock()

    @property
    def confereTrans(self):
        return self._confereTrans

    @confereTrans.setter
    def confereTrans(self, valor):
        self._confereTrans = valor

        # carlos = Conta("carlos", "123", 100, Cliente("Carlos", "Vale", "123"), 100.0).cadastra()
        # eduardo = Conta("dudu", "321", 101, Cliente("Eduardo", "Sousa", "321"), 100.0).cadastra()

    def criar_conexao(self, host, usuario, senha, banco):
        return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco, autocommit=True)

    def fechar_conexao(self, con):
        return con.close()

    def cadastra(self, usuario, senha, nome, cpf, saldo=0.0, limite=1000.00):
        # tratamento de erro para criar tabela usuarios
        try:
            self.cursor.execute(self.sql)
        except mysql.connector.Error as e:
            print("Erro ao criar tabela:", e)

        if not self.verificarCPF(cpf):
            if not self.verificarUsuario(usuario):
                data = datetime.datetime.today().strftime("%d/%m/%y %H:%M")
                while True:
                    numero = randint(100, 999)
                    if not self.verificarNumero(numero):
                        self.numero = numero
                        break
                sql = f'INSERT INTO usuarios(cpf, titular, usuario, senha, numero, saldo, limite, historico) VALUES ("{cpf}", "{nome}", "{usuario}", MD5("{senha}"), {numero}, {saldo}, {limite}, "Data de de abertura: {data}\n\n")'
                self.cursor.execute(sql)
                return True, "Cadastro realizado com sucesso."
            else:
                return False, 'Usuário já está cadastrado.'
        else:
            return False, 'CPF já está cadastrado.'

    def login(self, usuario, senha):
        verifica = self.verificarUsuario(usuario, senha, False)
        if verifica[0]:
            self.cursor.execute(
                f'select titular, saldo, numero, limite from usuarios where usuario = "{usuario}"')
            resul = self.cursor.fetchall()
            return True, resul
        else:
            return verifica

    def verificaSenha(self, senha, numero):
        self.cursor.execute(
            f'select usuario from usuarios where numero = {numero}')
        verifica = self.cursor.fetchall()
        confirma = self.verificarUsuario(verifica[0][0], senha, False)
        if confirma[0]:
            return True, "Ok"
        else:
            return False, "Senha incorreta"

    def verificarUsuario(self, usuario, senha=None, usuarioSenha=True):
        # se usuarioSenha for True é pq vem da funcao da cadastro do usuario
        if usuarioSenha:
            self.cursor.execute(
                f'SELECT usuario FROM usuarios WHERE usuario = "{usuario}"')
            v_existe = self.cursor.fetchall()
            if v_existe:
                return True
            return False
        # se nao, é pq vem da funcao de login
        else:
            self.cursor.execute(
                f'SELECT usuario, senha FROM usuarios WHERE usuario = "{usuario}" and senha = MD5("{senha}")')
            v_existe = self.cursor.fetchall()
            if v_existe:
                return True, 'Existe.'
            return False, 'Usuário e/ou senha não cadastrados'

    def verificarNumero(self, numero):
        self.cursor.execute(
            f'SELECT numero FROM usuarios WHERE numero = "{numero}"')
        verifica = self.cursor.fetchall()
        if verifica:
            return True
        else:
            return False

    def verificarCPF(self, cpf):
        self.cursor.execute(f'SELECT cpf FROM usuarios WHERE cpf = "{cpf}"')
        verifica = self.cursor.fetchall()
        if verifica:
            return True
        else:
            return False

    def atualiza_hist(self, numero, his):
        hist = self.pega_hist(numero)
        his = hist[0][0] + his
        self.cursor.execute(
            f'update usuarios set historico = "{his}" where numero = {numero}')

    def pega_hist(self, numero):
        self.cursor.execute(
            f'select historico from usuarios where numero = {numero}')
        x = self.cursor.fetchall()
        return x

    def pega_saldo(self, numero):
        self.cursor.execute(
            f'select saldo, limite from usuarios where numero = {numero}')
        flag = self.cursor.fetchall()
        if flag:
            return flag
        else:
            return False

    def atualiza_saldo(self, numero, valor, operacao=True):
        saldo = self.pega_saldo(numero)
        if operacao:  # se a operação for true é pq vem da funcao deposito, se nao é pq vem da funcao saque
            valor += saldo[0][0]
        else:
            valor = saldo[0][0] - valor
        self.cursor.execute(
            f'update usuarios set saldo = {valor} where numero = {numero}')

    # antiga classe conta

    def depositar(self, numero, valor):
        valor = float(valor)
        # a variavel saldo vai conter o saldo atual e o limite da conta
        saldo = self.pega_saldo(numero)
        if self.confereTrans == 0:
            self.sincroniza.acquire()
        if valor >= 0.01 and (float(saldo[0][0]) + valor <= float(saldo[0][1])):
            # ANTIGA FUNÇÃO DE DEPOSITO
            self.atualiza_saldo(numero, valor)
            if self.confereTrans == 0:
                if saldo:
                    his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Deposito de R${valor}\n'
                    self.atualiza_hist(numero, his)
                    return True, "Deposito realizado com sucesso."
            else:
                self.confereTrans = 0
        else:
            if self.confereTrans == 0:
                his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Falha no deposito\n'
                self.atualiza_hist(numero, his)
            else:
                self.confereTrans = 0
            return False, "Não foi possível fazer o deposito."

    # Função para fazer saque de um valor na conta: Essa função retornará True se
    # a transação ocorrer ou False se der algum problema no saque
    def sacar(self, numero, valor, senha):
        valor = float(valor)
        saldo = self.pega_saldo(numero)
        self.sincroniza.acquire()
        if saldo[0][0] < valor or valor < 0.01:
            if self.confereTrans == 0:
                his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Falha no saque\n'
                self.atualiza_hist(numero, his)
            else:
                self.confereTrans = 0
            return False, "Valor maior que o saldo ou valor menor que 0."
        else:
            if self.verificaSenha(senha, numero):
                self.atualiza_saldo(numero, valor, False)
                if self.confereTrans == 0:
                    if saldo:
                        his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Saque de R${valor}\n'
                        self.atualiza_hist(numero, his)
                else:
                    self.confereTrans = 0
                return True, "Saque realizado com sucesso."
            return False, "Senha invalida."

    # Função para fazer transferencia de uma conta para outra: Essa função retornará True se
    # a transação ocorrer ou False se der algum problema na transferencia
    def transfere(self, numero, senha, destino, valor):
        valor = float(valor)
        self.confereTrans = 1
        if self.verificarNumero(destino):
            retirou = self.sacar(numero, valor, senha)
            if retirou[0] == False:
                his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Falha na tranferencia de R${valor} para a conta {destino}\n'
                self.atualiza_hist(numero, his)
                return False, "Não foi possivel finalizar a transferencia."
            else:
                self.confereTrans = 1
                self.depositar(destino, valor)

                his = f'''{datetime.datetime.today().strftime(
                    "DATA: %d/%m/%Y - HORA: %H:%M")}: Tranferencia de R${valor} para a conta {destino}\n'''
                self.atualiza_hist(numero, his)
                his = f'''{datetime.datetime.today().strftime(
                    "DATA: %d/%m/%Y - HORA: %H:%M")}: Transferencia recebida da conta {numero} no valor de R${valor}\n'''
                self.atualiza_hist(destino, his)
                return True, "Transferencia realizada com sucesso."
        else:
            return False, "Conta de destino não consta na base de dados."

    # Função para retirar o extrato da conta
    def extrato(self, numero):
        saldo = self.pega_saldo(numero)
        print(f'Número: {numero} \n Saldo: {saldo}')
        his = f'{datetime.datetime.today().strftime("DATA: %d/%m/%Y - HORA: %H:%M")}: Tirou extrato - saldo R${saldo}\n'
        self.atualiza_hist(numero, his)

    def cadastra_bd(self, usuario, senha, numero, titular, saldo, limite, conta):
        self.sincroniza.acquire()
        sql = "INSERT INTO contas (numero, usuario, senha, titular, cpf, saldo, limite, obj_conta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (numero, usuario, senha, titular.nome +
                   " " + titular.sobrenome, titular.cpf, saldo, limite, conta)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        self.fechar_conexao(self.conexao)
        return True

    def operacoes(self, numero):
        for i in self.lista:
            if i.numero == numero:
                return i

    def busca_contas(self, usuario):
        for i in self.lista:
            if i.usuario == usuario:
                return i
        return False

    def busca_contas_num(self, numero):
        for i in self.lista:
            if i.numero == numero:
                return i
        return False

    def busca_usuario(self, usuario, senha):
        # nessa função, se o usuario e a senha forem encontrados vai retornar True
        # se a senha estiver errada vai retornar None e caso o usuario não for
        # encontrado ira retornar False
        self.cursor.execute(self.sql)
        sql = f"SELECT * FROM usuarios"
        self.cursor.execute(sql)
        for i in self.cursor:
            if i[3] == usuario:
                if i[4] == senha:
                    return True
                return None

        return False

    def excluir(self, numero):
        self.sincroniza.acquire()
        sql = f"DELETE FROM usuarios WHERE numero = {numero};"
        self.cursor.execute(sql)
        return True, "Conta excluida com sucesso!"
