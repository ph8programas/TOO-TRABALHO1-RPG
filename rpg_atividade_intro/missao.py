from enum import Enum
from abc import ABC


class StatusMissao(Enum):
    PENDENTE = "PENDENTE"
    EM_ANDAMENTO = "EM ANDAMENTO"
    CONCLUIDA = "CONCLUIDA"
    FRACASSADA = "FRACASSADA"



class Missao(ABC):
    def __init__(self, nome, descricao, recompensa, status):

        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = StatusMissao.PENDENTE
        self.__status = status
        
    

    ## Getters e Setters com validação
    
    ## Nome

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if nome is None or not isinstance(nome, str):
            raise ValueError("Nome é obrigatório e deve ser uma string")
        nome_limpo = nome.strip()
        if not nome_limpo:
            raise ValueError("Nome não pode estar vazio ou conter apenas espaços")
        self.__nome = nome_limpo
    

    ## Descrição

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    

    ## Recompensa

    @property
    def recompensa(self):
        return self.__recompensa
    
    @recompensa.setter
    def recompensa(self, recompensa):
        if not isinstance(recompensa, (int, float)):
            raise ValueError("Recompensa deve ser um valor numérico")
        if recompensa < 1 or recompensa > 50:
            raise ValueError("Recompensa deve ser um valor positivo entre 1 e 50")
        self.__recompensa = recompensa
    

    ## Status
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        status_validos = [StatusMissao.PENDENTE, StatusMissao.EM_ANDAMENTO, StatusMissao.CONCLUIDA, StatusMissao.FRACASSADA]
        
        if status not in status_validos:
            raise ValueError(f"Status deve ser um de: {status_validos}")
        
        transicoes_validas = {
            StatusMissao.PENDENTE: [StatusMissao.PENDENTE, StatusMissao.EM_ANDAMENTO],
            StatusMissao.EM_ANDAMENTO: [StatusMissao.EM_ANDAMENTO, StatusMissao.CONCLUIDA],
            StatusMissao.CONCLUIDA: [StatusMissao.CONCLUIDA],
            StatusMissao.FRACASSADA: [StatusMissao.FRACASSADA]
        }
        
        if status not in transicoes_validas.get(self.__status, []):
            raise ValueError(f"Transição de '{self.__status}' para '{status}' não é permitida. Fluxo esperado: PENDENTE -> EM ANDAMENTO -> CONCLUIDA")
        
        self.__status = status


    ## Funções

    def iniciar_missao(self):
        if self.status != StatusMissao.PENDENTE:
            raise ValueError("A missão só pode ser iniciada se estiver no status PENDENTE")
        self.status = StatusMissao.EM_ANDAMENTO
        print(f"Missão '{self.nome}' iniciada!\nO Objetivo da Missão é: {self.descricao}")

    def concluir_missao(self):
        if self.status == StatusMissao.FRACASSADA:
            raise ValueError("A missão já fracassou.")
        if self.status == StatusMissao.PENDENTE:
            raise ValueError("A missão só pode ser concluída se estiver EM ANDAMENTO.")
        if self.status == StatusMissao.CONCLUIDA:
            raise ValueError("A missão já foi concluída.")
        self.status = StatusMissao.CONCLUIDA
        print(f"Missão {self.nome} Concluída!")
        print(f"A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira.")
    


    def exibir_informacoes(self):
        print("\n")
        print(f"Missão [{self.__class__.__name__}]")
        print(f"Missão: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Recompensa: {self.recompensa} XP")
        print(f"Status: {self.status.value}")
    

    def __str__(self):
        return f"Missão: {self.nome} | Descrição: {self.descricao} | Recompensa: {self.recompensa} XP | Status: {self.status}"
    

    def __eq__(self, outro):
        if not isinstance(outro, Missao):
            return False
        return (self.nome == outro.nome and 
                self.descricao == outro.descricao and 
                self.recompensa == outro.recompensa and 
                self.status == outro.status)


class MissaoCombate(Missao):
    def __init__(self, nome, descricao, recompensa, inimigos_a_derrotar: int, inimigo: str, status):
        super().__init__(nome, descricao, recompensa, status)
        self.inimigos_a_derrotar = inimigos_a_derrotar
        self.inimigo = inimigo 

    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar
    
    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Deve ser um valor numérico")
        if valor < 1:
            raise ValueError("Deve ser um valor positivo")
        self.__inimigos_a_derrotar = valor

    @property
    def inimigo(self):
        return self.__inimigo
    
    @inimigo.setter
    def inimigo(self, valor):
        if isinstance(valor, str):
            self.__inimigo = valor.strip().title()    
        else: 
            raise ValueError("Deve ser um valor do tipo string")

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Inimigo: {self.inimigo}")
        print(f"Quantidade a derrotar: {self.inimigos_a_derrotar}")

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item_necessario:str, quantidade_item : int, status):
        super().__init__(nome, descricao, recompensa, status)
        self.item_necessario = item_necessario
        self.quantidade_item = quantidade_item

    @property
    def quantidade_item(self):
        return self.__quantidade_item
    
    @quantidade_item.setter
    def quantidade_item(self, quantidade_item):
        if not isinstance(quantidade_item, (int)):
            raise ValueError("Deve ser um valor numérico")
        if quantidade_item < 1:
            raise ValueError("Deve ser um valor positivo")
        self.__quantidade_item = quantidade_item

    @property
    def item_necessario(self):
        return self.__item_necessario
    
    @item_necessario.setter
    def item_necessario(self, item_necessario):
        if isinstance(item_necessario, (str)):
                self.__item_necessario = item_necessario.strip().title()    
        else: 
            raise ValueError("Deve ser um valor do tipo string")


    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Item a coletar: {self.__item_necessario}")
        print(f"Quantidade necessária: {self.__quantidade_item}")

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, local: str, distancia: float, tempo_limite: float, status):
        super().__init__(nome, descricao, recompensa, status)
        # Chamando os setters para validação imediata
        self.local = local
        self.distancia = distancia
        self.tempo_limite = tempo_limite

    # Propriedade: local
    @property
    def local(self):
        return self.__local
    
    @local.setter
    def local(self, local):
        if not isinstance(local, str):
            raise ValueError("O local deve ser uma string")
        self.__local = local.strip().title()

    # Propriedade: distancia
    @property
    def distancia(self):
        return self.__distancia
    
    @distancia.setter
    def distancia(self, distancia):
        if not isinstance(distancia, (int, float)):
            raise ValueError("A distância deve ser um valor numérico")
        if distancia < 0:
            raise ValueError("A distância não pode ser negativa")
        self.__distancia = distancia

    # Propriedade: tempo_limite
    @property
    def tempo_limite(self):
        return self.__tempo_limite
    
    @tempo_limite.setter
    def tempo_limite(self, tempo_limite):
        if not isinstance(tempo_limite, (int, float)):
            raise ValueError("O tempo limite deve ser um valor numérico")
        if tempo_limite <= 0:
            raise ValueError("O tempo limite deve ser maior que zero")
        self.__tempo_limite = tempo_limite

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Localização a explorar: {self.local}")
        print(f"Distância a percorrer: {self.distancia} km")
        print(f"Tempo limite: {self.tempo_limite} horas")