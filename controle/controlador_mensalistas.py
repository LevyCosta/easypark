from tkinter.constants import X

import PySimpleGUI as sg
from visual.tela_mensalistas import TelaMensalistas
from visual.tela_addMensalista import TelaAddMensalista
from entidade.mensalista import Mensalista

class ControladorMensalistas:
    __instance = None
    __mensalistas = [Mensalista]

    def __init__(self, constrolador_sistema):
        self.__controlador = constrolador_sistema
        self.__tela_mensalistas = TelaMensalistas(self)
        self.__tela_addMensalista = TelaAddMensalista(self)
        

    def abre_tela_principal(self):

        switcher = {'Novo': self.addMensalista, 'Remover': self.delMensalista, 'Editar': self.editarMensalista}

        while True:
            self.__tela_mensalistas.init_components()
            button = self.__tela_mensalistas.open()
            if button == sg.WIN_CLOSED:
                self.retorna()
            else:
                funcao = switcher[button]
                if funcao == self.addMensalista:
                    self.abre_tela_addMensalista()
                elif funcao == self.delMensalista():
                    self.delMensalista()
                elif funcao == self.editarMensalista():
                    self.editarMensalista()


    def abre_tela_addMensalista(self):
        
        switcher = {'Salvar': self.addMensalistaToList, 'Cancelar': self.cancelaAddMensalista}

        while True:
            self.__tela_addMensalista.init_components()
            button, values = self.__tela_addMensalista.open()
            if button == 'Cancelar' or button == sg.WIN_CLOSED:
                self.cancelaAddMensalista()
            else:
                funcao = switcher[button]
                if funcao == self.addMensalistaToList:
                    placa = values[placa]
        

    def addMensalista(self):
        self.abre_tela_addMensalista()

    def cancelaAddMensalista(self):
        self.__tela_addMensalista.close()

    def delMensalista(self):
        pass

    def editarMensalista(self):
        pass

    def getMensalistas(self):
        return self.__mensalistas


    def retorna(self):
        self.__tela_mensalistas.close()
        self.__controlador.abre_tela()



    