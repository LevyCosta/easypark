from visual.tela_promocao import TelaPromocao
from visual.tela_promocao_novo_editar import TelaPromocaoNovoEditar
from entidade.promocao import Promocao
import PySimpleGUI as sg

class ControladorPromocao:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__controlador = controlador_sistema
        self.__promocaoCarro = Promocao('carro', 0)
        self.__promocaoMoto = Promocao('moto', 0)
        self.__tela_promocao = TelaPromocao(self)
        self.__tela_promocao_novo_editar = TelaPromocaoNovoEditar(self)

    def get_desconto_carro(self):
        return self.__promocaoCarro.getDesconto()

    def set_desconto_carro(self, descontoCarro):
        self.__promocaoCarro.setDesconto(descontoCarro)

    def get_desconto_moto(self):
        return self.__promocaoMoto.getDesconto()

    def set_desconto_moto(self, descontoMoto):
        self.__promocaoMoto.setDesconto(descontoMoto)

    def abre_tela(self):
        switcher = {'Novo': self.opcao_novo,
                    'Remover': self.opcao_remover,
                    'Editar': self.opcao_editar,
                    'Cancelar': self.opcao_cancelar}
        while True:
            self.__tela_promocao.init_components(self.get_desconto_carro(), self.get_desconto_moto())
            button, values = self.__tela_promocao.open()
            if button == 'Cancelar' or button == sg.WIN_CLOSED:
                self.retorna()
            else:
                funcao_escolhida = switcher[button]
                self.__tela_promocao.close()
                funcao_escolhida()

    def opcao_novo(self):
        self.abre_tela_novo_editar()

    def salvar_desconto(self, desconto=0.0):
        self.__tela_promocao_novo_editar.close()
        return desconto

    def salvar_desconto_tipo(self, veiculo):
        self.__tela_promocao_novo_editar.close()
        return veiculo

    def retorna_tela_promo(self):
        self.__tela_promocao_novo_editar.close()
        self.abre_tela()

    def retorna(self):
        self.__tela_promocao.close()
        self.__controlador.abre_tela()

    def opcao_remover(self):
        self.set_desconto_moto(0)
        self.set_desconto_carro(0)

    def opcao_editar(self):
        self.abre_tela_editar()

    def abre_tela_editar(self):
        while True:
            while True:
                self.__tela_promocao_novo_editar.init_components()
                button, values = self.__tela_promocao_novo_editar.open()
                carro = values['_CARRO_']
                moto = values['_MOTO_']
                desconto = values['input_desconto']
                desconto_valido = self.fazer_validacao_desconto(desconto)
                if desconto_valido is not None:
                    break
                elif button == 'Cancelar' or button == sg.WIN_CLOSED:
                    self.__tela_promocao_novo_editar.close()
                    self.retorna_tela_promo()
                else:
                    sg.PopupOK('Valor inválido. Verifique novamente.', title='Erro')
                self.__tela_promocao_novo_editar.close()
            if button == 'Cancelar' or button == sg.WIN_CLOSED:
                self.__tela_promocao_novo_editar.close()
                self.retorna_tela_promo()
            else:
                valor_desconto = self.salvar_desconto(desconto_valido)
                veiculo = self.salvar_veiculo(carro, moto)
                if veiculo == 'moto':
                    self.set_desconto_moto(valor_desconto)
                elif veiculo == 'carro':
                    self.set_desconto_carro(valor_desconto)
                self.retorna_tela_promo()

    def opcao_cancelar(self):
        self.__tela_promocao.close()
        self.__controlador.abre_tela()

    def abre_tela_novo_editar(self):
        while True:
            while True:
                self.__tela_promocao_novo_editar.init_components()
                button, values = self.__tela_promocao_novo_editar.open()
                carro = values['_CARRO_']
                moto = values['_MOTO_']
                desconto = values['input_desconto']
                desconto_valido = self.fazer_validacao_desconto(desconto)
                if desconto_valido is not None:
                    break
                elif button == 'Cancelar' or button == sg.WIN_CLOSED:
                    self.__tela_promocao_novo_editar.close()
                    self.retorna_tela_promo()
                else:
                    sg.PopupOK('Valor inválido. Verifique novamente.', title='Erro')
                self.__tela_promocao_novo_editar.close()
            if button == 'Cancelar' or button == sg.WIN_CLOSED:
                self.__tela_promocao_novo_editar.close()
                self.retorna_tela_promo()
            else:
                valor_desconto = self.salvar_desconto(desconto_valido)
                veiculo = self.salvar_veiculo(carro, moto)
                if veiculo == 'carro':
                    if self.get_desconto_carro() != 0:
                        sg.PopupOK('Já existe um desconto de carro ativo! Não é possível fazer esta operação.',
                               title='Aviso Carro')
                        self.retorna_tela_promo()
                    else:
                        self.set_desconto_carro(valor_desconto)
                elif veiculo == 'moto':
                    if self.get_desconto_moto() != 0:
                        sg.PopupOK('Já existe um desconto de moto ativo! Não é possível fazer esta operação.',
                               title='Aviso Moto')
                        self.retorna_tela_promo()
                    else:
                        self.set_desconto_moto(valor_desconto)
                self.retorna_tela_promo()

    def fazer_validacao_desconto(self, desconto):
        try:
            desconto_num = float(desconto)
            if 0 <= desconto_num <= 100:
                desconto_valido = desconto_num
                return desconto_valido
            else:
                desconto_invalido = None
                return desconto_invalido
        except:
            desconto_invalido = None
            return desconto_invalido


    def alocar_atributo(self, veiculo_desconto, valor_desconto):
        if veiculo_desconto == 'carro':
            self.__descontoCarro = valor_desconto
            print(f'Veículo {veiculo_desconto}, desconto de {self.__descontoCarro}')
        elif veiculo_desconto == 'moto':
            self.__descontoMoto = valor_desconto
            print(f'Veículo {veiculo_desconto}, desconto de {self.__descontoMoto}')

    def salvar_veiculo(self, carro, moto):
        if carro is False:
            veiculo = 'moto'
            return veiculo
        elif moto is False:
            veiculo = 'carro'
            return veiculo

    def encerra(self):
        exit(0)
