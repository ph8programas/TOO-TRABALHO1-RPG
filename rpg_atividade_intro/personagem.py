from typing import Optional
from Item import Item
from missao import *
from Item import *

class Personagem:
    def __init__(self, nome, vida, nivel, xp):
        self._nome = nome
        self._vida = vida    
        self._nivel = nivel
        self._xp = xp
        self.__missoes = []
        self.__inventario = []
        self.__equipamentos: dict[TipoItem, Item | None] = {tipo: None for tipo in TipoItem}
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._nome = valor
        else:
            raise ValueError("Nome deve ser uma string não vazia")

    @property
    def vida(self):
        return self._vida

    @property
    def nivel(self):
        return self._nivel

    @property
    def xp(self):
        return self._xp

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}")
        print(f"Nível: {self.nivel}")
        print(f"XP: {self.xp}")

    def iniciar_missao_p(self,missao:Missao):
        if missao not in self.__missoes:
            try:
                self.__missoes.append(missao)
            except:
                 raise ValueError
            try:
                missao.iniciar_missao()
            except:
                raise ValueError      
            return
        else:
            print(f"Missão já iniciada para o personagem {self.nome}")
            return
        
    def progredir_missao(self, missao, progresso: int):
        # 1. Validação de segurança
        if missao not in self.__missoes:
            print(f"Missão não atribuída a {self.nome}")
            return

        # 2. Lógica de progresso (Polimórfica)
        # Todos os tipos de missão agora possuem a propriedade .objetivo
        alvo = missao.valor_objetivo 

        if progresso >= alvo:
            missao.concluir_missao()
            self._xp += missao.recompensa
            print(f"\n--- MISSÃO CONCLUÍDA ---")
            print(f"Missão: {missao.nome}")
            print(f"Recompensa: {missao.recompensa} XP")
            print(f"XP Total de {self.nome}: {self._xp}\n")
        else:
            print(f"Progresso em '{missao.nome}': {progresso}/{alvo}")

    def adicionar_item_inventario(self, item: Item):
        if item not in self.__inventario:
            try:
                self.__inventario.append(item)
                print(f"Item adicionado ao inventário de {self.nome}.")
                Item.exibir_informacoes(item)
            except ValueError:
                print(f"Erro ao adicionar o item '{item.nome}' ao inventário de {self.nome}.")
        else:
            print(f"Item '{item.nome}' já existe no inventário de {self.nome}.")

    def equipar_item(self, item: Item):
        if item not in self.__inventario:
            print(f"Item '{item.nome}' não encontrado no inventário.")
            return

        try:
            # 1. Descobrimos o slot (a chave do dicionário) através do tipo do item
            slot = item.tipo 

            # 2. Verificamos se já existe algo equipado nesse slot
            item_antigo = self.__equipamentos[slot]

            if item_antigo is not None:
                # Se existia algo, devolvemos para o inventário
                self.__inventario.append(item_antigo)
                print(f"Desequipando {item_antigo.nome}...")

            # 3. Agora removemos o novo item do inventário
            self.__inventario.remove(item)

            # 4. Colocamos o novo item no dicionário de equipamentos
            self.__equipamentos[slot] = item

            print(f"Item '{item.nome}' equipado no slot {slot.value} por {self.nome}.")
            item.exibir_informacoes() # Chamada direta se o método for de instância

        except ValueError:
            print(f"Erro ao manipular o inventário.")

        # Lógica de equipar o item (a ser implementada)
    def desequipar_slot(self, tipo_slot: TipoItem):
        item = self.__equipamentos[tipo_slot]
        if item:
            self.__equipamentos[tipo_slot] = None
            self.__inventario.append(item)
            print(f"{item.nome} movido para o inventário.")
        
    def equipar_itens(self, itens: list):
        for item in itens:
            self.equipar_item(item)



    def __str__(self):
        return f"Personagem(nome='{self.nome}', vida={self.vida}, nível={self.nivel}, xp={self.xp})"

    def __eq__(self, outro):
        if not isinstance(outro, Personagem):
            return False
        return self.nome == outro.nome and self.vida == outro.vida and self.nivel == outro.nivel and self.xp == outro.xp

    