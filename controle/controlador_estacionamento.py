from visual.tela_estacionamento import TelaEstacionamento
from entidade.estacionamento import Estacionamento
from DAO.estacionamento_DAO import EstacionamentoDAO
import PySimpleGUI as sg

class ControladorEstacionamento:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__estacionamento = Estacionamento(0, 0)
        self.__tela_estacionamento = TelaEstacionamento(self)
        self.__estacionamento_dao = EstacionamentoDAO()
        #self.__continua_exibindo_tela = True


    def abre_tela(self):

        switcher = {'Salvar alterações': self.alteraVagas, 'Voltar': self.retorna}

        while True:
            self.__tela_estacionamento.init_components()
            button, values = self.__tela_estacionamento.open()
            if button == 'Voltar' or button == sg.WIN_CLOSED:
                self.retorna()
            else:
                funcao_escolhida = switcher[button]
                if funcao_escolhida == self.alteraVagas:
                    carro = values['numCarro']
                    moto = values['numMoto']
                    self.alteraVagas(int(carro), int(moto))
                    self.retorna()

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
        self.__controlador.abre_tela()

    def alteraVagas(self, numCarros, numMotos):
        #for estacionamento in self.__estacionamento_dao.get_all():
            #if estacionamento.cod == 1:
                #self.__estacionamento_dao.remove(estacionamento)
            #self.__estacionamento = Estacionamento(numCarros, numMotos)
        self.__estacionamento.setNumVagasCarro(numCarros)
        self.__estacionamento.setNumVagasMoto(numMotos)
            #self.__estacionamento_dao.add(self.__estacionamento)
        self.__tela_estacionamento.mensagemSucesso()
