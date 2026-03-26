# TOO-TRABALHO1-RPG
Objetivo: Aplicar os conceitos de Herança da Orientação a Objetos para criar tipos específicos de missões no universo de “Ecos de Arcadia”.
Objetivo: Aplicar os conceitos de Herança da Orientação a Objetos para criar tipos específicos de missões no
universo de “Ecos de Arcadia”.

1. Contexto

Na etapa anterior, nós criamos a classe genérica Missao com os seus respectivos atributos e métodos de acesso
(Getters e Setters) para garantir o Encapsulamento seguro dos dados.
Agora, a equipe de design do jogo determinou que existem categorias diferentes de missões e que cada categoria
precisa armazenar informações exclusivas para funcionar.
O seu trabalho é expandir o sistema implementando as subclasses (filhas) especializadas da Missao , baseando-se
na proposta do Estudo de Caso, focando na Herança sem recriar todas as regras já blindadas na classe mãe!

2. A Tarefa Prática

Atenção: Nesta atividade, você utilizará apenas o recurso da Herança. O isolamento de comportamentos e o
mecanismo de assinaturas dinâmicas via Polimorfismo e interfaces serão assunto de atividades futuras. Ainda não
implementaremos associação com o jogador (Personagem). As missões funcionarão de forma autônoma como
prova de estrutura.
Diagrama de Classes UML

«Enum»
Status
PENDENTE
EM_ANDAMENTO
CONCLUIDA
FRACASSADA

Missao
-nome String
-descricao String
-recompensa int
-status Status
+iniciar_missao()
+concluir_missao()
+exibir_dados()

MissaoCombate
-inimigos_a_derrotar int
-inimigo String

MissaoExploracao
-local String
-distancia int
-tempo_limite int

MissaoColeta
-item_necessario String
-quantidade_item int

Passo 1: Trabalhando com Enums - Criando o Enum Status

Antes de refinarmos a Classe Mãe e criar as Filhas, vamos organizar os estados das missões para reforçar o
encapsulamento e a legibilidade do código.
O objetivo desta etapa é compreender:
O uso de enums para representar valores fixos (constantes nominais);
O conceito de tipo enumerado como blindagem da aplicação.
1. Criar o Enum Status:
Deverá ser utilizado na classe Missao para gerenciar a progressão e a situação atual da quest.
Arquivo: Status.py (ou dentro do seu pacote de modelos)
Valores obrigatórios: PENDENTE , EM_ANDAMENTO , CONCLUIDA , FRACASSADA
Passo 2: Refinando a Classe Mãe (Vincular o Enum e Ações)
A nossa classe mãe Missao já é responsável pela gestão de dados fundamentais ( nome , descricao , recompensa
e status ).
2.1 Ajustes na classe Missao:
O atributo status deve ser inicializado por padrão com o valor Status.PENDENTE .
No setter de status , adicione uma validação: o atributo SOMENTE deve aceitar valores definidos no tipo
enumerado Status .
Ajuste o método exibir_dados() para mostrar adequadamente o status do jogo.
2.2 Implementação dos Métodos de Ação:
Nesta atividade, você deverá obrigatoriamente implementar na própria classe Missao as duas funções
mecânicas básicas do sistema (que poderão ser invocadas depois por qualquer filha que venha a herdá-la):
1. iniciar_missao(self) :
O que deve fazer: Verifique se o atributo de status atual é Status.PENDENTE . Caso sim, o objeto deve
alterar e modificar o status seguro para Status.EM_ANDAMENTO e exibir um print limpo anunciando o start
(ex: “A missão ‘[nome]’ começou! Objetivo central da missão: [descricao]”). Caso já esteja em andamento, deve
impedir de iniciar novamente.
2. concluir_missao(self) :
O que deve fazer: Verifique se o status está constando adequadamente como Status.EM_ANDAMENTO . Caso
validado, promova o status para Status.CONCLUIDA e exiba uma mensagem confirmando o desfecho da
jornada, apontando que a recompensa de sistema já estaria livre (ex: “Missão concluída como sucesso. A
contabilidade do prêmio de [recompensa] XP agora está pronta para retirada financeira.”).
Caso já esteja concluída ou esteja como pendente ou fracassada, deve alertar o erro ao usuário.

Passo 3: Implementando as Subclasses Filhas de Especialização
Você vai criar três classes separadas que derivam logicamente as possibilidades de jogo. Cada uma dessas classes
tem uma obrigatoriedade técnica: ela necessita carregar a regra da linguagem responsável para herdar ( Missao ). O
construtor interno natural de cada uma delas precisa executar a instrução especial da linguagem orientada
( super() ) repassando as informações mandatórias à mãe antes de isolar as suas variáveis secundárias!
Construa a seguinte trindade de classes filhas:
1. MissaoCombate : Missões focadas em enviar aventureiros em frentes de batalha e alvos únicos.
O que ela carrega de Inédito: Um atributo interno armazenando o tipo_inimigo (string) e
inimigos_a_derrotar (valor numérico inteiro).
2. MissaoColeta : Eventos onde os membros realizam extração nos recursos florestais.
O que ela carrega de Inédito: Um atributo registrando o material em item_necessario (string) além da
requisição de quantidade em quantidade_item (valor numérico inteiro).
3. MissaoExploracao : Aventuras com limites geográficos que exigem do herói deslocamento explorando o
limite desconhecido ou masmorras trancadas.
O que ela carrega de Inédito: Um limite de fim de área ou bioma instanciado em regiao_destino
(string), sendo associado com o cálculo global do trajeto distancia_em_km (float).
(Encapsule todos os atributos próprios das classes filhas com a visibilidade privada - uso de __ nos métodos getter e
setter).

3. Testes, Entrega e Verificação Final

Implemente um teste contendo:
1. Instancie pelo menos um objeto concreto dos itens criados (seja missões de Coleta, Exploração ou
Combates), e vincule ou use os seus respectivos enums.
2. Depois de instanciar os 3 objetos, chame os métodos declarados no Pai: .iniciar_missao() seguido
sucessivamente do .concluir_missao() , e .exibir_dados() do objeto.
Dicas e Observações
Utilize Enum.value ou Enum.name para mostrar o texto amigável em sua formatação textual e no
exibir_dados() .
Lembre-se, o Enum ajuda a evitar erros de digitação e garante consistência no código de todos os
programadores da Arcadia Studios!
Entrega
Prazo de Entrega: Até dia 02 de Abril às 08h.
A forma principal (e recomendada) de entrega desta atividade é através de um Repositório Público no GitHub.
Envie pelo Classroom o Link do seu repositório GitHub como comentário da Tarefa.
O repositório deve estar Público para que a professora consiga ter acesso aos arquivos e realizar a correção.
Observação: Se você nunca utilizou o GitHub antes, consulte o material de apoio “ ADD - Tutorial GitHub com
VS Code.md ” disponibilizado no Classroom para guiá-lo passo a passo!

Forma Alternativa (Com Desconto):
Alternativamente, você poderá enviar o formato .zip caso tenha dificuldades de versionamento:
Envie via Google Classroom anexando os arquivos da sua solução compactados em uma pasta .zip .
Atenção: O envio do projeto via .zip acarretará um desconto de 0,1 pontos na nota final da sua atividade.