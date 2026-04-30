from enum import Enum
from missao import *

class TipoItem(Enum):
    ARMA = "ARMA"
    VESTIMENTA = "VESTIMENTA"
    UTILITARIO = "UTILITARIO"



class Item():
    def __init__(self, nome, descricao, valor_efeito, tipo):

        self.__nome = nome
        self.__descricao = descricao
        self.__valor_efeito = valor_efeito
        self.__tipo = TipoItem(tipo)
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor_efeito(self):
        return self.__valor_efeito

    @property
    def tipo(self):
        return self.__tipo
    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Valor do Efeito: {self.valor_efeito}")
        print(f"Tipo: {self.tipo.value}")
    
    def criar_item(self,nome, descricao, valor_efeito, tipo):
        return Item(nome, descricao, valor_efeito, tipo)

