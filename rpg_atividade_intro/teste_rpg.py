from missao import *
from personagem import *

p_Bianca = Personagem("Bianca", 100, 1, 0)
missao_tutorial = MissaoCombate("Complete o Tutorial", "Complete o Tutorial",50,1,"Dragão Celestial",StatusMissao.PENDENTE)
missao_coletar_ervas = MissaoColeta("Colete Ervas", "O Curandeiro da vila pediu para pegar ervas-raras", 20,"Erva-Rara",10,StatusMissao.PENDENTE)

p_Bianca.iniciar_missao_p(missao_tutorial)
p_Bianca.progredir_missao(missao_tutorial,1)

print("\n----------------------------------------\n")

p_Bianca.iniciar_missao_p(missao_coletar_ervas)

p_Bianca.progredir_missao(missao_coletar_ervas,5)
p_Bianca.progredir_missao(missao_coletar_ervas,10)