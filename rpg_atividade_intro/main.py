import os

from missao import Missao, MissaoColeta, MissaoCombate, MissaoExploracao, StatusMissao
from personagem import Personagem

os.system('cls')

input("Pressione Enter para Iniciar O RPG TOO:\n")
os.system('cls')

p_Pedro = Personagem("Pedro", 100, 1, 0)
p_Bianca = Personagem("Bianca", 100, 1, 0)
missao_tutorial = Missao("Complete o Tutorial", "Complete o Tutorial",20,StatusMissao.PENDENTE)

missao_tutorial.iniciar_missao()
missao_tutorial.concluir_missao()
missao_tutorial.exibir_informacoes()

print("\n\n----------------------------------\n\n")
input("Pressione Enter para continuar...")
os.system('cls')


missao_combate_goblins = MissaoCombate("Extermine os globins", "Globins são perigosos. Elimine todos.", 30, 10, "Goblin",StatusMissao.PENDENTE)
missao_combate_goblins.iniciar_missao()
missao_combate_goblins.concluir_missao()
missao_combate_goblins.exibir_informacoes()

print("\n\n----------------------------------\n\n")
input("Pressione Enter para continuar...")
os.system('cls')

missao_coleta_ervas = MissaoColeta("Colete Ervas para o Médico", "Seu companheiro foi ferido, o médico precisa de ervas medicianais para curá-lo.", 20,"Ervas Medicinais",10,StatusMissao.PENDENTE)
missao_coleta_ervas.iniciar_missao()
missao_coleta_ervas.concluir_missao()
missao_coleta_ervas.exibir_informacoes()

print("\n\n----------------------------------\n\n")
input("Pressione Enter para continuar...")
os.system('cls')

missao_exploracao_urithiru = MissaoExploracao("Explore a torre abandonada de Urithiru.", "A torre recém descoberta detém inúmeros segredos, explorea-a para a mapear!", 100, "Lagos Puros, Roshar", 1000, 60, StatusMissao.PENDENTE)
missao_exploracao_urithiru.iniciar_missao()
missao_exploracao_urithiru.concluir_missao()
missao_exploracao_urithiru.exibir_informacoes()

print("\n\n----------------------------------\n\n")



