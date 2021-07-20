from visual.tela_promocao import TelaPromocao
from visual.tela_promocao_novo_editar import TelaPromocaoNovoEditar
from entidade.promocao import Promocao
import PySimpleGUI as sg

class ControladorPromocao:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__promocao = Promocao
        self.__tela_promocao = TelaPromocao(self)
        self.__tela_promocao_novo_editar = TelaPromocaoNovoEditar(self)

    def abre_tela(self):
        switcher = {'Novo': self.opcao_novo, 'Remover': self.opcao_remover, 'Editar': self.opcao_editar, 'Cancelar': self.opcao_cancelar}
        while True:
            self.__tela_promocao.init_components()
            button, values = self.__tela_promocao.open()
            if button == 'Cancelar' or button == sg.WIN_CLOSED:
                self.retorna()
            else:
                funcao_escolhida = switcher[button]
                self.__tela_promocao.close()
                funcao_escolhida()


    def opcao_novo(self):
        self.abre_tela_novo_editar()

    def salvar_desconto(self):
        sg.PopupOK('Não foi possível salvar essa promoção. Verifique e tente novamente!', title='Aviso')

    def retorna_tela_promo(self):
        self.__tela_promocao_novo_editar.close()
        self.abre_tela()

    def retorna(self):
        self.__tela_promocao.close()
        self.__controlador.abre_tela()

    def opcao_remover(self):
        pass

    def opcao_editar(self):
        self.abre_tela_novo_editar()

    def opcao_cancelar(self):
        self.__tela_promocao.close()
        self.__controlador.abre_tela()

    def abre_tela_novo_editar(self):
        switcher = {'Salvar': self.salvar_desconto, 'Cancelar': self.retorna_tela_promo}
        while True:
            self.__tela_promocao_novo_editar.init_components()
            button, values = self.__tela_promocao_novo_editar.open()
            if button == 'Cancelar' or button == sg.WIN_CLOSED:
                self.__tela_promocao_novo_editar.close()
                self.retorna_tela_promo()
            else:
                funcao_escolhida = switcher[button]
                funcao_escolhida()
                self.retorna_tela_promo()

    def encerra(self):
        exit(0)