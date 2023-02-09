from conta import Conta
from cliente import Cliente


class Banco:
    def __init__(self):
        self._lista = [Conta("carlos", "123", 100, Cliente("Carlos", "Vale", "123"), 100.0), Conta("dudu", "321", 101, Cliente("Eduardo", "Sousa", "321"), 100.0)]

    @property
    def lista(self):
        return self._lista

    @lista.setter
    def lista(self, lista):
        self._lista = lista

    def cadastra(self, usuario, senha, numero, titular, saldo, limite=1000.00):
        for i in self.lista:
            if i.usuario == usuario:
                return False

        conta = Conta(usuario, senha, numero, titular, saldo, limite=1000.00)
        self.lista.append(conta)
        return True

    def mostrar_contas(self):
        print(self.lista)

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

        for i in self.lista:
            if i.usuario == usuario:
                if i.senha == senha:
                    return True
                return None

        return False

    def excluir(self, numero):
        cont=0
        for i in self.lista:
            if i.numero == numero:
                self.lista.pop(cont)
                return True
            cont+=1