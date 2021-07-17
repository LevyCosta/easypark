import datetime


class Estacionamento():

    def __init__(self, vagasCarro: int, vagasMoto: int, valorDiariaCarro: float, valorDiariaMoto:float,
                 valorHoraCarro: float, valorHoraMoto: float, valorPernoiteCarro: float, valorPernoiteMoto: float):
        if isinstance(vagasCarro, int):
            self.__vagasCarro = vagasCarro
        if isinstance(vagasMoto, int):
            self.__vagasMoto = vagasMoto
        if isinstance(valorDiariaCarro, float):
            self.__valorDiariaCarro = valorDiariaCarro
        if isinstance(valorDiariaMoto, float):
            self.__valorDiariaMoto = valorDiariaMoto
        if isinstance(valorHoraCarro, float):
            self.__valorHoraCarro = valorHoraCarro
        if isinstance(valorHoraMoto, float):
            self.__valorHoraMoto = valorHoraMoto
        if isinstance(valorPernoiteCarro, float):
            self.__valorPernoiteCarro = valorPernoiteCarro
        if isinstance(valorPernoiteMoto, float):
            self.__valorPernoiteMoto = valorPernoiteMoto
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
