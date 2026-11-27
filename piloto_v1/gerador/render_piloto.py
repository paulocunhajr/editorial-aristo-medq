"""Piloto v1.1: gera PNG 1080x1350 e PPTX editável (texto e formas nativos) da mesma fonte HTML.

Uso:  python3 piloto_v1/gerador/render_piloto.py
Saída: piloto_v1/entrega/{Aristo,MedQ}/AAAA-MM-DD/post-01/NN.png
       piloto_v1/entrega/editaveis/{Aristo,MedQ}_Piloto_v1_1.pptx
"""
import base64, html, json, os, re, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

G = Path(__file__).resolve().parent
P1 = G.parent
ROOT = P1.parent
OUT = P1 / 'entrega'
sys.path.insert(0, str(G))
from conteudo_piloto import POSTS  # noqa: E402

W, H = 1080, 1350
CHROME = os.environ.get('CHROME', '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome')

# Cores. MedQ: paleta oficial citada na auditoria v0 (#452B9A, #00DFE3, #B07DF4, #414042; secundárias #F51068, #FF5607).
# Aristo: azul #006BFD e marinho dos renders v1. Conferir ambas no manual (PDF não recebido nesta sessão).
C = {
    'MedQ': dict(dark='#452B9A', brand='#452B9A', acc='#00DFE3', lil='#B07DF4', ink='#414042', pink='#F51068',
                 orange='#FF5607', light='#F4F1FB', card='#FFFFFF', soft='#ECE6FA'),
    'Aristo': dict(dark='#021024', brand='#006BFD', acc='#006BFD', ink='#0B1324', light='#F2F5FA', card='#FFFFFF',
                   soft='#E3ECFB', mute='#5A6478'),
}


def b64(p):
    return 'data:image/png;base64,' + base64.b64encode(Path(p).read_bytes()).decode()


FONT = 'data:font/ttf;base64,' + base64.b64encode((ROOT / 'PublicSans-VF.ttf').read_bytes()).decode()
LOGO = {k: b64(G / f'logo-{k}.png') for k in ['aristo-cor', 'aristo-branco', 'medq-cor', 'medq-branco']}


def f(s):
    s = html.escape(s)
    return re.sub(r'\*\*(.+?)\*\*', r'<em>\1</em>', s)


def css(m):
    c = C[m]
    return f"""
@font-face{{font-family:'Public Sans';src:url({FONT}) format('truetype');font-weight:100 900}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:'Public Sans';color:{c['ink']};-webkit-font-smoothing:antialiased}}
#card{{position:absolute;inset:0;background:{c['light']};overflow:hidden}}
#card.dk{{background:{c['dark']};color:#fff}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:90px;position:relative}}
.pad{{position:absolute;left:88px;right:88px;top:84px;bottom:84px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:34px}}
.k{{font-size:25px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:{c['brand']};display:flex;align-items:center;gap:14px}}
.dk .k{{color:{c['acc'] if m == 'MedQ' else '#9DB8E6'}}}
.dot{{width:16px;height:16px;border-radius:4px;background:{c.get('acc')}}}
.n{{font-size:25px;font-weight:600;color:{c['ink']};opacity:.7}}
.dk .n{{color:#fff}}
.h1{{font-size:88px;line-height:1.06;font-weight:800;letter-spacing:-.02em}}
.h1 em{{font-style:normal;color:{c['acc'] if m == 'MedQ' else '#4D94FF'}}}
.h2{{font-size:56px;line-height:1.1;font-weight:800;letter-spacing:-.015em;color:{c['brand'] if m == 'MedQ' else c['ink']}}}
.dk .h2{{color:#fff}}
.sub{{font-size:36px;line-height:1.38;margin-top:30px;opacity:.88}}
.p{{font-size:38px;line-height:1.42}}
.p em{{font-style:normal;font-weight:800;color:{c['brand']}}}
.logo{{position:absolute;left:88px;bottom:84px;height:62px}}
.alts{{display:flex;flex-direction:column;gap:20px}}
.alt{{display:flex;align-items:center;gap:28px;background:{c['card']};border-radius:{'26px' if m == 'MedQ' else '18px'};padding:26px 30px;{'' if m == 'MedQ' else 'border:2px solid #D5DEEC;'}}}
.alt .l{{flex:none;width:58px;height:58px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800;{'background:' + c['brand'] + ';color:#fff' if m == 'MedQ' else 'border:3px solid ' + c['brand'] + ';color:' + c['brand']}}}
.alt .tx{{font-size:35px;line-height:1.32}}
.badge{{align-self:flex-start;font-size:29px;font-weight:800;color:#fff;background:{c['brand'] if m == 'MedQ' else c['dark']};border-radius:{'40px' if m == 'MedQ' else '10px'};padding:12px 30px;margin-bottom:30px}}
.stem{{font-size:42px;line-height:1.3;font-weight:700;margin-bottom:34px}}
.foot{{align-self:flex-end;margin-top:30px;font-size:29px;font-weight:600;color:{c['brand']}}}
.gab{{background:{c.get('acc')};border-radius:26px;padding:30px 34px;margin-bottom:40px}}
.gab .g{{font-size:26px;font-weight:800;letter-spacing:.06em;color:{c['brand']}}}
.gab .gt{{font-size:42px;line-height:1.22;font-weight:800;color:{c['brand']};margin-top:8px}}
.its{{display:flex;flex-direction:column;gap:32px}}
.it{{display:flex;gap:26px}}
.ic{{flex:none;width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:800}}
.ic.x{{border:4px solid {c.get('pink', '#D33')};color:{c.get('pink', '#D33')}}}
.ic.ok{{border:4px solid {c.get('acc')};color:{c['brand']}}}
.it .il{{font-size:31px;font-weight:800;color:{c['brand']}}}
.it .ix{{font-size:33px;line-height:1.36;margin-top:4px}}
.pal{{display:flex;flex-direction:column;gap:24px}}
.pw{{background:{c.get('soft')};border-radius:20px;padding:28px 32px;display:flex;gap:26px}}
.pw .bar{{flex:none;width:12px;border-radius:6px}}
.pw .pt{{font-size:40px;font-weight:800;color:{c['brand']}}}
.pw .px{{font-size:33px;line-height:1.36;margin-top:6px}}
.lbl{{display:flex;align-items:center;gap:22px;font-size:29px;font-weight:800;letter-spacing:.05em;text-transform:uppercase}}
.big{{font-size:50px;line-height:1.2;font-weight:800;margin:24px 0 56px}}
.rule{{height:3px;background:{c.get('soft')};margin:40px 0}}
.cta{{font-size:33px;line-height:1.36;font-weight:700;color:{c['brand']}}}
.pill{{align-self:flex-start;border-radius:40px;padding:18px 34px;font-size:30px;font-weight:800}}
.box{{background:{c['card']};border-radius:22px;padding:30px 34px}}
.box .bt{{font-size:26px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:{c['brand']};margin-bottom:10px}}
.num{{display:flex;flex-direction:column;gap:22px}}
.nc{{background:{c['card']};border:2px solid #D5DEEC;border-radius:18px;padding:26px 30px;display:flex;gap:24px}}
.nb{{flex:none;width:52px;height:52px;border-radius:50%;background:{c['brand']};color:#fff;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800}}
.nc .nt{{font-size:36px;font-weight:800}}
.nc .nx{{font-size:31px;line-height:1.36;margin-top:6px;color:{c['ink']}}}
.tbl{{border-radius:16px;overflow:hidden;background:{c['card']}}}
.tr{{display:grid;grid-template-columns:190px repeat(3,minmax(0,1fr))}}
.tr>div{{padding:20px 12px;font-size:26px;line-height:1.3;border-bottom:2px solid #E3E9F3}}
.th>div{{background:{c['dark']};color:#fff;font-weight:800;border-bottom:none}}
.tr>div:first-child{{font-weight:800}}
.tag{{flex:none;min-width:78px;height:50px;padding:0 14px;border-radius:10px;background:{c['dark']};color:#fff;display:flex;align-items:center;justify-content:center;font-size:27px;font-weight:800}}
.tag.hl{{background:{c['brand']}}}
.cal{{display:grid;grid-template-columns:repeat(7,1fr);gap:14px}}
.cd{{aspect-ratio:1;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:700;background:#fff;border:2px solid #D5DEEC}}
.cd.lu{{background:{c['dark']};color:#fff;border-color:{c['dark']}}}
.cd.ov{{background:{c['brand']};color:#fff;border-color:{c['brand']}}}
.leg{{display:flex;gap:40px;margin-top:28px;font-size:28px}}
.leg span{{display:flex;align-items:center;gap:12px}}
.sw{{width:26px;height:26px;border-radius:6px}}
.balao{{position:relative;align-self:flex-start;background:{c['brand']};color:#fff;font-size:38px;font-weight:800;border-radius:16px;padding:28px 44px;margin-top:56px}}
.tail{{position:absolute;left:46px;bottom:-26px;width:0;height:0;border-left:16px solid transparent;border-right:16px solid transparent;border-top:28px solid {c['brand']}}}
.ln{{display:flex;flex-direction:column;gap:26px;margin-top:40px}}
.ln>div{{display:flex;gap:26px;align-items:center;font-size:38px}}
.ln .nb{{background:{c['brand']}}}
"""


def head(c, k, dark=False):
    dot = "<div class='dot'></div>" if c['marca'] == 'MedQ' and not dark else ''
    return f"<div class='top'><div class='k'>{dot}<span class='t'>{html.escape(k)}</span></div><div class='n t'>{{N}}</div></div><!--/head-->"


def logo(m, dark):
    key = ('aristo' if m == 'Aristo' else 'medq') + ('-branco' if dark else '-cor')
    return f"<img class='logo' src='{LOGO[key]}'>"


def alts_html(alts):
    return "<div class='alts'>" + ''.join(f"<div class='alt'><div class='l t'>{k}</div><div class='tx t'>{f(v)}</div></div>" for k, v in alts.items()) + "</div>"


# Formas de apoio. Aristo: aba/encaixe (retângulo azul arredondado com recorte circular). MedQ: blocos geométricos.
def aristo_aba(pos):
    c = C['Aristo']
    if pos == 'tr':
        return (f"<div class='sh' style='position:absolute;right:-60px;top:-60px;width:330px;height:250px;border-radius:44px;background:{c['brand']}'></div>"
                f"<div class='sh' style='position:absolute;left:700px;top:-30px;width:190px;height:190px;border-radius:50%;background:{c['dark']}'></div>")
    return (f"<div class='sh' style='position:absolute;right:-60px;bottom:110px;width:220px;height:230px;border-radius:40px;background:{c['brand']}'></div>"
            f"<div class='sh' style='position:absolute;right:80px;bottom:140px;width:170px;height:170px;border-radius:50%;background:{c['dark']}'></div>")


def medq_blocos(pos):
    c = C['MedQ']
    if pos == 'tr':
        return (f"<div class='sh' style='position:absolute;left:740px;top:120px;width:220px;height:220px;border-radius:40px;background:{c['acc']}'></div>"
                f"<div class='sh' style='position:absolute;left:880px;top:250px;width:120px;height:120px;border-radius:50%;background:{c['pink']}'></div>"
                f"<div class='sh' style='position:absolute;left:880px;top:250px;width:80px;height:80px;border-radius:16px;background:{c['orange']}'></div>"
                f"<div class='sh' style='position:absolute;left:640px;top:300px;width:110px;height:110px;border-radius:50%;background:{c['lil']}'></div>")
    return (f"<div class='sh' style='position:absolute;left:810px;top:1010px;width:150px;height:150px;border-radius:30px;background:{c['acc']}'></div>"
            f"<div class='sh' style='position:absolute;left:910px;top:1100px;width:90px;height:90px;border-radius:50%;background:{c['pink']}'></div>"
            f"<div class='sh' style='position:absolute;left:910px;top:1100px;width:60px;height:60px;border-radius:12px;background:{c['orange']}'></div>")


def build(post, c, i):
    m = post['marca']
    c['marca'] = m
    t = c['t']
    dark = t in ('m_capa', 'm_final', 'a_capa', 'a_final')
    body, deco = '', ''
    if t == 'm_capa':
        deco = medq_blocos('tr')
        body = (head(c, c['kicker'], True) + f"<div style='margin-top:330px' class='h1 t'>{f(c['titulo'])}</div>"
                f"<div class='sub t'>{f(c['sub'])}</div><div class='pill t' style='margin-top:46px;background:{C[m]['acc']};color:{C[m]['brand']}'>{html.escape(c['botao'])}</div>")
    elif t == 'm_questao':
        body = (head(c, c['kicker']) + f"<div class='badge t'>{html.escape(c['badge'])}</div><div class='stem t'>{f(c['enunciado'])}</div>"
                + alts_html(c['alts']) + f"<div class='foot t'>{html.escape(c['rodape'])}</div>")
    elif t == 'm_caso':
        body = (head(c, c['kicker']) + f"<div class='p t'>{f(c['texto'])}</div>"
                f"<div class='box' style='margin-top:40px'><div class='bt t'>{html.escape(c['exame_titulo'])}</div><div class='p t' style='font-size:35px'>{f(c['exame'])}</div></div>"
                f"<div class='h2 t' style='margin-top:56px;font-size:48px'>{f(c['pergunta'])}</div>")
    elif t == 'm_alts':
        body = head(c, c['kicker']) + alts_html(c['alts'])
    elif t == 'm_resolucao':
        its = ''.join(f"<div class='it'><div class='ic {k} t'>{'✕' if k == 'x' else '✓'}</div><div><div class='il t'>{html.escape(l)}</div><div class='ix t'>{f(x)}</div></div></div>" for k, l, x in c['itens'])
        body = head(c, c['kicker']) + f"<div class='gab'><div class='g t'>GABARITO {c['gab']}</div><div class='gt t'>{f(c['gab_txt'])}</div></div><div class='its'>{its}</div>"
    elif t == 'm_palavras':
        cor = {'cyan': C[m]['acc'], 'lilas': C[m]['lil'], 'roxo': C[m]['brand']}
        its = ''.join(f"<div class='pw'><div class='bar sh' style='background:{cor[k]}'></div><div><div class='pt t'>{html.escape(a)}</div><div class='px t'>{f(b)}</div></div></div>" for k, a, b in c['itens'])
        body = head(c, c['kicker']) + f"<div class='h2 t' style='margin-bottom:40px'>{f(c['titulo'])}</div><div class='pal'>{its}</div>"
    elif t == 'm_erro':
        cta = f"<div class='rule'></div><div class='cta t'>{f(c['cta'])}</div>" if c.get('cta') else ''
        body = (head(c, c['kicker']) +
                f"<div class='lbl'><div class='ic x t' style='background:{C[m]['pink']};color:#fff;border-color:{C[m]['pink']}'>✕</div><span class='t' style='color:{C[m]['pink']}'>Erro mais comum</span></div>"
                f"<div class='big t'>{f(c['erro'])}</div>"
                f"<div class='lbl'><div class='ic ok t' style='background:{C[m]['acc']};border-color:{C[m]['acc']}'>✓</div><span class='t' style='color:{C[m]['brand']}'>Raciocínio certo</span></div>"
                f"<div class='p t' style='margin-top:24px'>{f(c['certo'])}</div>{cta}")
    elif t == 'm_final':
        deco = medq_blocos('br')
        bts = ''.join(f"<div class='pill t' style='border:3px solid {C[m]['acc']};color:#fff;margin-top:24px'>{html.escape(b)}</div>" for b in c['botoes'])
        body = head(c, c['kicker'], True) + f"<div style='margin-top:120px' class='h1 t'>{f(c['titulo'])}</div><div class='sub t'>{f(c['sub'])}</div><div style='margin-top:30px;display:flex;flex-direction:column'>{bts}</div>"
    elif t == 'm_fases':
        fases = [('Febril', C[m]['lil'], 300), ('Crítica', C[m]['pink'], 290), ('Recuperação', C[m]['acc'], 314)]
        bars = ''.join(f"<div style='width:{w}px'><div class='t' style='font-size:29px;font-weight:800;text-align:center;margin-bottom:12px;color:{C[m]['brand']}'>{n}</div><div class='sh' style='height:34px;border-radius:17px;background:{col}'></div></div>" for n, col, w in fases)
        sin = ''.join(f"<div style='display:flex;gap:18px;align-items:center'><div class='sh' style='flex:none;width:16px;height:16px;border-radius:50%;background:{C[m]['pink']}'></div><span class='t' style='font-size:31px'>{html.escape(s)}</span></div>" for s in c['sinais'])
        body = (head(c, c['kicker']) + f"<div class='h2 t' style='margin-bottom:40px'>{f(c['titulo'])}</div>"
                f"<div style='display:flex;gap:8px'>{bars}</div>"
                f"<div class='sh' style='margin:14px 0 0 282px;width:0;height:0;border-left:16px solid transparent;border-right:16px solid transparent;border-bottom:26px solid {C[m]['brand']}'></div>"
                f"<div class='t' style='font-size:31px;line-height:1.35;color:{C[m]['brand']};margin-top:10px'>{f(c['nota'])}</div>"
                f"<div class='t' style='font-size:27px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:{C[m]['pink']};margin:40px 0 20px'>{html.escape(c['sinais_titulo'])}</div>"
                f"<div style='display:flex;flex-direction:column;gap:14px'>{sin}</div>")
    elif t == 'm_ciclos':
        mx = max(d for d, _ in c['ciclos'])
        rows = ''
        for d, ov in c['ciclos']:
            wt = 700 * d / mx
            wf = wt * ov / d
            rows += (f"<div style='display:flex;align-items:center;gap:26px;margin-bottom:60px'><div class='t' style='width:150px;font-size:34px;font-weight:800;color:{C[m]['brand']}'>{d} dias</div>"
                     f"<div style='position:relative;width:{wt:.0f}px;height:64px'>"
                     f"<div class='sh' style='position:absolute;left:0;top:0;width:{wf:.0f}px;height:64px;border-radius:16px 0 0 16px;background:{C[m]['lil']}'></div>"
                     f"<div class='sh' style='position:absolute;left:{wf:.0f}px;top:0;right:0;height:64px;border-radius:0 16px 16px 0;background:{C[m]['brand']}'></div>"
                     f"<div class='sh' style='position:absolute;left:{wf - 20:.0f}px;top:12px;width:40px;height:40px;border-radius:50%;background:{C[m]['acc']};border:5px solid #fff'></div>"
                     f"<div class='t' style='position:absolute;left:{wf - 60:.0f}px;top:76px;width:120px;text-align:center;font-size:27px;font-weight:800;color:{C[m]['brand']}'>dia {ov}</div></div></div>")
        leg = (f"<div class='leg' style='margin-top:10px'><span><i class='sw sh' style='background:{C[m]['lil']}'></i><b class='t' style='font-weight:500'>Fase folicular: varia</b></span>"
               f"<span><i class='sw sh' style='background:{C[m]['brand']}'></i><b class='t' style='font-weight:500'>Fase lútea: cerca de 14 dias</b></span></div>")
        body = (head(c, c['kicker']) + f"<div class='h2 t' style='margin-bottom:64px'>{f(c['titulo'])}</div>{rows}{leg}"
                f"<div class='t' style='font-size:36px;line-height:1.36;font-weight:800;color:{C[m]['brand']};margin-top:50px'>{f(c['nota'])}</div>")
    elif t == 'a_capa':
        deco = aristo_aba('tr')
        body = (head(c, c['kicker'], True) + f"<div style='margin-top:300px' class='h1 t'>{f(c['titulo'])}</div>"
                f"<div class='sh' style='width:96px;height:8px;border-radius:4px;background:{C[m]['brand']};margin-top:40px'></div>"
                f"<div class='sub t' style='color:#C9D3E6;opacity:1'>{f(c['sub'])}</div>")
    elif t == 'a_roteiro':
        its = ''
        for n, (q, rs) in enumerate(c['itens'], 1):
            sub = ''.join(f"<div class='t' style='font-size:30px;margin-top:8px;color:{C[m]['mute']}'>{html.escape(r)}</div>" for r in rs)
            its += f"<div class='nc' style='padding:22px 28px'><div class='nb t'>{n}</div><div><div class='nt t' style='font-size:34px'>{html.escape(q)}</div>{sub}</div></div>"
        body = head(c, c['kicker']) + f"<div class='h2 t' style='margin-bottom:34px'>{f(c['titulo'])}</div><div class='num' style='gap:18px'>{its}</div>"
    elif t in ('a_questao', 'a_alts'):
        top = (f"<div class='badge t'>{html.escape(c['badge'])}</div><div class='stem t'>{f(c['enunciado'])}</div>" if t == 'a_questao'
               else f"<div class='h2 t' style='margin-bottom:40px;font-size:50px'>{f(c['titulo'])}</div>")
        body = head(c, c['kicker']) + top + alts_html(c['alts'])
    elif t == 'a_aplicando':
        rows = ''.join(f"<div style='display:grid;grid-template-columns:max-content 1fr;gap:16px 26px;font-size:33px;line-height:1.3'><b class='t'>{html.escape(a)}</b><span class='t' style='color:{C[m]['brand']};white-space:nowrap'>{html.escape(b)}</span></div>" for a, b in c['linhas'])
        des = ''.join(f"<div style='display:flex;gap:24px;align-items:flex-start'><div class='tag t'>{html.escape(a)}</div><div class='t' style='font-size:32px;line-height:1.36'>{html.escape(b)}</div></div>" for a, b in c['descarte'])
        body = (head(c, c['kicker']) + f"<div class='h2 t' style='margin-bottom:36px'>{f(c['titulo'])}</div><div style='display:flex;flex-direction:column;gap:20px'>{rows}</div>"
                f"<div class='sh' style='height:3px;background:#D5DEEC;margin:44px 0'></div><div class='t' style='font-size:38px;font-weight:800;margin-bottom:28px'>Descarte rápido</div>"
                f"<div style='display:flex;flex-direction:column;gap:26px'>{des}</div>")
    elif t == 'a_tabela':
        rows = "<div class='tr th'><div class='t'></div>" + ''.join(f"<div class='t'>{html.escape(x)}</div>" for x in c['colunas']) + "</div>"
        for a, vs in c['linhas']:
            rows += f"<div class='tr'><div class='t'>{html.escape(a)}</div>" + ''.join(f"<div class='t'>{html.escape(v)}</div>" for v in vs) + "</div>"
        nota = f"<div class='t' style='font-size:28px;line-height:1.35;margin-top:22px;color:{C[m]['mute']}'>{f(c['nota'])}</div>" if c.get('nota') else ''
        body = head(c, c['kicker']) + f"<div class='h2 t' style='margin-bottom:44px'>{f(c['titulo'])}</div><div class='tbl'>{rows}</div>{nota}"
    elif t == 'a_final':
        deco = aristo_aba('br')
        its = ''.join(f"<div><div class='nb t'>{n}</div><span class='t'>{html.escape(x)}</span></div>" for n, x in enumerate(c['itens'], 1))
        body = (head(c, c['kicker'], True) + f"<div style='margin-top:110px' class='h1 t' >{f(c['titulo'])}</div><div class='ln'>{its}</div>"
                f"<div class='balao'><span class='t'>{html.escape(c['balao'])}</span><div class='tail sh'></div></div>")
    elif t == 'a_caso':
        ex = ''.join(f"<div style='display:flex;justify-content:space-between;padding:16px 0;border-top:2px solid #E3E9F3;font-size:34px'><span class='t'>{html.escape(a)}</span><b class='t'>{html.escape(b)}</b></div>" for a, b in c['exames'])
        body = head(c, c['kicker']) + f"<div class='p t'>{f(c['texto'])}</div><div class='box' style='margin-top:44px;border:2px solid #D5DEEC'><div class='bt t'>Exames</div>{ex}</div>"
    elif t == 'a_numerado':
        its = ''.join(f"<div class='nc'><div class='nb t'>{n}</div><div><div class='nt t'>{html.escape(a)}</div><div class='nx t'>{f(b)}</div></div></div>" for n, (a, b) in enumerate(c['itens'], 1))
        body = head(c, c['kicker']) + f"<div class='h2 t' style='margin-bottom:40px'>{f(c['titulo'])}</div><div class='num'>{its}</div>"
    elif t == 'a_resolucao':
        its = ''.join(f"<div style='display:flex;gap:24px;align-items:flex-start'><div class='tag t{' hl' if c.get('destaque') == a else ''}'>{a}</div><div class='t' style='font-size:33px;line-height:1.36'>{f(b)}</div></div>" for a, b in c['itens'])
        cond = f"<div class='sh' style='height:3px;background:#D5DEEC;margin:44px 0 30px'></div><div class='t' style='font-size:34px;line-height:1.36;font-weight:800'>{f(c['conduta'])}</div>" if c.get('conduta') else ''
        body = head(c, c['kicker']) + f"<div class='h2 t' style='margin-bottom:30px'>{f(c['titulo'])}</div><div class='p t' style='font-size:36px;margin-bottom:44px'>{f(c['lead'])}</div><div style='display:flex;flex-direction:column;gap:30px'>{its}</div>{cond}"
    elif t == 'a_calendario':
        cells = ''.join(f"<div class='cd t{' ov' if d == c['ovulacao'] else ' lu' if d > c['ovulacao'] else ''}'>{d}</div>" for d in range(1, c['dias'] + 1))
        body = (head(c, c['kicker']) + f"<div class='h2 t' style='margin-bottom:40px'>{f(c['titulo'])}</div><div class='cal'>{cells}</div>"
                f"<div class='leg'><span><i class='sw sh' style='background:{C[m]['dark']}'></i><b class='t' style='font-weight:500'>14 dias de fase lútea</b></span><span><i class='sw sh' style='background:{C[m]['brand']}'></i><b class='t' style='font-weight:500'>ovulação estimada, dia {c['ovulacao']}</b></span></div>"
                f"<div class='t' style='font-size:40px;font-weight:800;margin-top:40px'>{f(c['nota'])}</div>")
    else:
        raise ValueError(t)
    return dark, deco, body


def page(m, dark, deco, body, z=1.0):
    if not dark and '<!--/head-->' in body:
        h, rest = body.split('<!--/head-->', 1)
        body = h + f"<div class='main' style='zoom:{z}'>" + rest + "</div>"
    return f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{css(m)}</style></head><body><div id='card' class='{'dk' if dark else ''}'>{deco}<div class='pad'>{body}</div>{logo(m, dark)}</div></body></html>"


# Coleta a geometria final do DOM para exportar ao PPTX.
JS = r"""
() => {
  const out=[]; const px=v=>parseFloat(v)||0;
  const rgb=s=>{const m=s.match(/rgba?\(([^)]+)\)/); if(!m) return null; const p=m[1].split(',').map(x=>parseFloat(x)); if(p.length>3&&p[3]===0) return null; return p.slice(0,3)};
  const card=document.getElementById('card'); const mn=document.querySelector('.main'); const Z=mn?parseFloat(mn.style.zoom||1):1; const zf=el=>(mn&&mn.contains(el))?Z:1; out.push({k:'bg',fill:rgb(getComputedStyle(card).backgroundColor)});
  for(const el of card.querySelectorAll('*')){
    const cs=getComputedStyle(el), r=el.getBoundingClientRect();
    if(r.width<1&&!(px(cs.borderBottomWidth)>0)) continue;
    if(el.tagName==='IMG'){out.push({k:'img',src:el.getAttribute('src'),x:r.left,y:r.top,w:r.width,h:r.height});continue}
    const fill=rgb(cs.backgroundColor), bw=px(cs.borderTopWidth), bc=bw?rgb(cs.borderTopColor):null;
    const tri = px(cs.borderBottomWidth)>0 && r.height<2 && cs.borderLeftColor.includes('0, 0, 0, 0') ? 'up' : (px(cs.borderTopWidth)>0 && r.height<2 && cs.borderLeftColor.includes('0, 0, 0, 0') ? 'down':null);
    if(tri){const w=(px(cs.borderLeftWidth)+px(cs.borderRightWidth))*zf(el), h=(tri==='up'?px(cs.borderBottomWidth):px(cs.borderTopWidth))*zf(el); const col=rgb(tri==='up'?cs.borderBottomColor:cs.borderTopColor); out.push({k:'tri',dir:tri,x:r.left,y:r.top,w,h,fill:col}); continue}
    if(fill||bc){const rad=px(cs.borderTopLeftRadius); out.push({k:'rect',x:r.left,y:r.top,w:r.width,h:r.height,fill,stroke:bc,sw:bw*zf(el),rad:rad*zf(el),dash:cs.borderTopStyle==='dashed'})}
    if(el.classList.contains('t')){
      const runs=[]; const walk=(n,st)=>{for(const ch of n.childNodes){ if(ch.nodeType===3){ if(ch.textContent) runs.push({t:ch.textContent,sz:px(st.fontSize)*zf(n),b:parseInt(st.fontWeight),c:rgb(st.color)})} else if(ch.nodeType===1 && !ch.classList.contains('sh')){ walk(ch,getComputedStyle(ch)) } } };
      walk(el,cs);
      if(runs.length){const ta=cs.textAlign; const disp=cs.display; const center=(cs.justifyContent==='center'&&disp.includes('flex'))||ta==='center';
        out.push({k:'text',x:r.left+px(cs.paddingLeft)*zf(el),y:r.top+px(cs.paddingTop)*zf(el),w:r.width-(px(cs.paddingLeft)+px(cs.paddingRight))*zf(el),h:r.height-(px(cs.paddingTop)+px(cs.paddingBottom))*zf(el),runs,lh:(px(cs.lineHeight)||px(cs.fontSize)*1.2)*zf(el),ls:cs.letterSpacing,center,upper:cs.textTransform==='uppercase',vcenter:disp.includes('flex')&&cs.alignItems==='center'})}
    }
  }
  return out;
}
"""

E = lambda v: Emu(int(round(v * 9525)))


def to_pptx(prs, items):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    for it in items:
        k = it['k']
        if k == 'bg' and it['fill']:
            s.background.fill.solid(); s.background.fill.fore_color.rgb = RGBColor(*map(int, it['fill']))
        elif k == 'img':
            data = base64.b64decode(it['src'].split(',', 1)[1])
            import io
            s.shapes.add_picture(io.BytesIO(data), E(it['x']), E(it['y']), E(it['w']), E(it['h']))
        elif k == 'tri':
            sh = s.shapes.add_shape(MSO_SHAPE.ISOSCELES_TRIANGLE, E(it['x']), E(it['y'] - (0 if it['dir'] == 'up' else 0)), E(it['w']), E(it['h']))
            if it['dir'] == 'down':
                sh.rotation = 180
            sh.fill.solid(); sh.fill.fore_color.rgb = RGBColor(*map(int, it['fill'])); sh.line.fill.background()
        elif k == 'rect':
            w, h, r = it['w'], it['h'], it['rad']
            if r >= min(w, h) / 2 - 1 and abs(w - h) < 2:
                shp = MSO_SHAPE.OVAL
            elif r > 0:
                shp = MSO_SHAPE.ROUNDED_RECTANGLE
            else:
                shp = MSO_SHAPE.RECTANGLE
            sh = s.shapes.add_shape(shp, E(it['x']), E(it['y']), E(w), E(h))
            if shp == MSO_SHAPE.ROUNDED_RECTANGLE:
                sh.adjustments[0] = min(0.5, r / min(w, h))
            if it['fill']:
                sh.fill.solid(); sh.fill.fore_color.rgb = RGBColor(*map(int, it['fill']))
            else:
                sh.fill.background()
            if it['stroke'] and it['sw']:
                sh.line.color.rgb = RGBColor(*map(int, it['stroke'])); sh.line.width = Pt(it['sw'] * .75)
            else:
                sh.line.fill.background()
            sh.shadow.inherit = False
        elif k == 'text':
            tb = s.shapes.add_textbox(E(it['x'] - 2), E(it['y']), E(min(it['w'] * 1.05 + 10, W - it['x'])), E(max(it['h'], 10)))
            tf = tb.text_frame; tf.word_wrap = True
            tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE if it['vcenter'] else MSO_ANCHOR.TOP
            para = tf.paragraphs[0]
            if it['center']:
                para.alignment = PP_ALIGN.CENTER
            sz0 = it['runs'][0]['sz'] or 30
            para.line_spacing = Pt(it['lh'] * .75)
            for rr in it['runs']:
                txt = re.sub(r'\s+', ' ', rr['t'])
                if it['upper']:
                    txt = txt.upper()
                run = para.add_run(); run.text = txt
                fo = run.font; fo.name = 'Public Sans'; fo.size = Pt(rr['sz'] * .75); fo.bold = rr['b'] >= 600
                if rr['c']:
                    fo.color.rgb = RGBColor(*map(int, rr['c']))
            # remove espaço inicial/final
            if para.runs:
                para.runs[0].text = para.runs[0].text.lstrip(); para.runs[-1].text = para.runs[-1].text.rstrip()
    return s


def main():
    decks = {}
    report = []
    with sync_playwright() as pw:
        br = pw.chromium.launch(executable_path=CHROME)
        pg = br.new_page(viewport={'width': W, 'height': H})
        for post in POSTS:
            m = post['marca']
            if m not in decks:
                prs = Presentation(); prs.slide_width = E(W); prs.slide_height = E(H); decks[m] = prs
            folder = OUT / m / post['data'] / 'post-01'
            folder.mkdir(parents=True, exist_ok=True)
            for old in folder.glob('*.png'):
                old.unlink()
            n = len(post['cards'])
            for i, card in enumerate(post['cards'], 1):
                dark, deco, body = build(post, card, i)
                b = body.replace('{N}', f'{i}/{n}')
                z = 1.0
                if not dark:
                    for cand in (1.3, 1.25, 1.2, 1.15, 1.1, 1.05, 1.0, 0.95, 0.9, 0.85):
                        pg.set_content(page(m, dark, deco, b, cand)); pg.evaluate('document.fonts.ready')
                        fit = pg.evaluate("""() => {const mn=document.querySelector('.main'); if(!mn) return true; const lim=document.querySelector('.logo').getBoundingClientRect().top-30;
                            let b=0; for(const el of mn.querySelectorAll('*')){const r=el.getBoundingClientRect(); if(r.width>0) b=Math.max(b,r.bottom)}
                            return b<=lim && [...mn.querySelectorAll('*')].every(e=>e.scrollWidth<=e.clientWidth+2)}""")
                        if fit:
                            z = cand; break
                pg.set_content(page(m, dark, deco, b, z))
                pg.evaluate('document.fonts.ready')
                ov = pg.evaluate("""() => {const pad=document.querySelector('.pad'); const lim=document.querySelector('.logo').getBoundingClientRect().top - 24;
                   let worst=0; for(const el of pad.querySelectorAll('*')){if(el.classList.contains('main')) continue; const r=el.getBoundingClientRect(); if(r.width>0) worst=Math.max(worst,r.bottom)}
                   const sw=[...document.querySelectorAll('.t')].filter(e=>e.scrollWidth>e.clientWidth+2).length;
                   return {bottom:worst, lim, hscroll:sw}}""")
                fn = folder / f'{i:02d}.png'
                pg.screenshot(path=str(fn))
                flag = 'OK' if ov['bottom'] <= ov['lim'] and not ov['hscroll'] else f"VERIFICAR bottom={ov['bottom']:.0f} lim={ov['lim']:.0f} hscroll={ov['hscroll']}"
                report.append((post['id'], i, flag))
                to_pptx(decks[m], pg.evaluate(JS))
        br.close()
    ed = OUT / 'editaveis'; ed.mkdir(parents=True, exist_ok=True)
    for m, prs in decks.items():
        prs.save(ed / f'{m}_Piloto_v1_1.pptx')
    for r in report:
        print(*r)


if __name__ == '__main__':
    main()
