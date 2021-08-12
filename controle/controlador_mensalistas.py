from tkinter.constants import FALSE, X
#look at me testing
import PySimpleGUI as sg
from visual.tela_mensalistas import TelaMensalistas
from visual.tela_addMensalista import TelaAddMensalista
from visual.tela_editMensalista import TelaEditMensalista
from entidade.mensalista import Mensalista

class ControladorMensalistas:
    __instance = None
    __mensalistas = [Mensalista('ABC1234')]
    __placas = ['ABC1234']

    def __init__(self, constrolador_sistema):

        self.__controlador = constrolador_sistema
        self.__tela_mensalistas = TelaMensalistas(self, self.__placas)
        self.__tela_addMensalista = TelaAddMensalista(self)
        self.__tela_editMensalista = TelaEditMensalista(self)
        

    def abre_tela_principal(self):
        stillAdding = True
        
        while stillAdding:
            self.updatePlacas()
            self.__tela_mensalistas.init_components()
            #print('hey')
            button, values = self.__tela_mensalistas.open()
            #print('hello')]
            if button == None:
                stillAdding = False
            else:
                if button == 'novo':
                    self.abre_tela_addMensalista()
                elif button == 'remover':
                    placa = values["placa"]
                    self.delMensalista(placa)
                elif button == 'editar':
                    placa = values["placa"]
                    self.abre_tela_editMensalista(placa)
            self.retorna()
        

    def abre_tela_addMensalista(self):
        added = True

        while added:
            self.__tela_addMensalista.init_components()
            button, values = self.__tela_addMensalista.open()
            if button == 'Cancelar' or button == None:
                added = False
            elif button == 'Salvar':
                    placa = values["placa"]
                    self.addMensalistaToList(placa)
                    added = False
            self.fechaAddMensalista()
        
    def abre_tela_editMensalista(self, placaEscolhida):
        edited = True

        while edited:
            self.__tela_editMensalista.init_components(placaEscolhida)
            button, values = self.__tela_editMensalista.open()
            if button == 'Cancelar' or button == None:
                edited = False
            elif button == 'Salvar':
                    placaNova = values["placaNova"]
                    self.editMensalista(placaNova, placaEscolhida)
                    edited = False
            self.fechaEditMensalista()

    def addMensalista(self):
        self.abre_tela_addMensalista()

    def addMensalistaToList(self, placa):
        self.__mensalistas.append(Mensalista(placa))
        self.__placas.append(placa)
        #print('lista de placas de Mens: ', self.__mensalistas)

    def fechaAddMensalista(self):
        self.__tela_addMensalista.close()
    
    def fechaEditMensalista(self):
        self.__tela_editMensalista.close()

    def delMensalista(self, placa):
        #print('tamanho da lista de placas: ', len(self.__placas), '.')
        #print('tamanho da lista de mensalistas: ', len(self.__mensalistas), '.')
        for x in range(len(self.__placas) -1, -1, -1):
            if self.__placas[x] is placa[0]:
                #print('placa removed')
                self.__placas.remove(placa[0])
                
                
        for y in range(len(self.__mensalistas) -1, -1, -1):
            if self.__mensalistas[y].getPlaca() == placa[0]:
               self.__mensalistas.pop(y)  


       # self.__placas.pop()
        

    def editMensalista(self, placaNova, placaEscolhida): 
        
        self.addMensalistaToList(placaNova)
        self.delMensalista(placaEscolhida)

    def getMensalistas(self):
        return self.__mensalistas

    def getPlacas(self):
        return self.__placas
 
    def updatePlacas(self):
        for x in range(len(self.__mensalistas)):
            if self.__mensalistas[x].getPlaca() not in self.__placas:
                self.__placas.append(self.__mensalistas[x].getPlaca())

    def retorna(self):
        self.__tela_mensalistas.close()



    