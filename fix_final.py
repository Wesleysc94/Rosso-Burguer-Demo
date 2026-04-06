"""
Rosso Burguer — Comprehensive Final Fix
Resolve: paleta laranja Aura, CSS duplicado, identidade verde ausente, ingredientes Aura.
"""
SRC = 'index.html'

with open(SRC, 'r', encoding='utf-8') as f:
    html = f.read()

orig_len = len(html)
changes = []

def replace_once(old, new, label):
    global html
    if old in html:
        html = html.replace(old, new, 1)
        changes.append(f'  OK  {label}')
    else:
        changes.append(f'  !! NOT FOUND: {label}')

def replace_second(block, label):
    """Remove second occurrence of a block, keep first."""
    global html
    first = html.find(block)
    if first == -1:
        changes.append(f'  !! NOT FOUND: {label}')
        return
    second = html.find(block, first + len(block))
    if second == -1:
        changes.append(f'  ~~ only once (ok): {label}')
        return
    html = html[:second] + html[second + len(block):]
    changes.append(f'  OK  {label}')

# ══════════════════════════════════════════════════════════════
# 1. CLEAN :root — remove --orange alias + duplicate --green
# ══════════════════════════════════════════════════════════════
replace_once(
    '      --orange: #2d6a4f;  /* kept as alias */\n      --green: #2d6a4f;\n      --green-hover: #245c43;',
    '      --orange: #E85D16;  /* Aura accent — kept for canvas compat */',
    ':root cleanup — remove duplicate green, restore orange'
)

# ══════════════════════════════════════════════════════════════
# 2. REMOVE DUPLICATE CSS BLOCK (reveal/btn/navbar appears twice)
# ══════════════════════════════════════════════════════════════
DUPE = (
    '    .reveal[data-delay="1"] { transition-delay: 100ms; }\n'
    '    .reveal[data-delay="2"] { transition-delay: 200ms; }\n'
    '    .reveal[data-delay="3"] { transition-delay: 300ms; }\n'
    '    .reveal[data-delay="4"] { transition-delay: 400ms; }\n'
    '    .reveal[data-delay="5"] { transition-delay: 500ms; }\n'
    '\n'
    '    /* BUTTONS */\n'
    '    .btn {\n'
    '      font-family: var(--font-display); font-weight: 700; font-size: 14px;\n'
    '      letter-spacing: 0.15em; text-transform: uppercase; padding: 16px 32px;\n'
    '      border: none; display: inline-flex; align-items: center; gap: 8px;\n'
    '      transition: all var(--dur-fast) var(--ease-smooth); position: relative; overflow: hidden;\n'
    '    }\n'
    '    .btn::after {\n'
    '      content: \'\'; position: absolute; inset: 0; background: rgba(255,255,255,0.1);\n'
    '      transform: translateX(-100%); transition: transform 300ms var(--ease-smooth);\n'
    '    }\n'
    '    .btn:hover::after { transform: translateX(0); }\n'
    '    .btn--primary { background: var(--red); color: var(--white); }\n'
    '    .btn--primary:hover { background: var(--red-hover); transform: translateY(-2px); box-shadow: 0 8px 32px rgba(232, 22, 27, 0.4); }\n'
    '    .btn--outline { background: transparent; color: var(--white); border: 1px solid rgba(255,255,255,0.4); }\n'
    '    .btn--outline:hover { border-color: var(--white); background: rgba(255,255,255,0.05); transform: translateY(-2px); }\n'
    '\n'
    '    /* NAVBAR */\n'
    '    .navbar {\n'
    '      position: fixed; top: 0; left: 0; right: 0; z-index: 1000; padding: 0;\n'
    '      background: rgba(10,10,10,0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);\n'
    '      border-bottom: 1px solid transparent; transition: border-color var(--dur-med), background var(--dur-med);\n'
    '      height: 72px; display: flex; align-items: center;\n'
    '    }\n'
    '    .navbar.scrolled { background: rgba(8,8,8,0.97); border-bottom-color: var(--red); box-shadow: 0 4px 40px rgba(0,0,0,0.6); }\n'
    '    .navbar-inner { display: flex; align-items: center; justify-content: space-between; width: 100%; }\n'
    '    .navbar-logo { font-family: var(--font-display); font-weight: 900; font-size: 20px; text-transform: uppercase; color: var(--white); display: flex; align-items: center; gap: 10px; letter-spacing: 0.05em; }\n'
    '    .navbar-links { display: flex; gap: 40px; }\n'
    '    .nav-link { font-family: var(--font-display); font-size: 13px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: var(--gray-1); transition: color var(--dur-fast); position: relative; padding-bottom: 4px; }\n'
    '    .nav-link::after { content: \'\'; position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--red); transition: width var(--dur-fast) var(--ease-smooth); }\n'
    '    .nav-link:hover { color: var(--white); }\n'
    '    .nav-link:hover::after, .nav-link.active::after { width: 100%; }\n'
    '    .nav-link.active { color: var(--white); }\n'
    '    .navbar-actions { display: flex; align-items: center; gap: 20px; }\n'
    '    .lang-switcher { display: flex; align-items: center; gap: 4px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 4px; border-radius: 4px !important; z-index: 99; }\n'
    '    .lang-btn { background: transparent; border: none; color: var(--gray-1); font-family: var(--font-display); font-size: 13px; font-weight: 700; cursor: pointer; padding: 4px 8px; transition: all var(--dur-fast); border-radius: 2px !important; }\n'
    '    .lang-btn:hover { color: var(--white); }\n'
    '    .lang-btn.active { background: var(--red); color: var(--white); }\n'
    '    @media (max-width: 1024px) { .lang-switcher.hide-mobile { display: none !important; } }\n'
    '    .hamburger { display: none; flex-direction: column; gap: 5px; background: none; border: none; padding: 8px; }\n'
    '    .hamburger span { display: block; width: 24px; height: 2px; background: var(--white); transition: all 300ms var(--ease-smooth); }\n'
    '    .hamburger.active span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }\n'
    '    .hamburger.active span:nth-child(2) { opacity: 0; transform: translateX(-8px); }'
)
replace_second(DUPE, 'Duplicate reveal/btn/navbar CSS block')

# ══════════════════════════════════════════════════════════════
# 3. HERO LAMP PULSE — orange → subtle crimson
# ══════════════════════════════════════════════════════════════
replace_once(
    'background: radial-gradient(circle at center, rgba(255, 180, 100, 0.35) 0%, rgba(252, 140, 50, 0.1) 35%, transparent 60%);',
    'background: radial-gradient(circle at center, rgba(200, 16, 46, 0.18) 0%, rgba(200, 16, 46, 0.05) 35%, transparent 60%);',
    'Hero lamp pulse — orange to crimson'
)

# ══════════════════════════════════════════════════════════════
# 4. HERO PARTICLES — orange → red embers
# ══════════════════════════════════════════════════════════════
replace_once(
    '      background: rgba(255, 140, 50, 0.4);',
    '      background: rgba(232, 22, 27, 0.35);',
    'Hero particles — orange to red'
)

# ══════════════════════════════════════════════════════════════
# 5. TICKER — red background → GREEN (Rosso brand primary)
# ══════════════════════════════════════════════════════════════
replace_once(
    '.ticker { background: var(--red); height: 40px; overflow: hidden; display: flex; align-items: center; }',
    '.ticker { background: var(--green); height: 40px; overflow: hidden; display: flex; align-items: center; }',
    'Ticker background — red to green'
)

# ══════════════════════════════════════════════════════════════
# 6. TICKER-BRIDGE — red → green
# ══════════════════════════════════════════════════════════════
replace_once(
    '      background: var(--red);\n    }\n    .ticker-bridge::before {\n      display: none;\n    }',
    '      background: var(--green);\n    }\n    .ticker-bridge::before {\n      display: none;\n    }',
    'Ticker-bridge background — red to green'
)
replace_once(
    '      background: linear-gradient(180deg, var(--red) 0%, #050505 100%);',
    '      background: linear-gradient(180deg, var(--green) 0%, #050505 100%);',
    'Ticker-bridge ::after gradient — red to green'
)

# ══════════════════════════════════════════════════════════════
# 7. STATS BAR — red → green
# ══════════════════════════════════════════════════════════════
replace_once(
    '.stats-bar { background: var(--red); display: flex; justify-content: space-evenly; padding: 40px 24px; flex-wrap: wrap; gap: 24px; }',
    '.stats-bar { background: var(--green); display: flex; justify-content: space-evenly; padding: 40px 24px; flex-wrap: wrap; gap: 24px; }',
    'Stats bar background — red to green'
)

# ══════════════════════════════════════════════════════════════
# 8. ASSEMBLY PROGRESS BAR — red/orange gradient → green
# ══════════════════════════════════════════════════════════════
replace_once(
    '      background: linear-gradient(180deg, var(--red) 0%, var(--orange) 100%);',
    '      background: var(--green);',
    'Assembly progress bar — to green'
)

# ══════════════════════════════════════════════════════════════
# 9. FILTER TAB ACTIVE — red → green
# ══════════════════════════════════════════════════════════════
replace_once(
    '    .filter-tab.active { color: #fff; border-bottom-color: var(--red); }',
    '    .filter-tab.active { color: #fff; border-bottom-color: var(--green); }',
    'Filter tab active underline — red to green'
)
replace_once(
    '    .filter-tab.active .filter-count { background: var(--red); color: white; }',
    '    .filter-tab.active .filter-count { background: var(--green); color: white; }',
    'Filter count badge active — red to green'
)

# ══════════════════════════════════════════════════════════════
# 10. CARDÁPIO SECTION bottom banner — red → green
# ══════════════════════════════════════════════════════════════
replace_once(
    '    <div style="background:var(--red);padding:40px;text-align:center;">',
    '    <div style="background:var(--green);padding:40px;text-align:center;">',
    'Cardápio bottom banner — red to green'
)

# ══════════════════════════════════════════════════════════════
# 11. CAREERS HERO glow — red → green tint
# ══════════════════════════════════════════════════════════════
replace_once(
    '        radial-gradient(circle at 50% 30%, rgba(232,22,27,0.16) 0%, rgba(232,22,27,0.02) 34%, transparent 58%),\n        linear-gradient(180deg, #1b0907 0%, #0f0f0f 42%, #080808 100%);',
    '        radial-gradient(circle at 50% 30%, rgba(45,106,79,0.18) 0%, rgba(45,106,79,0.03) 34%, transparent 58%),\n        linear-gradient(180deg, #071209 0%, #0f0f0f 42%, #080808 100%);',
    'Careers hero glow — red to green'
)

# ══════════════════════════════════════════════════════════════
# 12. SUBPAGE HERO GRADIENTS — warm red-dark (#1a0500) → dark green-tint
# ══════════════════════════════════════════════════════════════
# Cardápio page hero
replace_once(
    'min-height:35vh;background:linear-gradient(to bottom,#1a0500,#111)',
    'min-height:35vh;background:linear-gradient(to bottom,#091609,#111)',
    'Cardápio hero gradient — warm red to dark green'
)
# História page hero
replace_once(
    'min-height:50vh;background:linear-gradient(160deg,#1a0500 0%,#111 60%)',
    'min-height:50vh;background:linear-gradient(160deg,#091609 0%,#111 60%)',
    'História hero gradient — warm red to dark green'
)

# ══════════════════════════════════════════════════════════════
# 13. ASSEMBLY INGREDIENTS — update ingredient 07 name
# ══════════════════════════════════════════════════════════════
replace_once(
    '            <span class="assembly-label-name">Maionese Verde</span>\n            <span class="assembly-label-desc">Receita secreta desde 2017</span>',
    '            <span class="assembly-label-name">Molho Rosso</span>\n            <span class="assembly-label-desc">Receita exclusiva da casa, desde 2017</span>',
    'Assembly ingredient 07 — Maionese Verde → Molho Rosso'
)

# Update ingredient 03 to mention parrilla
replace_once(
    '            <span class="assembly-label-name">Blend 160g</span>\n            <span class="assembly-label-desc">Costela + fraldinha, moído na hora</span>',
    '            <span class="assembly-label-name">Blend na Parrilla</span>\n            <span class="assembly-label-desc">Costela + fraldinha, selado na brasa</span>',
    'Assembly ingredient 03 — Blend 160g → Blend na Parrilla'
)

# ══════════════════════════════════════════════════════════════
# 14. ASSEMBLY PHASE 3 — add parrilla narrative
# ══════════════════════════════════════════════════════════════
replace_once(
    '            <span class="assembly-phase-title">160g de costela<br>e fraldinha.</span>\n            <span class="assembly-phase-body">Blend exclusivo moído na hora. A diferença que você sente na primeira mordida.</span>',
    '            <span class="assembly-phase-title">Na parrilla<br>à lenha.</span>\n            <span class="assembly-phase-body">Blend selado na brasa. O calor da parrilla forma a crosta que você sente na primeira mordida.</span>',
    'Assembly phase 3 — parrilla narrative'
)

# Update phase 3 eyebrow
replace_once(
    '          <div class="assembly-phase" data-phase-start="0.35" data-phase-end="0.62">\n            <span class="assembly-phase-eyebrow">O coração</span>',
    '          <div class="assembly-phase" data-phase-start="0.35" data-phase-end="0.62">\n            <span class="assembly-phase-eyebrow">A parrilla</span>',
    'Assembly phase 3 eyebrow — O coração → A parrilla'
)

# ══════════════════════════════════════════════════════════════
# 15. FOOTER — remove duplicate contact email
# ══════════════════════════════════════════════════════════════
replace_once(
    '            <li>contato@rossoburguer.com.br</li>\n            <li>rh@rossoburguer.com.br</li>\n            <li>contato@rossoburguer.com.br</li>',
    '            <li><a href="mailto:contato@rossoburguer.com.br" style="color:var(--gray-1);">contato@rossoburguer.com.br</a></li>\n            <li><a href="mailto:rh@rossoburguer.com.br" style="color:var(--gray-1);">rh@rossoburguer.com.br</a></li>',
    'Footer — remove duplicate email, add mailto links'
)

# ══════════════════════════════════════════════════════════════
# 16. NAVBAR LOGO — increase size (44px → 60px)
# ══════════════════════════════════════════════════════════════
replace_once(
    'style="height:44px;width:44px;object-fit:contain;"',
    'style="height:58px;width:58px;object-fit:contain;"',
    'Navbar logo — 44px to 58px'
)

# ══════════════════════════════════════════════════════════════
# 17. CITY TAB ACTIVE — red → green (Unidades page)
# ══════════════════════════════════════════════════════════════
replace_once(
    '    .city-tab.active { background: var(--red); border-color: var(--red); color: white; }',
    '    .city-tab.active { background: var(--green); border-color: var(--green); color: white; }',
    'City tab active — red to green'
)

# ══════════════════════════════════════════════════════════════
# 18. UCARD city color (red → green accent)
# ══════════════════════════════════════════════════════════════
replace_once(
    '    .ucard-city { font-size: 12px; color: var(--red); font-weight: 600; margin: 4px 0 14px; }',
    '    .ucard-city { font-size: 12px; color: var(--green); font-weight: 600; margin: 4px 0 14px; }',
    'Ucard city color — red to green'
)

# ══════════════════════════════════════════════════════════════
# 19. TIMELINE CARD border-top and year badge — keep red (CTA), fine
# (no change — red accent on timeline is fine)
# ══════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════
# 20. Add green accent for navbar scrolled (Italian flag accent on scroll)
# ══════════════════════════════════════════════════════════════
# The navbar uses red border on scroll — this is brand CTA, keep red
# But add a subtle green left accent to the navbar brand text

# ══════════════════════════════════════════════════════════════
# 21. LEAD POPUP — remove fire emoji, keep hamburger emoji
# ══════════════════════════════════════════════════════════════
replace_once(
    '      <div class="lead-popup-icon">🔥</div>',
    '      <div class="lead-popup-icon">🍔</div>',
    'Lead popup icon — fire to burger'
)
# Remove emoji from disclaimer
replace_once(
    '      <p class="lead-popup-disclaimer">Sem spam. Só hambúrguer. 🍔</p>',
    '      <p class="lead-popup-disclaimer">Sem spam. Só hambúrguer.</p>',
    'Lead popup disclaimer — remove emoji'
)

# ══════════════════════════════════════════════════════════════
# 22. ITALIAN BAR duplicate — only one needed
# ══════════════════════════════════════════════════════════════
ITALIAN_DUP = (
    '\n\n    /* Italian accent bar */\n'
    '    .italian-bar {\n'
    '      display: inline-flex;\n'
    '      height: 3px;\n'
    '      width: 60px;\n'
    '      background: linear-gradient(90deg, #009246 33%, #ffffff 33% 66%, #ce2b37 66%);\n'
    '      margin-bottom: 20px;\n'
    '    }\n'
)
replace_second(ITALIAN_DUP, 'Italian bar CSS duplicate')

# ══════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════
with open(SRC, 'w', encoding='utf-8') as f:
    f.write(html)

print('Original: %d chars' % orig_len)
print('Final:    %d chars' % len(html))
print('Saved:    %d chars' % (orig_len - len(html)))
print('\nChanges:')
for c in changes:
    print(c)
print('\nDone! index.html saved.')
