import PySimpleGUI as sg

class TelaEditMensalista():

    def __init__(self, controlador_mensalistas):
        self.__controlador = controlador_mensalistas
        self.__windows = None
        self.init_components('xxx')

    def init_components(self, placaEscolhida):
        sg.ChangeLookAndFeel('Reddit')
        layout= [
            [sg.Text('Placa Atual: ', justification= 'c', font=("Helvetica", 12)), sg.Text(placaEscolhida[0])],
            [sg.Text('Nova Placa: ', justification='c', font=("Helvetica", 12))],
            [sg.Input(key='placaNova', default_text= 'exemplo: BRA0101')],
            [sg.Button('Salvar')],
            [sg.Button('Cancelar')]
        ]

        self.__windows = sg.Window('Mensalista', layout, default_button_element_size=(40, 1), element_justification='c', size=(800, 420), resizable=True)

    def open(self):
        while True:
            button, values = self.__windows.Read()
            return button, values

    def close(self):
        self.__windows.Close()

    def success(self):
        sg.PopupOK("Novo Mensalista cadastrado!", title="Sucesso")

