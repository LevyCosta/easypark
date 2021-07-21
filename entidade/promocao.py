
class Promocao:

    def __init__(self, tipoVeiculo, desconto=0):
        self.__tipoVeiculo = tipoVeiculo
        self.__desconto = desconto

    def getTipoVeiculo(self):
        return self.__tipoVeiculo

    def setTipoVeiculo(self, tipo):
        self.__tipoVeiculo = tipo

    def getDesconto(self):
        return self.__desconto

    def setDesconto(self, novoDesconto):
        self.__desconto = novoDesconto

