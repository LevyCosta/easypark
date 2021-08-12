import PySimpleGUI as sg

class TelaEntrada:

    def __init__(self, controlador_entrada):
        self.__controlador = controlador_entrada
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout_promo_novo = [
            [sg.Text('Tipo de Veículo: ', size=(12, 1), font=('Helvetica', 10))],
            [sg.Radio('Carro', 'RADIO1', default=True, key='_CARRO_'), sg.Radio('Moto', 'RADIO1', key='_MOTO_')],
            [sg.Text('Placa: '), sg.InputText('', size=(10, 1), key='input_placa')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window(title='Registrar Entrada', layout=layout_promo_novo,
                                  default_button_element_size=(20, 1),
                                  element_justification='l', size=(400, 200), resizable=True)

    def open(self):
        while True:
            button, values = self.__window.Read()
            return button, values

    def close(self):
        self.__window.Close()
