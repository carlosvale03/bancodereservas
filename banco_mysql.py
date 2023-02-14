import mysql.connector
import datetime
from random import randint
import threading

# from conta_mysql import Conta
# from cliente import Cliente


class Banco:
    '''
    Essa é uma classe que representa o banco.

    Atributos
    ---------
    conexao : mysql connector
    sql : cursor
    confereTrans : int
    sincroniza : 
    '''
    __slots__ = ["conexao", "cursor", "sql", "_confereTrans", "sincroniza"]

    def __init__(self):
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

    def fechar_conexao(self, con):
        """
        Fecha a conexão com o banco de dados.

        Parametros
        ----------
        con : objeto de conexão do banco de dados
            A conexão que será fechada.

        Returns
        -------
        None
        """
        return con.close()

    def cadastra(self, usuario, senha, nome, cpf, saldo=0.0, limite=1000.00):
        """
        Registra um novo usuário no sistema, com as informações fornecidas.

        Parametros
        ----------
        usuario : str
            Nome de usuário do novo usuário
        senha : str
            Senha do novo usuário
        nome : str
            Nome do novo usuário
        cpf : str
            CPF do novo usuário
        saldo : float, opcional
            Saldo inicial da conta do novo usuário (padrão é 0.0)
        limite : float, opcional
            Limite de crédito da conta do novo usuário (padrão é 1000.00)

        Returns
        -------
        tuple
            Um tuple contendo um booleano e uma mensagem de status. 
            O booleano indica se o cadastro foi realizado com sucesso ou não. 
            A mensagem de status contém informações adicionais sobre o resultado do cadastro.
        """
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
        '''
        A função realiza o login de um usuário de acordo com as informações fornecidas.

        ...
        Parâmetros
        ---------
            usuario : str 
                O nome do usuário
            senha : str 
                A senha do usuário

        Retorno:
        --------
            Se as formações fornecidas forem válidas, a função vai retornar um valor booleano True e um object tupla como com informações da conta do usuário.
            Se não retorna uma tupla com valor booleano False e uma mensagem de erro.

        '''
        verifica = self.verificarUsuario(usuario, senha, False)
        if verifica[0]:
            self.cursor.execute(
                f'select titular, saldo, numero, limite from usuarios where usuario = "{usuario}"')
            resul = self.cursor.fetchall()
            return True, resul
        else:
            return verifica

    def verificaSenha(self, senha, numero):
        """
        Verifica se a senha é válida para um determinado número de conta.

        Parametros
        ----------
        senha : str
            A senha a ser verificada.
        numero : int
            O número da conta cuja senha será verificada.

        Returns
        -------
        tuple
            Uma tupla contendo um valor booleano que indica se a senha é válida e uma mensagem de status.
        """
        self.cursor.execute(
            f'select usuario from usuarios where numero = {numero}')
        verifica = self.cursor.fetchall()
        confirma = self.verificarUsuario(verifica[0][0], senha, False)
        if confirma[0]:
            return True, "Ok"
        else:
            return False, "Senha incorreta"

    def verificarUsuario(self, usuario, senha=None, usuarioSenha=True):
        """
        Verifica se um usuário ou um usuário e senha são válidos.

        Parametros
        ----------
        usuario : str
            O nome de usuário a ser verificado.
        senha : str, optional
            A senha a ser verificada (padrão é None).
        usuarioSenha : bool, optional
            Indica se a verificação será feita apenas no nome de usuário (True) ou se incluirá a senha (False).

        Returns
        -------
        se usuarioSenha for True:
            booleano
                Um valor booleano que indica se o usuario está cadastrado no banco de dados
        se usuarioSenha for False:
            tuple
                Uma tupla contendo um valor booleano que indica se o usuário ou usuário/senha 
                são válidos e uma mensagem de status.
        """
        if usuarioSenha:
            self.cursor.execute(
                f'SELECT usuario FROM usuarios WHERE usuario = "{usuario}"')
            v_existe = self.cursor.fetchall()
            if v_existe:
                return True
            return False
        else:
            self.cursor.execute(
                f'SELECT usuario, senha FROM usuarios WHERE usuario = "{usuario}" and senha = MD5("{senha}")')
            v_existe = self.cursor.fetchall()
            if v_existe:
                return True, 'Existe.'
            return False, 'Usuário e/ou senha não cadastrados'


    def verificarNumero(self, numero):
        """
        Verifica se o número existe no banco de dados.

        Parametros
        ----------
        numero : int
            O número da conta cuja será verificado.

        Returns
        -------
        booleano
            Um valor booleano que indica se o número existe ou não no banco de dados.
        """
        self.cursor.execute(
            f'SELECT numero FROM usuarios WHERE numero = "{numero}"')
        verifica = self.cursor.fetchall()
        if verifica:
            return True
        else:
            return False

    def verificarCPF(self, cpf):
        """
        Verifica se o cpf existe no banco de dados.

        Parametros
        ----------
        cpf : str
            O cpf que será verificado.

        Returns
        -------
        booleano
            Um valor booleano que indica se o cpf existe ou não no banco de dados.
        """
        self.cursor.execute(f'SELECT cpf FROM usuarios WHERE cpf = "{cpf}"')
        verifica = self.cursor.fetchall()
        if verifica:
            return True
        else:
            return False

    def atualiza_hist(self, numero, his):
        """
        Atualiza o histórico de transações de uma determinada conta.

        Parametros
        ----------
        numero : int
            O número da conta cujo histórico será atualizado.
        his : str
            A transação a ser adicionada ao histórico.

        Returns
        -------
        None
        """
        hist = self.pega_hist(numero)
        his = hist[0][0] + his
        self.cursor.execute(
            f'update usuarios set historico = "{his}" where numero = {numero}')

    def pega_hist(self, numero):
        """
        Retorna o histórico de transações de uma determinada conta.

        Parametros
        ----------
        numero : int
            O número da conta cujo histórico será retornado.

        Returns
        -------
        list
            Uma lista contendo o histórico de transações.
        """
        self.cursor.execute(
            f'select historico from usuarios where numero = {numero}')
        x = self.cursor.fetchall()
        return x

    def pega_saldo(self, numero):
        """
        Retorna o saldo e limite do usuário, buscando pelo número da conta.

        Parametros
        ----------
        numero : int
            Número da conta do usuário.

        Returns
        -------
        list
            Lista contendo duas tuplas, sendo a primeira referente ao saldo e a segunda ao limite.
            Caso o número da conta seja inválido, retorna False.
        """
        self.cursor.execute(
            f'select saldo, limite from usuarios where numero = {numero}')
        flag = self.cursor.fetchall()
        if flag:
            return flag
        else:
            return False

    def atualiza_saldo(self, numero, valor, operacao=True):
        """
        Atualiza o saldo do usuário, acrescentando ou subtraindo o valor passado como parâmetro.

        Parametros
        ----------
        numero : int
            Número da conta do usuário.
        valor : float
            Valor a ser acrescentado ou subtraído do saldo do usuário.
        operacao : bool, optional
            Indica se a operação é de depósito (True) ou de saque (False). O valor padrão é True.

        Returns
        -------
        None
        """
        saldo = self.pega_saldo(numero)
        if operacao:  # se a operação for true é pq vem da funcao deposito, se nao é pq vem da funcao saque
            valor += saldo[0][0]
        else:
            valor = saldo[0][0] - valor
        self.cursor.execute(
            f'update usuarios set saldo = {valor} where numero = {numero}')

    
    # antiga classe conta

    def depositar(self, numero, valor):
        """
        Realiza um depósito na conta com o número informado.

        Parametros
        ----------
        numero : int
            Número da conta na qual será realizado o depósito.
        valor : float
            Valor a ser depositado na conta.

        Returns
        -------
        tuple
            Um tuple contendo um booleano e uma mensagem de status. O booleano indica se o depósito foi realizado 
            com sucesso ou não. A mensagem de status contém informações adicionais sobre o resultado do depósito.

        Notes
        -----
        A variável `confereTrans` serve para conferir se a função foi chamada a partir da função de transferência 
        (`self.confereTrans == 1`) ou é um depósito normal (`self.confereTrans == 0`).

        Raises
        ------
        ValueError
            Se o valor informado for menor que 0.01.
        ValueError
            Se o saldo atual da conta mais o valor do depósito ultrapassar o limite da conta.
        """
        valor = float(valor)
        # a variavel saldo vai conter o saldo atual e o limite da conta
        saldo = self.pega_saldo(numero)
        if self.confereTrans == 0:
            self.sincroniza.acquire()
        if valor >= 0.01 and (float(saldo[0][0]) + valor <= float(saldo[0][1])):
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

    
    def sacar(self, numero, valor, senha):
        """
        Realiza uma operação de saque na conta corrente.
        
        Parametros
        ----------
        numero : int
            Número da conta corrente do usuário.
        valor : float
            Valor do saque a ser realizado.
        senha : str
            Senha do usuário para autenticação.

        Returns
        -------
        tuple
            Um tuple contendo um booleano e uma mensagem de status. O booleano indica se a operação de saque 
            foi realizada com sucesso ou não. A mensagem de status contém informações adicionais sobre o resultado 
            da operação.
        """
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
