
class Personagem:
    def __init__(self, nome, vida, nivel, xp):
        self._nome = nome
        self._vida = vida    
        self._nivel = nivel
        self._xp = xp

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

    def __str__(self):
        return f"Personagem(nome='{self.nome}', vida={self.vida}, nível={self.nivel}, xp={self.xp})"

    def __eq__(self, outro):
        if not isinstance(outro, Personagem):
            return False
        return self.nome == outro.nome and self.vida == outro.vida and self.nivel == outro.nivel and self.xp == outro.xp

    