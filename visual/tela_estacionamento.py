import PySimpleGUI as sg



class TelaEstacionamento():

    def __init__(self, controlador_estacionamento):
        self.__controlador = controlador_estacionamento
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('EasyPark', justification='c', size=(20, 1), font=("Helvetica", 14))],
            [sg.Text('Número de vagas para carros:'), sg.InputText(default_text=str(self.__controlador.getNumeroVagasCarros()))],
            [sg.Text('Número de vagas para moto:'), sg.InputText(default_text=str(self.__controlador.getNumeroVagasMotos()))],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]

        self.__window = sg.Window('Estacionamento Park', layout, default_button_element_size=(40, 1), element_justification='c', size=(800, 400), resizable=True)

    def open(self):
        while True:
            input, values = self.__window.Read()
            return input, values

    def close(self):
            self.__window.Close()
