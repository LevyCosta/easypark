from visual.tela_promocao import TelaPromocao
from entidade.promocao import Promocao
import PySimpleGUI as sg

class ControladorPromocao:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__promocao = Promocao
        self.__tela_promocao = TelaPromocao(self)

    def abre_tela(self):
        pass


    def salvarDesconto(self):
        pass

    def retorna(self):
        pass