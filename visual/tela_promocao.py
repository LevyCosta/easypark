import PySimpleGUI as sg

class TelaPromocao:

    def __init__(self, controlador_promocao):
        self.__controlador = controlador_promocao
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout_promo = [
            [sg.Text('Promoções ativas:', size=(15, 1), font=('Helvetica', 12))],
            [sg.Text('Promo Ativa 1 (só exemplo - achar a list correta)')],
            [sg.Text('Promo Ativa 2')],
            [sg.Button('Novo'), sg.Button('Remover'), sg.Button('Editar')]
        ]
        self.__window = sg.Window(title='Promoções', layout=layout_promo, default_button_element_size=(20, 1), element_justification='c', size=(400, 400), resizable=True)

    def open(self):
        while True:
            button, values = self.__window.Read()
            return button, values

    def close(self):
            self.__window.Close()
