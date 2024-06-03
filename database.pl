% Definição de sintomas
sintoma(manchas_nas_folhas).
sintoma(murchamento_das_folhas).
sintoma(crescimento_lento).
sintoma(presenca_de_insetos).
sintoma(descoloracao_das_folhas).
sintoma(folhas_comidas).

% Definição de pragas e doenças e seus sintomas associados
praga(pulgao, [presenca_de_insetos, manchas_nas_folhas, descoloracao_das_folhas]).
praga(lagarta, [presenca_de_insetos, folhas_comidas]).
doenca(fungo, [manchas_nas_folhas, descoloracao_das_folhas, murchamento_das_folhas]).
doenca(virus, [manchas_nas_folhas, descoloracao_das_folhas, crescimento_lento]).

% Regra para verificar se uma lista de sintomas corresponde a uma praga ou doença
diagnostico(Sintomas, Problema) :-
    ( praga(Problema, SintomasProblema) ; doenca(Problema, SintomasProblema) ),
    subset(Sintomas, SintomasProblema).

% Função auxiliar para verificar se uma lista é subconjunto de outra
subset([], _).
subset([H|T], List) :-
    member(H, List),
    subset(T, List).