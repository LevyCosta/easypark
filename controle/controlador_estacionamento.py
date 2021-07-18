from visual.tela_estacionamento import TelaEstacionamento
from entidade.estacionamento import Estacionamento
import PySimpleGUI as sg

class ControladorEstacionamento:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__estacionamento = Estacionamento()
        self.__tela_estacionamento = TelaEstacionamento(self)
        self.__continua_exibindo_tela = True


    def abre_tela(self):
        while True:
            input, values = self.__tela_estacionamento.open()
            if input == sg.WIN_CLOSED:
                exit(0)

    def getNumeroVagasCarros(self):
        return self.__estacionamento.vagasCarro

    def setNumeroVagasCarros(self):
        self.__estacionamento.vagasCarro(5)

    def getNumeroVagasMotos(self):
        return self.__estacionamento.vagasMoto

    def setNumeroVagasMotos(self):
        self.__estacionamento.vagasMoto(5)