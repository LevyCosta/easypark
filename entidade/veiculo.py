class Veiculo:

    def __init__(self, tipo_veiculo, placa=0, desconto=0):
        self.__tipo_veiculo = tipo_veiculo
        self.__placa = placa
        self.__desconto = desconto

    def setTipoVeiculo(self, tipo_veiculo):
        self.__tipo_veiculo = tipo_veiculo

    def getTipoVeiculo(self):
        return self.__tipo_veiculo

    def setPlaca(self, placa):
        self.__placa = placa

    def getPlaca(self):
        return self.__placa



