import PySimpleGUI as sg

class TelaAddMensalista():

    def __init__(self, controlador_mensalistas):
        self.__controlador = controlador_mensalistas
        self.__windows = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout= [
            [sg.Text('Nova Placa: ', justification='c', font=("Helvetica", 12))],
            [sg.Input(key='placa', default_text= 'exemplo: BRA0101')],
            [sg.Button('Salvar')],
            [sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Mensalista', layout, default_button_element_size=(40, 1), element_justification='c', size=(800, 420), resizable=True)

    def open(self):
        while True:
            button, values = self.__window.Read()
            return button, values

    def close(self):
        self.__window.Close()

    def success(self):
        sg.PopupOK("Novo Mensalista cadastrado!", title="Sucesso")

