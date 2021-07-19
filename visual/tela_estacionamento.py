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
            [sg.Text('Número de vagas para carros:'), sg.Input(key='numCarro', default_text=self.__controlador.getNumeroVagasCarros())],
            [sg.Text('Número de vagas para moto:'), sg.Input(key='numMoto', default_text=self.__controlador.getNumeroVagasMotos())],
            [sg.Button('Salvar alterações'), sg.Button('Voltar')]
        ]

        self.__window = sg.Window('Estacionamento Park', layout, default_button_element_size=(40, 1), element_justification='c', size=(800, 400), resizable=True)

    def open(self):
        while True:
            button, values = self.__window.Read()
            return button, values

    def close(self):
            self.__window.Close()

    def mensagemSucesso(self):
        sg.PopupOK("Atualização realizada com sucesso!", title="Atualização de vagas")