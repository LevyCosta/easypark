import PySimpleGUI as sg

class TelaPromocao:


    def __init__(self, controlador_promocao):
        self.__controlador = controlador_promocao
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        self.__window = sg.Window(title='Promoções', layout=[[]], margins=(200, 200), resizable=True).read()

    def open(self):
        while True:
            button, values = self.__window.Read()
            return button, values

    def close(self):
            self.__window.Close()
