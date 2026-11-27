# Semana 30/11 a 06/12/2026 · USP-SP e IPSEMG (as duas provas em 06/12).
# Autorização: mensagem do usuário de 27/11/2026 ("Vamos montar da próxima segunda até dia 6, que é a prova da USP").
#
# Fonte dos números (nada estimado):
#   USP-SP 2024: radar-editorial-USP-SP-SP-2024.pdf (211 alunos, 117 itens válidos)
#   IPSEMG 2024: ipsemg22.pdf / painel administrativo (254 alunos, 95 itens válidos)
#   Texto e gabarito: blocos do próprio relatório ou banco questoes-discriminacao_1.csv (conferidos).
# Descartados: IPSEMG 2025 (quintis incoerentes) e 2026 (11 alunos); questões que dependem de imagem não recebida;
# discriminação negativa; gabarito discutível. Ver SEMANA.md.
#
# Capa e legenda citam "Dados da plataforma Aristo" (também na MedQ, autorizado em 27/11) e não citam o nº de alunos.
# Texto revisado em passada de humanização (frases naturais, sem fórmulas repetidas), conteúdo técnico preservado.
# Marcação: **x** destaque (negrito / cor da marca na capa).

PROVAS = {'USP-SP': '06/12', 'IPSEMG': '06/12'}

POSTS = [{'id': 'ARISTO-20261130-01',
  'marca': 'Aristo',
  'data': '2026-11-30',
  'banca': 'USP-SP',
  'ano': '2024',
  'q': 'Q082',
  'area': 'Clínica Médica',
  'tema': 'Tuberculose: manejo de contatos',
  'titulo': 'TB: o bebê do contato não espera exame',
  'gabarito': 'B',
  'linha': 'PMB',
  'capa': {'headline': 'Bebê de 1 mês, sem vacina, na casa de um paciente com TB. **43% erraram a conduta.**',
           'dado': 'Na USP, quase metade escolheu errado entre tratar, investigar e vacinar.'},
  'enunciado': 'Homem, 32 anos, residente em uma grande cidade brasileira e procedente de outro país latino-americano, procura a UBS com '
               'queixa de tosse produtiva há dois meses. Nas últimas semanas, os episódios de tosse se intensificaram e, em um deles, '
               'foram vistos "raios de sangue" no catarro. Foi solicitada a baciloscopia do escarro, o TRM-TB, a sorologia para HIV e '
               'iniciado o tratamento de tuberculose. A vigilância epidemiológica do município realizou a investigação domiciliar. A '
               'família do paciente é formada pela sua esposa, de 27 anos, sogra, de 53 anos, e **filha de um mês de idade**. Chegaram ao '
               'Brasil há seis meses. Nenhuma delas refere sintomatologia respiratória. **A criança não recebeu nenhuma vacina.**',
  'comando': 'Além da solicitação de sorologia para HIV, assinale qual deve ser a conduta em relação aos contatos domiciliares do caso '
             'neste momento.',
  'alternativas': {'A': 'Tratar ILTB em todos os contatos domiciliares.',
                   'B': 'Investigar ILTB nas adultas e tratar ILTB na criança.',
                   'C': 'Investigar ILTB em todas e vacinar a criança com BCG.',
                   'D': 'Investigar ILTB e iniciar tratamento para todas.'},
  'raio': {'titulo': 'Gap de desempenho',
           'linhas': [('85,7%', 'acerto dos 20% com as melhores notas', 1), ('40,5%', 'acerto dos alunos com nota média (3º quintil)', 0)],
           'nota': 'Acerto geral: 56,9%. Diferença de **45,2 pontos** entre as melhores notas e as notas médias.'},
  'vies': [('Tratar todo mundo (A e D)', 'As adultas não têm sintomas. Antes de tratar, é preciso investigar a ILTB nelas.'),
           ('Vacinar com BCG (C)', 'Parece proteger, mas a criança já foi exposta a um caso bacilífero. A vacina não trata infecção.')],
  'pulo': {'pergunta': 'Por que a criança trata antes de investigar?',
           'blocos': [('O critério',
                       'Um bebê de 1 mês, sem vacina, morando com um caso bacilífero, tem risco alto de adoecer e de ter formas graves.'),
                      ('O que o Ministério da Saúde manda',
                       'A criança começa o tratamento da ILTB sem esperar a prova tuberculínica; depois é reavaliada e, se for o caso, '
                       'vacinada com BCG. As adultas são investigadas.')],
           'gabarito': 'Gabarito B: investigar as adultas e tratar a criança.'},
  'fecho': 'Com tuberculose em casa, quem tem 1 mês de vida não espera exame.',
  'legenda': 'Bebê de 1 mês, sem vacina, morando com um paciente com tuberculose: 43% erraram a conduta na USP-SP 2024. Tratar, investigar '
             'ou vacinar? A resposta está no carrossel. Dados da plataforma Aristo. A USP-SP é domingo, 06/12. #Aristo #USP #Tuberculose '
             '#ResidenciaMedica',
  'pergunta': 'Você trataria antes de investigar? Conte nos comentários.'},
 {'id': 'MEDQ-20261130-01',
  'marca': 'MedQ',
  'data': '2026-11-30',
  'banca': 'IPSEMG',
  'ano': '2024',
  'q': 'Q013',
  'area': 'Cirurgia Geral',
  'tema': 'Insuficiência venosa crônica: CEAP',
  'titulo': 'CEAP: a úlcera ainda está aberta',
  'gabarito': 'A',
  'linha': 'Ponto Cego de raciocínio',
  'capa': {'headline': 'Úlcera venosa aberta nas duas pernas. **44% chamaram de cicatrizada.**',
           'dado': 'Só 29,4% acertaram a CEAP. C5 ou C6?'},
  'enunciado': 'Paciente do sexo feminino, 55 anos, obesa, tabagista, apresenta quadro de insuficiência venosa crônica dos membros '
               'inferiores. Tem queixa de dor, edema, queimação e varizes de membros inferiores. Ao exame físico: membro inferior direito '
               '– varizes de grosso calibre, edema 2+/4, sinais de dermatite ocre e lipodermatoesclerose e **úlcera próximo de maléolo '
               'medial, medindo cerca de 2cm, com fundo granulado**, sem sinais de infecção. Membro inferior esquerdo – varizes de grosso '
               'calibre, edema 2+/4, sinais de dermatite ocre e **úlcera próxima de maléolo medial, medindo cerca de 5cm, com fundo '
               'granulado**, sem sinais de infecção.',
  'comando': 'De acordo com as Classificação CEAP para insuficiência venosa crônica, esta paciente deve ser categorizada na avaliação '
             'clínica como',
  'alternativas': {'A': 'C6.', 'B': 'C5.', 'C': 'C4.', 'D': 'C3.'},
  'raio': {'titulo': 'Distribuição das respostas',
           'linhas': [('44%', 'marcaram C5 (alternativa B)', 0), ('29,4%', 'marcaram C6, a correta (alternativa A)', 1)],
           'nota': 'O distrator atraiu **mais** que o gabarito.'},
  'vies': [('Por que o C5 atrai', 'C5 e C6 falam de úlcera. O que muda é se ela já fechou (C5) ou se continua aberta (C6).'),
           ('O que o enunciado mostra', 'Duas úlceras com fundo granulado, de 2 cm e 5 cm. Estão abertas.')],
  'pulo': {'pergunta': 'A escada clínica da CEAP',
           'blocos': [('C3 e C4', 'C3 é edema. C4 são as alterações de pele: pigmentação ou eczema (C4a) e lipodermatoesclerose (C4b).'),
                      ('C5 e C6',
                       'C5 é a úlcera venosa já cicatrizada. C6 é a úlcera ativa. Se há úlcera aberta, a classificação é C6, mesmo com '
                       'dermatite ocre e lipodermatoesclerose junto.')],
           'gabarito': 'Gabarito A: úlcera aberta é C6.'},
  'fecho': 'Cicatrizada é C5. Aberta é C6. A questão inteira cabe nessa diferença.',
  'legenda': 'Úlcera venosa aberta nas duas pernas, e 44% dos alunos a classificaram como cicatrizada. Só 29,4% acertaram a CEAP no IPSEMG '
             '2024. Veja no carrossel onde termina o C5. Dados da plataforma Aristo. O IPSEMG é domingo, 06/12. #MedQ #IPSEMG '
             '#CirurgiaVascular #ResidenciaMedica',
  'pergunta': 'Você teria marcado C5? Diga nos comentários.'},
 {'id': 'ARISTO-20261201-01',
  'marca': 'Aristo',
  'data': '2026-12-01',
  'banca': 'IPSEMG',
  'ano': '2024',
  'q': 'Q075',
  'area': 'Saúde Coletiva',
  'tema': 'Sensibilidade, especificidade e valores preditivos',
  'titulo': 'Trocar de teste: o que muda',
  'gabarito': 'A',
  'linha': 'PMB',
  'capa': {'headline': 'Teste rápido mais sensível na urgência. **46% não souberam o preço da troca.**',
           'dado': 'Sensibilidade de 93% contra 83%. O que sobe e o que cai quando você troca?'},
  'enunciado': 'Em um serviço de urgência, alguns kits de teste rápido foram avaliados para Influenza. O teste I apresenta **sensibilidade '
               'de 93% e especificidade de 95%**. Já o teste II tem **sensibilidade de 83% e especificidade de 100%**.',
  'comando': 'Quanto a esses conceitos, ao adotar o teste I neste serviço, comparado com o teste II, pode trazer',
  'alternativas': {'A': 'maior valor preditivo negativo e aumento de resultados falsos positivos.',
                   'B': 'maior valor preditivo negativo e aumento de resultados falsos negativos.',
                   'C': 'maior valor preditivo positivo e aumento de resultados falsos negativos.',
                   'D': 'positivos menor valor preditivo e aumento de resultados falsos positivos.'},
  'raio': {'titulo': 'Gap de desempenho',
           'linhas': [('85,7%', 'acerto dos 20% com as melhores notas', 1), ('43,1%', 'acerto dos alunos com nota média (3º quintil)', 0)],
           'nota': 'Acerto geral: 53,8%. Diferença de **42,6 pontos** entre as melhores notas e as notas médias.'},
  'vies': [('Sinais trocados',
            'Quem decorou "sensível exclui" sem pensar no tipo de erro acaba invertendo falso positivo e falso negativo.'),
           ('O detalhe do 100%', 'Com especificidade de 100%, o teste II não dá falso positivo. O teste I, com 95%, dá.')],
  'pulo': {'pergunta': 'Duas setas resolvem a questão',
           'blocos': [('Mais sensibilidade (93% contra 83%)',
                       'Menos falsos negativos. Um resultado negativo passa a valer mais: o VPN sobe.'),
                      ('Menos especificidade (95% contra 100%)', 'Aparecem falsos positivos, e o VPP cai.')],
           'gabarito': 'Gabarito A: ganha-se VPN e paga-se com falsos positivos.'},
  'fecho': 'Nenhum teste é de graça. Antes de trocar, pergunte qual erro você aceita.',
  'legenda': 'Trocar o teste rápido de influenza por um mais sensível parece só vantagem. 46% erraram o preço dessa troca no IPSEMG 2024. '
             'No carrossel, o que sobe e o que cai. Dados da plataforma Aristo. O IPSEMG é domingo, 06/12. #Aristo #IPSEMG #Epidemiologia '
             '#ResidenciaMedica',
  'pergunta': 'Na sua urgência, qual teste você usaria? Comente.'},
 {'id': 'MEDQ-20261201-01',
  'marca': 'MedQ',
  'data': '2026-12-01',
  'banca': 'USP-SP',
  'ano': '2024',
  'q': 'Q014',
  'area': 'Pediatria',
  'tema': 'Hipocalcemia neonatal',
  'titulo': 'Convulsão no prematuro: não era a glicose',
  'gabarito': 'B',
  'linha': 'Ponto Cego de raciocínio',
  'capa': {'headline': 'Prematuro de 800 g convulsionando. **Metade da prova correu para a glicose.**',
           'dado': '50,5% aumentaram o soro. Só 32,4% acharam a causa certa.'},
  'enunciado': ['Recém-nascido **pré-termo, com idade gestacional de 25+2/7 semanas**, nasceu de parto vaginal. Gestante apresentou '
                '**diabetes melito gestacional** manejada com orientações dietéticas, além de doença hipertensiva específica da gestação '
                'tratada com metildopa. Evoluiu com trabalho de parto prematuro. Feita administração de sulfato de magnésio e uma dose de '
                'corticoide antes do parto.',
                'RN nasceu hipotônico e sem choro, realizado clampeamento imediato do cordão umbilical e levado para o berço aquecido, '
                'realizada reanimação neonatal com necessidade de intubação orotraqueal, sendo encaminhado para Unidade de Terapia '
                'Intensiva (UTI) neonatal, após estabilização. **Peso ao nascimento: 800 g.** Apgar 3, 5 e 8, no primeiro, quinto e décimo '
                'minutos de vida, respectivamente.',
                'Na UTI foi mantido em ventilação mecânica, em jejum com sonda orogástrica aberta. Iniciada administração de soro '
                'glicosado a 10%, 56 mL e solução de aminoácidos 10%, 16 mL, intravenoso (IV), em 24 horas. **Glicemia capilar ("Dextro") '
                'controle, uma hora após o início do soro, de 50 mg/dL.** Com **15 horas de vida** paciente apresentou tremores de '
                'membros. Realizado eletroencefalograma de amplitude integrada que confirmou tratar-se de convulsão. A investigação '
                'laboratorial revelou causa metabólica.'],
  'comando': 'Assinale o tratamento adequado para a provável causa metabólica do episódio citado.',
  'alternativas': {'A': 'Ringer lactato 16 mL via IV.',
                   'B': 'Gluconato de cálcio 10%, 0,8 mL via IV.',
                   'C': 'Aumento do soro glicosado 10% para 65 mL via IV nas 24 horas.',
                   'D': 'Sulfato de magnésio 50% 0,1 mL via IM.'},
  'raio': {'titulo': 'Distribuição das respostas',
           'linhas': [('50,5%', 'aumentaram o soro glicosado (alternativa C)', 0),
                      ('32,4%', 'trataram com gluconato de cálcio, a correta (B)', 1)],
           'nota': 'O distrator atraiu **mais** que o gabarito.'},
  'vies': [('O reflexo da glicose',
            'Prematuro extremo, mãe com diabetes gestacional, convulsão: a hipoglicemia é a primeira hipótese que aparece.'),
           ('O dado que desmonta', 'O controle de glicemia deu 50 mg/dL. Não há hipoglicemia que explique a crise.')],
  'pulo': {'pergunta': 'Por que pensar em cálcio?',
           'blocos': [('Hipocalcemia precoce',
                       'Aparece nas primeiras 72 horas. Prematuridade, asfixia e mãe diabética são fatores de risco, e este recém-nascido '
                       'tem os três.'),
                      ('Como corrigir',
                       'Gluconato de cálcio a 10% na veia, devagar e com monitor cardíaco. Para 800 g, 0,8 mL é 1 mL/kg.')],
           'gabarito': 'Gabarito B: a convulsão era por hipocalcemia.'},
  'fecho': 'A glicemia está no enunciado justamente para você descartar a glicose.',
  'legenda': 'Prematuro de 800 g convulsionando, e metade da prova foi direto para a glicose: 50,5% aumentaram o soro na USP-SP 2024. A '
             'causa era outra, e só 32,4% acertaram. Veja no carrossel o dado que desmonta a hipoglicemia. Dados da plataforma Aristo. A '
             'USP-SP é domingo, 06/12. #MedQ #USP #Neonatologia #ResidenciaMedica',
  'pergunta': 'Qual exame você pediria primeiro? Responda nos comentários.'},
 {'id': 'ARISTO-20261202-01',
  'marca': 'Aristo',
  'data': '2026-12-02',
  'banca': 'USP-SP',
  'ano': '2024',
  'q': 'Q004',
  'area': 'Pediatria',
  'tema': 'Asma na criança: tratamento de controle',
  'titulo': 'Asma aos 3 anos: o degrau certo',
  'gabarito': 'C',
  'linha': 'PMB',
  'capa': {'headline': '3 anos, três internações por asma em 6 meses. **41% pularam degraus no tratamento.**',
           'dado': 'Mais da metade errou. Qual é o primeiro degrau aos 3 anos?'},
  'enunciado': ['Paciente do sexo feminino, **3 anos**, é admitida no pronto-socorro com quadro de tosse e dificuldade para respirar há um '
                'dia, sem febre ou coriza associados. Apresenta histórico de ter apresentado **três crises semelhantes nos últimos 06 '
                'meses, com necessidade de internação**. Na triagem, apresentava-se taquidispneica, sendo levada à sala de emergência.',
                'Na avaliação sistematizada em sala de emergência, a paciente apresentava os seguintes dados de exame físico e '
                'monitorização: A: Via aérea pérvia. B: Murmúrio vesicular com sibilos difusos, tempo expiratório prolongado, FR: 45 ipm, '
                'tiragens subdiafragmática, intercostal e de fúrcula, SpO2 93% em máscara não reinalante. C: 2BRNF sem sopros, FC: 140 '
                'bpm, tempo de enchimento capilar de 2 segundos, pulsos cheios. D: Alerta e orientada. E: **Lesões eritemato-crostosas em '
                'superfícies flexoras de pernas e braços.**'],
  'comando': 'Quanto ao uso profilático de corticoide inalatório no momento da alta hospitalar, é correto afirmar:',
  'alternativas': {'A': 'Não está indicado para essa paciente.',
                   'B': 'Deve estar associado ao beta agonista de longa duração.',
                   'C': 'Deve ser prescrito em dose baixa',
                   'D': 'Deve ser associado ao antileucotrieno.'},
  'raio': {'titulo': 'Raio-x da questão',
           'linhas': [('41%', 'associaram beta-agonista de longa duração (B)', 0),
                      ('73,8%', 'acerto dos 20% com as melhores notas', 1),
                      ('33,3%', 'acerto dos alunos com nota média (3º quintil)', 0)],
           'nota': 'Acerto geral: 46,2%. Diferença de **40,5 pontos** entre as melhores notas e as notas médias.'},
  'vies': [('A gravidade empurra para cima',
            'Três internações em seis meses levam o candidato a pular degraus e associar LABA logo de saída.'),
           ('A idade', 'Aos 3 anos, LABA não é o começo do tratamento de controle.')],
  'pulo': {'pergunta': 'Por onde começa o controle até os 5 anos?',
           'blocos': [('Precisa de controle?',
                       'Sim. Crises que internam e sinais de atopia (lesões nas dobras) mostram asma não controlada.'),
                      ('Por onde começar (GINA, até 5 anos)',
                       'Corticoide inalatório todos os dias, em dose baixa. Se não controlar, dobra-se a dose. LABA e antileucotrieno não '
                       'são o primeiro passo.')],
           'gabarito': 'Gabarito C: corticoide inalatório em dose baixa.'},
  'fecho': 'Crise grave não define o degrau da manutenção. A escada começa no mesmo lugar.',
  'legenda': '3 anos e três internações por asma em seis meses: 41% pularam degraus e associaram broncodilatador de longa duração na '
             'USP-SP 2024. No carrossel, o primeiro degrau para essa idade. Dados da plataforma Aristo. A USP-SP é domingo, 06/12. #Aristo '
             '#USP #Pediatria #ResidenciaMedica',
  'pergunta': 'O que você prescreveria na alta? Comente.'},
 {'id': 'MEDQ-20261202-01',
  'marca': 'MedQ',
  'data': '2026-12-02',
  'banca': 'IPSEMG',
  'ano': '2024',
  'q': 'Q015',
  'area': 'Cirurgia Geral',
  'tema': 'Câncer de próstata: classificação de D’Amico',
  'titulo': 'D’Amico: o que fica de fora',
  'gabarito': 'D',
  'linha': 'Ponto Cego de raciocínio',
  'capa': {'headline': 'PSA fora da classificação de risco do câncer de próstata? **39,5% acharam que sim.**',
           'dado': 'Só 36% acertaram qual critério realmente fica de fora.'},
  'enunciado': 'Para definir o tratamento do câncer de próstata, é necessário inicialmente saber se a doença é localizada, ou se já há '
               'acometimento a distância. Nos casos de doença localizada, a classificação mais aceita para o câncer de próstata é a de '
               "D'amico, que divide a doença em três grupos: baixo risco, risco intermediário e alto risco.",
  'comando': 'Essa classificação é definida levando em conta os seguintes parâmetros, **à exceção de um**. Assinale-o.',
  'alternativas': {'A': 'estadiamento clínico do tumor (“T”)',
                   'B': 'escore de Gleason',
                   'C': 'antígeno prostático específico sérico',
                   'D': 'idade do paciente'},
  'raio': {'titulo': 'Distribuição das respostas',
           'linhas': [('39,5%', 'disseram que o PSA fica de fora (C)', 0), ('36%', 'marcaram a idade, a correta (D)', 1)],
           'nota': 'O distrator atraiu **mais** que o gabarito.'},
  'vies': [('Pergunta pelo avesso', 'A banca quer o que NÃO entra. Na pressa, o candidato procura o que entra.'),
           ('A idade parece importante', 'E é, mas para escolher o tratamento, não para classificar o risco.')],
  'pulo': {'pergunta': 'Três critérios, três grupos',
           'blocos': [('Os critérios', 'Estadiamento clínico (T), escore de Gleason e PSA sérico.'),
                      ('Os grupos',
                       'Baixo risco: T1 a T2a, Gleason até 6 e PSA abaixo de 10. Alto risco: T2c ou mais, Gleason 8 ou mais, ou PSA acima '
                       'de 20. O restante é intermediário.')],
           'gabarito': 'Gabarito D: idade não entra na D’Amico.'},
  'fecho': 'T, Gleason e PSA. A idade fica para a conversa sobre tratamento.',
  'legenda': 'PSA fora da classificação de D’Amico? 39,5% dos alunos acharam que sim no IPSEMG 2024, e só 36% acertaram. No carrossel, os '
             'três critérios e os três grupos de risco. Dados da plataforma Aristo. O IPSEMG é domingo, 06/12. #MedQ #IPSEMG #Urologia '
             '#ResidenciaMedica',
  'pergunta': 'Você teria caído no comando negativo? Conte nos comentários.'},
 {'id': 'ARISTO-20261203-01',
  'marca': 'Aristo',
  'data': '2026-12-03',
  'banca': 'IPSEMG',
  'ano': '2024',
  'q': 'Q043',
  'area': 'Ginecologia e Obstetrícia',
  'tema': 'Indução do parto com cesárea prévia',
  'titulo': '41 semanas e cesárea prévia: como induzir',
  'gabarito': 'C',
  'linha': 'PMB',
  'capa': {'headline': '41 semanas, uma cesárea anterior, e ela quer parto normal. **Você usaria misoprostol?**',
           'dado': '48,2% erraram a conduta no IPSEMG.'},
  'enunciado': 'Gestante 36 anos, GII, PI, A0 (**PC há 4 anos**), **IG: 41 semanas**, foi encaminhada do pré-natal de risco habitual para '
               'resolução da gestação. Nega comorbidades, vícios ou alergias. Apresenta relutância a ser submetida a nova cesariana, e '
               '**deseja parto normal**. Ao exame, ausência de metrossístoles em 10 minutos, **colo fechado, grosso, posterior**, BCF: '
               '142, rítmico.',
  'comando': 'Diante do quadro em questão, qual conduta deverá ser tomada?',
  'alternativas': {'A': 'Iniciar indução com 50mcg de misoprostol via vaginal após autorização da paciente.',
                   'B': 'Explicar à paciente a necessidade de resolução por via alta devido à contraindicação a indução do trabalho de '
                        'parto.',
                   'C': 'Orientar acerca da tentativa de indução por método de Krause iniciar procedimento após autorização.',
                   'D': 'Aguardar trabalho de parto espontâneo.'},
  'raio': {'titulo': 'Gap de desempenho',
           'linhas': [('77,6%', 'acerto dos 20% com as melhores notas', 1), ('35,3%', 'acerto dos alunos com nota média (3º quintil)', 0)],
           'nota': 'Acerto geral: 51,8%. Diferença de **42,3 pontos** entre as melhores notas e as notas médias.'},
  'vies': [('Misoprostol (A)', 'É o indutor que vem primeiro à cabeça para colo desfavorável, mas a cicatriz uterina o contraindica.'),
           ('Cesárea obrigatória (B)', 'Cesárea anterior não proíbe a indução. Proíbe o misoprostol.')],
  'pulo': {'pergunta': 'Como induzir com útero cicatricial?',
           'blocos': [('Resolver', 'Com 41 semanas a gestação precisa ser resolvida. Esperar sem prazo (D) não é opção.'),
                      ('Como induzir',
                       'Colo desfavorável e cesárea prévia pedem método mecânico (sonda de Foley, método de Krause), com consentimento, '
                       'ocitocina se precisar e vigilância para rotura uterina.')],
           'gabarito': 'Gabarito C: indução mecânica, sem misoprostol.'},
  'fecho': 'Ela pode tentar o parto normal. O que muda é o método de indução.',
  'legenda': '41 semanas, uma cesárea anterior e uma gestante que quer parto normal: 48,2% erraram a conduta no IPSEMG 2024. Misoprostol, '
             'cesárea ou outra saída? Veja no carrossel. Dados da plataforma Aristo. O IPSEMG é domingo, 06/12. #Aristo #IPSEMG '
             '#Obstetricia #ResidenciaMedica',
  'pergunta': 'Você já induziu com Krause? Conte nos comentários.'},
 {'id': 'MEDQ-20261203-01',
  'marca': 'MedQ',
  'data': '2026-12-03',
  'banca': 'USP-SP',
  'ano': '2024',
  'q': 'Q068',
  'area': 'Saúde Coletiva',
  'tema': 'Coma: topografia da lesão',
  'titulo': 'Coma: as pupilas localizam a lesão',
  'gabarito': 'D',
  'linha': 'Ponto Cego de raciocínio',
  'capa': {'headline': 'Coma com pupilas médio-fixas. **41% apontaram a lesão no lugar errado.**',
           'dado': 'Só 22,5% acertaram. Você localiza a lesão pela pupila?'},
  'enunciado': 'Paciente do sexo masculino, desconhecido, foi encontrado em coma em via pública e trazido por ambulância à sala de '
               'emergência. Foi submetido à intubação orotraqueal na cena do resgate. Na avaliação inicial, há a descrição do seguinte '
               'exame neurológico: **resposta motora com extensão em membros inferiores e flexão em membros superiores aos estímulos '
               'dolorosos, pupilas médio-fixas**. Encontra-se em ventilação mecânica através de tubo orotraqueal.',
  'comando': 'Assinale qual é a topografia lesional atual para o caso conforme o exame neurológico descrito no caso apresentado.',
  'alternativas': {'A': 'Bulbo.', 'B': 'Ponte.', 'C': 'Córtex difuso.', 'D': 'Mesencéfalo.'},
  'raio': {'titulo': 'Distribuição das respostas',
           'linhas': [('41,1%', 'marcaram ponte (alternativa B)', 0), ('22,5%', 'marcaram mesencéfalo, a correta (D)', 1)],
           'nota': 'O distrator atraiu **quase o dobro** do gabarito.'},
  'vies': [('Por que a ponte atrai', 'Coma profundo e postura anormal fazem pensar no tronco mais baixo.'),
           ('O que a ponte mostraria', 'Lesão de ponte dá pupilas puntiformes, não médio-fixas.')],
  'pulo': {'pergunta': 'As pupilas localizam',
           'blocos': [('Médio-fixas', 'Mesencéfalo: as vias simpática e parassimpática são atingidas ao mesmo tempo.'),
                      ('Puntiformes ou reativas',
                       'Puntiformes apontam a ponte. Pupilas reativas num paciente em coma sugerem lesão cortical difusa ou causa '
                       'metabólica.')],
           'gabarito': 'Gabarito D: pupilas médio-fixas indicam mesencéfalo.'},
  'fecho': 'No coma, a lanterna localiza a lesão antes da tomografia.',
  'legenda': 'Coma com pupilas médio-fixas: 41,1% dos alunos apontaram a ponte na USP-SP 2024, e só 22,5% acertaram a topografia. No '
             'carrossel, como a pupila localiza a lesão. Dados da plataforma Aristo. A USP-SP é domingo, 06/12. #MedQ #USP #Neurologia '
             '#ResidenciaMedica',
  'pergunta': 'Qual achado você olha primeiro? Comente.'},
 {'id': 'ARISTO-20261204-01',
  'marca': 'Aristo',
  'data': '2026-12-04',
  'banca': 'USP-SP',
  'ano': '2024',
  'q': 'Q081',
  'area': 'Clínica Médica',
  'tema': 'Tuberculose resistente à rifampicina',
  'titulo': 'TB resistente: quem conduz o esquema',
  'gabarito': 'D',
  'linha': 'Pulo do Gato',
  'capa': {'headline': 'TB resistente à rifampicina na UBS. **39% começaram o tratamento ali mesmo.**',
           'dado': 'Mais da metade errou a conduta na USP. Quem conduz esse paciente?'},
  'enunciado': 'Homem, 32 anos, residente em uma grande cidade brasileira e procedente de outro país latino-americano, procura a UBS com '
               'queixa de tosse produtiva há dois meses. Nas últimas semanas, os episódios de tosse se intensificaram e, em um deles, '
               'foram vistos "raios de sangue" no catarro. Foi solicitada a baciloscopia do escarro, o TRM-TB, a sorologia para HIV e '
               'iniciado o tratamento de tuberculose. Em seu retorno, duas semanas depois, refere discreta melhora da tosse, mas "continua '
               'tossindo muito". O resultado da baciloscopia foi negativo para BAAR, enquanto resultado do **TRM-TB apresentou MTB '
               'detectado e resistência à rifampicina**.',
  'comando': 'Assinale qual deve ser a conduta adotada para o caso.',
  'alternativas': {'A': 'Solicitar novo TRM-TB, cultura e TS, e mantê-lo em seguimento na UBS até o resultado dos exames.',
                   'B': 'Solicitar novo TRM-TB, cultura e TS, e encaminhá-lo ao hospital especializado para isolamento.',
                   'C': 'Solicitar cultura e TS e iniciar esquema terapêutico para TB resistente, na própria UBS.',
                   'D': 'Solicitar novo TRM-TB, cultura e TS, e encaminhá-lo à referência terciária mantendo o acompanhamento na UBS.'},
  'raio': {'titulo': 'Raio-x da questão',
           'linhas': [('39,2%', 'iniciaram o esquema na UBS (alternativa C)', 0),
                      ('76,2%', 'acerto dos 20% com as melhores notas', 1),
                      ('46,3%', 'acerto dos alunos com nota boa (4º quintil)', 0)],
           'nota': 'Acerto geral: 46,9%. É o detalhe que separa o bom do ótimo: **29,9 pontos** entre o quintil 4 e o 5.'},
  'vies': [('Resolver na UBS (C)', 'Parece resolutivo, mas o esquema para TB resistente é definido e acompanhado pela referência.'),
           ('Internar para isolar (B)', 'Resistência, sozinha, não indica internação para isolamento.')],
  'pulo': {'pergunta': 'Quem faz o quê na TB resistente?',
           'blocos': [('Confirmar', 'Novo TRM-TB, cultura e teste de sensibilidade.'),
                      ('Encaminhar sem soltar',
                       'A referência terciária define e acompanha o esquema. A UBS continua com o paciente: tratamento observado e busca '
                       'dos contatos.')],
           'gabarito': 'Gabarito D: referência terciária, com a UBS junto.'},
  'fecho': 'Encaminhar não é passar o paciente adiante e esquecer dele.',
  'legenda': 'TRM-TB com resistência à rifampicina: 39% iniciaram o tratamento na própria UBS, e mais da metade errou a conduta na USP-SP '
             '2024. No carrossel, o que fica com a referência e o que fica com a UBS. Dados da plataforma Aristo. A USP-SP é domingo, '
             '06/12. #Aristo #USP #Tuberculose #ResidenciaMedica',
  'pergunta': 'Na sua UBS, como funciona esse encaminhamento? Comente.'},
 {'id': 'MEDQ-20261204-01',
  'marca': 'MedQ',
  'data': '2026-12-04',
  'banca': 'IPSEMG',
  'ano': '2024',
  'q': 'Q044',
  'area': 'Ginecologia e Obstetrícia',
  'tema': 'Classificação de Robson',
  'titulo': 'Robson: primigesta pélvica',
  'gabarito': 'A',
  'linha': 'Ponto Cego de raciocínio',
  'capa': {'headline': 'Primeira gestação, bebê pélvico. **Quase 7 em cada 10 erraram o grupo de Robson.**',
           'dado': '33,1% marcaram o grupo 7. Qual é o certo?'},
  'enunciado': 'A classificação de Robson é utilizada para avaliar, monitorar e comparar taxas de cesárea de forma prospectiva em uma '
               'mesma instituição ou entre instituições ao longo do tempo. Uma gestante, **primigesta**, com feto em **apresentação '
               'pélvica**, classifica-se como Robson',
  'comando': '',
  'alternativas': {'A': '6', 'B': '7', 'C': '8', 'D': '9'},
  'raio': {'titulo': 'Distribuição das respostas',
           'linhas': [('33,1%', 'marcaram o grupo 7 (alternativa B)', 0), ('31,5%', 'marcaram o grupo 6, a correta (A)', 1)],
           'nota': 'O distrator atraiu **mais** que o gabarito.'},
  'vies': [('6 e 7 são vizinhos', 'Os dois grupos são de feto pélvico. O que separa é a paridade.'),
           ('A palavra que decide', 'Primigesta é nulípara. Grupo 6.')],
  'pulo': {'pergunta': 'Os grupos que a banca vizinhou',
           'blocos': [('Grupos 6 e 7',
                       'Grupo 6: nulípara com feto único pélvico. Grupo 7: multípara com feto único pélvico, incluindo com cesárea '
                       'anterior.'),
                      ('Grupos 8 e 9',
                       'Grupo 8: gestação múltipla, incluindo com cesárea anterior. Grupo 9: feto único em situação transversa ou '
                       'oblíqua.')],
           'gabarito': 'Gabarito A: nulípara com feto pélvico é Robson 6.'},
  'fecho': 'Na Robson, uma palavra do enunciado muda o grupo.',
  'legenda': 'Primeira gestação, bebê pélvico: quase 7 em cada 10 alunos erraram o grupo de Robson no IPSEMG 2024, e 33,1% marcaram o '
             'grupo 7. No carrossel, os grupos que a banca colocou lado a lado. Dados da plataforma Aristo. O IPSEMG é domingo, 06/12. '
             '#MedQ #IPSEMG #Obstetricia #ResidenciaMedica',
  'pergunta': 'Você sabe os 10 grupos de cor? Conte nos comentários.'},
 {'id': 'ARISTO-20261205-01',
  'marca': 'Aristo',
  'data': '2026-12-05',
  'banca': 'IPSEMG',
  'ano': '2024',
  'q': 'Q014',
  'area': 'Cirurgia Geral',
  'tema': 'Câncer gástrico: classificação de Lauren',
  'titulo': 'Lauren: intestinal ou difuso',
  'gabarito': 'B',
  'linha': 'PMB',
  'capa': {'headline': 'Câncer gástrico do tipo intestinal. **48% não souberam como ele se espalha.**',
           'dado': 'Três das alternativas eram do tipo difuso. Você separa os dois?'},
  'enunciado': 'A classificação de Lauren para os tumores epiteliais do estômago despertou grande interesse entre os especialistas porque '
               'aborda um aspecto inédito que é a possibilidade de correlação entre a histologia com etiologia, patogenia, e mesmo a '
               'epidemiologia do câncer gástrico. Tal possibilidade valoriza consideravelmente a diferenciação histológica descrita por '
               'Lauren, entre o câncer gástrico do tipo difuso e tipo intestinal.',
  'comando': 'Considerando tal contexto, assinale a alternativa que apresente uma característica mais correlacionada com o câncer gástrico '
             'do **tipo intestinal**.',
  'alternativas': {'A': 'tipo sanguíneo A',
                   'B': 'disseminação hematogênica',
                   'C': 'células em anel de sinete',
                   'D': 'faixa etária mais jovem'},
  'raio': {'titulo': 'Gap de desempenho',
           'linhas': [('83,7%', 'acerto dos 20% com as melhores notas', 1), ('47,1%', 'acerto dos alunos com nota média (3º quintil)', 0)],
           'nota': 'Acerto geral: 51,6%. Diferença de **36,6 pontos** entre as melhores notas e as notas médias.'},
  'vies': [('Três alternativas do mesmo lado',
            'Tipo sanguíneo A, anel de sinete e paciente mais jovem são características do tipo difuso.'),
           ('Onde se erra', 'Sem os dois tipos organizados lado a lado, o candidato escolhe o termo que soa mais familiar.')],
  'pulo': {'pergunta': 'Intestinal contra difuso',
           'blocos': [('Intestinal',
                       'Associado a H. pylori, gastrite atrófica e metaplasia intestinal; mais diferenciado; idosos; disseminação '
                       'hematogênica (fígado).'),
                      ('Difuso',
                       'Células em anel de sinete, pouco diferenciado, mais jovens, tipo sanguíneo A e componente hereditário (CDH1); '
                       'dissemina por contiguidade e para o peritônio.')],
           'gabarito': 'Gabarito B: o tipo intestinal se espalha por via hematogênica.'},
  'fecho': 'Quem tinha a tabela intestinal contra difuso na cabeça resolveu em segundos.',
  'legenda': 'Câncer gástrico do tipo intestinal: 48% dos alunos não souberam como ele se espalha no IPSEMG 2024. No carrossel, intestinal '
             'e difuso lado a lado. Dados da plataforma Aristo. O IPSEMG é amanhã, 06/12. #Aristo #IPSEMG #Cirurgia #ResidenciaMedica',
  'pergunta': 'Qual característica você confundiria? Comente.'},
 {'id': 'MEDQ-20261205-01',
  'marca': 'MedQ',
  'data': '2026-12-05',
  'banca': 'USP-SP',
  'ano': '2024',
  'q': 'Q030',
  'area': 'Cirurgia Geral',
  'tema': 'Trauma toracoabdominal',
  'titulo': 'Trauma toracoabdominal: a resposta já estava na toracotomia',
  'gabarito': 'C',
  'linha': 'Ponto Cego de raciocínio',
  'capa': {'headline': 'Facada no tórax, toracotomia já feita. **89% erraram o que fazer com o abdome.**',
           'dado': '38,1% mandaram para a tomografia. A resposta já estava na cirurgia.'},
  'enunciado': 'Homem, 23 anos, vítima de ferimento por faca de cozinha em hemitórax direito, **sétimo espaço intercostal, linha axilar '
               'anterior**. Na sala de trauma encontra-se agitado, hipotenso (PA 80x45 mmHg) e com FC de 140 bpm. Realizado diagnóstico de '
               'hemitórax maciço e indicada toracotomia direita de emergência. O achado intraoperatório foi de lesão de artéria '
               'intercostal, resolvido através de ligadura primária, controle do sangramento e melhora dos parâmetros hemodinâmicos. **A '
               'cavidade torácica foi adequadamente inspecionada e não foram identificadas outras alterações no seu interior.** O '
               'cirurgião finaliza a abordagem cirúrgica torácica.',
  'comando': 'Considerando a situação desse paciente e seu ferimento na região toracoabdominal, assinale qual a conduta mais adequada '
             'neste momento.',
  'alternativas': {'A': 'Realizar laparotomia exploradora.',
                   'B': 'Realizar laparoscopia exploradora.',
                   'C': 'Lesões abdominais podem ser descartadas.',
                   'D': 'Encaminhar o paciente para tomografia de abdome.'},
  'raio': {'titulo': 'Distribuição das respostas',
           'linhas': [('38,1%', 'pediram tomografia de abdome (alternativa D)', 0),
                      ('11,4%', 'descartaram lesão abdominal, a correta (C)', 1)],
           'nota': 'Mesmo entre os 20% melhores, só **31%** acertaram.'},
  'vies': [('O alerta da região toracoabdominal', 'Facada abaixo do 4º ou 5º espaço intercostal faz pensar em diafragma e abdome.'),
           ('O que o enunciado já contou',
            'O cirurgião inspecionou a cavidade torácica, diafragma incluído, e não achou mais nada. Não houve trajeto para o abdome.')],
  'pulo': {'pergunta': 'Por que não investigar o abdome?',
           'blocos': [('O medo', 'Na região toracoabdominal, o risco é a lesão do diafragma, que abre caminho para o abdome.'),
                      ('O achado',
                       'A toracotomia não encontrou nada além da artéria intercostal. Sem lesão no diafragma, o ferimento ficou no '
                       'tórax.')],
           'gabarito': 'Gabarito C: a inspeção na cirurgia descartou lesão abdominal.'},
  'fecho': 'Às vezes a melhor conduta é não pedir mais nenhum exame.',
  'legenda': 'Facada no tórax, toracotomia já feita, e 89% erraram o que fazer com o abdome na USP-SP 2024: 38,1% pediram tomografia. No '
             'carrossel, o achado da cirurgia que já respondia a questão. Dados da plataforma Aristo. A USP-SP é amanhã, 06/12. #MedQ #USP '
             '#Trauma #ResidenciaMedica',
  'pergunta': 'Você teria pedido a tomografia? Comente.'},
 {'id': 'ARISTO-20261206-01',
  'marca': 'Aristo',
  'data': '2026-12-06',
  'banca': 'USP-SP',
  'ano': '2024',
  'q': 'Q100',
  'area': 'Ginecologia e Obstetrícia',
  'tema': 'Dismenorreia: conduta inicial',
  'titulo': 'Dismenorreia: estudar mais não resolveu',
  'gabarito': 'B',
  'linha': 'Ponto Cego de nível',
  'capa': {'headline': 'Cólica menstrual aos 20 anos. **Até entre os melhores alunos, mais da metade errou.**',
           'dado': 'Estudar mais não resolveu essa questão. Você investigaria antes de tratar?'},
  'enunciado': 'Paciente, 20 anos, queixa-se de **cólica intensa durante os ciclos menstruais regulares e mensais**. Nega outras '
               'comorbidades ou uso de medicamentos, com exceção de anti-inflamatórios e analgésicos por ocasião da dor menstrual. '
               'Avaliação clínica geral sem alterações. Exame ginecológico especular com conteúdo vaginal habitual, colo epitelizado; '
               'toque vaginal colo fibroelástico, fórnices vaginais regulares **sem massas identificáveis** e dor no fórnice vaginal '
               'posterior, útero antevertido e volume regular, não doloroso, regiões anexiais sem achados significativos.',
  'comando': 'Assinale qual é a conduta mais adequada neste momento.',
  'alternativas': {'A': 'Inserir sistema intrauterino de progesterona.',
                   'B': 'Iniciar contraceptivo hormonal oral combinado.',
                   'C': 'Prosseguir na investigação com ressonância magnética pélvica.',
                   'D': 'Prosseguir na investigação com ultrassom e preparo intestinal.'},
  'raio': {'titulo': 'Ponto cego de nível',
           'linhas': [('47,6%', 'acerto dos 20% com as melhores notas', 1), ('40,5%', 'acerto dos 20% com as notas mais baixas', 0)],
           'nota': 'Acerto geral: 41,6%. Só **7,1 pontos** separam o topo da base: o erro atinge todos por igual.'},
  'vies': [('A dor no fórnice posterior', 'Lembra endometriose e puxa para a investigação por imagem (C e D).'),
           ('Por que todo mundo erra',
            'O problema não é falta de estudo. É a ordem da conduta, e isso só se corrige com o conteúdo certo.')],
  'pulo': {'pergunta': 'Tratar ou investigar primeiro?',
           'blocos': [('A ordem',
                       'Jovem com dismenorreia, exame sem massas e alívio incompleto com anti-inflamatório: começa-se pelo contraceptivo '
                       'hormonal combinado.'),
                      ('Quando investigar',
                       'Se a dor continuar depois de 3 a 6 meses de tratamento bem feito, ou se houver massa no exame, a investigação de '
                       'endometriose passa à frente.')],
           'gabarito': 'Gabarito B: tratar primeiro e investigar se não melhorar.'},
  'fecho': 'Hoje é dia de prova. Sem massa no exame, trate primeiro. Boa prova.',
  'legenda': 'Cólica menstrual aos 20 anos: na USP-SP 2024, até entre os melhores alunos mais da metade errou. O problema era a ordem da '
             'conduta. Veja no carrossel. Dados da plataforma Aristo. Hoje é dia de USP-SP: boa prova. #Aristo #USP #Ginecologia '
             '#ResidenciaMedica',
  'pergunta': 'Depois conte como foi a prova.'},
 {'id': 'MEDQ-20261206-01',
  'marca': 'MedQ',
  'data': '2026-12-06',
  'banca': 'IPSEMG',
  'ano': '2024',
  'q': 'Q097',
  'area': 'Pediatria',
  'tema': 'Vacinação do recém-nascido prematuro',
  'titulo': 'Prematuro: idade corrigida não vale para vacina',
  'gabarito': 'D',
  'linha': 'Pulo do Gato',
  'capa': {'headline': 'Prematuro saindo da UTI. **56% erraram o calendário de vacinas.**', 'dado': 'Você vacinaria pela idade corrigida?'},
  'enunciado': 'Sobre a vacinação do RN prematuro, marque a alternativa correta.',
  'comando': '',
  'alternativas': {'A': 'Todos devem estar vacinados com BCG na alta.',
                   'B': 'A vacinação deverá ser realizada conforme idade gestacional corrigida.',
                   'C': 'A vacinação com quaisquer tipos de vacina deverá ser iniciada ainda na UTI Neonatal.',
                   'D': 'Em relação à hepatite B deverão receber 4 doses.'},
  'raio': {'titulo': 'Raio-x da questão',
           'linhas': [('71,4%', 'acerto dos 20% com as melhores notas', 1), ('50%', 'acerto dos alunos com nota boa (4º quintil)', 0)],
           'nota': 'Acerto geral: 44,2%. O detalhe que separa o bom do ótimo: **21,4 pontos**.'},
  'vies': [('Idade corrigida (B)', 'Serve para avaliar o desenvolvimento. O calendário vacinal do prematuro segue a idade cronológica.'),
           ('BCG e UTI (A e C)', 'A BCG espera o bebê chegar a 2 kg, e nem toda vacina pode ser dada na UTI neonatal.')],
  'pulo': {'pergunta': 'O que muda no calendário do prematuro?',
           'blocos': [('Hepatite B', 'Recém-nascido com menos de 2 kg ou menos de 33 semanas recebe 4 doses.'),
                      ('O resto do calendário', 'Segue a idade cronológica. A BCG espera os 2 kg.')],
           'gabarito': 'Gabarito D: hepatite B em 4 doses.'},
  'fecho': 'Hoje é dia de prova. Prematuro se vacina pela idade cronológica, e a hepatite B ganha uma dose a mais. Boa prova.',
  'legenda': 'Prematuro saindo da UTI: 56% erraram o calendário de vacinas no IPSEMG 2024. Idade corrigida ou cronológica? Veja no '
             'carrossel. Dados da plataforma Aristo. Hoje é dia de IPSEMG: boa prova. #MedQ #IPSEMG #Pediatria #ResidenciaMedica',
  'pergunta': 'Depois conte como foi a prova.'}]
