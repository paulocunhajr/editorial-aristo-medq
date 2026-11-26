# Semana 30/11 a 06/12/2026: formato "prova real"

Foco nas provas que estão chegando: **USP-SP (06/12)** e **SES-DF (12/12)**. Os posts antigos (16/11 a 31/01) saíram do site e das pastas; continuam no histórico do Git.

## Grade

| Dia | Aristo | MedQ |
|---|---|---|
| Seg 30/11 | SES-DF 2025 · Sífilis na gestante: tratar antes de confirmar? **(professor)** | SES-DF 2024 · Metildopa previne pré-eclâmpsia? |
| Ter 01/12 | SES-DF 2024 · A frase adulterada do Código de Ética | SES-DF 2024 · Índice de envelhecimento **(professor)** |
| Qua 02/12 | SES-DF 2025 · Fios cirúrgicos: qual o corpo não absorve? **(professor)** | livre (ver abaixo) |
| Qui 03/12 | USP-SP 2024 · Enxaqueca menstrual: qual contraceptivo? **(professor)** | USP-SP 2024 · Palpação das mamas: qual posição? |
| Sex 04/12 | USP-SP 2024 · Vasculite por IgA: o que vigiar depois | USP-SP 2024 · ICFEr: FC 68 e a ivabradina **(professor)** |
| Sáb 05 / Dom 06 | véspera e dia da USP-SP: sem carrossel | |

A SES-DF vem antes porque tem mais questões no banco; a USP-SP fica para quinta e sexta, mais perto da prova.

## Estrutura de cada carrossel

1. **Capa:** gancho provocativo, dado de erro e a chancela "Dados extraídos de N resoluções desta questão na plataforma".
2. **Questão oficial:** enunciado com as pistas em negrito e as alternativas. Vira dois cards quando não cabe em um.
3. **O ponto cego:** distribuição real das respostas e por que cada distrator atrai.
4. **O que a banca cobrou:** a resolução técnica e o gabarito.
5. **Comentário do professor:** foto, nome, área e uma fala curta em primeira pessoa. Entra em 5 dos 9 posts.
6. **Fechamento:** provocação final, "Salve para revisar" e "Envie para quem vai fazer a prova".

Regras do prompt seguidas: nenhum número inventado, sem jargão de cursinho, sem clichês ("regra de ouro", "virada de chave") e sem emojis.

## Pendências antes de publicar

- **Relatório de cada prova.** Precisamos do % de erro (capa) e do % por alternativa (card 3) das 9 questões. No card, esses campos aparecem como `__%` em amarelo. O N de resoluções já é real e vem do banco anterior.
- **Professores.** Faltam nome e foto dos 5 professores (Obstetrícia, Medicina Preventiva, Cirurgia Geral, Ginecologia e Cardiologia), e cada um precisa validar ou reescrever a própria fala.
- **Revisão docente** de toda a parte científica.
- **Logo vetorial.** O logo atual foi recortado das artes antigas; para a versão final, usar o arquivo do João.
- **MedQ quarta 02/12.** A questão de hernioplastia da SES-DF depende de uma imagem de terceiro (Instituto Simutec), então ficou de fora. Também não há questões de SCM-SP (05/12) nem de IPSEMG (06/12) no banco. Se mandarem uma questão dessas provas, ela entra nesse espaço.

## Como regerar

Os textos ficam em `gerador/conteudo.py`. Para preencher os dados, troque `[[__]]` pelo número na capa e acrescente `dist={"A": 12, "B": 8, ...}` ao post para o card 3. Depois rode:

```
python3 gerador/render.py
```

O script refaz os JPGs, os ZIPs por post e por dia e o `index.html`.
