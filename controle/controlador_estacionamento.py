from visual.tela_estacionamento import TelaEstacionamento
from entidade.estacionamento import Estacionamento
import PySimpleGUI as sg

class ControladorEstacionamento:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__estacionamento = Estacionamento()
        self.__tela_estacionamento = TelaEstacionamento(self)
        #self.__continua_exibindo_tela = True


    def abre_tela(self):

        switcher = {'Salvar alterações': self.alteraVagas, 'Voltar': self.retorna}

        while True:
            self.__tela_estacionamento.init_components()
            button, values = self.__tela_estacionamento.open()
            if button == 'Voltar' or button == sg.WIN_CLOSED:
                self.retorna()
                self.__controlador.abre_tela()
            else:
                funcao_escolhida = switcher[button]
                if funcao_escolhida == self.alteraVagas:
                    carro = values['numCarro']
                    moto = values['numMoto']
                    self.alteraVagas(carro, moto)
                    self.retorna()
                    self.__controlador.abre_tela()
                #funcao_escolhida()


    def getNumeroVagasCarros(self):
        return self.__estacionamento.getNumVagasCarro()

    def setNumeroVagasCarros(self, vagas):
        self.__estacionamento.setNumVagasCarro(vagas)

    def getNumeroVagasMotos(self):
        return self.__estacionamento.getNumVagasMoto()

    def setNumeroVagasMotos(self, vagas):
        self.__estacionamento.setNumVagasMoto(vagas)

    def retorna(self):
        self.__tela_estacionamento.close()

    def alteraVagas(self, numCarros, numMotos):
        self.setNumeroVagasMotos(numMotos)
        self.setNumeroVagasCarros(numCarros)
