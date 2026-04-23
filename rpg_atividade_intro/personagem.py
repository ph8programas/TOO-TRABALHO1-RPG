from missao import *

class Personagem:
    def __init__(self, nome, vida, nivel, xp):
        self._nome = nome
        self._vida = vida    
        self._nivel = nivel
        self._xp = xp
        self.__missoes = []

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
        
    def progredir_missao(self, missao: Missao, progresso: int):
        objetivo_valor = 0

        if missao not in self.__missoes:
            print(f"Missão não está atribuída ao personagem {self.nome}")
            return

        match missao:
            case MissaoColeta() as m:
                objetivo_valor = m.quantidade_item
            case MissaoCombate() as m:
                objetivo_valor = m.inimigos_a_derrotar
            case MissaoExploracao() as m:
                objetivo_valor = m.distancia
            case _:
                print("Tipo de missão desconhecido")
                return

        if progresso >= objetivo_valor:
            missao.concluir_missao()
            self._xp += missao.recompensa
            print(f"Missão '{missao.nome}' concluída!")
            print(f"Recompensa: {missao.recompensa} XP. XP Atual: {self._xp}")
        else:
            print(f"Progresso insuficiente para '{missao.nome}': {progresso}/{objetivo_valor}")



    def __str__(self):
        return f"Personagem(nome='{self.nome}', vida={self.vida}, nível={self.nivel}, xp={self.xp})"

    def __eq__(self, outro):
        if not isinstance(outro, Personagem):
            return False
        return self.nome == outro.nome and self.vida == outro.vida and self.nivel == outro.nivel and self.xp == outro.xp

    