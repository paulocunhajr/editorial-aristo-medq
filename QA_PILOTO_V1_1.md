# QA do piloto v1.1 (6 carrosséis): 27/11/2026

Escopo: somente os 6 pilotos autorizados (Gate 1). Nada foi publicado, agendado ou enviado. Os outros 148 não foram tocados nesta etapa.

## 1. Material: o que foi aberto e o que falta

| Material | Situação | Como foi verificado |
|---|---|---|
| ZIP `ARISTO_MEDQ_TRANSFERENCIA_COMPLETA_PARA_CLAUDE_2026-11-15.zip` | **NÃO RECEBIDO.** O caminho está no Mac do usuário, inacessível desta sessão na nuvem. Também não está no Google Drive (busca por nome e por ZIP) | `ls` nos uploads e busca no Drive |
| Q01–Q78, Checkpoint v1.0, Riscos e Conflitos, histórico reconstituído, LEIA_ME | **Não lidos** (estão no ZIP) | — |
| 43 prints de posts, 4 calendários, manual de marca (PDF, 96 p.) | **Não vistos** (estão no ZIP) | — |
| `questoes-discriminacao.csv` | Aberto: 5.452 linhas, 24 instituições; colunas id, instituição, ano, ordem, enunciado, discriminação, imagens; **sem alternativas e sem gabarito** | `csv` em Python |
| `questoes-discriminacao-imagem.csv` | Aberto: 414 linhas, mesmas colunas | idem |
| Versões `_1` dos CSVs, enviadas antes nesta conversa | Abertas: 5.452 e 414 linhas, **com** alternativas, gabarito e comentário. Origem a confirmar | idem |
| SCMGO e HA-SP nos CSVs | **Ausentes** em todas as versões; as 4 peças de questão dependem só dos prints | busca por instituição |
| Auditoria v0, `piloto_mestre` (154), controle Sheets, IMAGENS_A_ENVIAR | Lidos | leitura integral |
| PPTX v0 do Drive (Aristo e MedQ) | Baixados: 15 slides cada, texto nativo, únicas imagens = logotipos; ainda trazem o selo "PILOTO · REVISÃO DOCENTE PENDENTE" na arte | python-pptx; SHA-256 em `_recebido/` |
| Renders v1 (pós-auditoria) | Achados no Git (commit `bfc8614`), mas só em JPG 720×900 e sem fonte editável | `git show`, inspeção visual de todos os 34 |

**Achado fora do escopo, só registrado:** a `piloto_mestre` traz 154 posts, incluindo lotes "etapa 2" (versão `v1 · lote etapa 2`/`questões etapa 2`), e o repositório chegou a ter os 154 renderizados. Não sei se houve autorização explícita da etapa 2 em mensagem que eu não vi. Não usei nem alterei esse material.

## 2. Auditoria do piloto v1 (P0 a P3) e o que foi feito

| Nível | Achado | Post | Ação na v1.1 |
|---|---|---|---|
| **P0** pedagógico | O roteiro de 3 perguntas (quem define a exposição / pessoa ou grupo / seguimento no tempo) **não separa coorte de caso-controle**, e a capa dizia que ele classifica "quase qualquer desenho" | Aristo 23/11 | 4ª pergunta acrescentada: "Parte da exposição ou do desfecho?" (cards 1, 2, 4, 6, legenda e ficha) |
| P0 menor | Tabela: custo "altos" da coorte vale para a prospectiva | Aristo 23/11 | Trocado para "maiores" + nota "Na coorte retrospectiva, custo e tempo podem ser menores" |
| P1 | Resolução do dengue dizia só "reposição volêmica imediata"; a ficha já tinha o volume do MS | MedQ 17/11 | Card 4 cita 10 mL/kg de SF 0,9% na 1ª hora e leito por no mínimo 48 h; sinais de alarme destacados no card 2 |
| P1 | Rodapé "Marque a sua e deslize" sobrepunha a alternativa D | MedQ 18/11 | Rodapé dentro do fluxo |
| P2 | PNG da v1 em 720×900 JPG, abaixo do formato exigido | todos | Nova renderização em PNG 1080×1350 (34 de 34 conferidos) |
| P2 | Paleta MedQ | MedQ | Usa a paleta citada na auditoria v0 (#452B9A, #00DFE3, #B07DF4, #414042; #F51068, #FF5607). **Não conferida no PDF do manual** |
| P2 | Logotipo | todos | Extraído dos PPTX v0 (que a auditoria diz vir do manual vetorial); versão branca gerada a partir do mesmo alfa |
| P3 | Vazios grandes nos cards claros, corpo ~28 px | todos | Conteúdo centrado e ampliado até o limite (corpo 31 a 42 px); verificação automática de sobreposição e corte |

Mantido da v1 sem mudança: gabaritos (A, C, D, A, A, D), textos das questões, legendas (exceto Aristo 23/11), formatos por marca, ausência de selo de ficção na arte e ausência de qualquer percentual de acerto.

Riscos herdados (atelectasia, "fase IV" e CDIS "sempre cirúrgico"): nenhum aparece nos 6. A rechecagem independente da auditoria v0 continua válida. Não reli as fontes nesta sessão.

## 3. Conferências realizadas

- **PNG:** 34 arquivos em 1080×1350; todos inspecionados em miniatura e os cards corrigidos em tamanho cheio; checagem automática de texto cortado e de sobreposição ao logo: 0 ocorrências.
- **PPTX (`editaveis/`):** texto e formas nativos (Aristo: 220 caixas de texto, 124 formas, 17 logotipos; MedQ: 165, 108, 17). Renderizados no LibreOffice e comparados com os PNG: fiéis. Diferença residual: sombra leve nas formas no LibreOffice.
- **Google Drive (criados como arquivos novos, nada sobrescrito):**
  - Aristo Slides nativo: https://docs.google.com/presentation/d/120CeuG0A5moBwJYAF36fOIP3zSwgjedJxlf8EZM2c3M/edit
  - MedQ Slides nativo: https://docs.google.com/presentation/d/1TxnCID1VqcTlU6B00q3cR60fHHVKmZPMsqTLieZ7jyI/edit
  - Sheets nativo: https://docs.google.com/spreadsheets/d/1PXZydvMvSbTzyE--Lq0U1aoDwRohANJo2rSwOnEGbW4/edit
  - Lidos de volta: tipos `google-apps.presentation`/`spreadsheet`, todo o texto presente. **Não vi a renderização visual** dentro do Google Slides. A coluna `candidato_reel` do Aristo 23/11 no Sheets ainda diz "roteiro de 3 perguntas"; a versão local já está corrigida.
- **Biblioteca HTML offline:** abre por `file://` sem nenhuma requisição de rede, sem erro de JavaScript, imagens e ZIPs com caminhos relativos existentes; calendário, filtros, prévias, legenda, fundamentação, status e marcação de Reel funcionando.

## 4. Pendências que bloqueiam a aprovação

1. **ZIP de transferência:** sem ele, não li as decisões Q01–Q78, o Checkpoint nem os Riscos e Conflitos, e não vi o manual nem os prints. Qualquer conflito com essas decisões não foi checado.
2. **Questões SCMGO 2022 e HA-SP 2017 (4 peças):** transcrição não reconferida com os prints nesta sessão, e a prova original segue ausente (existência de alternativa E e gabarito oficial). Até isso, elas não podem ir a PRONTO.
3. **Revisão docente** dos 6, em especial a 4ª pergunta do roteiro (Aristo 23/11), o volume do grupo C (dengue) e os cortes de Hb (anemia).
4. **Conferência visual** contra o manual: cores Aristo (#006BFD e marinho #021024 vieram dos renders v1), paleta MedQ e as formas de apoio (aba e balão da Aristo; blocos da MedQ).
5. **Datas:** todas as datas previstas (16 a 25/11) já passaram. Nada foi publicado. As datas precisam ser remanejadas após a aprovação.

## 5. Arquivos

`piloto_v1/entrega/` (o mesmo conteúdo de `Piloto_Aristo_MedQ_v1_1_entrega.zip`):
- `Aristo|MedQ/AAAA-MM-DD/post-01/`: `01.png…`, `legenda.txt`, `ficha.json`
- `editaveis/`: `Aristo_Piloto_v1_1.pptx` e `MedQ_Piloto_v1_1.pptx`
- `controle/`: `piloto_mestre_v1_1.json`, `.csv` e `.xlsx` (status manuais com validação e status geral por fórmula)
- `biblioteca.html` + `zip/` + fonte
- `gerador/`: scripts que refazem tudo a partir de `conteudo_piloto.py` e da ficha-mestre
