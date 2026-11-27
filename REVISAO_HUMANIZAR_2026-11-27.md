# Revisão editorial Humanizar — 27/11/2026

## Escopo

20 carrosséis: seis do piloto e 14 da semana de 30/11 a 06/12. Revisão da redação visível em index.html, das 20 legendas individuais, das seis fichas do piloto e dos controles JSON/CSV do piloto. Revisão de títulos, conceitos e comentários pedagógicos quando necessário. Os dados de desempenho, referências, identificadores, datas, gabaritos, caminhos de arquivos e status de aprovação permanecem os mesmos.

A revisão é textual, não uma nova validação clínica ou confirmação dos relatórios de desempenho. Nenhuma questão foi promovida a PRONTO.

## Mudanças importantes

- Remoção de slogans, contrastes artificiais, frases repetidas e atribuição especulativa de motivos aos candidatos.
- Legendas com foco no caso, no dado de desempenho e no conceito a revisar, com variação das chamadas. A chancela Aristo foi mantida para as duas marcas.
- Ovulação: tratar o cálculo como estimativa, não como previsão individual.
- Dismenorreia: retirar a inferência de que estudar mais não resolveu; os dados de acerto não demonstram a causa do erro.
- Convulsão neonatal: contextualizar a glicemia de 50 mg/dL na questão; não apresentá-la isoladamente como exclusão universal de hipoglicemia.
- Trauma toracoabdominal: vincular a conclusão ao cenário e ao gabarito, evitando extrapolação para outros pacientes.

## Bloqueios antes da publicação

- Não foi possível renderizar o site publicado nem inspecionar as artes rasterizadas (PNG/JPG), os PPTX/XLSX ou o conteúdo dos ZIPs nesta revisão.
- Sincronizar os textos revisados nas artes e títulos de capa quando aplicável; preservar enunciados e alternativas oficiais.
- Regenerar os ZIPs afetados e os editáveis; sincronizar o XLSX do piloto com o JSON/CSV. Confirmar que a legenda copiada no site é idêntica à incluída no ZIP.
- Validar as fontes clínicas e os dados de desempenho, com revisão docente independente. Conferir especialmente os itens de glicemia neonatal, VPN, vacinação do prematuro, tuberculose em lactentes, localização pupilar e trauma.
- Conferir visualmente os cards após a substituição de texto; remover o aviso de revisão do HTML somente depois de sincronizar os arquivos e passar pela revisão visual.

## Verificações executadas

- 20 registros JSON no HTML antes e depois; chaves protegidas preservadas.
- 20 legendas TXT derivadas diretamente da mesma revisão dos registros HTML.
- Seis fichas JSON e controle mestre JSON/CSV atualizados, sem alterar campos protegidos.
- Não houve teste de navegador, inspeção visual de imagens, comparação individual de todos os TXT anteriores ou validação de ZIP. Não publicar esta revisão sem concluir os bloqueios.

## Segunda rodada: voz editorial e fidelidade aos dados

Revisão de 55 campos dos mesmos 20 posts. A primeira versão das 20 legendas individuais foi conferida com o HTML e todas coincidiram. A segunda versão foi aplicada aos TXT, ao HTML e às fichas/controles textuais do piloto.

**Aristo:** destaque para o método de revisão e para os percentuais por quintil quando disponíveis. **MedQ:** destaque para a resolução do caso e as alternativas escolhidas pelos alunos. A diferenciação segue a finalidade editorial das marcas; não é um novo levantamento de desempenho.

Os percentuais agregados de 43% (TB contato), 46% (teste influenza), 48,2% (indução), 48% (Lauren) e 56% (vacinação do prematuro) foram substituídos nas legendas por percentuais por quintil registrados nas respectivas justificativas. Esses agregados estavam nas legendas anteriores, mas não constavam das justificativas numéricas consultadas; a substituição não afirma que os dados anteriores eram falsos. No trauma, Robson e TB resistente, priorizaram-se os percentuais de alternativas diretamente registrados. As justificativas, referências, gabaritos, metadados e status não foram alterados. O material original segue no histórico do Git.

A revisão clínica é de redação e delimitação ao enunciado, não confirmação de condutas. Foram contextualizados os conceitos de hipocalcemia neonatal, VPN, asma, indução com cesárea prévia, topografia pupilar, Robson, disseminação do câncer gástrico, trauma e vacinação. A equipe docente deve verificar as fontes e os casos completos antes de aprovar.

As chamadas comerciais e os convites a revisar variam conforme o assunto. Mantidas as hashtags e a identificação dos casos fictícios. Não houve revisão visual dos 117 cards ou regeneração de ZIP/PPTX/XLSX; o PR permanece rascunho. Não publicar antes da sincronização e aprovação.

## Solicitação de simplificação visual

- Removida a frase “Dados da plataforma Aristo.” das 14 legendas da semana de 30/11 a 06/12, tanto no HTML quanto nos TXT correspondentes. Fontes dos dados, referências e identificação da banca mantidas nas fichas.
- Removido o contador de navegação x/n sobre o visualizador do site, mantendo as setas e miniaturas.
- A área e o tema permanecem como metadados de classificação no site (filtros, gráficos e fichas). Não os apagar das fontes estruturadas.
- Inspeção de 11 artes originais: a numeração e os rótulos solicitados também estão incorporados aos pixels das imagens, não apenas ao HTML. Exemplos: p/Aristo/2026-11-30/post-01/01.jpg (chancela e rodapé de área/tema), p/Aristo/2026-11-30/post-01/02.jpg (2/6), MedQ/2026-11-16/post-01/01.png (1/6 e rótulo de área). Remover esses elementos nos arquivos fonte ou no processo de renderização; não apagar textos dos enunciados, alternativas, referências internas, números das questões, percentuais de acerto, datas de prova nem logos. Regenerar as imagens e os ZIPs correspondentes, além dos PPTX editáveis do piloto. A edição binária não foi executada nesta rodada porque o repositório não está acessível ao ambiente de processamento de arquivos; o acesso pelo conector permite inspeção, mas não fornece um checkout local. Não considerar esta etapa visual concluída.
