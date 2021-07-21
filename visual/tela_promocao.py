import PySimpleGUI as sg

class TelaPromocao:

    def __init__(self, controlador_promocao):
        self.__controlador = controlador_promocao
        self.__window = None
        self.init_components()

    def init_components(self, descontoCarro=0, descontoMoto=0):
        sg.ChangeLookAndFeel('Reddit')
        layout_promo = [
            [sg.Text('Promoções Ativas', size=(15, 1), font=('Helvetica', 12))],
 #           [sg.Listbox(values=(f'Desconto para Carros de {self.descontoCarro}%',
 #                               f'Desconto para Motos de {descontoMoto}%'), size=(30, 3), key='_LISTBOX_')],
            [sg.Listbox(values=(f'Desconto para Carros de {descontoCarro}',
                                f'Desconto para Motos de {descontoMoto}'))],
            [sg.Button('Novo'), sg.Button('Remover'), sg.Button('Editar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window(title='Promoções', layout=layout_promo, default_button_element_size=(20, 1), element_justification='c', size=(400, 300), resizable=True)

    def open(self):
        while True:
            button, values = self.__window.Read()
            return button, values

    def close(self):
            self.__window.Close()

    def mensagem_sucesso(self):
        sg.PopupOK('Promoção ativada com sucesso!', title='Valor da Promoção')


