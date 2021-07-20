from visual.tela_promocao import TelaPromocao
from visual.tela_promocao_novo_editar import TelaPromocaoNovoEditar
from entidade.promocao import Promocao
import PySimpleGUI as sg

class ControladorPromocao:

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__promocao = Promocao
        self.__tela_promocao = TelaPromocao(self)
        self.__tela_promocao_novo_editar = TelaPromocaoNovoEditar(self)

    def abre_tela(self):
        switcher = {'Novo': self.opcao_novo, 'Remover': self.opcao_remover, 'Editar': self.opcao_editar}
        while True:
            button, values = self.__tela_promocao.open()
            if button == sg.WIN_CLOSED:
                exit(0)
            else:
                funcao_escolhida = switcher[button]
                funcao_escolhida()

    def opcao_novo(self):
        switcher = {'Salvar': self.salvar_desconto, 'Cancelar': self.retornar}
        while True:
            button, values = self.__tela_promocao_novo_editar.open()
            if button == sg.WIN_CLOSED:
                exit(0)
            else:
                funcao_escolhida = switcher[button]
                funcao_escolhida()

    def salvar_desconto(self):
        pass

    def retornar(self):
        self.__tela_promocao_novo_editar.close()
        self.__tela_promocao.open()

    def opcao_remover(self):
        pass

    def opcao_editar(self):
        switcher = {'Salvar': self.salvar_desconto, 'Cancelar': self.retornar}
        while True:
            button, values = self.__tela_promocao_novo_editar.open()
            if button == sg.WIN_CLOSED:
                exit(0)
            else:
                funcao_escolhida = switcher[button]
                funcao_escolhida()
