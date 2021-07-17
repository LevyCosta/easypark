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
            [sg.Text('Número de vagas para carros:'), sg.InputText()],
            [sg.Text('Número de vagas para moto:'), sg.InputText(default_text="teste")],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]

        self.__window = sg.Window('Estacionamento Parl', default_button_element_size=(40, 1), size=(400, 550),
                                  element_justification='c').Layout(layout)

    def open(self):
            button, values = self.__window.Read()
            return button, values

    def close(self):
            self.__window.Close()
