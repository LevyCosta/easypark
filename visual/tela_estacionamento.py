import PySimpleGUI as sg


class TelaEstacionamento:

    def __init__(self, controlador_estacionamento):
        self.__controlador = controlador_estacionamento
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Informações gerais do estacionamento Park', justification='c', font=("Helvetica", 14))],
            [sg.Text(' ')],
            [sg.Text('Valores do estacionamento', justification='c', font=("Helvetica", 12))],
            [sg.Text('Carro (segunda a sexta)'), sg.Text('                  '), sg.Text('Moto (segunda a sexta)')],
            [sg.Text('Por hora: R$8,00'), sg.Text('                          '),sg.Text('Por hora: R$6,00')],
            [sg.Text('Diária: R$35,00'), sg.Text('                          '), sg.Text('Diária: R$30,00')],
            [sg.Text('Pernoite: R$35,00'), sg.Text('                          '), sg.Text('Pernoite: R$30,00')],
            [sg.Text(' ')],
            [sg.Text('Carro (sábado e domingo)'), sg.Text('                  '), sg.Text('Moto (sábado e domingo)')],
            [sg.Text('Por hora: R$4,00'), sg.Text('                          '), sg.Text('Por hora: R$3,00')],
            [sg.Text('Diária: R$25,00'), sg.Text('                          '), sg.Text('Diária: R$20,00')],
            [sg.Text('Pernoite: R$35,00'), sg.Text('                          '), sg.Text('Pernoite: R$30,00')],
            [sg.Text(' ')],
            [sg.Text('Número de vagas para carros:'), sg.Input(key='numCarro', default_text=self.__controlador.vagasCarroDAO(), size=(10,5)),
             sg.Text('Número de vagas para moto:'), sg.Input(key='numMoto', default_text=self.__controlador.vagasMotoDAO(), size=(10,5))],
            [sg.Text(' ')],
            [sg.Button('Salvar alterações'), sg.Button('Voltar')]
        ]

        self.__window = sg.Window('Estacionamento Park', layout, default_button_element_size=(40, 1), element_justification='c', size=(800, 420), resizable=True)

    def open(self):
        while True:
            button, values = self.__window.Read()
            return button, values

    def close(self):
            self.__window.Close()

    def mensagemSucesso(self):
        sg.PopupOK("Atualização realizada com sucesso!", title="Atualização de vagas")
