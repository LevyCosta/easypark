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
        switcher = {'Definir Vagas': self.opcao_vagas,
                    'Registrar Entrada': self.opcao_entrada,
                    'Registrar Saída': self.opcao_saida,
                    'Consultar Veículo Estacionado': self.opcao_consultar_estacionado,
                    'Consultar Valor': self.opcao_consultar_valor,
                    'Cadastrar Promoção': self.opcao_promocoes,
                    'Cadastrar Mensalista': self.opcao_mensalistas,
                    'Realizar Sorteio': self.opcao_sorteio,
                    'Gerar Relatório': self.opcao_relatorio,
                    'Sair': self.opcao_encerra}
        while True:
            button, values = self.__tela_sistema.open()
            if button == sg.WIN_CLOSED:
                self.opcao_encerra()
            funcao_escolhida = switcher[button]
            funcao_escolhida()

    def opcao_entrada(self):
        pass

    def opcao_saida(self):
        pass

    def opcao_consultar_estacionado(self):
        pass

    def opcao_consultar_valor(self):
        pass

    def opcao_sorteio(self):
        pass

    def opcao_relatorio(self):
        pass

    def opcao_vagas(self):
        self.__controlador_estacionamento.abre_tela()

    def opcao_promocoes(self):
        self.__controlador_promocao.abre_tela()

    def opcao_mensalistas(self):
        self.__controlador_mensalistas.abre_tela_principal()

    def opcao_encerra(self):
        exit(0)
