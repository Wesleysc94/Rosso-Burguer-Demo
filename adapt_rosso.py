#!/usr/bin/env python3
"""
Adapts the full Aura Burger index.html → Rosso Burguer premium demo.
Run from the Rosso-Burguer-Demo directory:
  python adapt_rosso.py
"""
import re, sys

SRC  = r"C:\Users\wesle\.gemini\antigravity\scratch\Aura burger\index.html"
DEST = r"C:\Users\wesle\.gemini\antigravity\scratch\Rosso burguer demo\Rosso-Burguer-Demo\index.html"

with open(SRC, "r", encoding="utf-8") as f:
    html = f.read()

# ─── 1. TITLE / META ────────────────────────────────────────────────────────
html = html.replace(
    "<title>AURA BURGER | O hambúrguer com alma paulistana</title>",
    "<title>ROSSO BURGUER | O Hambúrguer Artesanal com a Tradição Italiana</title>"
)
html = re.sub(
    r'<meta name="description"[^>]*>',
    '<meta name="description" content="Rosso Burguer — hambúrguer artesanal feito na parrilla à lenha. Tradição italiana desde 2017. 5 unidades em São Paulo e Jundiaí.">',
    html
)
# OG tags
html = html.replace("Aura Burger | O hambúrguer com alma paulistana", "Rosso Burguer | O Hambúrguer Artesanal com a Tradição Italiana")
html = html.replace("AURA BURGER | O hambúrguer com alma paulistana", "ROSSO BURGUER | O Hambúrguer Artesanal com a Tradição Italiana")
html = html.replace("O hambúrguer com alma paulistana. Nascido na Vila Madalena.", "Feito na parrilla à lenha. Sem atalhos. Desde 2017.")

# Favicon
html = html.replace(
    '<link rel="icon" href="/assets/logo-aura.svg" type="image/svg+xml">',
    '<link rel="icon" href="/assets/rosso/logo-oficial.jpeg" type="image/jpeg">'
)
# Also handle if no favicon tag — add one before </head>
if '/assets/rosso/logo-oficial.jpeg' not in html:
    html = html.replace("</head>", '  <link rel="icon" href="/assets/rosso/logo-oficial.jpeg" type="image/jpeg">\n</head>')

# ─── 2. COLORS: orange → green ──────────────────────────────────────────────
html = html.replace("--orange: #E85D16;", "--orange: #2d6a4f;  /* verde musgo Rosso */")
html = html.replace("--orange: #E85D04;", "--orange: #2d6a4f;")
# orange-hover
html = html.replace("background: rgba(232,22,27,0) 100%);", "background: rgba(232,22,27,0) 100%);")
# badge--new background orange → green
html = html.replace(".badge--new { background: var(--orange);", ".badge--new { background: var(--green, #2d6a4f);")
# Add --green CSS variable after --orange
html = html.replace(
    "--red-hover: #ff1f25;",
    "--red-hover: #ff1f25;\n      --green: #2d6a4f;\n      --green-hover: #245c43;"
)
# Replace orange text in scrollbar/selection/etc only where it was for accent
html = html.replace("::-webkit-scrollbar-thumb { background: var(--red); }", "::-webkit-scrollbar-thumb { background: var(--red); }")

# ─── 3. BRAND NAME ──────────────────────────────────────────────────────────
html = html.replace("AURA BURGER", "ROSSO BURGUER")
html = html.replace("Aura Burger", "Rosso Burguer")
html = html.replace("Aura burger", "Rosso Burguer")

# Tagline swaps
html = html.replace("alma paulistana", "tradição italiana")
html = html.replace("Alma Paulistana", "Tradição Italiana")
html = html.replace("O melhor hambúrguer de São Paulo", "O hambúrguer artesanal com a tradição italiana")
html = html.replace("Vila Madalena, SP", "São Paulo &amp; Jundiaí")
html = html.replace("SÃO PAULO · DESDE 2018", "SÃO PAULO · DESDE 2017")
html = html.replace("Desde 2018", "Desde 2017")
html = html.replace("desde 2018", "desde 2017")
html = html.replace("FUNDADOR, 2018", "FUNDADOR, 2017")
html = html.replace(">2018<", ">2017<")
html = html.replace("©️ 2018", "© 2017")
html = html.replace("em 2018", "em 2017")
html = html.replace("ano de 2018", "ano de 2017")
html = html.replace("nasceu em 2018", "nasceu em 2017")
html = html.replace(", 2018.", ", 2017.")
html = html.replace("desde 2018.", "desde 2017.")

# ─── 4. NAVBAR LOGO ─────────────────────────────────────────────────────────
# Replace the text logo "AB" initials badge with real image
html = re.sub(
    r'<div class="logo-mark"[^>]*>.*?</div>',
    '<img src="/assets/rosso/logo-transparente.png" alt="Rosso Burguer" style="height:44px;width:44px;object-fit:contain;">',
    html, flags=re.DOTALL
)
# Also replace simpler logo mark patterns
html = html.replace(
    '<div class="logo-mark">AB</div>',
    '<img src="/assets/rosso/logo-transparente.png" alt="Rosso Burguer" style="height:44px;width:44px;object-fit:contain;">'
)

# ─── 5. PRELOADER ───────────────────────────────────────────────────────────
html = html.replace('<div class="preloader-icon">🔥</div>', '<div class="preloader-icon"><img src="/assets/rosso/logo-transparente.png" style="height:60px;object-fit:contain;filter:brightness(0)invert(1)"></div>')
html = html.replace('<div class="preloader-text">AURA BURGER</div>', '<div class="preloader-text">ROSSO BURGUER</div>')

# ─── 6. HERO CONTENT ────────────────────────────────────────────────────────
# Badge
html = html.replace(
    '<span class="hero-badge reveal" data-delay="1">SÃO PAULO · DESDE 2018</span>',
    '<span class="hero-badge reveal" data-delay="1">SÃO PAULO · DESDE 2017</span>'
)
# H1
html = html.replace(
    '''<h1 class="hero-headline">
          <span class="line reveal" data-delay="1">O MELHOR</span>
          <span class="line reveal" data-delay="2">HAMBÚRGUER</span>
          <span class="line line--red reveal" data-delay="3">DA CIDADE.</span>
        </h1>''',
    '''<h1 class="hero-headline">
          <span class="line reveal" data-delay="1">HAMBÚRGUER</span>
          <span class="line reveal" data-delay="2">ARTESANAL COM A</span>
          <span class="line line--red reveal" data-delay="3">TRADIÇÃO ITALIANA.</span>
        </h1>'''
)
# Subheadline
html = html.replace(
    '''<p class="hero-sub reveal" data-delay="4">
          <span class="hero-sub-line">Blend artesanal, ingredientes frescos, <span class="keep-together">sem atalhos.</span></span>
          <span class="hero-sub-line">O hambúrguer com alma paulistana.</span>
        </p>''',
    '''<p class="hero-sub reveal" data-delay="4">
          <span class="hero-sub-line">Feito na parrilla à lenha, <span class="keep-together">sem atalhos.</span></span>
          <span class="hero-sub-line">A tradição italiana no smash burger paulistano.</span>
        </p>'''
)
# Pills
html = html.replace(
    '''<div class="hero-pills reveal" data-delay="5">
          <span class="pill pill--red">● CARNE FRESCA DIÁRIA</span>
          <span class="pill pill--green">● PÃO ARTESANAL</span>
          <span class="pill pill--red">● FEITO NA HORA</span>
        </div>''',
    '''<div class="hero-pills reveal" data-delay="5">
          <span class="pill pill--red">● PARRILLA À LENHA</span>
          <span class="pill pill--green">● 5 UNIDADES EM SP</span>
          <span class="pill pill--red">● SINCE 2017</span>
        </div>'''
)
# Hero CTAs
html = html.replace(
    '''<div class="hero-ctas reveal" data-delay="4">
          <a href="#" onclick="showPage('cardapio'); return false;" class="btn btn--primary">VER CARDÁPIO &rarr;</a>
          <a href="#" onclick="showPage('historia'); return false;" class="btn btn--outline">NOSSA HISTÓRIA</a>
        </div>''',
    '''<div class="hero-ctas reveal" data-delay="4">
          <a href="#unidades" onclick="document.getElementById('unidades').scrollIntoView({behavior:'smooth'});return false;" class="btn btn--primary">VER LOJAS &rarr;</a>
          <a href="#historia" onclick="document.getElementById('historia').scrollIntoView({behavior:'smooth'});return false;" class="btn btn--outline">NOSSA HISTÓRIA</a>
        </div>'''
)

# ─── 7. TICKER ──────────────────────────────────────────────────────────────
html = re.sub(
    r'<div class="ticker-track promo-ticker">.*?</div>\s*</div>\s*<!-- BURGER',
    '''<div class="ticker-track promo-ticker">
      <span>HAMBÚRGUER ARTESANAL COM TRADIÇÃO ITALIANA</span><span class="dot">•</span>
      <span>FEITO NA PARRILLA À LENHA</span><span class="dot">•</span>
      <span>5 UNIDADES EM SP E JUNDIAÍ</span><span class="dot">•</span>
      <span>SINCE 2017 · BENVENUTI</span><span class="dot">•</span>
      <span>PEÇA DIRETO OU PELO IFOOD</span><span class="dot">•</span>
      <span>HAMBÚRGUER ARTESANAL COM TRADIÇÃO ITALIANA</span><span class="dot">•</span>
      <span>FEITO NA PARRILLA À LENHA</span><span class="dot">•</span>
      <span>5 UNIDADES EM SP E JUNDIAÍ</span><span class="dot">•</span>
      <span>SINCE 2017 · BENVENUTI</span><span class="dot">•</span>
      <span>PEÇA DIRETO OU PELO IFOOD</span><span class="dot">•</span>
    </div>
  </div>

  <!-- BURGER''',
    html, flags=re.DOTALL
)

# ─── 8. ASSEMBLY SECTION — Rosso ingredient labels ──────────────────────────
html = html.replace(
    '<span class="assembly-label-name">Pão Brioche</span>\n            <span class="assembly-label-desc">Assado por parceiro artesanal toda manhã</span>',
    '<span class="assembly-label-name">Pão Brioche</span>\n            <span class="assembly-label-desc">Assado por parceiro artesanal toda manhã</span>'
)
# Phase headlines → Rosso
html = html.replace(
    '<span class="assembly-phase-title">Cada camada tem<br>uma história.</span>\n            <span class="assembly-phase-body">Role para descobrir o que vai dentro de cada Aura Burger.</span>',
    '<span class="assembly-phase-title">Cada camada tem<br>uma história.</span>\n            <span class="assembly-phase-body">Role para descobrir o que vai dentro de cada Rosso Burguer.</span>'
)
html = html.replace(
    '<span class="assembly-phase-title">O melhor<br>da cidade.</span>\n            <span class="assembly-phase-body">São Paulo tem seus favoritos. O Aura Clássico é o nosso.</span>',
    '<span class="assembly-phase-title">A tradição<br>italiana.</span>\n            <span class="assembly-phase-body">São Paulo tem seus favoritos. O Rosso Clássico é o nosso.</span>'
)
html = html.replace("VER O CARDÁPIO COMPLETO", "VER AS NOSSAS LOJAS")
html = html.replace("onclick=\"showPage('cardapio'); return false;\" class=\"btn btn--primary\">VER O CARDÁPIO COMPLETO",
    "href=\"#unidades\" onclick=\"document.getElementById('unidades').scrollIntoView({behavior:'smooth'});return false;\" class=\"btn btn--primary\">VER AS NOSSAS LOJAS")

# ─── 9. FAVORITOS — swap photos to Rosso real images ────────────────────────
# Featured card (Rosso Clássico)
html = html.replace(
    "photo-1568901346375-23c9450c58cd?w=900&q=85",
    "/assets/rosso/hero-dois-lanches.jpeg"
)
html = html.replace('alt="Aura Clássico"', 'alt="Rosso Clássico"')
html = html.replace('<h3 class="card-name">AURA CLÁSSICO</h3>', '<h3 class="card-name">ROSSO CLÁSSICO</h3>')
html = html.replace("Pão brioche artesanal, blend 160g de costela, queijo prato derretido, alface americana, tomate e nossa maionese verde secreta.", "Pão brioche artesanal, blend 160g na parrilla, queijo prato derretido, alface americana, tomate e nossa maionese secreta.")

# Duplo Cheddar
html = html.replace(
    "photo-1553979459-d2229ba7433b?w=800&q=85",
    "/assets/rosso/lanche-queijo.jpeg"
)
html = html.replace('alt="Duplo Cheddar"', 'alt="Duplo Queijo"')

# Smash Duplo
html = html.replace(
    "photo-1607013251379-e6eecfffe234?w=800&q=85",
    "/assets/rosso/lanche-01.jpeg"
)
html = html.replace('alt="Smash Duplo"', 'alt="Smash Rosso"')
html = html.replace('<h3 class="card-name">SMASH DUPLO</h3>', '<h3 class="card-name">SMASH ROSSO</h3>')

# Vegano
html = html.replace(
    "photo-1525059696034-4967a8e1dca2?w=600&q=80",
    "/assets/rosso/lanche-02.jpeg"
)
html = html.replace('<h3 class="card-name">VEGANO DA VILA</h3>', '<h3 class="card-name">ROSSO ESPECIAL</h3>')

# O Clássico → Fritas
html = html.replace(
    "photo-1571091718767-18b5b1457add?w=600&q=80",
    "/assets/rosso/batata-frita.jpeg"
)
html = html.replace('<h3 class="card-name">O CLÁSSICO</h3>', '<h3 class="card-name">FRITAS ROSSO</h3>')

# ─── 10. EDITORIAL SECTION ──────────────────────────────────────────────────
html = html.replace(
    'photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=2200&q=80',
    '/assets/rosso/hero-dois-lanches.jpeg'
)
html = html.replace('alt="Qualidade Aura Burger"', 'alt="Rosso Burguer — parrilla à lenha"')
html = html.replace(
    '<span class="editorial-ghost" aria-hidden="true">2018</span>',
    '<span class="editorial-ghost" aria-hidden="true">2017</span>'
)
html = html.replace(
    '<blockquote class="editorial-quote">QUALIDADE QUE<br><em>VOCÊ PROVA.</em></blockquote>',
    '<blockquote class="editorial-quote">TRADIÇÃO QUE<br><em>VOCÊ SENTE.</em></blockquote>'
)
html = html.replace(
    '<span>FUNDADOR, 2018</span>',
    '<span>ROSSO BURGUER · SINCE 2017</span>'
)

# ─── 11. DELIVERY SECTION — keep iFood + add WhatsApp, remove Rappi/Keeta ───
# The delivery section is complex — keep the structure but update copy
html = html.replace(
    "Peça pelo app, receba em casa.",
    "Peça direto ou pelo iFood."
)
html = html.replace(
    "Disponível nos principais apps de delivery.",
    "Peça pelo WhatsApp e receba em até 45 minutos."
)

# ─── 12. UNITS SECTION — Replace with 5 real Rosso units ───────────────────
UNITS_NEW = '''  <!-- UNIDADES -->
  <section class="section units-section" id="unidades">
    <div class="container">
      <div class="section-header-center reveal">
        <span class="eyebrow">NOSSAS UNIDADES</span>
        <h2 class="section-title-xl">FAÇA SEU PEDIDO.</h2>
        <p style="color:var(--gray-1);margin-top:16px;font-size:16px;">5 unidades para você. Peça direto pelo WhatsApp ou pelo iFood.</p>
      </div>

      <div class="units-grid">

        <article class="unit-card reveal" data-delay="1">
          <div class="unit-number" aria-hidden="true">01</div>
          <div class="unit-content">
            <div class="unit-status">
              <span class="status-dot status--live"></span>
              <span>DISPONÍVEL</span>
            </div>
            <h3 class="unit-name">SHOPPING ANÁLIA FRANCO</h3>
            <address class="unit-address">Praça de Alimentação – Av. Reg. Feijó, 1739<br>Vila Reg. Feijó, São Paulo – SP, 03342-900</address>
            <div class="unit-actions" style="display:flex;flex-direction:column;gap:10px;margin-top:24px;">
              <a href="https://wa.me/5511947936611?text=Ol%C3%A1!+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+Rosso+Burguer+An%C3%A1lia+Franco" target="_blank" rel="noopener" class="btn btn--primary" style="justify-content:center;font-size:13px;padding:14px 20px;">PEDIR DIRETO →</a>
              <a href="https://www.ifood.com.br/delivery/sao-paulo-sp/rosso-burguer---analia-franco-vila-regente-feijo/c0221e7c-ccf1-4d1e-b66f-cf753365a7a0" target="_blank" rel="noopener" class="btn btn--outline" style="justify-content:center;font-size:13px;padding:14px 20px;">IFOOD →</a>
            </div>
          </div>
        </article>

        <article class="unit-card reveal" data-delay="2">
          <div class="unit-number" aria-hidden="true">02</div>
          <div class="unit-content">
            <div class="unit-status">
              <span class="status-dot status--live"></span>
              <span>DISPONÍVEL</span>
            </div>
            <h3 class="unit-name">PARK SHOPPING SÃO CAETANO SUL</h3>
            <address class="unit-address">Praça de Alimentação – Alameda Terracota, 545<br>Cerâmica, São Caetano do Sul – SP, 09531-190</address>
            <div class="unit-actions" style="display:flex;flex-direction:column;gap:10px;margin-top:24px;">
              <a href="https://wa.me/5511947921707?text=Ol%C3%A1!+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+Rosso+Burguer+S%C3%A3o+Caetano" target="_blank" rel="noopener" class="btn btn--primary" style="justify-content:center;font-size:13px;padding:14px 20px;">PEDIR DIRETO →</a>
              <a href="https://www.ifood.com.br/delivery/sao-caetano-do-sul-sp/rosso-burguer---sao-caetano-ceramica/0f8f3a19-8e77-407d-8133-6a48b4295f20" target="_blank" rel="noopener" class="btn btn--outline" style="justify-content:center;font-size:13px;padding:14px 20px;">IFOOD →</a>
            </div>
          </div>
        </article>

        <article class="unit-card reveal" data-delay="3">
          <div class="unit-number" aria-hidden="true">03</div>
          <div class="unit-content">
            <div class="unit-status">
              <span class="status-dot status--live"></span>
              <span>DISPONÍVEL</span>
            </div>
            <h3 class="unit-name">ROSSO BURGUER SAPOPEMBA</h3>
            <address class="unit-address">R. Adutora de Rio Claro, 151<br>Vila Primavera, São Paulo – SP, 03374-050</address>
            <div class="unit-actions" style="display:flex;flex-direction:column;gap:10px;margin-top:24px;">
              <a href="https://wa.me/5511961809916?text=Ol%C3%A1!+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+Rosso+Burguer+Sapopemba" target="_blank" rel="noopener" class="btn btn--primary" style="justify-content:center;font-size:13px;padding:14px 20px;">PEDIR DIRETO →</a>
              <a href="https://www.ifood.com.br/delivery/sao-paulo-sp/rosso-burguer-vila-primavera/55527464-4001-4f67-ae9f-597cfc75ca9b" target="_blank" rel="noopener" class="btn btn--outline" style="justify-content:center;font-size:13px;padding:14px 20px;">IFOOD →</a>
            </div>
          </div>
        </article>

        <article class="unit-card reveal" data-delay="4">
          <div class="unit-number" aria-hidden="true">04</div>
          <div class="unit-content">
            <div class="unit-status">
              <span class="status-dot status--live"></span>
              <span>DISPONÍVEL</span>
            </div>
            <h3 class="unit-name">JUNDIAÍ SHOPPING</h3>
            <address class="unit-address">Praça de Alimentação – Av. 9 de Julho, 3333<br>Anhangabaú, Jundiaí – SP</address>
            <div class="unit-actions" style="display:flex;flex-direction:column;gap:10px;margin-top:24px;">
              <a href="https://wa.me/5511947925999?text=Ol%C3%A1!+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+Rosso+Burguer+Jundia%C3%AD" target="_blank" rel="noopener" class="btn btn--primary" style="justify-content:center;font-size:13px;padding:14px 20px;">PEDIR DIRETO →</a>
              <a href="https://www.ifood.com.br/delivery/jundiai-sp/rosso-burguer---jundiai-anhangabau/16db2830-8f4f-414c-9554-1cafeb46af8b" target="_blank" rel="noopener" class="btn btn--outline" style="justify-content:center;font-size:13px;padding:14px 20px;">IFOOD →</a>
            </div>
          </div>
        </article>

        <article class="unit-card reveal" data-delay="5">
          <div class="unit-number" aria-hidden="true">05</div>
          <div class="unit-content">
            <div class="unit-status">
              <span class="status-dot status--live"></span>
              <span>DISPONÍVEL</span>
            </div>
            <h3 class="unit-name">ROSSO BURGUER VILA PRUDENTE</h3>
            <address class="unit-address">São Paulo – SP</address>
            <div class="unit-actions" style="display:flex;flex-direction:column;gap:10px;margin-top:24px;">
              <a href="https://wa.me/5511993471000?text=Ol%C3%A1!+Vi+no+site+e+gostaria+de+informa%C3%A7%C3%B5es+sobre+a+Rosso+Burguer+Vila+Prudente" target="_blank" rel="noopener" class="btn btn--primary" style="justify-content:center;font-size:13px;padding:14px 20px;">PEDIR DIRETO →</a>
              <a href="https://www.ifood.com.br/delivery/sao-paulo-sp/rosso-burguer---vila-prudente-vila-prudente/d45b7eaa-a1b5-415e-b802-e73f2617e989" target="_blank" rel="noopener" class="btn btn--outline" style="justify-content:center;font-size:13px;padding:14px 20px;">IFOOD →</a>
            </div>
          </div>
        </article>

      </div>
    </div>
  </section>'''

# Replace the units section
html = re.sub(
    r'<!-- UNIDADES -->.*?</div>\s*</section>\s*\n\s*<!-- TESTIMONIALS -->',
    UNITS_NEW + '\n\n  <!-- TESTIMONIALS -->',
    html, flags=re.DOTALL
)

# ─── 13. TESTIMONIALS — update brand name ───────────────────────────────────
html = html.replace(
    '"Melhor hambúrguer que já comi em SP. O blend derrete na boca e o pão artesanal é absurdamente bom. Vou toda semana!"',
    '"Melhor hambúrguer que já comi em SP. O blend na parrilla é absurdamente bom. Vou toda semana!"'
)
html = html.replace(
    '"Ambiente incrível, atendimento rápido e o smash burger é perfeito. Nota 10 pra tudo. Melhor hamburgueria da Vila Madalena!"',
    '"Ambiente incrível, atendimento rápido e o smash burger é perfeito. Nota 10 pra tudo. Melhor hamburgueria de SP!"'
)
html = html.replace(
    '"A Trufa Negra com blend wagyu é nível de restaurante fine dining, mas num preço acessível. Impressionante!"',
    '"O Rosso Clássico com blend na parrilla é nível de restaurante fine dining, mas num preço acessível. Impressionante!"'
)

# ─── 14. NAVBAR — restructure to LOJAS / TRAMPE / FALE CONOSCO ─────────────
# Replace nav links
html = re.sub(
    r'<div class="navbar-links">.*?</div>\s*<div class="navbar-actions">',
    '''<div class="navbar-links">
          <a href="#unidades" onclick="document.getElementById('unidades').scrollIntoView({behavior:'smooth'});return false;" class="nav-link">LOJAS</a>
          <a href="mailto:rh@rossoburguer.com.br" class="nav-link">TRAMPE NO ROSSO</a>
          <a href="mailto:contato@rossoburguer.com.br" class="nav-link">FALE CONOSCO</a>
        </div>
        <div class="navbar-actions">''',
    html, flags=re.DOTALL
)
# Remove the CTA button from navbar (Rosso doesn't have it)
html = re.sub(
    r'<a[^>]*class="[^"]*navbar-cta[^"]*"[^>]*>.*?</a>',
    '',
    html, flags=re.DOTALL
)

# ─── 15. MOBILE DRAWER NAV ──────────────────────────────────────────────────
html = re.sub(
    r'<nav class="drawer-nav">.*?</nav>',
    '''<nav class="drawer-nav">
          <a href="#unidades" onclick="document.getElementById(\'unidades\').scrollIntoView({behavior:\'smooth\'});toggleMenu(false);return false;">LOJAS</a>
          <a href="mailto:rh@rossoburguer.com.br">TRAMPE NO ROSSO</a>
          <a href="mailto:contato@rossoburguer.com.br">FALE CONOSCO</a>
        </nav>''',
    html, flags=re.DOTALL
)

# ─── 16. HISTORIA PAGE — adapt to Rosso ─────────────────────────────────────
html = html.replace(
    "Da garagem na Zona Oeste para o coração da Vila Madalena.",
    "Da parrilla à lenha para 5 unidades em SP e Jundiaí."
)
html = html.replace(
    "O Aura Burger nasceu em 2018, numa garagem apertada na Zona Oeste de São Paulo.",
    "O Rosso Burguer nasceu em 2017, com uma missão: trazer a tradição da parrilla à lenha para o smash burger paulistano."
)
html = html.replace(
    "continuamos moendo nossa carne diariamente, recebendo pães frescos todas as manhãs e preparando nossa maionese verde com a mesma receita daquela garagem em 2018. A aura continua a mesma.",
    "seguimos o mesmo princípio: blend artesanal, ingredientes frescos e muito respeito pelo processo. Benvenuti."
)

# ─── 17. FOOTER ─────────────────────────────────────────────────────────────
# Tagline in footer
html = html.replace(
    "O hambúrguer com alma paulistana. Nascido na Vila Madalena, feito para quem exige o melhor da cidade.",
    '"O Hambúrguer Artesanal com a Tradição Italiana." — Since 2017.'
)
# Footer address
html = html.replace(
    "Rua Fradique Coutinho, 1234<br>Vila Madalena, São Paulo - SP",
    "5 unidades em São Paulo e Jundiaí"
)
html = html.replace(
    "contato@auraburger.com.br",
    "contato@rossoburguer.com.br"
)
html = html.replace(
    "rh@auraburger.com.br",
    "rh@rossoburguer.com.br"
)
# Copyright
html = html.replace(
    "© 2025 Aura Burger SP. Todos os direitos reservados.",
    "© 2026 Rosso Burguer · Since 2017 · Todos os direitos reservados."
)
html = html.replace(
    "&copy; 2025 Aura Burger SP. Todos os direitos reservados.",
    "&copy; 2026 Rosso Burguer · Since 2017 · Todos os direitos reservados."
)
html = html.replace(
    "© 2024 Aura Burger SP. Todos os direitos reservados.",
    "© 2026 Rosso Burguer · Since 2017 · Todos os direitos reservados."
)

# ─── 18. WHATSAPP FLOAT — Update to Rosso ───────────────────────────────────
html = html.replace(
    "https://wa.me/5511999999999?text=Ol%C3%A1!%20Vi%20o%20card%C3%A1pio%20e%20quero%20fazer%20um%20pedido%20%F0%9F%8D%94",
    "https://wa.me/5511947936611?text=Ol%C3%A1!%20Vi%20o%20site%20e%20gostaria%20de%20informa%C3%A7%C3%B5es%20sobre%20a%20Rosso%20Burguer"
)
html = html.replace(
    '<span class="whatsapp-tooltip">Peça pelo WhatsApp! 🍔</span>',
    '<span class="whatsapp-tooltip">Peça pelo WhatsApp!</span>'
)

# ─── 19. NEWSLETTER label ───────────────────────────────────────────────────
html = html.replace("AURA NEWS", "ROSSO NEWS")
html = html.replace("Aura News", "Rosso News")

# ─── 20. SPA pages — remove Cardápio/Carreiras references from nav display ──
# The SPA pages can stay but just make the history section have Rosso id
html = html.replace('<div id="page-historia"', '<div id="historia" id="page-historia"')
html = html.replace(
    'Tudo começou com uma chapa',
    'Tudo começou com uma parrilla'
)

# ─── 21. Fix remaining Aura references ──────────────────────────────────────
html = html.replace("Aura Clássico", "Rosso Clássico")
html = html.replace("AURA CLÁSSICO", "ROSSO CLÁSSICO")
html = html.replace("aura-classico", "rosso-classico")
html = html.replace("'aura-classico'", "'rosso-classico'")
html = html.replace('"aura-classico"', '"rosso-classico"')

# ─── 22. Italian flag style in CSS ──────────────────────────────────────────
# Add Italian flag bar style after body::after grain
ITALIAN_STYLE = """
    /* Italian accent bar */
    .italian-bar {
      display: inline-flex;
      height: 3px;
      width: 60px;
      background: linear-gradient(90deg, #009246 33%, #ffffff 33% 66%, #ce2b37 66%);
      margin-bottom: 20px;
    }
"""
html = html.replace("</style>", ITALIAN_STYLE + "\n    </style>", 1)

# ─── WRITE OUTPUT ────────────────────────────────────────────────────────────
with open(DEST, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Done! Wrote {len(html):,} chars to {DEST}")
line_count = html.count('\n') + 1
print(f"Lines: {line_count:,}")
