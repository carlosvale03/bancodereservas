class Pessoa:
    __slots__ = ['_nome', '_endereco', '_cpf', '_nascimento']

    def __init__(self, nome, endereco, cpf, nascimento):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._nascimento = nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        self._endereco = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, value):
        self._nascimento = value
