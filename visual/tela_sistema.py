import PySimpleGUI as sg


class TelaSistema():

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
                    [sg.Text('', justification='c', size=(15, 1))],
                    [sg.Text('EasyPark', justification='c', size=(20, 1), font=("Helvetica", 25))],
                    [sg.Text('Escolha a opção: ')],
                    [sg.Button('Vagas', size=(15, 2), font=('Helvetica', 20))],
                    [sg.Button('Promoções', size=(15, 2), font=('Helvetica', 20))],
                    [sg.Button('Mensalistas', size=(15, 2), font=('Helvetica', 20))],
                    [sg.Cancel('Sair', font=('Helvetica', 20), size=(15, 2), button_color=('white', 'red'))]
                ]
        self.__window = sg.Window('EasyPark', layout, default_button_element_size=(40, 1), element_justification='c', size=(800, 400), resizable=True).Finalize()
        #self.__window.Maximize

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
