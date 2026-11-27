# Auditoria crítica do piloto anterior (v0) — 15/11/2026

Escopo: os 6 carrosséis em `04_PILOTO_JA_PRODUZIDO/piloto_extraido` (30 PNGs, 2 PPTX, HTML, CSV/JSON/XLSX), comparados com os prints originais, o manual de marcas e as decisões Q01–Q78. Nenhum arquivo original foi alterado.

## 1. Integridade verificada (por inspeção real)

| Item | Resultado |
|---|---|
| ZIP de transferência | 132 arquivos extraídos; 130/130 hashes SHA-256 do manifesto conferem (os 2 restantes são o próprio manifesto/CSV de hashes) |
| Prints de posts | 43 PNG, todos 942×2048, todos abrem; inspecionados em folhas de contato e recortes ampliados |
| Calendários | 4 JPEG, 738×1600, legíveis (Medway e Grupo Medcof) |
| Manual | PDF de 96 páginas (Illustrator, 2025-01-20), texto extraível; páginas 22–28 (Aristo) e 66–72 (MedQ) lidas |
| CSVs | `questoes-discriminacao.csv`: 5.452 linhas/IDs únicos, 24 instituições, anos 2021–2026. `…-imagem.csv`: 414 linhas, 22 instituições. Só 2 de 5.452 enunciados trazem alternativas embutidas; nenhum gabarito; pasta `images/questions/` ausente |
| PNGs do piloto | 30, todos 1080×1350 |
| PPTX do piloto | 2 × 15 slides; texto nativo em Public Sans + formas nativas; únicas imagens são os logotipos (editável de fato) |
| HTML do piloto | referências relativas; funciona offline |

**Achado estrutural:** SCMGO e HA-SP **não existem nos CSVs** (as instituições lá são 24 outras, e os anos começam em 2021). As duas questões do piloto vêm exclusivamente de prints de posts antigos do MedQ (IMG_4718 e IMG_4713). São arquivos fornecidos pelo usuário (Q10 atendida), mas a prova original **não** está no pacote: a transcrição é fiel ao print, não à prova.

## 2. Questões originais — conferência literal com o print

- **SCMGO-GO 2022 (IMG_4718)**: enunciado "O estudo de coorte:" + A–D integralmente visíveis; gabarito A no print IMG_4721(1). O v0 transcreveu corretamente, inclusive "estudo de casos" na alternativa C (o post antigo IMG_4720 parafraseava como "caso-controle" — não repetir a paráfrase como se fosse literal).
- **HA-SP-SP 2017 (IMG_4713)**: enunciado + A–D visíveis; gabarito D no print IMG_4716. Transcrição do v0 correta.
- Pendência que permanece: confirmar com a prova original se havia alternativa E e se o gabarito oficial coincide. Sem isso, nenhuma das duas pode ir a PRONTO.

## 3. Achados classificados

### P0 — científico
1. **Nenhum erro científico de mérito nos 6 rascunhos.** Gabaritos A, C, D, A, A, D conferem com o conteúdo e com a literatura.
2. **Os três riscos herdados não estão no piloto, mas foram rechecados de forma independente** (ver §4). Nenhum deles foi reaproveitado.
3. Card 5 de todos os posts apresenta o *erro de raciocínio* como frase solta, sem rótulo ("Confundir acompanhamento longitudinal com ensaio clínico randomizado"). Lido isoladamente, parece recomendação. **Risco de mensagem invertida** → corrigido com rótulo explícito "Erro mais comum".
4. Dengue (v0): "Avaliação hospitalar imediata" é vago para o grupo C do Ministério da Saúde. A conduta central é **hidratação venosa imediata em qualquer ponto de atenção + leito de observação/internação**. Corrigido.

### P1 — clareza
1. Esqueleto idêntico de 5 cards nas duas marcas, com cards 3 e 4 praticamente iguais entre MedQ e Aristo → viola Q04/Q34 (abordagem e visual devem mudar).
2. Card 2 usa setas que sugerem sequência onde não há ("OBSERVAR → INTERVIR", "CICLO → PRÓXIMA", "DIA 1 → DIA 30").
3. Gancho do caso de anemia entrega a resposta ("Ferritina baixa").
4. "Resolução visual" da ovulação reduzida a três pontos numa linha; não explica *por que* (fase folicular variável × fase lútea ~constante).
5. Selo "PILOTO · REVISÃO DOCENTE PENDENTE" impresso nas artes. Status pertence à planilha/HTML, não ao PNG final.
6. Caso de dengue sem dado de sexo/FC; caso de anemia sem a pista clínica que ensina (consumo excessivo de leite de vaca).
7. Resolução só explica a correta; Q46 pede também o principal erro de raciocínio, e o formato MedQ pede o que cada alternativa cobrava.

### P2 — marca
1. MedQ usa roxo muito escuro (fora da paleta); a paleta oficial é #00DFE3, #452B9A, #B07DF4, #414042 (+ #F51068, #FF5607, #9CBFDA secundárias).
2. Nenhum recurso gráfico próprio das marcas: Aristo tem "formas de apoio" (aba, balão, encaixe, corte) no manual, p. 28; o v0 não usa.
3. Logotipos do v0 eram PNG redimensionados; agora extraídos diretamente do manual vetorial (versão original e monocromática branca).
4. Os PNGs do v0 foram renderizados sem Public Sans instalada (fonte de fallback); o PPTX declara Public Sans. Agora a renderização usa a Public Sans oficial (OFL, google/fonts).

### P3 — polimento
Contador de página dentro de círculo cortado; grandes vazios no card de questão; corpo de texto a ~28 px (abaixo do ideal para celular); CTA desenhado como botão (não clicável no Instagram).

## 4. Rechecagem independente dos três riscos legados (não herdar)

| Post antigo | Afirmação | Avaliação | Decisão |
|---|---|---|---|
| MedQ, IMG_4706–4710 (HC-UFPR 2020) | Atelectasia é a principal causa de febre nas primeiras 48 h | Contestada. Revisão sistemática (Mavros et al., *Chest* 2011) não encontrou associação entre atelectasia e febre pós-operatória precoce; a febre precoce é atribuída principalmente à resposta inflamatória ao trauma cirúrgico | Questão **excluída** por divergência científica (Q44) |
| MedQ, IMG_4711 (UNESP 2023) | "Um ensaio clínico de fase IV tem como objetivo:" com alternativas Longitudinalidade/Acessibilidade/Integralidade/Coordenação | Alternativas são atributos da APS (Starfield), incompatíveis com o enunciado; transcrição corrompida | **Bloqueada** (enunciado/alternativas não íntegros, Q05) |
| Aristo, IMG_4683 | Tratamento do CDIS "é sempre cirúrgico" | Absolutização incorreta. Cirurgia segue como padrão, mas há ensaios de monitoramento ativo em CDIS de baixo risco (COMET, LORIS, LORD); resultados de 2 anos do COMET (JAMA, 2024) não mostraram inferioridade do monitoramento para câncer invasivo ipsilateral nesse subgrupo | Não reutilizar a frase; qualquer post futuro deve dizer "tratamento padrão" e citar a exceção em investigação |

Outras alegações numéricas dos prints ("87% acertaram", "29% erraram", "117 questões em 3 anos", "94%" em IMG_4695) **não têm fonte auditável no pacote** e não foram usadas.

## 5. Calendários (Q70)

Os pilotos não dependem de prova iminente: SCMGO e HA-SP não constam dos calendários fornecidos. Provas próximas das datas do piloto (UNICAMP 15/11, USP-RP 20/11, SCM-BH 21/11, AMRIGS/PSU-MG 22/11, PSU-GO/UNIFESP/SUS-BA 29/11) não têm questão completa disponível no pacote (os CSVs não trazem alternativas nem gabarito). Desvio de Q72 registrado; as artes não insinuam vínculo com provas próximas (Q33). Comparação visual entre os dois calendários: as instituições presentes em ambos têm as mesmas datas; a cobertura difere. A comparação foi visual, não uma OCR exaustiva.

## 6. Datas

Hoje é 15/11/2026. O primeiro post MedQ está previsto para 16/11, e nenhum post passou por revisão docente. As datas foram mantidas como **previstas** (Q38/Q69). Se a aprovação não ocorrer a tempo, elas devem ser remanejadas na planilha-mestre, e nada pode ser registrado como publicado.
