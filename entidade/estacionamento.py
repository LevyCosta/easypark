import datetime


class Estacionamento():

    def __init__(self, numVagasCarro: int, numVagasMoto: int):
        self.__cod = 1
        if isinstance(numVagasCarro, int):
            self.__numVagasCarro = numVagasCarro
        if isinstance(numVagasMoto, int):
            self.__numVagasMoto = numVagasMoto
        self.__valorDiariaCarro = 35.0
        self.__valorDiariaMoto = 30.0
        self.__valorHoraCarro = 8.0
        self.__valorHoraMoto = 6.0
        self.__valorPernoiteCarro = 35.0
        self.__valorPernoiteMoto = 30.0
        self.__carrosEstacionados = [] #quando add a este array, limitar a numVagasCarro
        self.__motosEstacionadas = [] #quando add a este array, limitar a numVagasMoto
        self.__mensalistas = []
        self.__promocoes = []
        self.__relatorios = []

    def getNumVagasCarro(self):
        return self.__numVagasCarro

    def setNumVagasCarro(self, vagas):
        self.__numVagasCarro = vagas

    def getNumVagasMoto(self):
        return self.__numVagasMoto

    def setNumVagasMoto(self, vagas):
        self.__numVagasMoto = vagas

    @property
    def cod(self):
        return self.__cod
