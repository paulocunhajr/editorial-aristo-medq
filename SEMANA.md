# Semana 30/11 a 06/12/2026: USP-SP e IPSEMG (as duas provas em 06/12)

Autorização: mensagem do usuário de 27/11/2026, "Vamos montar da próxima segunda até dia 6, que é a prova da USP". É uma autorização à parte dos 6 pilotos (Gate 1), registrada aqui e na ficha de cada post.

## Grade

| Dia | Aristo | MedQ |
|---|---|---|
| Seg 30/11 | USP Q082 · TB: contato de 1 mês. Medianos 40,5% × topo 85,7% | IPSEMG Q013 · CEAP: 44% marcaram C5, só 29,4% acertaram C6 |
| Ter 01/12 | IPSEMG Q075 · VPN e falsos positivos. Medianos 43,1% × topo 85,7% | USP Q014 · Convulsão no RN de 800 g: 50,5% aumentaram o soro, 32,4% acertaram o cálcio |
| Qua 02/12 | USP Q004 · Asma aos 3 anos: 41% associaram LABA; medianos 33,3% | IPSEMG Q015 · D'Amico: 39,5% tiraram o PSA, 36% acertaram |
| Qui 03/12 | IPSEMG Q043 · Indução com cesárea prévia. Medianos 35,3% × topo 77,6% | USP Q068 · Coma: 41,1% apontaram a ponte, 22,5% o mesencéfalo |
| Sex 04/12 | USP Q081 · TB resistente: 39,2% trataram na UBS; quintil 4 46,3% × quintil 5 76,2% | IPSEMG Q044 · Robson: 33,1% grupo 7, 31,5% grupo 6 |
| Sáb 05/12 | IPSEMG Q014 · Lauren. Medianos 47,1% × topo 83,7% | USP Q030 · Trauma toracoabdominal: 11,4% de acerto, 38,1% pediram TC |
| Dom 06/12 | USP Q100 · Dismenorreia: topo 47,6% × base 40,5% (ponto cego de nível) | IPSEMG Q097 · Vacinação do prematuro: quintil 4 50% × quintil 5 71,4% |

## Fonte dos números

- **USP-SP 2024:** `radar-editorial-USP-SP-SP-2024.pdf` (211 alunos, 117 itens válidos, 3 anulados).
- **IPSEMG 2024:** `ipsemg22.pdf` e o painel administrativo (254 alunos, 95 itens válidos, 5 anulados).
- Todo número de capa e do card de dados foi copiado do relatório, sem estimativa. Quando o relatório não traz a distribuição completa, o card mostra só o que existe: acerto, distrator dominante e quintis.
- Enunciados, alternativas e gabaritos foram conferidos com o banco `questoes-discriminacao_1.csv`. Os 14 conferem; a única diferença é a correção de acento em "família".

## O que ficou de fora e por quê

- **IPSEMG 2025:** os quintis são incoerentes (Q5 = 0% em itens com 80% de acerto) e há 190 itens, o que sugere duas provas misturadas.
- **IPSEMG 2026:** só 11 alunos.
- **Dependem de imagem que não recebi:** USP Q033 (fratura exposta), Q037 (cateter), Q064 (veia cava), Q118, Q120, Q044; IPSEMG Q004 (TC de pâncreas).
- **Gabarito discutível:** IPSEMG Q033 (pielonefrite: o gabarito é uma descrição radiológica), Q006 (Forrest: a alternativa C também é questionável) e Q098 (HIV na sala de parto).
- **Discriminação negativa:** USP Q076 e Q005; IPSEMG Q029.
- **Sem professor nesta semana:** não há nomes nem fotos, e o checkpoint proíbe placeholders na arte.

## Pendências antes de publicar

1. **Revisão docente dos 14.** Pontos de atenção: USP Q030 (a toracotomia descarta lesão abdominal) e USP Q068 (a postura de decorticação sugere lesão acima do mesencéfalo; o gabarito se apoia nas pupilas).
2. **Chancela nos posts MedQ.** Os dados vêm do painel Aristo. Nos posts MedQ, a linha diz "Dados de N alunos que resolveram..." sem citar plataforma. É preciso confirmar se pode.
3. **Conferência visual.**

## Como regerar

Os textos estão em `gerador/conteudo.py`. Para refazer os JPGs, os ZIPs e o `index.html`, rode `python3 gerador/render.py`.
