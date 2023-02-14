from typing import Type
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from banco_mysql import Banco

from random import randint

from page_cadastro import Page_cadastro
from page_home_conta import Page_home_conta
from widget_confirma_excluir import Page_confirma_excluir
from widget_depositar import Page_depositar
from widget_excluir import Page_excluir
from widget_historico import Page_historico
from widget_login import Ui_login
from widget_sacar import Page_sacar
from widget_transferir import Page_transferir

from servidor_cliente import *


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()

        self.tela_inicial = Ui_login()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastrar = Page_cadastro()
        self.tela_cadastrar.setupUi(self.stack1)

        self.tela_home = Page_home_conta()
        self.tela_home.setupUi(self.stack2)

        self.tela_depositar = Page_depositar()
        self.tela_depositar.setupUi(self.stack3)

        self.tela_sacar = Page_sacar()
        self.tela_sacar.setupUi(self.stack4)

        self.tela_transferir = Page_transferir()
        self.tela_transferir.setupUi(self.stack5)

        self.tela_historico = Page_historico()
        self.tela_historico.setupUi(self.stack6)

        self.tela_excluir = Page_excluir()
        self.tela_excluir.setupUi(self.stack7)

        self.tela_confirma_excluir = Page_confirma_excluir()
        self.tela_confirma_excluir.setupUi(self.stack8)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)


class Main(QMainWindow, Ui_Main):
    """
    A classe Main é uma subclasse da classe QMainWindow e da classe Ui_Main. Essa classe é responsável 
    por implementar a lógica de negócios da aplicação.

    Methods
    -------
    request_server(self, request: str):
        Método responsável por enviar uma solicitação para o servidor e retornar a resposta.

    concatenar(self, string: str):
        Método que recebe uma string contendo as palavras a serem concatenadas. Concatena as palavras de uma string,
        separadas por espaços.

    concatenarHis(self, string: str):
        Concatena as linhas de uma string separadas pelo caractere '\\n'.

    botaoTransferir2(self):
        Função responsável por transferir um valor para outra conta. Essa função é chamada ao 
        clicar no botão "Transferir" na tela de transferência. Ela obtém o valor digitado pelo usuário, 
        o número da conta de destino e a senha do usuário. Em seguida, valida se o valor é numérico e 
        realiza a solicitação de transferência para o servidor. Se a transação for bem-sucedida, exibe uma 
        mensagem de sucesso e atualiza o saldo do usuário.
    
    botaoSacar2(self):
        Realiza a operação de saque na conta do usuário, ao inserir um valor e senha.

    botaoDepositar2(self):
        Realiza a operação de deposito na conta do usuário, ao inserir um valor e senha.

    botaoExcluir2(self):
        A função representa botão excluir que vai chamar a tela de confirmação 
        que a conta será excluida

    botaoConfirmar(self):
        A função representa botão confirmar que a conta será excluida

    botaoVoltaHome(self):
        Função vai fazer com que o usuário volte para a tela home

    botaoExcluir(self):
        Função vai redirecionar para tela de excluir login

    botaoHistorico(self):
        Atualiza a tela de histórico de transações com as informações da conta especificada.

    botaoTransferencia(self):
        Limpa os campos de valor e senha na tela de transferência e muda a exibição para a tela de transferência.

    botaoSacar(self):
        Limpa os campos de valor e senha na tela de saque e muda a exibição para a tela de saque.

    botaoDepositar(self):
        Limpa os campos de valor e senha na tela de deposito e muda a exibição para a tela de deposito.

    botaoSair(self):
        Função vai fazer com que o usuário saia do banco.

    atualizaSaldo(self):
        Função para atalizar o saldo que é mostrado na tela Home sempre que o botão "ocultar saldo" aparecer.

    botaoVerSaldo(self):
        Função para alterar o botão "ver saldo" para "ocultar saldo" e vice versa. 
        Essa função também vai mostrar e ocultar o saldo, dependendo da condição.

    abrirHomeConta(self, usuario: bool, senha: bool):
        Verifica as credenciais de login do usuário e abre a tela principal se o login for bem-sucedido.

    abrirTelaCadastro(self):
        Função para abrir tela de cadastro a partir do botão "cadastrar" na tela de login.
    
    sorteiaNum(self):
        Função para sortear numero aleatorio entre 100 e 1000 para as contas.

    botaoCadastra(self):
        Função para conferir dados passados pelo usuario e cadastra-lo no banco.

    botaoVoltar(self):
        Função para voltar para tela de login.


    Slots
    -----
    Os seguintes Slots são utilizados para conectar os botões das telas com as funções correspondentes:
        - abrirHomeConta
        - abrirTelaCadastro
        - botaoCadastra
        - botaoVoltar
        - botaoVerSaldo
        - botaoSair
        - botaoDepositar
        - botaoSacar
        - botaoTransferencia
        - botaoHistorico
        - botaoExcluir
        - botaoVoltaHome
        - botaoExcluir2
        - botaoConfirmar
        - botaoDepositar2
        - botaoSacar2
        - botaoTransferir2

        Cada slot é responsável por executar uma determinada ação quando o botão correspondente é clicado. As ações
        executadas pelos slots incluem a exibição das telas, a realização das operações bancárias, e o envio de
        solicitações ao servidor.
    """
    def __init__(self):
        """
        Método construtor da classe. É responsável por inicializar os atributos da classe. Além disso, cria uma instância
        da classe Banco, que será utilizada para fazer as operações bancárias. Também tenta se conectar com o servidor
        através da função servidor_cliente, e exibe uma mensagem de erro caso a conexão não seja bem sucedida.
        """
        super(Main, self).__init__(None)
        self.setupUi(self)

        self.banco = Banco()

        try:
            self.server = servidor_cliente('localhost', 8000)
        except ConnectionRefusedError:
            QtWidgets.QMessageBox.information(None, 'ERROR', f'Não foi possível conectar ao servidor.'
                                                             f'\nVerifique a conexão e tente novamente')
            sys.exit()

        self.index = None

        # botões da tela de login
        self.tela_inicial.btn_login.clicked.connect(self.abrirHomeConta)
        self.tela_inicial.btn_cadastrar.clicked.connect(self.abrirTelaCadastro)

        # botões da tela cadastrar
        self.tela_cadastrar.btn_cadastrar.clicked.connect(self.botaoCadastra)
        self.tela_cadastrar.btn_voltar.clicked.connect(self.botaoVoltar)

        # botões da tela Home do banco
        self.tela_home.btn_verSaldo.clicked.connect(self.botaoVerSaldo)
        self.tela_home.btn_sair.clicked.connect(self.botaoSair)
        self.tela_home.btn_depositar.clicked.connect(self.botaoDepositar)
        self.tela_home.btn_sacar.clicked.connect(self.botaoSacar)
        self.tela_home.btn_transferencia.clicked.connect(
            self.botaoTransferencia)
        self.tela_home.btn_historico.clicked.connect(self.botaoHistorico)
        self.tela_home.btn_excluir.clicked.connect(self.botaoExcluir)
        # self.tela_home.btn_transferencia.clicked.connect(self.botaoTransferencia)

        # botões de voltar para a tela Home do banco
        self.tela_depositar.btn_voltar.clicked.connect(self.botaoVoltaHome)
        self.tela_sacar.btn_voltar.clicked.connect(self.botaoVoltaHome)
        self.tela_transferir.btn_voltar.clicked.connect(self.botaoVoltaHome)
        self.tela_historico.btn_voltar.clicked.connect(self.botaoVoltaHome)
        self.tela_excluir.btn_voltar.clicked.connect(self.botaoVoltaHome)

        # botoes nas telas de excluir conta
        self.tela_excluir.btn_excluir.clicked.connect(self.botaoExcluir2)
        self.tela_confirma_excluir.btn_confirma.clicked.connect(
            self.botaoConfirmar)
        self.tela_confirma_excluir.btn_cancelar.clicked.connect(
            self.botaoVoltaHome)

        # Botões das subtelas da Home, exceto historico e excluir
        self.tela_depositar.btn_depositar.clicked.connect(self.botaoDepositar2)
        self.tela_sacar.btn_sacar.clicked.connect(self.botaoSacar2)
        self.tela_transferir.btn_transferir.clicked.connect(
            self.botaoTransferir2)

    def request_server(self, request):
        '''
        Função responsável por enviar uma solicitação para o servidor e retornar a resposta.

        Parameters
        ----------
        request : str
            Uma string que contém o método e os parâmetros da solicitação.

        Returns
        -------
        list
            Uma lista que contém os resultados da solicitação. A primeira posição é um booleano que indica se a 
            solicitação foi bem sucedida ou não. A segunda posição pode conter uma string com informações adicionais 
            dependendo da função do banco.
        '''
        self.server.send(request.encode())
        recv = self.server.recv(2048)
        flag = recv.decode()
        flag = flag.replace("(", "").replace(")", "").replace(
            "[", "").replace("]", "").replace(",", "").replace("'", '').split()
        return flag

    def concatenar(self, string):
        '''
        Concatena as palavras de uma string, separadas por espaços.

        Parameters
        ----------
        string : str
            Uma string contendo as palavras a serem concatenadas.

        Returns
        -------
        str
            Uma string com as palavras concatenadas.
        '''
        noti = ''
        for i in range(1, len(string)):
            noti += string[i] + " "
        return noti

    def concatenarHis(self, string):
        '''
        Concatena as linhas de uma string separadas pelo caractere '\\n'.

        Parameters
        ----------
        string : str
            Uma string contendo as linhas a serem concatenadas.

        Returns
        -------
        str
            Uma string com as linhas concatenadas e separadas por '\\n'.
        '''
        noti = ''
        for i in range(len(string)):
            noti += string[i] + ' '
        noti = noti.split('\\n')
        a = ''
        for i in noti:
            a += i + '\n'
        return a

    def botaoTransferir2(self):
        '''
        Função responsável por transferir um valor para outra conta. Essa função é chamada ao 
        clicar no botão "Transferir" na tela de transferência. Ela obtém o valor digitado pelo usuário, 
        o número da conta de destino e a senha do usuário. Em seguida, valida se o valor é numérico e 
        realiza a solicitação de transferência para o servidor. Se a transação for bem-sucedida, exibe uma 
        mensagem de sucesso e atualiza o saldo do usuário.

        ...
        Parameters
        ----------
            valor(str): valor da transferência
            numDestino(str): número da conta de destino
            senha(str): senha da conta

        Return:
            None.

        '''
        valor = self.tela_transferir.txt_valor.text()
        numDestino = self.tela_transferir.txt_destino.text()
        senha = self.tela_transferir.txt_senha.text()
        try:
            float(valor.replace(",", "."))
            x = True
        except ValueError:
            x = False

        if not(valor == '' or numDestino == '' or senha == ''):
            if x == True:
                valor = "%.2f" % float(valor.replace(",", "."))
                numero = self.tela_home.txt_numero.text()
                solicit = f'transfere*{numero}*{senha}*{numDestino}*{valor}'
                flag = self.request_server(solicit)
                if flag[0]:
                    noti = self.concatenar(flag)
                    QMessageBox.information(
                        None, 'POOII', noti)
                    self.atualizaSaldo()
                    self.botaoVoltaHome()
                    self.tela_transferir.txt_valor.setText('')
                    self.tela_transferir.txt_destino.setText('')
                    self.tela_transferir.txt_senha.setText('')
                else:
                    QMessageBox.information(
                        None, 'POOII', "Senha incorreta!")
            else:
                self.tela_transferir.txt_valor.setText('')
                self.tela_transferir.txt_senha.setText('')
                QMessageBox.information(
                    None, 'POOII', 'O valor digitado deve ser um número!')
        else:
            QMessageBox.information(
                None, 'POOII', 'Todos os campos devem ser preenchidos!')

    def botaoSacar2(self):
        '''
        Realiza a operação de saque na conta do usuário, ao inserir um valor e senha.

        Parameters
        ----------
            valor(str): valor do saque
            senha(str): senha da conta

        '''
        valor = self.tela_sacar.txt_valor.text()
        senha = self.tela_sacar.txt_senha.text()
        try:
            float(valor.replace(",", "."))
            x = True
        except ValueError:
            x = False
        if not(valor == '' or senha == ''):
            if x == True:
                valor = "%.2f" % float(valor.replace(",", "."))
                numero = self.tela_home.txt_numero.text()
                solicit = f'sacar*{numero}*{float(valor)}*{senha}'
                flag = self.request_server(solicit)
                if flag[0]:
                    noti = self.concatenar(flag)
                    QMessageBox.information(
                        None, 'POOII', noti)
                    self.atualizaSaldo()
                    self.botaoVoltaHome()
                    self.tela_transferir.txt_valor.setText('')
                    self.tela_transferir.txt_senha.setText('')
                else:
                    self.tela_transferir.txt_senha.setText('')
                    QMessageBox.information(
                        None, 'POOII', "Senha incorreta!")
            else:
                self.tela_sacar.txt_valor.setText('')
                self.tela_sacar.txt_senha.setText('')
                QMessageBox.information(
                    None, 'POOII', 'O valor digitado deve ser um número!')

        else:
            QMessageBox.information(
                None, 'POOII', 'Todos os campos devem ser preenchidos!')

    def botaoDepositar2(self):
        '''
        Realiza a operação de deposito na conta do usuário, ao inserir um valor e senha.

        Parameters
        ----------
            valor(str): valor do deposito
            senha(str): senha da conta

        '''
        valor = self.tela_depositar.txt_valor.text()
        senha = self.tela_depositar.txt_senha_2.text()
        try:
            float(valor.replace(",", "."))
            x = True
        except ValueError:
            x = False
        if not(valor == '' or senha == ''):
            if x == True:
                numero = self.tela_home.txt_numero.text()
                if self.request_server(f"verificaSenha*{senha}*{numero}"):
                    valor = "%.2f" % float(valor.replace(",", "."))
                    solicit = f'depositar*{numero}*{float(valor)}'
                    flag = self.request_server(solicit)
                    noti = self.concatenar(flag)
                    if flag[0]:
                        QMessageBox.information(
                            None, 'POOII', noti)
                        self.atualizaSaldo()
                        self.botaoVoltaHome()
                        self.tela_depositar.txt_valor.setText('')
                        self.tela_depositar.txt_senha_2.setText('')
                    else:
                        self.tela_depositar.txt_valor.setText('')
                        self.tela_depositar.txt_senha_2.setText('')
                        QMessageBox.information(
                            None, 'POOII', noti)
                else:
                    self.tela_depositar.txt_senha_2.setText('')
                    QMessageBox.information(
                        None, 'POOII', "Senha incorreta!")
            else:
                self.tela_depositar.txt_valor.setText('')
                self.tela_depositar.txt_senha_2.setText('')
                QMessageBox.information(
                    None, 'POOII', 'O valor digitado deve ser um número!')
        else:
            QMessageBox.information(
                None, 'POOII', 'Todos os campos devem ser preenchidos!')

    # funções para confirmação da exclusão de conta

    def botaoExcluir2(self):
        '''
        A função representa botão excluir que vai chamar a tela de confirmação 
        que a conta será excluida

        ...
        Parameters
        ----------
            senha(str): senha do usuário
            numero(str): número da conta

        '''
        senha = self.tela_excluir.txt_senha.text()
        numero = self.tela_home.txt_numero.text()
        if not senha == '':
            solicit = f"verificaSenha*{senha}*{numero}"
            flag = self.request_server(solicit)
            noti = self.concatenar(flag)
            if flag[0] == 'True':
                self.QtStack.setCurrentIndex(8)
            else:
                QMessageBox.information(None, 'POOII', noti)
                self.tela_excluir.txt_senha.setText('')
        else:
            QMessageBox.information(
                None, 'POOII', 'Todos os campos devem ser preenchidos!')

    def botaoConfirmar(self):
        '''
        A função representa botão confirmar que a conta será excluida

        Parameters
        ----------
            numero(str): número da conta
            solict(str): vai pegar uma string contendo o metodo e os atributos que serão passados para o servidor
            flag(list): vai verificar qual foi a solicitação e receber valor booleano na primeira posição e uma 
            string na segunda
            noti(str): vai receber a notificação que será retornada na variavel flag e concatenada

        '''
        numero = self.tela_home.txt_numero.text()
        solicit = f'excluir*{numero}'
        flag = self.request_server(solicit)
        noti = self.concatenar(flag)
        if flag[0] == 'True':
            QMessageBox.information(
                None, 'POOII', noti)
            self.QtStack.setCurrentIndex(0)
        else:
            QMessageBox.information(None, 'POOII', noti)

    # funções para navegar entre a tela Home e suas subtelas

    def botaoVoltaHome(self):
        '''Função vai fazer com que o usuário volte para a tela home'''
        self.QtStack.setCurrentIndex(2)

    def botaoExcluir(self):
        '''Função vai redirecionar para tela de excluir login'''
        self.QtStack.setCurrentIndex(7)

    def botaoHistorico(self):
        '''
        Atualiza a tela de histórico de transações com as informações da conta especificada.

        Parameters
        ----------
            numero(str): número da conta
            solict(str): vai pegar uma string contendo o metodo e os atributos que serão passados para o servidor
            flag(list): vai verificar qual foi a solicitação e receber valor booleano na primeira posição e 
            uma string na segunda
            noti(str): vai receber a notificação que será retornada na variavel flag e concatenada
        '''
        numero = self.tela_home.txt_numero.text()
        solicit = f'pega_hist*{numero}'
        flag = self.request_server(solicit)
        noti = self.concatenarHis(flag)
        self.tela_historico.txt_historico.setText(noti)
        self.QtStack.setCurrentIndex(6)

    def botaoTransferencia(self):
        '''
        Limpa os campos de valor e senha na tela de transferência e muda a exibição para a tela de transferência.
        '''
        self.tela_transferir.txt_valor.setText('')
        self.tela_transferir.txt_senha.setText('')
        self.QtStack.setCurrentIndex(5)

    def botaoSacar(self):
        '''
        Limpa os campos de valor e senha na tela de saque e muda a exibição para a tela de saque.
        '''
        self.tela_sacar.txt_valor.setText('')
        self.tela_sacar.txt_senha.setText('')
        self.QtStack.setCurrentIndex(4)

    def botaoDepositar(self):
        '''
        Limpa os campos de valor e senha na tela de deposito e muda a exibição para a tela de deposito.
        '''
        self.tela_depositar.txt_valor.setText('')
        self.tela_depositar.txt_senha_2.setText('')
        self.QtStack.setCurrentIndex(3)

    def botaoSair(self):
        '''
        Função vai fazer com que o usuário saia do banco.
        '''
        self.QtStack.setCurrentIndex(0)

    # função para atalizar o saldo que é mostrado na tela Home

    def atualizaSaldo(self):
        '''
        Função para atalizar o saldo que é mostrado na tela Home sempre que o botão "ocultar saldo" aparecer.

        Parameters
        ----------
            numero(str): número da conta
            solict(str): vai pegar uma string contendo o metodo e os atributos que serão passados para o servidor
            flag(list): vai verificar qual foi a solicitação e receber valor booleano na primeira posição e 
            uma string na segunda
        '''
        if self.tela_home.url_verSaldo == ("\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "image: url(banco_interface/imgs/svgviewer-output2.svg);\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}"):
            numero = self.tela_home.txt_numero.text()
            solicit = f'pega_saldo*{numero}'
            flag = self.request_server(solicit)
            self.tela_home.txt_saldo.setText(f"R$ {float(flag[0]):.2f}")

    # função para utilizar o botao de ver e ocultar o saldo
    def botaoVerSaldo(self):
        '''
        Função para alterar o botão "ver saldo" para "ocultar saldo" e vice versa. 
        Essa função também vai mostrar e ocultar o saldo, dependendo da condição.
        '''
        _translate = QtCore.QCoreApplication.translate
        if self.tela_home.url_verSaldo == ("\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "image: url(banco_interface/imgs/svgviewer-output.svg);\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}"):
            self.tela_home.url_verSaldo = (
                "\n"
                "\n"
                "QPushButton{\n"
                "image: url(banco_interface/imgs/svgviewer-output2.svg);\n"
                "border-radius: 5px;\n"
                "}\n"
                "\n"
                "QPushButton:hover{\n"
                "background-color: rgb(255, 255, 255);\n"
                "    color: rgb(0, 0, 0);\n"
                "}")
            self.tela_home.btn_verSaldo.setStyleSheet(
                self.tela_home.url_verSaldo)
            self.tela_home.btn_verSaldo.setToolTip(_translate(
                "MainWindow", "<html><head/><body><p>Ocultar saldo</p></body></html>"))
            self.atualizaSaldo()
        elif self.tela_home.url_verSaldo == ("\n"
                                             "\n"
                                             "QPushButton{\n"
                                             "image: url(banco_interface/imgs/svgviewer-output2.svg);\n"
                                             "border-radius: 5px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "background-color: rgb(255, 255, 255);\n"
                                             "    color: rgb(0, 0, 0);\n"
                                             "}"):
            self.tela_home.url_verSaldo = (
                "\n"
                "\n"
                "QPushButton{\n"
                "image: url(banco_interface/imgs/svgviewer-output.svg);\n"
                "border-radius: 5px;\n"
                "}\n"
                "\n"
                "QPushButton:hover{\n"
                "background-color: rgb(255, 255, 255);\n"
                "    color: rgb(0, 0, 0);\n"
                "}")
            self.tela_home.btn_verSaldo.setStyleSheet(
                self.tela_home.url_verSaldo)
            self.tela_home.btn_verSaldo.setToolTip(_translate(
                "MainWindow", "<html><head/><body><p>Ver saldo</p></body></html>"))
            self.tela_home.txt_saldo.setText("")

    
    def abrirHomeConta(self, usuario=False, senha=False):
        '''
        Verifica as credenciais de login do usuário e abre a tela principal se o login for bem-sucedido.

        Parameters
        ----------
            usuario (bool): Nome de usuário do cliente (opcional). Se não for especificado, 
            o nome de usuário da caixa de texto da tela inicial será usado.
            senha (bool): Senha do cliente (opcional). Se não for especificado, a senha da 
            caixa de texto da tela inicial será usada.

        Return:
            None.
        '''
        if usuario == False and senha == False:
            usuario = self.tela_inicial.txt_usuario.text()
            senha = self.tela_inicial.txt_senha.text()
        if not(usuario == '' or senha == ''):
            solicit = f'login*{usuario}*{senha}'
            flag = self.request_server(solicit)
            if flag[0] == 'True':
                self.tela_inicial.txt_usuario.setText('')
                self.tela_inicial.txt_senha.setText('')
                self.tela_home.txt_ola_nome.setText(
                    f'Olá, {flag[1]}!')
                self.tela_home.txt_limite.setText(f'R$ {float(flag[5])}')
                self.tela_home.txt_numero.setText(f'{int(flag[4])}')
                self.atualizaSaldo()
                self.QtStack.setCurrentIndex(2)
            else:
                noti = self.concatenar(flag)
                QMessageBox.information(
                    None, 'POOII', noti)
        else:
            QMessageBox.information(
                None, 'POOII', 'Todos os campos devem ser preenchidos!')


    def abrirTelaCadastro(self):
        '''
        Função para abrir tela de cadastro a partir do botão "cadastrar" na tela de login.
        '''
        self.QtStack.setCurrentIndex(1)

    
    def sorteiaNum(self):
        '''
        Função para sortear numero aleatorio entre 100 e 1000 para as contas.

        Parameters
        ----------
            num(int): Variável representa um número que será sorteado.

        Return:
            Número que foi sorteado.
        '''
        num = randint(100, 1000)
        if not num in self.lista:
            self.lista.append(num)
            return num
        self.sorteiaNum()


    def botaoCadastra(self):
        '''
        Função para conferir dados passados pelo usuario e cadastra-lo no banco.

        Parameters
        ----------
            usuario(str): Nome de usuário.
            senha(str): Senha do usuário.
            nome(str): Nome do usuário.
            sobrenome(str): Sobrenome do usuário.
            cpf(str): CPF do usuário.

        Return:
            None.

        Examples:
            Se o usuário tiver digitado todos os dados obrigatórios para o cadastro, a função vai 
            fazer as verificações necessárias e se tudo der certo o usuário já vai ter acesso a 
            página home do banco. Se não der certo a função vai informar ao usuário os erros que ele cometeu.
        '''
        usuario = self.tela_cadastrar.txt_usuario.text()
        senha = self.tela_cadastrar.txt_senha.text()
        nome = self.tela_cadastrar.txt_nome.text()
        sobrenome = self.tela_cadastrar.txt_sobrenome.text()
        cpf = self.tela_cadastrar.lineEdit_5.text()

        if not(usuario == '' or senha == '' or nome == '' or sobrenome == '' or cpf == ''):
            name = nome + ' ' + sobrenome
            if cpf.isdigit() and len(cpf) == 11:
                solicit = f'cadastra*{usuario}*{senha}*{name}*{cpf}'
                flag = self.request_server(solicit)
                noti = self.concatenar(flag)
                QMessageBox.information(
                    None, 'POO-II', noti)
                self.tela_cadastrar.txt_usuario.setText('')
                self.tela_cadastrar.txt_senha.setText('')
                self.tela_cadastrar.txt_nome.setText('')
                self.tela_cadastrar.txt_sobrenome.setText('')
                self.tela_cadastrar.lineEdit_5.setText('')
                self.abrirHomeConta(usuario, senha)
            else:
                QMessageBox.information(
                    None, 'POOII', 'O CPF não atende aos parametros!')
        else:
            QMessageBox.information(
                None, 'POOII', 'Todos os campos devem ser preenchidos!')

    def botaoVoltar(self):
        '''
        Função para voltar para tela de login.
        '''
        self.QtStack.setCurrentIndex(0)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
