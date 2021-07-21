import PySimpleGUI as sg
from visual.tela_sistema import TelaSistema
from controle.controlador_estacionamento import ControladorEstacionamento
from controle.controlador_mensalistas import ControladorMensalistas
from controle.controlador_promocao import ControladorPromocao

class ControladorSistema():
    __instance = None

    def __init__(self):
        self.__tela_sistema = TelaSistema(self)
        self.__controlador_estacionamento = ControladorEstacionamento(self)
        self.__controlador_mensalistas = ControladorMensalistas(self)
        self.__controlador_promocao = ControladorPromocao(self)

    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        switcher = {'Vagas': self.opcao_vagas, 'Promoções': self.opcao_promocoes,
                        'Mensalistas': self.opcao_mensalistas, 'Sair': self.opcao_encerra}
        while True:
            button, values = self.__tela_sistema.open()
            if button == sg.WIN_CLOSED:
                exit(0)
            funcao_escolhida = switcher[button]

            funcao_escolhida()

    def opcao_vagas(self):
        self.__controlador_estacionamento.abre_tela()

    def opcao_promocoes(self):
        self.__controlador_estacionamento.abre_tela()

    def opcao_mensalistas(self):
        self.__controlador_mensalistas.abre_tela_principal()

    def opcao_encerra(self):
        exit(0)