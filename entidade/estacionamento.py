import datetime


class Estacionamento():

    def __init__(self):
        self.__numVagasCarro = 0
        self.__numVagasMoto = 0
        self.__valorDiariaCarro = 35.0
        self.__valorDiariaMoto = 30.0
        self.__valorHoraCarro = 8.0
        self.__valorHoraMoto = 6.0
        self.__valorPernoiteCarro = 35.0
        self.__valorPernoiteMoto = 30.0
        #self.__veiculosEstacionados = []*(self.__vagasMoto+self.__vagasCarro)
        self.__carrosEstacionados = []*self.__numVagasCarro
        self.__motosEstacionadas = []*self.__numVagasMoto
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

