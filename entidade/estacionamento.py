import datetime


class Estacionamento():

    def __init__(self, vagasCarro: int, vagasMoto: int):
        self.__cod = 1
        if isinstance(vagasCarro, int):
            self.__vagasCarro = vagasCarro
        if isinstance(vagasMoto, int):
            self.__vagasMoto = vagasMoto
        self.__valorDiariaCarro = 35.0
        self.__valorDiariaMoto = 30.0
        self.__valorHoraCarro = 8.0
        self.__valorHoraMoto = 6.0
        self.__valorPernoiteCarro = 35.0
        self.__valorPernoiteMoto = 30.0
        self.__veiculosEstacionados = []
        self.__mensalistas = []
        self.__promocoes = []
        self.__relatorios = []

    def getVagasCarro(self):
        return self.__vagasCarro

    def setVagasCarro(self, vagas):
        self.__vagasCarro = vagas

    def getVagasMoto(self):
        return self.__vagasMoto

    def setVagasMoto(self, vagas):
        self.__vagasMoto = vagas

    @property
    def cod(self):
        return self.__cod
