import datetime


class Estacionamento():

    def __init__(self):
        self.__vagasCarro = 0
        self.__vagasMoto = 0
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

    @property
    def vagasCarro(self):
        return self.__vagasCarro

    @vagasCarro.setter
    def vagasCarro(self, vagasCarro: int):
        if isinstance(vagasCarro, int):
            self.__vagasCarro = vagasCarro

    @property
    def vagasMoto(self):
        return self.__vagasMoto

    @vagasMoto.setter
    def vagasMoto(self, vagasMoto: int):
        if isinstance(vagasMoto, int):
            self.__vagasMoto = vagasMoto
