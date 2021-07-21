from tkinter.constants import FALSE, X

import PySimpleGUI as sg
from visual.tela_mensalistas import TelaMensalistas
from visual.tela_addMensalista import TelaAddMensalista
from entidade.mensalista import Mensalista

class ControladorMensalistas:
    __instance = None
    __mensalistas = [Mensalista('ABC1234')]
    __placas = ['ABC1234']

    def __init__(self, constrolador_sistema):

        self.__controlador = constrolador_sistema
        self.__tela_mensalistas = TelaMensalistas(self, self.__placas)
        self.__tela_addMensalista = TelaAddMensalista(self)
        

    def abre_tela_principal(self):
        stillAdding = True
        
        while stillAdding:
            self.updatePlacas()
            self.__tela_mensalistas.init_components()
            #print('hey')
            button, values = self.__tela_mensalistas.open()
            #print('hello')]
            print(button)
            if button == None:
                stillAdding = False
            else:
                if button == 'novo':
                    print('entrou novo')
                    self.abre_tela_addMensalista()
                elif button == 'remover':
                    print('entrou remover')
                    placa = values["placa"]
                    self.delMensalista(placa)
                elif button == 'editar':
                    print('entrou editar')
                    self.editarMensalista()
            self.retorna()
        

    def abre_tela_addMensalista(self):
        added = True

        while added:
            self.__tela_addMensalista.init_components()
            button, values = self.__tela_addMensalista.open()
            print(button)
            print('valores: ', values)
            if button == 'Cancelar' or button == None:
                added = False
            elif button == 'Salvar':
                    print('entrou em salvar')
                    placa = values["placa"]
                    print('placa a ser adicionada: ', placa)
                    self.addMensalistaToList(placa)
                    #self.fechaAddMensalista()
                    print(self.__mensalistas)
                    added = False
            self.fechaAddMensalista()
        

    def addMensalista(self):
        self.abre_tela_addMensalista()

    def addMensalistaToList(self, placa):
        print('placa prestes a ser add: ', placa)
        p1 = Mensalista(placa)
        print('p1.getplaca: ', p1.getPlaca)
        self.__mensalistas.append(p1)
        self.__placas.append(placa)
        for x in range(len(self.__mensalistas)):
            print('iteracao na lista de mens: ', self.__mensalistas[x].getPlaca())

    def fechaAddMensalista(self):
        self.__tela_addMensalista.close()

    def delMensalista(self, placa):
        #print('entrou no delete. placa: ', placa[0])
        #print('lista de placas atual: ', self.__placas)
        for x in range(len(self.__placas)):
            #print('placa na iteração: ', self.__placas[x])
            #print('tipo x do array: ', type(self.__placas[x]))
            #print('tipo do placa: ', type(placa[0]))
            #print('is: ', self.__placas[x] is placa[0], '  ==: ', self.__placas[x] == placa[0] )
            if self.__placas[x] is placa[0]:
                print('se igual, é esse: ', self.__placas[x])
                self.__placas.remove(placa[0])

       # self.__placas.pop()
        print('entrando no loop')
        for x in range(len(self.__mensalistas)):
            if self.__mensalistas[x].getPlaca() == placa[0]:
                self.__mensalistas.pop(x)
                
        print('lista de placas atual (mensalistas): ', self.__mensalistas)

    def editarMensalista(self):
        pass

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



    