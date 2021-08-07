import datetime


class Estacionamento():

    def __init__(self, vagasCarro: int, vagasMoto: int):
        self.__cod = 1
        if isinstance(vagasCarro, int):
            self.__vagasCarro = vagasCarro
        if isinstance(vagasMoto, int):
            self.__vagasMoto = vagasMoto
        self.__valorDiariaCarroSemana = 35.0
        self.__valorDiariaCarroFinde = 25.0
        self.__valorDiariaMotoSemana = 30.0
        self.__valorDiariaMotoFinde = 20.0
        self.__valorHoraCarroSemana = 8.0
        self.__valorHoraCarroFinde = 4.0
        self.__valorHoraMotoSemana = 6.0
        self.__valorHoraMotoFinde = 3.0
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
