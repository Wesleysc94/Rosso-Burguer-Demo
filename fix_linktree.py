import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)

# 1. Remove o card 99Food completo da pagina delivery
old_99food_card = '''          <!-- 99Food -->
          <div class="partner-card reveal" data-delay="2" style="background:rgba(15,15,15,0.8);border:1px solid rgba(255,255,255,0.06);padding:40px;display:grid;grid-template-columns:80px 1fr auto;gap:32px;align-items:center;">
            <div style="width:80px;height:80px;background:linear-gradient(135deg,#ffde59,#f6b900);display:flex;align-items:center;justify-content:center;font-weight:900;font-family:var(--font-display);font-size:11px;letter-spacing:0.1em;color:#111;text-align:center;">99FOOD</div>
            <div>
              <h3 style="font-family:var(--font-display);font-size:24px;font-weight:900;text-transform:uppercase;color:white;margin-bottom:8px;">99Food</h3>
              <p style="color:var(--gray-1);font-size:14px;line-height:1.6;">Algumas unidades aparecem com rota ativa no Linktree oficial da Rosso. Use como canal complementar quando disponível.</p>
            </div>
            <a href="https://linktr.ee/RossoBurguerr?utm_source=linktree_profile_share&ltsid=20bdebfb-1d77-4994-8188-0dfec3befac3" target="_blank" rel="noopener" class="btn btn--outline" style="white-space:nowrap;">ABRIR LINKTREE &rarr;</a>
          </div>'''
if old_99food_card in html:
    html = html.replace(old_99food_card, '', 1)
    print('OK  Removido card 99Food/Linktree do delivery')
else:
    print('!!  Card 99Food nao encontrado - verifique')

# 2. Corrigir passo 3 do "Como Funciona" - remover mencao a 99Food
html = html.replace(
    'Siga para iFood, WhatsApp ou 99Food quando houver disponibilidade ativa para concluir o pedido com segurança.',
    'Siga para o iFood ou WhatsApp da unidade escolhida e conclua o pedido com segurança.',
    1
)
print('OK  Corrigido passo 3 delivery (sem 99Food)')

# 3. Remover pill-btn 99Food da pagina de home (cardapio area)
html = html.replace(
    '''      <a href="https://linktr.ee/RossoBurguerr?utm_source=linktree_profile_share&ltsid=20bdebfb-1d77-4994-8188-0dfec3befac3" class="pill-btn" target="_blank" rel="noopener noreferrer">99FOOD</a>''',
    '',
    1
)
print('OK  Removido pill-btn 99Food')

# 4. Lead popup - remover linktree
html = html.replace(
    'Peça pelo iFood, fale direto no WhatsApp da loja ou abra o Linktree oficial para ver os canais ativos da Rosso.',
    'Peça pelo iFood ou fale direto no WhatsApp da sua unidade mais próxima.',
    1
)
print('OK  Lead popup copy corrigida')

html = html.replace(
    '''        <a href="https://linktr.ee/RossoBurguerr?utm_source=linktree_profile_share&ltsid=20bdebfb-1d77-4994-8188-0dfec3befac3" target="_blank" rel="noopener" class="lead-popup-btn" style="text-decoration:none;text-align:center;background:#0f0f0f;color:white;border:1px solid #2a2a2a;">ABRIR LINKTREE</a>''',
    '',
    1
)
print('OK  Removido botao Linktree do lead popup')

# 5. Footer - remover linktree
html = html.replace(
    '''          <a href="https://linktr.ee/RossoBurguerr?utm_source=linktree_profile_share&ltsid=20bdebfb-1d77-4994-8188-0dfec3befac3" target="_blank" rel="noopener" class="btn btn--outline newsletter-btn" style="display:inline-flex;align-items:center;justify-content:center;text-decoration:none;">LINKTREE</a>''',
    '',
    1
)
print('OK  Removido botao Linktree do footer')

# 6. Footer - remover mencao a Linktree no texto
html = html.replace(
    'Instagram oficial, Linktree com canais ativos e contato institucional em um bloco mais fiel à operação real da marca.',
    'Instagram oficial e contato institucional da marca.',
    1
)
print('OK  Footer texto corrigido')

# 7. Item modal - remover 99Food do item panel cta
html = html.replace(
    '''            <a href="https://linktr.ee/RossoBurguerr?utm_source=linktree_profile_share&ltsid=20bdebfb-1d77-4994-8188-0dfec3befac3" target="_blank" rel="noopener noreferrer" class="item-cta-secondary item-cta--99food">99FOOD</a>''',
    '',
    1
)
print('OK  Removido 99Food do item modal CTA')

# 8. Remover referencia ao partner card 99food na home (se existir)
linktree_url = 'https://linktr.ee/RossoBurguerr'
remaining = html.count(linktree_url)
if remaining > 0:
    print(f'!! ATENCAO: ainda existem {remaining} ocorrencias de linktr.ee')
else:
    print('OK  Nenhum linktr.ee restante no arquivo')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

new_len = len(html)
print(f'\nArquivo salvo. {original_len} -> {new_len} chars ({original_len - new_len} chars removidos)')
