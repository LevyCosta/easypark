from visual.tela_estacionamento import TelaEstacionamento
from entidade.estacionamento import Estacionamento
import PySimpleGUI as sg

class ControladorEstacionamento:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__tela_estacionamento = TelaEstacionamento(self)
        self.__continua_exibindo_tela = True


    def abre_tela(self):
        self.__tela_estacionamento.init_components()
