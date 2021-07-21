import PySimpleGUI as sg

class TelaPromocao:

    def __init__(self, controlador_promocao):
        self.__controlador = controlador_promocao
        self.__window = None
        self.init_components()

    def init_components(self, desconto=0):
        sg.ChangeLookAndFeel('Reddit')
        layout_promo = [
            [sg.Text('Promoções Ativas', size=(15, 1), font=('Helvetica', 12))],
            [sg.Listbox(values=('Desconto para Carros de 15%', 'Desconto para Motos de 20%'), size=(30, 3), key='listbox')],
            [sg.Button('Novo'), sg.Button('Remover'), sg.Button('Editar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window(title='Promoções', layout=layout_promo, default_button_element_size=(20, 1), element_justification='c', size=(400, 200), resizable=True)




    def open(self):
        while True:
            button, values = self.__window.Read()
            return button, values

    def close(self):
            self.__window.Close()

    def mensagem_sucesso(self):
        sg.PopupOK('Promoção ativada com sucesso!', title='Valor da Promoção')

