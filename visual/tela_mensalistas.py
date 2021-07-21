from tkinter import Place
import PySimpleGUI as sg


class TelaMensalistas():
    
    def __init__(self, controlador_mensalistas, placas):
        self.__controlador = controlador_mensalistas
        self.__window = None
        self.__mensalistas = placas
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Listbox(values = self.__mensalistas, key="placa", size=(30, 6))],
            [sg.Button('Novo', key="novo"), sg.Button('Remover', key="remover"), sg.Button('Editar', key="editar")]
        ]
        self.__window = sg.Window('Mensalistas', layout, default_button_element_size=(40,1), element_justification='c', size=(800, 420), resizable=True)


    def open(self):
        while True:
            button, values = self.__window.read()
            return button, values
    
    def close(self):
        self.__window.Close()