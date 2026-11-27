"""Gera os carrosséis da semana em JPG 1080x1350, um ZIP por post e por dia, e atualiza o site.

Uso (a partir da raiz do repositório):
    python3 gerador/render.py

Lê gerador/conteudo.py. Os campos [[__]] saem marcados como dado pendente.
"""
import html, json, re, shutil, sys, zipfile, base64
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
GER = ROOT / 'gerador'
sys.path.insert(0, str(GER))
from conteudo import POSTS, PROVAS  # noqa: E402

W, H = 1080, 1350

TEMAS = {
    'Aristo': dict(dark='#040A1C', dark2='#0B1E4A', brand='#1677FF', brand2='#4C9BFF', light='#EEF4FC',
                   ink='#0A1022', soft='#DCE8FA', hi='#1677FF', acc='#1677FF', acc_ink='#FFFFFF', logo='logo-aristo.png', plataforma='Aristo'),
    # paleta oficial MedQ (manual de marca): #00DFE3, #452B9A, #B07DF4, #414042
    'MedQ': dict(dark='#452B9A', dark2='#452B9A', brand='#452B9A', brand2='#00DFE3', light='#F3F0FC',
                 ink='#414042', soft='#E4DCFA', hi='#00DFE3', acc='#00DFE3', acc_ink='#452B9A', logo='logo-medq.png', plataforma='MedQ'),
}


def b64(p):
    return 'data:image/%s;base64,%s' % (p.suffix[1:].replace('jpg', 'jpeg'), base64.b64encode(p.read_bytes()).decode())


FONT = b64(ROOT / 'PublicSans-VF.ttf').replace('data:image/ttf', 'data:font/ttf')


def fmt(s):
    s = html.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<em>\1</em>', s)
    s = s.replace('[[__]]', '<span class="slot">__%</span>')
    return s


def css(t):
    return f"""
@font-face{{font-family:PS;src:url({FONT}) format('truetype');font-weight:100 900}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:PS,sans-serif;color:{t['ink']};background:{t['light']};position:relative;-webkit-font-smoothing:antialiased}}
.card{{position:absolute;inset:0;padding:110px 96px 96px;display:flex;flex-direction:column}}
.dark{{background:radial-gradient(120% 80% at 0% 0%,{t['dark2']} 0%,{t['dark']} 60%);color:#fff}}
.brandbg{{background:{t['brand']};color:#fff}}
.top{{display:flex;justify-content:space-between;align-items:baseline;font-weight:800;letter-spacing:.16em;font-size:27px;text-transform:uppercase;color:{t['brand']};margin-bottom:26px}}
.dark .top,.brandbg .top{{color:#fff}}
.top i{{font-style:italic;letter-spacing:0;font-weight:500;font-size:34px;color:{t['ink']}}}
.dark .top i,.brandbg .top i{{color:#fff}}
h1{{font-size:84px;line-height:1.04;font-weight:850;letter-spacing:-.025em}}
h1 em{{font-style:normal;color:{t['hi'] if t['hi']!=t['brand'] else t['brand2']}}}
h2{{font-size:56px;line-height:1.05;font-weight:850;letter-spacing:-.02em;text-transform:uppercase}}
h2 em{{font-style:normal;color:{t['brand']}}}
.sub{{font-size:34px;line-height:1.25;font-weight:600;margin-top:12px}}
.dado{{font-size:44px;line-height:1.22;font-weight:600;margin-top:40px}}
.fonte{{font-size:29px;font-style:italic;opacity:.85;margin-top:30px;line-height:1.3}}
.slot{{display:inline-block;border:3px dashed #FFB020;color:#FFB020;background:rgba(255,176,32,.12);border-radius:12px;padding:0 12px;font-style:normal;font-weight:800}}
.light .slot{{color:#8A5300;border-color:#E39A00;background:#FFF2DB}}
.bubble{{position:relative;display:inline-block;align-self:flex-start;background:{t['brand']};color:#fff;font-weight:800;font-size:44px;border-radius:18px;padding:22px 52px}}
.bubble:after{{content:'';position:absolute;left:96px;bottom:-24px;border:14px solid transparent;border-top:12px solid {t['brand']};border-left-width:18px;border-right-width:18px;border-top-width:26px}}
.dark .bubble{{background:{t['acc']};color:{t['acc_ink']}}}.dark .bubble:after{{border-top-color:{t['acc']}}}.dark .bubble.ghost{{background:transparent;color:#fff;border:3px solid {t['acc']}}}.brandbg .bubble{{background:#fff;color:{t['brand']}}}.brandbg .bubble:after{{border-top-color:#fff}}
.meta{{font-size:30px;font-weight:600;margin-top:46px}}
.logo{{height:64px;margin-top:auto;align-self:flex-start}}
.light .logo{{filter:brightness(0) saturate(100%)}}
.mtop{{margin-top:auto}}
.enun{{font-size:37px;line-height:1.36;font-weight:420}}
.enun em{{font-style:normal;font-weight:800}}
.cmd{{font-size:37px;line-height:1.3;font-weight:800;margin-top:22px}}
.cmd em{{font-style:normal}}
.lab{{font-size:27px;font-weight:800;letter-spacing:.16em;color:{t['brand']};margin:30px 0 16px}}
.alts{{display:flex;flex-direction:column;gap:16px}}
.alt{{display:flex;gap:26px;align-items:center;background:#fff;border:3px solid {t['brand']};border-radius:22px;padding:18px 26px;font-size:33px;line-height:1.28}}
.alt b{{flex:none;width:62px;height:62px;border-radius:50%;background:{t['brand']};color:#fff;display:grid;place-items:center;font-size:34px;font-weight:850}}
.small .vies p{{font-size:27px}}.small .vies h4{{font-size:30px}}.small .vies{{margin-top:34px;gap:20px}}.small .bars{{gap:12px}}.xs .alt{{font-size:26px;padding:10px 20px;gap:18px}}.xs .alts{{gap:12px}}.xs h2{{display:none}}.xs .bubble{{margin-top:22px!important;font-size:36px;padding:14px 38px}}.xs .enun{{font-size:31px;margin-top:14px!important}}.xs .cmd{{font-size:31px;margin-top:14px}}.xs .alt b{{width:48px;height:48px;font-size:27px}}.xs .lab{{margin:20px 0 12px}}.small .enun{{font-size:33px}}.small .alt{{font-size:29px;padding:14px 22px}}.small .alt b{{width:54px;height:54px;font-size:30px}}.small .cmd{{font-size:33px}}
.img{{flex:none;align-self:flex-start;width:600px;margin-top:26px;border-radius:22px;overflow:hidden;border:3px solid {t['soft']}}}.img img{{display:block;width:100%}}
.bars{{display:flex;flex-direction:column;gap:18px;margin-top:34px}}
.bar{{display:grid;grid-template-columns:62px 1fr 150px;gap:22px;align-items:center;font-size:30px}}
.bar b{{width:62px;height:62px;border-radius:50%;border:3px solid {t['brand']};color:{t['brand']};display:grid;place-items:center;font-size:32px;font-weight:850}}
.bar .tr{{height:40px;border-radius:10px;background:repeating-linear-gradient(-45deg,{t['soft']} 0 14px,#fff 14px 28px);border:2px dashed #E39A00}}
.bar .v{{text-align:right}}
.bar.ok b{{background:{t['brand']};color:#fff}}
.bar.ok .lbl{{color:{t['brand']};font-weight:800}}
.vies{{margin-top:44px;display:flex;flex-direction:column;gap:26px}}
.vies div{{border-left:8px solid {t['brand']};padding:4px 0 4px 26px}}
.vies h4{{font-size:33px;font-weight:850;margin-bottom:6px}}
.vies p{{font-size:30px;line-height:1.34}}
.blk{{margin-top:36px}}
.blk h4{{font-size:31px;font-weight:850;letter-spacing:.06em;text-transform:uppercase;margin-bottom:10px}}
.blk p{{font-size:33px;line-height:1.36}}
.gab{{margin-top:44px;background:#fff;color:{t['brand']};border-radius:24px;padding:30px 34px;font-size:33px;line-height:1.32;font-weight:800}}
.rule{{height:4px;background:#fff;margin:34px 0 0;opacity:.9}}
.prof{{display:flex;gap:34px;align-items:center;margin-top:20px}}
.foto{{flex:none;width:190px;height:190px;border-radius:50%;border:4px dashed #E39A00;background:#FFF2DB;color:#8A5300;display:grid;place-items:center;text-align:center;font-weight:800;font-size:24px;line-height:1.2}}
.prof .n{{font-size:42px;font-weight:850}}.prof .a{{font-size:31px;color:{t['brand']};font-weight:700;margin-top:6px}}
.pend{{display:inline-block;margin-top:10px;font-size:22px;font-weight:800;letter-spacing:.1em;color:#8A5300;background:#FFF2DB;border-radius:8px;padding:4px 12px}}
.quote{{margin-top:50px;font-size:44px;line-height:1.34;font-weight:550;position:relative;padding-left:40px;border-left:10px solid {t['brand']}}}
.fecho{{font-size:66px;line-height:1.12;font-weight:850;letter-spacing:-.02em;margin-top:30px}}
.fecho2{{font-size:36px;line-height:1.3;margin-top:36px;opacity:.9}}
.cta{{display:flex;flex-direction:column;gap:46px;margin-top:60px}}
.blob{{position:absolute;pointer-events:none;z-index:0}}.card>*:not(.blob){{position:relative;z-index:1}}.dark h1,.fecho{{max-width:800px}}.ghost:after{{display:none}}.bubble{{margin-bottom:34px}}.logo{{flex:none}}
"""


BLOB_TR = '<svg class="blob" style="right:-60px;top:-80px" width="330" height="490" viewBox="0 0 430 640"><path d="M430 0 L120 0 C150 60 200 70 160 150 C120 230 10 250 40 330 C70 400 230 420 300 520 C340 580 380 620 430 640 Z" fill="{c}"/></svg>'
BLOB_TL = '<svg class="blob" style="left:-10px;top:-10px" width="150" height="250" viewBox="0 0 150 250"><path d="M0 0 L150 0 C110 30 120 70 70 110 C30 140 30 200 0 250 Z" fill="{c}"/></svg>'
BLOB_BR = '<svg class="blob" style="right:-10px;bottom:-10px" width="120" height="140" viewBox="0 0 120 140"><path d="M120 0 L120 140 L0 140 C40 120 60 60 120 0 Z" fill="{c}"/></svg>'
BLOB_R = '<svg class="blob" style="right:-10px;top:520px" width="70" height="330" viewBox="0 0 70 330"><path d="M70 0 C40 80 0 110 20 170 C40 230 70 260 70 330 Z" fill="{c}"/></svg>'


def page(t, cls, body, deco=''):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css(t)}</style></head><body><div class='card {cls}'>{deco}{body}</div></body></html>"


def logo(t):
    return f"<img class='logo' src='{b64(GER / 'assets' / t['logo'])}'>"


def cards(p, split=False):
    t = TEMAS[p['marca']]
    prova = f"{p['banca']} {p['ano']}"
    data_prova = PROVAS.get(p['banca'])
    out = []

    # 1 capa
    c = p['capa']
    out.append(('dark', f"""
<div class='top' style='margin-top:120px'><span>Prova real • {prova}</span></div>
<h1 style='font-size:{84 if len(c["headline"]) < 70 else 72 if len(c["headline"]) < 90 else 64}px'>{fmt(c['headline'])}</h1>
<div class='dado'>{fmt(c['dado'])}</div>
<div class='fonte'>Dados extraídos de {f"{p['n']:,}".replace(',', '.')} resoluções desta questão na plataforma {t['plataforma']}.</div>
<div class='bubble' style='margin-top:52px'>Veja a questão ›</div>
<div class='meta'>{html.escape(p['area'])} • {html.escape(p['tema'])}{f' • prova em {data_prova}' if data_prova else ''}</div>
{logo(t)}""", BLOB_TR.format(c=t['acc'])))

    alts = ''.join(f"<div class='alt'><b>{k}</b><span>{fmt(v)}</span></div>" for k, v in p['alternativas'].items())
    cmd = f"<div class='cmd'>{fmt(p['comando'])}</div>" if p['comando'] else ''
    head = lambda tit: f"<div class='top'><span>{prova} • {tit}</span><i>{{n}}</i></div>"
    if p.get('imagem') or split:
        img = f"<div class='img'><img src='{b64(GER / p['imagem'])}'></div>" if p.get('imagem') else ''
        out.append(('light', head('Questão oficial') + f"<h2 style='font-size:46px'>Enunciado oficial da prova</h2><div class='enun' style='margin-top:22px;{'font-size:31px' if img else ''}'>{fmt(p['enunciado'])}</div>{img}{'' if img else "<div class='bubble' style='margin-top:44px'>Veja as alternativas ›</div>"}{logo(t)}", BLOB_TL.format(c=t['brand'])))
        out.append(('light auto', head('Alternativas') + f"{cmd}<div class='lab'>ALTERNATIVAS</div><div class='alts'>{alts}</div><div class='bubble' style='margin-top:44px'>Qual você marcaria? ›</div>{logo(t)}", BLOB_TL.format(c=t['brand'])))
    else:
        out.append(('light auto', head('Questão oficial') + f"<h2 style='font-size:46px'>Enunciado oficial da prova</h2><div class='enun' style='margin-top:22px'>{fmt(p['enunciado'])}</div>{cmd}<div class='lab'>ALTERNATIVAS</div><div class='alts'>{alts}</div><div class='bubble' style='margin-top:40px'>Qual você marcaria? ›</div>{logo(t)}", BLOB_TL.format(c=t['brand'])))

    # 3 ponto cego
    bars = ''.join(
        f"<div class='bar{' ok' if k == p['gabarito'] else ''}'><b>{k}</b><div><div class='lbl' style='font-size:24px;margin-bottom:6px'>{'Gabarito' if k == p['gabarito'] else '&nbsp;'}</div>{f"<div class='tr' style='background:{t['brand'] if k == p['gabarito'] else '#9AA3B5'};border:0;width:{p['dist'][k]}%'></div>" if p.get('dist') else "<div class='tr'></div>"}</div><span class='v'>{f"<b style='border:0;width:auto;height:auto;font-size:34px'>{p['dist'][k]}%</b>" if p.get('dist') else "<span class='slot'>__%</span>"}</span></div>"
        for k in p['alternativas'])
    vies = ''.join(f"<div><h4>{fmt(a)}</h4><p>{fmt(b)}</p></div>" for a, b in p['vies'])
    out.append(('light auto', head('O ponto cego') + f"<h2>Onde a <em>maioria</em> errou</h2><div class='sub'>Distribuição real das respostas:</div><div class='bars'>{bars}</div><div class='vies'>{vies}</div>{logo(t)}", BLOB_R.format(c=t['brand'])))

    # 4 pulo do gato
    pu = p['pulo']
    blks = ''.join(f"<div class='blk'><h4>{fmt(a)}:</h4><p>{fmt(b)}</p></div>" for a, b in pu['blocos'])
    out.append(('brandbg', head('O que a banca cobrou') + f"<h2 style='color:#fff'>O que a banca cobrou</h2><div class='sub'>{fmt(pu['pergunta'])}</div><div class='rule'></div>{blks}<div class='gab'>{fmt(pu['gabarito'])}</div>{logo(t)}", ''))

    # 5 professor (opcional)
    pr = p.get('professor')
    if pr:
        out.append(('light', head('Comentário do professor') + f"""
<h2>O professor <em>comenta</em></h2>
<div class='prof' style='margin-top:50px'><div class='foto'>FOTO DO<br>PROFESSOR</div><div><div class='n'>Prof. [nome]</div><div class='a'>{html.escape(pr['area'])}</div><div class='pend'>FALA EM VALIDAÇÃO</div></div></div>
<div class='quote'>“{fmt(pr['fala'])}”</div>{logo(t)}""", BLOB_BR.format(c=t['brand'])))

    # 6 fechamento
    out.append(('dark', head('Antes da prova') + f"""
<div class='fecho' style='margin-top:120px'>{fmt(p['fecho'])}</div>
<div class='fecho2'>Qual seria a sua conduta? Discuta nos comentários.</div>
<div class='cta'><div class='bubble'>Salve para revisar ›</div><div class='bubble' style='background:transparent;border:3px solid {t['brand2']};color:#fff'>Envie para quem vai fazer a {p['banca']} ›</div></div>
{logo(t)}""".replace("<div class='bubble' style='background:transparent", "<div class='bubble ghost' style='background:transparent"), BLOB_BR.format(c=t['acc'])))

    N = len(out)
    return [(cls, body.replace('{n}', f'{i + 1}/{N}'), deco) for i, (cls, body, deco) in enumerate(out)], t


def main():
    pdir, zdir = ROOT / 'p', ROOT / 'z'
    for d in (pdir, zdir):
        shutil.rmtree(d, ignore_errors=True)
        d.mkdir()
    data, by_day = [], {}
    with sync_playwright() as pw:
        br = pw.chromium.launch(executable_path=__import__('os').environ.get('CHROME', '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'))
        pg = br.new_page(viewport={'width': W, 'height': H})
        for p in POSTS:
          for split in (False, True):
            cs, t = cards(p, split)
            folder = pdir / p['marca'] / p['data'] / 'post-01'
            shutil.rmtree(folder, ignore_errors=True)
            folder.mkdir(parents=True)
            imgs, refaz = [], False
            for i, (cls, body, deco) in enumerate(cs, 1):
                pg.set_content(page(t, cls.replace(' auto', ''), body, deco))
                pg.evaluate('document.fonts.ready')
                if 'auto' in cls and pg.evaluate("document.querySelector('.logo').getBoundingClientRect().bottom") > H - 70:
                    pg.set_content(page(t, cls.replace(' auto', '') + ' small', body, deco))
                    pg.evaluate('document.fonts.ready')
                    if pg.evaluate("document.querySelector('.logo').getBoundingClientRect().bottom") > H - 70:
                        pg.set_content(page(t, cls.replace(' auto', '') + ' small xs', body, deco))
                        pg.evaluate('document.fonts.ready')
                over = pg.evaluate("document.querySelector('.logo').getBoundingClientRect().bottom")
                if over > H - 60:
                    if not split and 'Questão oficial' in body:
                        refaz = True
                        break
                    print(f"ATENÇÃO: {p['id']} card {i} transborda ({over:.0f}px)")
                f = folder / f'{i:02d}.jpg'
                pg.screenshot(path=str(f), type='jpeg', quality=92)
                imgs.append(f.relative_to(ROOT).as_posix())
            if not refaz:
                break
          if True:
            (folder / 'legenda.txt').write_text(p['legenda'] + '\n', encoding='utf-8')
            z = zdir / f"{p['data']}_{p['marca']}.zip"
            with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
                for f in sorted(folder.iterdir()):
                    zf.write(f, f.name)
            by_day.setdefault(p['data'], []).append(folder)
            pend = ['% de erro da capa', 'distribuição das respostas por alternativa (card 3)']
            if p.get('professor'):
                pend.append('nome, foto e validação da fala do professor')
            data.append(dict(
                id=p['id'], marca=p['marca'], data_prevista=p['data'], titulo=p['titulo'], tema=p['tema'],
                dificuldade='Não classificada', grande_area=p['area'], instituicao=p['banca'], ano=p['ano'],
                tipo='Questão original', formato='Prova real · dado + professor' if p.get('professor') else 'Prova real · dado',
                familia_gancho='dado de erro + provocação', gabarito=p['gabarito'],
                conceito_decisivo=re.sub(r'\*\*', '', p['pulo']['gabarito']),
                erro_principal=' '.join(re.sub(r'\*\*', '', a) + ': ' + b for a, b in p['vies']),
                discriminacao='', fonte_questao=f"{p['banca']} {p['ano']}", referencias=[],
                justificativa_selecao=f"Prova {p['banca']} em {PROVAS.get(p['banca'], '?')}/2026.",
                texto_opcional_carrossel='', notas_auditoria='PENDENTE: ' + '; '.join(pend) + '.',
                candidato_reel='não por ora', legenda=p['legenda'], imagens_pendentes=[],
                status_cientifico='PENDENTE: revisão docente', status_visual='PENDENTE: dados do relatório',
                status_geral='PENDENTE', versao='v2 · formato prova real', autorizacao='', n_cards=len(imgs),
                imagens=[], pasta=f"{p['marca']}/{p['data']}/post-01", status_derivado='PENDENTE',
                banca=f"{p['banca']} {p['ano']}", imgs=imgs, zip=z.relative_to(ROOT).as_posix()))
        br.close()
    dayz = {}
    for d, folders in by_day.items():
        z = zdir / f'{d}.zip'
        with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
            for fo in folders:
                for f in sorted(fo.iterdir()):
                    zf.write(f, f"{fo.parent.parent.name}/{f.name}")
        dayz[d] = z.relative_to(ROOT).as_posix()

    idx = ROOT / 'index.html'
    s = idx.read_text(encoding='utf-8')
    i = s.index('const DATA=') + len('const DATA=')
    _, end = json.JSONDecoder().raw_decode(s[i:])
    s = s[:i] + json.dumps(data, ensure_ascii=False) + s[i + end:]
    s = re.sub(r'DAYZ=\{.*?\}', lambda m: 'DAYZ=' + json.dumps(dayz), s, count=1, flags=re.S)
    s = s.replace('${DATA.length} de 154 produzidos', '${DATA.length} carrosséis da semana')
    idx.write_text(s, encoding='utf-8')
    print(len(data), 'posts;', sum(len(d['imgs']) for d in data), 'cards')


if __name__ == '__main__':
    main()
