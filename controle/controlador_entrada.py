import PySimpleGUI as sg
from visual.tela_entrada import TelaEntrada
from entidade.veiculo import Veiculo

class ControladorEntrada:

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__tela_entrada = TelaEntrada(self)
        self.__veiculo = Veiculo(self)
#       self.__arquivo_entradas_carro = arquivo_entradas_carro
#       self.__arquivo_entradas_moto = arquivo_entradas_moto

    def abre_tela(self):
        while True:
            while True:
                self.__tela_entrada.init_components()
                button, values = self.__tela_entrada.open()
                carro = values['_CARRO_']
                moto = values['_MOTO_']
                placa = values['input_placa']
                placa_valido = self.fazer_validacao_placa(placa)
                if placa == '' or placa_valido is None:
                    sg.PopupOK('Placa Inválida. Verifique novamente.', title='Erro')
                elif button == 'Cancelar' or button == sg.WIN_CLOSED:
                    self.retorna_tela_sistema()
                elif placa_valido is not None:
                    sg.PopupOK('Placa válida. Registro realizado.', title='Sucesso')
                    self.retorna_tela_sistema()
                    break
                self.__tela_entrada.close()
            self.__tela_entrada.close()
            if button == 'Cancelar' or button == sg.WIN_CLOSED:
                self.__tela_entrada.close()
            else:
                self.guardar_em_arquivo()

    def guardar_em_arquivo(self):
        pass
        #guardar o registro do veículo em arquivo
        #ver tipo moto/carro, placa e guardar

                # if funcao_escolhida == self.opcao_registrar_entrada:
                #     placa_valido = self.fazer_validacao_placa(placa)
                #     if placa_valido is not None:
                #         self.opcao_registrar_entrada()
                #         break
                #     elif button == 'Cancelar' or button == sg.WIN_CLOSED:
                #         self.__tela_entrada.close()
                #         self.retorna_tela_sistema()
                #         break
                #     else:
                #         sg.PopupOK('Placa inválida. Verifique novamente.', title='Erro')
                #         print('Placa inválida, parou no abre_tela')
                #         self.__tela_entrada.close()
                # elif button == 'Cancelar' or button == sg.WIN_CLOSED:
                #     self.__tela_entrada.close()
                #     self.retorna_tela_sistema()

    def fazer_validacao_placa(self, placa):
        lista_placa = []
        placa_resultado = 0
        tam_lista = 0
        print('Início ======')
        try:
            placa_sem_espaco = placa.strip()
            print(f'Placa como entra no método: {placa}\n Placa sem espaço: {placa_sem_espaco}')
            num_caracteres = len(placa_sem_espaco)
            if num_caracteres > 7:
                placa_resultado = None
                print('Ponto 01.')
            else:
                placa_letra = placa_sem_espaco[:3]
                placa_numero = placa_sem_espaco[3:7]
                print(f'Placa de letras: {placa_letra}')
                print(f'Placa de numeros: {placa_numero}')
                for letra in placa_letra:
                    letra_incognita = letra
                    try:
                        letra_incognita = int(letra)
                    except:
                        letra_incognita = letra
                    finally:
                        eh_letra = isinstance(letra_incognita, str)
                        if eh_letra is True:
                            lista_placa.append(letra)
                            print(f'Ponto 02. Achamos uma letra string real: {letra}')
                for num in placa_numero:
                    try:
                        num_int = int(num)
                        eh_num = isinstance(num_int, int)
                    except:
                        eh_num = False
                    if eh_num is True:
                        lista_placa.append(num)
                        print(f'Ponto 02,5. Achamos um número int real: {num}')
                        tam_lista = len(lista_placa)
                        if tam_lista > 7:
                            placa_resultado = None
                            print('Ponto 03.')
                        else:
                            print('Ponto 04.')
                            print(f'Lista caracteres: {lista_placa}')
                    else:
                        print('Ponto 05. Valor não é número.')
                        placa_resultado = None
            print(f'Até aqui foi. Tamanho lista de strings: {tam_lista}')
        except:
            print(f'Lista caracteres da placa: {lista_placa}')
            print('Deu erro na validação da placa.')
            return placa_resultado
        finally:
            return placa_resultado

    def retorna_tela_sistema(self):
        self.__tela_entrada.close()
        self.__controlador.abre_tela()

    def opcao_registrar_entrada(self):
        pass

    # def abre_tela(self):
    #     while True:
    #         while True:
    #             self.__tela_entrada.init_components()
    #             button, values = self.__tela_entrada.open()
    #             carro = values['_CARRO_']
    #             moto = values['_MOTO_']
    #             placa = values['input_placa']
    #             placa_valido = self.fazer_validacao_placa(placa)
    #             if placa_valido is not None:
    #                 break
    #             elif button == 'Cancelar' or button == sg.WIN_CLOSED:
    #                 self.__tela_entrada.close()
    #                 self.retorna_tela_sistema()
    #             else:
    #                 sg.PopupOK('Placa inválida. Verifique novamente.', title='Erro')
    #             self.__tela_entrada.close()
    #         if button == 'Cancelar' or button == sg.WIN_CLOSED:
    #             self.__tela_entrada.close()
    #             self.retorna_tela_sistema()
    #         else: #continuar controlador_promocao linha139
    #             # a ideia é:
    #             # valor_placa = self.salvar_placa(placa_valido)
    #             # veiculo = self.salvar_veiculo(carro, moto)
    #             # if veiculo == 'carro':
    #             # and
    #             # if placa_valido is not in arquivos_carro_entrada
    #             #   then registrar_entrada(placa_valido) -> guardar no arquivo
    #             # else:
    #                 # sg.PopupOK('Essa placa já está registrada. Tente novamente.', title='Aviso Placa')
    #                 # self.retorna_tela_sistema()
    #             # if veiculo == 'moto':
    #             # and
    #             # if placa_valido is not in arquivos_moto_entrada
    #             #   then registrar_entrada(placa_valido) -> guardar no arquivo
    #             # else:
    #             #   sg.PopupOK('Essa placa já está registrada. Tente novamente.', title='Aviso Placa')
    #             #   self.retorna_tela_sistema()
    #
    #
    def opcao_cancelar(self):
        self.retorna_tela_sistema()

    # def salvar_veiculo(self, carro, moto):
    #     if carro is False:
    #         veiculo = 'moto'
    #         return veiculo
    #     elif moto is False:
    #         veiculo = 'carro'
    #         return veiculo

    def atribuir_dia_entrada_objeto(self):
        dia_entrada = date.today()                   # É um objeto. Para transformar em string:
        return dia_entrada                                            # self.pegar_dia_em_string()

    def pegar_dia_entrada_em_string(self):
        dia_em_string = atribuir_dia_entrada().strftime("d%m%y%")
        return dia_em_string

    def atribuir_hora_entrada_objeto(self):
        hora_entrada = datetime.now()
        return hora_entrada

    def pegar_hora_entrada_string(self):
        hora_em_string = atribuir_hora_entrada_objeto().strftime("H%M%S%")
        return hora_em_string
