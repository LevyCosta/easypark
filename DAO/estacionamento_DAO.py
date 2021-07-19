from DAO.abstract_DAO import DAO
from entidade.estacionamento import Estacionamento

class EstacionamentoDAO(DAO):
    def __init__(self):
        super().__init__('estacionamento.pkl')

    def add(self, estacionamento: Estacionamento):
        if (estacionamento is not None) and (isinstance(estacionamento.cod, int)) and (isinstance(estacionamento, Estacionamento)):
            super().add(estacionamento.cod, estacionamento)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
