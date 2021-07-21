import PySimpleGUI as sg


class TelaMensalistas():
    
    def __init__(self, controlador_mensalistas):
        self.__controlador = controlador_mensalistas
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Listbox(values= self.__controlador.getMensalistas())],
            [sg.Button('Novo')], 
            [sg.Button('Remover')],
            [sg.Button('Editar')]
        ]
        self.__window = sg.Window('Mensalistas', layout, default_button_element_size=(40,1), element_justification='c', size=(800, 420), resizable=True)


    def open(self):
        while True:
            button = self.__window.Read()
            return button
    
    def close(self):
        self.__window.Close()