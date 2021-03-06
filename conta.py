class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_do_saque):
        valor_limite_saque = self.__saldo + self.__limite
        return valor_do_saque <= valor_limite_saque

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} não pode ser sacado pois ultrapassa o limíte".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        return {'Banco do Brasil': '001', 'Caixa economica Federal': '104', 'Itaú': '341', 'Bradesco':'237'}
