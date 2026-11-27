# Semana 30/11 a 06/12/2026 · foco nas provas que estão chegando
# USP-SP (06/12) e SES-DF (12/12). Calendário de provas recebido pela equipe.
#
# Marcação usada nos textos:
#   **texto**  destaque (cor da marca na capa; negrito no enunciado = pista clínica)
#   [[__]]     dado PENDENTE do relatório da prova. Nunca preencher com estimativa.
#
# Números já confirmados: n_resolucoes (alunos que resolveram a questão na plataforma).
# Números pendentes: % de erro da capa e a distribuição por alternativa (card 3).
# Para preencher o card 3, acrescente ao post: dist={'A': 12, 'B': 8, 'C': 20, 'D': 60}

PROVAS = {
    'USP-SP': '06/12',
    'SES-DF': '12/12',
}

POSTS = [
# ───────────────────────── SEGUNDA 30/11 ─────────────────────────
dict(
    id='ARISTO-20261130-01', marca='Aristo', data='2026-11-30',
    banca='SES-DF', ano='2025', area='Obstetrícia', tema='Sífilis na gestação',
    titulo='Sífilis na gestante: tratar antes de confirmar?',
    gabarito='D', n=472,
    capa=dict(
        headline='VDRL 1/128 com 14 semanas. **Você esperaria o teste confirmatório?**',
        dado='[[__]] dos alunos erraram a conduta inicial.',
    ),
    enunciado='Uma gestante de **14 semanas** realizou exame de **VDRL com resultado de 1/128**, sem demais alterações nos exames de primeiro trimestre.',
    comando='Qual é a indicação referente ao tratamento inicial da paciente, **segundo o protocolo do Ministério da Saúde**?',
    alternativas={
        'A': 'Iniciar tratamento com penicilina benzatina, 2,4 milhões, dose única, em todos os casos.',
        'B': 'Não há necessidade de tratamento do parceiro por não ser transmissível na gravidez.',
        'C': 'Não há necessidade de solicitar nenhum teste confirmatório.',
        'D': 'Não há necessidade de aguardar confirmação diagnóstica para início do tratamento.',
    },
    vies=[
        ('A parece a mais segura', 'Penicilina benzatina é a droga certa. O erro está em "dose única em todos os casos": sem data de infecção conhecida, é sífilis latente de duração ignorada, e o esquema é de 3 doses.'),
        ('C e D parecem iguais', 'Não são. O teste confirmatório continua sendo pedido; ele só não pode atrasar a primeira dose.'),
    ],
    pulo=dict(
        pergunta='Por que não esperar o treponêmico?',
        blocos=[
            ('O reflexo', 'Confirmar antes de tratar, para não expor a gestante a um falso-positivo.'),
            ('O que o protocolo manda', 'Na gestante, um único teste reagente já autoriza iniciar penicilina benzatina. O segundo teste é solicitado junto e não atrasa o tratamento: cada semana sem penicilina é exposição fetal.'),
        ],
        gabarito='Gabarito D. Dose única só para sífilis recente. Sem data de infecção: 2,4 milhões UI por semana, por 3 semanas, e tratar a parceria.',
    ),
    professor=dict(area='Obstetrícia',
        fala='No pré-natal, eu não deixo a gestante sair com VDRL reagente sem a primeira dose. Peço o teste treponêmico no mesmo dia e chamo a parceria. Tratar só a gestante é contratar a reinfecção.'),
    fecho='A SES-DF não perguntou o diagnóstico. Perguntou se você deixaria a gestante voltar para casa sem penicilina.',
    legenda='VDRL 1/128 com 14 semanas. Você esperaria o teste confirmatório para tratar? A SES-DF cobrou exatamente essa decisão, segundo o protocolo do Ministério da Saúde. A resolução comentada está no carrossel, com o comentário do professor. Dados de 472 resoluções desta questão na plataforma Aristo. A SES-DF é em 12/12: salve para revisar. #Aristo #SESDF #Obstetricia #ResidenciaMedica',
),
dict(
    id='MEDQ-20261130-01', marca='MedQ', data='2026-11-30',
    banca='SES-DF', ano='2024', area='Obstetrícia', tema='Prevenção de pré-eclâmpsia',
    titulo='Pré-eclâmpsia: o que não previne',
    gabarito='B', n=859,
    capa=dict(
        headline='Metildopa controla a pressão. **Ela previne pré-eclâmpsia?**',
        dado='[[__]] dos alunos erraram uma questão de uma linha.',
    ),
    enunciado='Quanto às condições inerentes ao estado gestacional, assinale a alternativa correspondente à medida ou à droga que **não é recomendada para diminuição do risco** de pré-eclâmpsia.',
    comando='',
    alternativas={
        'A': 'Aspirina.',
        'B': 'Metildopa.',
        'C': 'Suplementação de cálcio caso o consumo seja menor do que 900 mg por dia.',
        'D': 'Atividade física por pelo menos 140 minutos por semana.',
    },
    vies=[
        ('O comando é negativo', 'A banca pede o que NÃO reduz o risco. Na leitura rápida, o candidato procura a medida que funciona.'),
        ('Metildopa "parece" a resposta certa', 'É a droga mais associada à gestação. Por isso o candidato a deixa de fora da lista de erradas.'),
        ('Atividade física parece conselho genérico', 'Mas tem efeito protetor documentado e entra nas recomendações de prevenção.'),
    ],
    pulo=dict(
        pergunta='Tratar a pressão é prevenir a doença?',
        blocos=[
            ('Reduzem o risco', 'AAS em baixa dose a partir de 12 semanas em gestante de risco; cálcio quando a ingestão é baixa; atividade física regular de pelo menos 140 minutos por semana.'),
            ('Não reduz o risco', 'Metildopa trata a hipertensão. Não muda a placentação, que é onde a pré-eclâmpsia começa.'),
        ],
        gabarito='Gabarito B. Anti-hipertensivo controla a pressão; não previne pré-eclâmpsia.',
    ),
    professor=None,
    fecho='Controlar a pressão não é prevenir a doença. A SES-DF cobrou essa diferença em uma única linha.',
    legenda='Metildopa controla a pressão. Ela previne pré-eclâmpsia? A SES-DF cobrou essa diferença com um comando negativo, e quem lê rápido cai. AAS, cálcio, atividade física e metildopa: só um não reduz o risco. Dados de 859 resoluções desta questão na plataforma MedQ. A SES-DF é em 12/12: salve para revisar. #MedQ #SESDF #Obstetricia #ResidenciaMedica',
),
# ───────────────────────── TERÇA 01/12 ─────────────────────────
dict(
    id='ARISTO-20261201-01', marca='Aristo', data='2026-12-01',
    banca='SES-DF', ano='2024', area='Ética Médica', tema='Código de Ética Médica',
    titulo='A frase adulterada do Código de Ética',
    gabarito='D', n=888,
    capa=dict(
        headline='A banca copiou uma frase do Código de Ética **e inverteu o sentido.**',
        dado='[[__]] dos alunos não perceberam. Você perceberia?',
    ),
    enunciado='Em relação ao **código de ética médica**, assinale a alternativa correta.',
    comando='',
    alternativas={
        'A': 'Faz parte dos princípios fundamentais a afirmação de que "o médico deve exercer a medicina com honra e dignidade, independentemente das condições de trabalho e da remuneração".',
        'B': 'É caracterizada como imprudência a omissão do médico em uma situação na qual o paciente necessite de intervenção imediata.',
        'C': 'Cabe ao médico, diante de um paciente em cuidados paliativos exclusivos com importante sofrimento, promover medidas que venham a antecipar a sua morte, desde que tenha sido previamente acordado com os familiares.',
        'D': 'O médico não pode divulgar, fora do meio científico, tratamento cujo valor ainda não esteja expressamente reconhecido cientificamente por órgão competente.',
    },
    vies=[
        ('A: a frase adulterada', 'O Princípio Fundamental III diz o contrário: para exercer a medicina com honra e dignidade, o médico necessita de boas condições de trabalho e remuneração justa.'),
        ('B: o termo trocado', 'Omitir-se diante de quem precisa de intervenção imediata é negligência. Imprudência é agir de forma precipitada.'),
        ('C: a vedação explícita', 'Abreviar a vida do paciente é vedado (art. 41), ainda que a pedido dele ou da família.'),
    ],
    pulo=dict(
        pergunta='O que diz o artigo 113?',
        blocos=[
            ('O texto do Código', 'É vedado ao médico divulgar, fora do meio científico, processo de tratamento ou descoberta cujo valor ainda não esteja expressamente reconhecido cientificamente por órgão competente.'),
            ('Na prática', 'Rede social, entrevista e material para o público leigo estão fora do meio científico.'),
        ],
        gabarito='Gabarito D. Em ética médica, a questão se decide pelo texto exato do Código.',
    ),
    professor=None,
    fecho='Em ética médica, a alternativa errada costuma ser uma frase verdadeira com uma palavra trocada. Leia devagar.',
    legenda='A SES-DF copiou uma frase do Código de Ética Médica e inverteu o sentido. Você perceberia? No carrossel: qual alternativa foi adulterada, qual termo foi trocado e o artigo que decide a questão. Dados de 888 resoluções desta questão na plataforma Aristo. A SES-DF é em 12/12: salve para revisar. #Aristo #SESDF #EticaMedica #ResidenciaMedica',
),
dict(
    id='MEDQ-20261201-01', marca='MedQ', data='2026-12-01',
    banca='SES-DF', ano='2024', area='Saúde Coletiva', tema='Indicadores demográficos',
    titulo='Índice de envelhecimento: o número trocado',
    gabarito='D', n=804,
    capa=dict(
        headline='60 ou 65 anos? Nascidos vivos ou menores de 15? **Um número decide a questão.**',
        dado='[[__]] dos alunos erraram o denominador.',
    ),
    enunciado='A respeito dos **indicadores utilizados para estudar a demografia no Brasil**, assinale a alternativa correta.',
    comando='',
    alternativas={
        'A': 'A taxa de fecundidade total é a relação entre o número de nascidos vivos e as mulheres com idade entre 20 e 45 anos.',
        'B': 'O índice de envelhecimento é a relação entre o número de pessoas com mais de 65 anos de idade e o número de nascidos vivos.',
        'C': 'A taxa de fecundidade total é a relação entre o número de nascidos vivos e o total da população.',
        'D': 'O índice de envelhecimento é a relação entre o número de pessoas com mais de 60 anos e o número de pessoas com menos de 15 anos de idade.',
    },
    vies=[
        ('B: dois números trocados', 'A estrutura está certa, mas troca 60 por 65 anos e menores de 15 por nascidos vivos.'),
        ('A e C: fecundidade com definição de outro indicador', 'Nascidos vivos sobre a população total é taxa de natalidade. Fecundidade total é número médio de filhos por mulher.'),
    ],
    pulo=dict(
        pergunta='Escreva a fração antes de ler a alternativa',
        blocos=[
            ('Índice de envelhecimento', 'Pessoas com 60 anos ou mais ÷ menores de 15 anos, por 100 (RIPSA).'),
            ('Natalidade e fecundidade', 'Natalidade: nascidos vivos ÷ população total, por mil. Fecundidade total: número médio de filhos por mulher ao fim da idade fértil (15 a 49 anos).'),
        ],
        gabarito='Gabarito D. A banca altera um elemento da fração: numerador, denominador ou faixa etária.',
    ),
    professor=dict(area='Medicina Preventiva',
        fala='Indicador demográfico se resolve pelo denominador. Antes de ler as alternativas, eu escrevo a fração no rascunho: quem está em cima, quem está embaixo e por quanto multiplica. A banca quase sempre altera um desses três.'),
    fecho='Na prova, quem escreve a fração no rascunho encontra a troca em segundos. Quem confia na memória, não.',
    legenda='60 ou 65 anos? Nascidos vivos ou menores de 15? Na SES-DF, um número decidiu a questão de indicadores demográficos. No carrossel, a fração de cada indicador e o comentário do professor. Dados de 804 resoluções desta questão na plataforma MedQ. A SES-DF é em 12/12: salve para revisar. #MedQ #SESDF #SaudeColetiva #ResidenciaMedica',
),
# ───────────────────────── QUARTA 02/12 ─────────────────────────
dict(
    id='ARISTO-20261202-01', marca='Aristo', data='2026-12-02',
    banca='SES-DF', ano='2025', area='Cirurgia', tema='Fios cirúrgicos',
    titulo='Fios cirúrgicos: natural não é absorvível',
    gabarito='D', n=795,
    capa=dict(
        headline='Categute, polidioxanona, poliglactina, seda. **Qual deles o corpo não absorve?**',
        dado='[[__]] dos alunos erraram uma questão de quatro palavras.',
    ),
    enunciado='Assinale a alternativa que corresponde a um **fio cirúrgico inabsorvível**:',
    comando='',
    alternativas={'A': 'Categute.', 'B': 'Polidioxanona.', 'C': 'Poliglactina.', 'D': 'Seda.'},
    vies=[
        ('Natural parece absorvível', 'Categute e seda são de origem natural. O primeiro é absorvido; o segundo, não. A origem não define o destino do fio.'),
        ('Polidioxanona parece permanente', 'É monofilamentar e de absorção lenta, por meses. Mesmo assim, é absorvível.'),
    ],
    pulo=dict(
        pergunta='Classifique pela absorção, não pela origem',
        blocos=[
            ('Absorvíveis', 'Categute (natural); poliglactina (Vicryl), poliglecaprona e polidioxanona (PDS), sintéticos.'),
            ('Inabsorvíveis', 'Seda e algodão (naturais); náilon, polipropileno (Prolene) e poliéster (sintéticos).'),
        ],
        gabarito='Gabarito D. A seda perde força tênsil com o tempo, mas é classificada como inabsorvível.',
    ),
    professor=dict(area='Cirurgia Geral',
        fala='Na sala, ninguém escolhe fio pela origem. Escolhe por quanto tempo o tecido precisa de sustentação. Quando você pensa assim, a classificação de absorvível e inabsorvível deixa de ser decoreba.'),
    fecho='Origem natural não quer dizer absorção. A SES-DF montou a questão inteira sobre essa confusão.',
    legenda='Categute, polidioxanona, poliglactina e seda. Qual deles o corpo não absorve? A SES-DF montou uma questão de quatro palavras sobre a confusão entre origem e absorção. No carrossel, a classificação completa e o comentário do professor. Dados de 795 resoluções desta questão na plataforma Aristo. A SES-DF é em 12/12: salve para revisar. #Aristo #SESDF #Cirurgia #ResidenciaMedica',
),
# MedQ 02/12: espaço livre (ver SEMANA.md).
# ───────────────────────── QUINTA 03/12 ─────────────────────────
dict(
    id='ARISTO-20261203-01', marca='Aristo', data='2026-12-03',
    banca='USP-SP', ano='2024', area='Ginecologia', tema='Contracepção na enxaqueca',
    titulo='Enxaqueca menstrual: qual contraceptivo?',
    gabarito='C', n=1391,
    capa=dict(
        headline='Enxaqueca sem aura não contraindica a pílula combinada. **A USP, mesmo assim, não a aceitou.**',
        dado='[[__]] dos alunos erraram. Você prescreveria a pílula?',
    ),
    enunciado='Paciente, 24 anos, deseja contracepção. Refere **cólica e cefaleia intensa que se inicia cerca de 2 dias antes da menstruação e piora com o início do fluxo**. Eventualmente apresenta náusea, mas **nega sintomas visuais**. Exame clínico e ginecológico sem alterações.',
    comando='Assinale qual é a alternativa mais adequada.',
    alternativas={
        'A': 'Preservativo.',
        'B': 'Dispositivo intrauterino cobre.',
        'C': 'Pílula progestagênica contínua.',
        'D': 'Pílula estrogênica-progestagênica cíclica.',
    },
    vies=[
        ('O acerto pelo motivo errado', 'Quem decorou "enxaqueca contraindica estrogênio" marcou C sem saber por quê. Sem aura e abaixo dos 35 anos, o combinado é permitido.'),
        ('A armadilha de D', 'A banca não perguntou o que é permitido. Perguntou o que é mais adequado para esta paciente.'),
    ],
    pulo=dict(
        pergunta='Por que não a pílula combinada cíclica?',
        blocos=[
            ('O padrão da crise', 'A dor começa 2 dias antes do fluxo: é enxaqueca menstrual, disparada pela queda do estrogênio. A pausa da pílula cíclica reproduz essa queda todo mês.'),
            ('O que resolve as duas queixas', 'Progestagênio contínuo, sem pausa, inibe a ovulação e reduz o sangramento: trata a cólica e tira o gatilho da crise. O DIU de cobre tende a piorar a cólica.'),
        ],
        gabarito='Gabarito C. Com aura, o estrogênio é contraindicado em qualquer idade. Sem aura, ele é permitido, mas não é a melhor escolha aqui.',
    ),
    professor=dict(area='Ginecologia',
        fala='No consultório, a primeira pergunta é quando a dor começa. Se ela acompanha o fluxo, a pausa da pílula é o gatilho, não a solução. O método contínuo trata a cólica e a crise com uma prescrição só.'),
    fecho='Permitido não é o mesmo que indicado. A USP cobra essa diferença na anamnese.',
    legenda='Enxaqueca sem aura não contraindica a pílula combinada. A USP, mesmo assim, não aceitou a pílula cíclica. Você sabe por quê? No carrossel, a leitura da anamnese e o comentário do professor. Dados de 1.391 resoluções desta questão na plataforma Aristo. A USP-SP é domingo, 06/12: salve para a véspera. #Aristo #USP #Ginecologia #ResidenciaMedica',
),
dict(
    id='MEDQ-20261203-01', marca='MedQ', data='2026-12-03',
    banca='USP-SP', ano='2024', area='Ginecologia', tema='Exame clínico das mamas',
    titulo='Palpação das mamas: qual posição?',
    gabarito='C', n=448,
    capa=dict(
        headline='Sentada, com os braços para cima. **É assim que você palparia a mama?**',
        dado='[[__]] dos alunos erraram a posição.',
    ),
    enunciado='Paciente, 26 anos, refere ter palpado tumor na mama direita e está preocupada com a possibilidade de ser câncer. Nuligesta, uso de contraceptivo hormonal oral combinado, sem comorbidades ou uso de medicamentos.',
    comando='Assinale qual é a forma adequada de **palpação** das mamas.',
    alternativas={
        'A': 'Paciente sentada em frente ao examinador, com elevação dos membros superiores acima da cabeça.',
        'B': 'Paciente sentada em frente ao examinador, com os membros superiores ao longo do tronco e as mãos espalmadas nas cristas ilíacas.',
        'C': 'Paciente em decúbito dorsal, com elevação dos membros superiores acima da cabeça.',
        'D': 'Paciente em decúbito dorsal, com os membros superiores ao longo do corpo.',
    },
    vies=[
        ('A e B descrevem inspeção', 'Paciente sentada, braços elevados ou mãos na cintura: são manobras da inspeção dinâmica, não da palpação.'),
        ('D está quase certa', 'Deitada é correto, mas com o braço ao longo do corpo a mama não se espalha sobre o tórax.'),
    ],
    pulo=dict(
        pergunta='Cada etapa do exame tem a sua posição',
        blocos=[
            ('Sentada', 'Inspeção estática (braços ao longo do corpo), inspeção dinâmica (braços elevados; mãos na cintura contraindo o peitoral) e palpação de axilas e fossas supraclaviculares.'),
            ('Deitada', 'Palpação das mamas em decúbito dorsal, com o braço do lado examinado elevado: a mama se espalha sobre a parede torácica e o tecido fica mais fino para palpar.'),
        ],
        gabarito='Gabarito C. A banca misturou as posições da inspeção com a da palpação.',
    ),
    professor=None,
    fecho='Inspeção e palpação usam posições diferentes. A USP perguntou só uma delas.',
    legenda='Sentada, com os braços para cima. É assim que você palparia a mama? A USP misturou as posições da inspeção com a da palpação. No carrossel, a posição de cada etapa do exame. Dados de 448 resoluções desta questão na plataforma MedQ. A USP-SP é domingo, 06/12: salve para a véspera. #MedQ #USP #Ginecologia #ResidenciaMedica',
),
# ───────────────────────── SEXTA 04/12 ─────────────────────────
dict(
    id='ARISTO-20261204-01', marca='Aristo', data='2026-12-04',
    banca='USP-SP', ano='2024', area='Pediatria', tema='Vasculite por IgA',
    titulo='Vasculite por IgA: o que vigiar depois',
    gabarito='C', n=1487,
    capa=dict(
        headline='As lesões já sumiram. **A USP quer saber o que você vigia nos próximos meses.**',
        dado='[[__]] dos alunos erraram o seguimento.',
    ),
    enunciado='Paciente de 4 anos previamente hígido está passando em consulta de rotina pediátrica. Mãe refere que, há cerca de 2 semanas, ele apresentou um quadro de **dor nos punhos e tornozelos, dor abdominal e "caroços elevados" pelo corpo**. Ela o medicou com **amoxicilina** por conta própria e refere que, após cerca de uma semana, as lesões começaram a melhorar. Ao exame, está em BEG, corado, hidratado, FC: 92 bpm, FR: 20 ipm, PA: 82x50 mmHg. Restante do exame clínico sem alterações, exceto por **lesões residuais em membros inferiores**, conforme imagem a seguir.',
    imagem='assets/usp2024-q11.jpg',
    comando='Considerando a principal hipótese diagnóstica, assinale os exames que deverão ser realizados de forma **seriada nos meses subsequentes**.',
    alternativas={
        'A': 'Hemograma com contagem de plaquetas e coagulograma.',
        'B': 'Anticorpo antiestreptolisina O e ecocardiograma.',
        'C': 'Função renal e sedimento urinário.',
        'D': 'Frações C3 e C4 do complemento.',
    },
    vies=[
        ('B: a pista falsa da amoxicilina', 'Artralgia e uso de antibiótico puxam para febre reumática. Mas não há cardite nem infecção estreptocócica documentada.'),
        ('A e D: exames de outras doenças', 'Púrpura palpável sem plaquetopenia não pede hemograma seriado. Complemento baixo é de glomerulonefrite pós-estreptocócica e lúpus; na vasculite por IgA, ele é normal.'),
    ],
    pulo=dict(
        pergunta='Por que o rim, se a pele melhorou?',
        blocos=[
            ('O diagnóstico', 'Púrpura palpável em membros inferiores, artralgia e dor abdominal em criança: vasculite por IgA (púrpura de Henoch-Schönlein).'),
            ('O seguimento', 'A nefrite define o prognóstico e pode surgir semanas depois da melhora da pele. Urina, pressão arterial e função renal seriadas por cerca de 6 meses.'),
        ],
        gabarito='Gabarito C. Na vasculite por IgA, o seguimento é renal.',
    ),
    professor=None,
    fecho='A pele melhora sozinha. O rim não avisa. A USP cobrou o seguimento, não o diagnóstico.',
    legenda='As lesões já sumiram. A USP quer saber o que você vigia nos próximos meses. Amoxicilina, artralgia e púrpura: a pista falsa e o diagnóstico estão no carrossel. Dados de 1.487 resoluções desta questão na plataforma Aristo. A USP-SP é domingo, 06/12: salve para a véspera. #Aristo #USP #Pediatria #ResidenciaMedica',
),
dict(
    id='MEDQ-20261204-01', marca='MedQ', data='2026-12-04',
    banca='USP-SP', ano='2024', area='Clínica Médica', tema='Tratamento da ICFEr',
    titulo='ICFEr: o pilar que falta',
    gabarito='D', n=1091,
    capa=dict(
        headline='Frequência cardíaca de 68. **Quem marcou ivabradina errou por 2 batimentos.**',
        dado='[[__]] dos alunos erraram a prescrição. Você completaria o tratamento?',
    ),
    enunciado='Mulher de 65 anos, **diabética** em uso de metformina 1.000 mg de 12/12 horas/dia, procura UBS por dispneia aos médios esforços, há 2 meses. Relata infarto agudo do miocárdio (IAM) há 4 anos e traz ECO com **fração de ejeção de 33%** e hipocinesia de parede lateral. Está em uso de AAS 100 mg/dia, atorvastatina 40 mg/dia, **carvedilol 25 mg duas vezes/dia, enalapril 20 mg duas vezes/dia, espironolactona 25 mg uma vez/dia** e furosemida 40 mg/dia. Ao exame físico, apresenta PA: 120x76 mmHg e **FC: 68 bpm**, ausculta pulmonar normal e sem edema de membros inferiores.',
    comando='Assinale o tratamento medicamentoso indicado para essa paciente.',
    alternativas={
        'A': 'Introduzir ivabradina ou aumentar dose de espironolactona.',
        'B': 'Substituir carvedilol por bisoprolol para melhor beta bloquear e aumentar furosemida.',
        'C': 'Associar sacubitril-valsartana e diminuir dose de carvedilol.',
        'D': 'Associar iSGLT2 ou trocar enalapril por sacubitril-valsartana.',
    },
    vies=[
        ('A: a ivabradina', 'Exige ritmo sinusal com FC de pelo menos 70 bpm apesar do betabloqueador otimizado. Ela está com 68.'),
        ('C: a associação proibida', 'Sacubitril-valsartana com IECA aumenta o risco de angioedema. A troca exige 36 horas sem enalapril; associar, nunca.'),
        ('B: a troca sem motivo', 'Carvedilol 25 mg duas vezes ao dia já é dose-alvo, com benefício comprovado.'),
    ],
    pulo=dict(
        pergunta='Qual pilar está faltando?',
        blocos=[
            ('O que ela já usa', 'Betabloqueador (carvedilol), IECA (enalapril) e antagonista mineralocorticoide (espironolactona): três dos quatro pilares da ICFEr.'),
            ('O que falta', 'iSGLT2 (dapagliflozina ou empagliflozina), indicado na ICFEr com ou sem diabetes. Trocar o IECA por sacubitril-valsartana também é recomendado para quem segue sintomático.'),
        ],
        gabarito='Gabarito D. A alternativa traz as duas condutas recomendadas.',
    ),
    professor=dict(area='Cardiologia',
        fala='Diante de ICFEr sintomática, eu não começo mexendo no diurético. Confiro os quatro pilares e pergunto qual está faltando. Aqui faltava o iSGLT2, e o diabetes só reforça a indicação.'),
    fecho='Quatro pilares. Ela usava três. A USP quis saber se você sentiria falta do quarto.',
    legenda='Frequência cardíaca de 68. Quem marcou ivabradina errou por 2 batimentos. A USP montou uma questão de ICFEr com três pilares prescritos e um faltando. No carrossel, cada distrator e o comentário do professor. Dados de 1.091 resoluções desta questão na plataforma MedQ. A USP-SP é domingo, 06/12: salve para a véspera. #MedQ #USP #Cardiologia #ResidenciaMedica',
),
]
