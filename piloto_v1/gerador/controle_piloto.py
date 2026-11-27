"""Fichas, legendas, planilha-mestre (JSON/CSV/XLSX), biblioteca HTML offline e ZIP de entrega do piloto v1.1.

Fonte: _recebido/piloto_mestre_v1_154.json (fichas v1 de 15/11) + mudanças da v1.1 abaixo.
Uso: python3 piloto_v1/gerador/controle_piloto.py  (depois de render_piloto.py)
"""
import csv, json, re, shutil, zipfile
from pathlib import Path

G = Path(__file__).resolve().parent
P1 = G.parent
ROOT = P1.parent
OUT = P1 / 'entrega'
IDS = ['MEDQ-20261116-01', 'MEDQ-20261117-01', 'MEDQ-20261118-01', 'ARISTO-20261123-01', 'ARISTO-20261124-01', 'ARISTO-20261125-01']

V11 = {
    'MEDQ-20261116-01': 'v1.1: redesenho em 1080x1350 PNG; texto da v1 mantido.',
    'MEDQ-20261117-01': 'v1.1: resolução do card 4 passa a citar a conduta completa do grupo C (10 mL/kg de SF 0,9% na 1ª hora; leito por no mínimo 48 h), já registrada no conceito decisivo da v1; dor e vômitos destacados no card 2.',
    'MEDQ-20261118-01': 'v1.1: redesenho; rodapé "Marque a sua" passa a ficar no fluxo do card (não sobrepõe a alternativa D).',
    'ARISTO-20261123-01': 'v1.1 (P0 pedagógico): o roteiro de 3 perguntas não distinguia coorte de caso-controle (ambos individuados, observacionais e com dimensão temporal) e a capa dizia que classificava "quase qualquer desenho". Acrescentada a 4ª pergunta (parte da exposição ou do desfecho?) nos cards 1, 2, 4 e 6; tabela do card 5 troca "altos" por "maiores" e ganha nota sobre coorte retrospectiva.',
    'ARISTO-20261124-01': 'v1.1: redesenho; conteúdo da v1 mantido.',
    'ARISTO-20261125-01': 'v1.1: redesenho; conteúdo da v1 mantido.',
}
LEGENDA_V11 = {
    'ARISTO-20261123-01': 'Pare de decorar os tipos de estudo: quatro perguntas classificam os desenhos que mais caem. Testamos o roteiro numa questão da SCMGO 2022. Salve para a revisão. #Aristo #Epidemiologia #ResidenciaMedica',
}
CONCEITO_V11 = {
    'ARISTO-20261123-01': 'Roteiro de 4 perguntas: quem define a exposição (observacional × experimental), pessoa ou grupo (individuado × agregado), seguimento no tempo (longitudinal × transversal) e ponto de partida (exposição: coorte × desfecho: caso-controle).',
}
REEL_V11 = {
    'ARISTO-20261123-01': 'sim (hipótese editorial, sem dado de desempenho): roteiro de 4 perguntas aplicável em vídeo curto',
}
TEXTO_OPC_V11 = {
    'ARISTO-20261123-01': 'O roteiro vale para os desenhos mais cobrados em prova; a SCMGO 2022 é só o teste.',
}


def fichas():
    base = {r['id']: r for r in json.loads((P1 / '_recebido' / 'piloto_mestre_v1_154.json').read_text())}
    out = []
    for i in IDS:
        r = dict(base[i])
        r['versao'] = 'v1.1 · 2026-11-27'
        r['legenda'] = LEGENDA_V11.get(i, r['legenda'])
        r['conceito_decisivo'] = CONCEITO_V11.get(i, r['conceito_decisivo'])
        r['texto_opcional_carrossel'] = TEXTO_OPC_V11.get(i, r['texto_opcional_carrossel'])
        r['candidato_reel'] = REEL_V11.get(i, r['candidato_reel'])
        r['notas_auditoria'] = r['notas_auditoria'] + ' ' + V11[i]
        if r['tipo'] == 'Questão original':
            r['notas_auditoria'] += ' Bloqueio de PRONTO mantido: os prints IMG_4713–4721 e a prova original não foram recebidos nesta sessão (ZIP de transferência inacessível), então a transcrição não pôde ser reconferida.'
        r['data_nota'] = 'Data prevista já passou em 27/11/2026; nada foi publicado. Remanejar na planilha após aprovação (Q38/Q69).'
        folder = OUT / r['marca'] / r['data_prevista'] / 'post-01'
        imgs = sorted(p.relative_to(OUT).as_posix() for p in folder.glob('*.png'))
        r['imagens'] = imgs
        r['n_cards'] = len(imgs)
        r['status_cientifico'] = 'PENDENTE: revisão docente'
        r['status_visual'] = 'PENDENTE: conferência visual'
        r['status_geral'] = 'PENDENTE'
        r['imagens_pendentes'] = []
        out.append(r)
        (folder / 'legenda.txt').write_text(r['legenda'] + '\n', encoding='utf-8')
        (folder / 'ficha.json').write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding='utf-8')
    return out


COLS = ['id', 'marca', 'data_prevista', 'titulo', 'tema', 'dificuldade', 'grande_area', 'instituicao', 'ano', 'tipo', 'formato',
        'familia_gancho', 'gabarito', 'n_cards', 'status_cientifico', 'status_visual', 'status_geral', 'candidato_reel', 'discriminacao',
        'conceito_decisivo', 'erro_principal', 'fonte_questao', 'referencias', 'justificativa_selecao', 'texto_opcional_carrossel',
        'notas_auditoria', 'data_nota', 'legenda', 'versao', 'autorizacao']


def planilhas(rows):
    c = OUT / 'controle'; c.mkdir(parents=True, exist_ok=True)
    (c / 'piloto_mestre_v1_1.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
    with open(c / 'piloto_mestre_v1_1.csv', 'w', newline='', encoding='utf-8-sig') as fh:
        w = csv.writer(fh)
        w.writerow(COLS)
        for r in rows:
            w.writerow([' | '.join(r[k]) if isinstance(r.get(k), list) else r.get(k, '') for k in COLS])
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill, Alignment
        from openpyxl.worksheet.datavalidation import DataValidation
        wb = Workbook(); ws = wb.active; ws.title = 'Piloto v1.1'
        ws.append(COLS)
        for r in rows:
            ws.append([' | '.join(r[k]) if isinstance(r.get(k), list) else r.get(k, '') for k in COLS])
        for cell in ws[1]:
            cell.font = Font(bold=True, color='FFFFFF'); cell.fill = PatternFill('solid', fgColor='1D1E24')
        # status geral derivado dos dois status manuais (mesma regra da planilha v1.2)
        sci, vis, ger = COLS.index('status_cientifico') + 1, COLS.index('status_visual') + 1, COLS.index('status_geral') + 1
        from openpyxl.utils import get_column_letter as L
        for i in range(2, len(rows) + 2):
            ws.cell(i, ger).value = (f'=IF(OR(ISNUMBER(SEARCH("BLOQUEADO",{L(sci)}{i})),ISNUMBER(SEARCH("BLOQUEADO",{L(vis)}{i}))),"BLOQUEADO",'
                                     f'IF(AND(LEFT({L(sci)}{i},8)="APROVADO",LEFT({L(vis)}{i},8)="APROVADO"),"PRONTO","PENDENTE"))')
        dv = DataValidation(type='list', formula1='"PENDENTE: revisão docente,APROVADO,BLOQUEADO"', allow_blank=False)
        dv2 = DataValidation(type='list', formula1='"PENDENTE: conferência visual,APROVADO,BLOQUEADO"', allow_blank=False)
        ws.add_data_validation(dv); ws.add_data_validation(dv2)
        dv.add(f'{L(sci)}2:{L(sci)}{len(rows) + 1}'); dv2.add(f'{L(vis)}2:{L(vis)}{len(rows) + 1}')
        for col in range(1, len(COLS) + 1):
            ws.column_dimensions[L(col)].width = 40 if COLS[col - 1] in ('notas_auditoria', 'legenda', 'conceito_decisivo', 'referencias', 'fonte_questao', 'justificativa_selecao') else 18
            for row in ws.iter_rows(min_row=2, min_col=col, max_col=col):
                row[0].alignment = Alignment(wrap_text=True, vertical='top')
        ws.freeze_panes = 'B2'
        wb.save(c / 'piloto_mestre_v1_1.xlsx')
        print('xlsx ok')
    except ImportError:
        print('openpyxl ausente: XLSX não gerado')


def biblioteca(rows):
    """Reaproveita o catálogo HTML do repositório (calendário, filtros, prévias, legendas, status) com os dados do piloto."""
    src = (ROOT / 'index.html').read_text(encoding='utf-8')
    data = []
    for r in rows:
        d = dict(r)
        d['imgs'] = r['imagens']
        d['zip'] = f"zip/{r['data_prevista']}_{r['marca']}.zip"
        d['pasta'] = f"{r['marca']}/{r['data_prevista']}/post-01"
        d['banca'] = f"{r['instituicao']} {r['ano']}".strip() if r['instituicao'] != 'Não se aplica' else 'Caso autoral'
        d['status_derivado'] = r['status_geral']
        d['referencias'] = r['referencias']
        d['notas_auditoria'] = r['notas_auditoria'] + ' ' + r['data_nota']
        data.append(d)
    i = src.index('const DATA=') + len('const DATA=')
    _, end = json.JSONDecoder().raw_decode(src[i:])
    s = src[:i] + json.dumps(data, ensure_ascii=False) + src[i + end:]
    dayz = {r['data_prevista']: f"zip/{r['data_prevista']}_{r['marca']}.zip" for r in rows}
    s = re.sub(r'DAYZ=\{.*?\}', lambda m: 'DAYZ=' + json.dumps(dayz), s, count=1, flags=re.S)
    s = s.replace('${DATA.length} carrosséis da semana', '${DATA.length} carrosséis do piloto (Gate 1)')
    s = s.replace('<title>Banco Aristo + MedQ</title>', '<title>Piloto Aristo + MedQ</title>')
    s = s.replace('<h1>Banco Aristo + MedQ</h1>', '<h1>Piloto Aristo + MedQ · v1.1</h1>')
    (OUT / 'biblioteca.html').write_text(s, encoding='utf-8')
    shutil.copy(ROOT / 'PublicSans-VF.ttf', OUT / 'PublicSans-VF.ttf')
    z = OUT / 'zip'; z.mkdir(exist_ok=True)
    for r in rows:
        folder = OUT / r['marca'] / r['data_prevista'] / 'post-01'
        with zipfile.ZipFile(z / f"{r['data_prevista']}_{r['marca']}.zip", 'w', zipfile.ZIP_DEFLATED) as zf:
            for f in sorted(folder.iterdir()):
                zf.write(f, f.name)


def pacote():
    dst = P1 / 'Piloto_Aristo_MedQ_v1_1_entrega.zip'
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(OUT.rglob('*')):
            if f.is_file():
                zf.write(f, 'Piloto_v1_1/' + f.relative_to(OUT).as_posix())
        for extra in ['QA_PILOTO_V1_1.md']:
            if (P1 / extra).exists():
                zf.write(P1 / extra, 'Piloto_v1_1/' + extra)
        for f in sorted(G.glob('*.py')):
            zf.write(f, 'Piloto_v1_1/gerador/' + f.name)
    print(dst, dst.stat().st_size)


if __name__ == '__main__':
    rows = fichas()
    planilhas(rows)
    biblioteca(rows)
    pacote()
