#!/usr/bin/env python3
"""
Complete fix for Rosso Burguer Demo — fixes ALL remaining issues after adapt_rosso.py.
Run: python fix_rosso_complete.py
"""
import re

FILE = r"C:\Users\wesle\.gemini\antigravity\scratch\Rosso burguer demo\Rosso-Burguer-Demo\index.html"

with open(FILE, "r", encoding="utf-8") as f:
    html = f.read()

# ═══════════════════════════════════════════════════════════════════════════════
# 1. FIX BROKEN DOUBLE-SLASH IMAGE URLS
#    The previous script replaced "photo-XXX?w=..." with "/assets/rosso/..."
#    but left the "https://images.unsplash.com/" prefix, creating broken URLs.
# ═══════════════════════════════════════════════════════════════════════════════
html = html.replace("https://images.unsplash.com//assets/rosso/", "/assets/rosso/")

# ═══════════════════════════════════════════════════════════════════════════════
# 2. FIX CSS VARIABLE — rename --orange to proper semantic name
# ═══════════════════════════════════════════════════════════════════════════════
# Keep --orange as alias but add --green as primary
html = html.replace(
    "--orange: #2d6a4f;  /* verde musgo Rosso */",
    "--orange: #2d6a4f;  /* kept as alias */\n      --green: #2d6a4f;\n      --green-hover: #245c43;"
)

# ═══════════════════════════════════════════════════════════════════════════════
# 3. FIX MENUDATA — replace ALL Unsplash URLs with Rosso local images
#    and update item names/descriptions to Rosso identity
# ═══════════════════════════════════════════════════════════════════════════════
NEW_MENU_DATA = """    const menuData = [
      {
        id:'rosso-classico', category:'hamburguer', catLabel:'HAMBÚRGUER',
        name:'Rosso Clássico', tagline:'O clássico que fez a nossa história.',
        image:'/assets/rosso/hero-dois-lanches.jpeg',
        badge:{label:'MAIS PEDIDO',type:'top'},
        desc:'Pão brioche artesanal, blend 160g na parrilla à lenha, queijo prato derretido, alface americana, tomate e nossa maionese secreta.',
        ingredients:['Pão Brioche','Blend 160g Parrilla','Queijo Prato','Alface Americana','Tomate','Maionese Secreta'],
        extras:[{name:'Bacon Crocante',price:6},{name:'Cheddar Extra',price:4},{name:'Ovo Caipira',price:4}],
        price:36, kcal:780, prepTime:'12 min', rating:4.9, reviews:2847, popular:true, isNew:false
      },
      {
        id:'duplo-cheddar', category:'hamburguer', catLabel:'HAMBÚRGUER',
        name:'Duplo Cheddar', tagline:'Dois blends. Cheddar que escorre.',
        image:'/assets/rosso/lanche-queijo.jpeg',
        badge:null,
        desc:'Pão australiano, dois blends 160g na parrilla, muito cheddar cremoso, fatias de bacon crocante e cebola caramelizada.',
        ingredients:['Pão Australiano','2× Blend 160g','Cheddar Cremoso','Bacon Crocante','Cebola Caramelizada'],
        extras:[{name:'Bacon Extra',price:6},{name:'Cheddar Extra',price:4},{name:'Picles',price:2}],
        price:48, kcal:1020, prepTime:'14 min', rating:4.8, reviews:1923, popular:false, isNew:false
      },
      {
        id:'smash-rosso', category:'hamburguer', catLabel:'HAMBÚRGUER',
        name:'Smash Rosso', tagline:'Crocante por fora. Suculento por dentro.',
        image:'/assets/rosso/lanche-01.jpeg',
        badge:{label:'NOVO',type:'novo'},
        desc:'Pão de batata, dois smash burgers 90g na parrilla, american cheese, picles e mostarda artesanal.',
        ingredients:['Pão de Batata','2× Smash 90g Parrilla','American Cheese','Picles','Mostarda Artesanal'],
        extras:[{name:'Bacon Crocante',price:6},{name:'Jalapeño',price:3},{name:'Molho Rosso Extra',price:2}],
        price:34, kcal:720, prepTime:'10 min', rating:4.7, reviews:842, popular:false, isNew:true
      },
      {
        id:'rosso-especial', category:'hamburguer', catLabel:'HAMBÚRGUER',
        name:'Rosso Especial', tagline:'O mais completo da nossa parrilla.',
        image:'/assets/rosso/lanche-02.jpeg',
        badge:{label:'ESPECIAL',type:'especial'},
        desc:'Pão brioche artesanal, blend 200g wagyu na parrilla, queijo brie, rúcula, cebola caramelizada e molho especial Rosso.',
        ingredients:['Pão Brioche','Blend 200g Wagyu','Queijo Brie','Rúcula','Cebola Caramelizada','Molho Rosso'],
        extras:[{name:'Bacon Extra',price:6},{name:'Trufa',price:10},{name:'Ovo Caipira',price:4}],
        price:54, kcal:960, prepTime:'16 min', rating:4.9, reviews:678, popular:false, isNew:false
      },
      {
        id:'rosso-bacon', category:'hamburguer', catLabel:'HAMBÚRGUER',
        name:'Rosso Bacon', tagline:'Pra quem gosta de intensidade.',
        image:'/assets/rosso/lanche-queijo.jpeg',
        badge:null,
        desc:'Pão rústico, blend 160g na parrilla, creme de cheddar, fatias generosas de bacon e molho defumado.',
        ingredients:['Pão Rústico','Blend 160g Parrilla','Creme Cheddar','Bacon Generoso','Molho Defumado'],
        extras:[{name:'Bacon Extra',price:6},{name:'Jalapeño',price:3},{name:'Cheddar Extra',price:4}],
        price:42, kcal:890, prepTime:'12 min', rating:4.8, reviews:1102, popular:false, isNew:false
      },
      {
        id:'rosso-frango', category:'hamburguer', catLabel:'HAMBÚRGUER',
        name:'Rosso Frango', tagline:'Leveza com a assinatura Rosso.',
        image:'/assets/rosso/lanche-01.jpeg',
        badge:null,
        desc:'Pão brioche, filé de frango empanado artesanal, queijo prato, alface, tomate e maionese de ervas.',
        ingredients:['Pão Brioche','Frango Empanado Artesanal','Queijo Prato','Alface','Tomate','Maionese de Ervas'],
        extras:[{name:'Bacon Crocante',price:6},{name:'Cheddar Extra',price:4},{name:'Abacaxi Grelhado',price:3}],
        price:38, kcal:680, prepTime:'12 min', rating:4.6, reviews:514, popular:false, isNew:false
      },
      {
        id:'fritas-rosso', category:'acompanhamento', catLabel:'ACOMPANHAMENTO',
        name:'Fritas Rosso', tagline:'Crocantes. Temperadas. Irresistíveis.',
        image:'/assets/rosso/batata-frita.jpeg',
        badge:{label:'MAIS PEDIDO',type:'top'},
        desc:'Batatas rústicas com casca, temperadas com sal grosso e ervas. Crocantes por fora, macias por dentro.',
        ingredients:['Batata Rústica com Casca','Sal Grosso','Ervas Frescas','Azeite'],
        extras:[{name:'Cheddar Cremoso',price:6},{name:'Bacon Bits',price:4},{name:'Cebola Crispy',price:3}],
        price:18, kcal:380, prepTime:'8 min', rating:4.8, reviews:3421, popular:true, isNew:false
      },
      {
        id:'fritas-cheddar', category:'acompanhamento', catLabel:'ACOMPANHAMENTO',
        name:'Fritas com Cheddar', tagline:'Nossa frita favorita, no próximo nível.',
        image:'/assets/rosso/batata-cheddar.jpeg',
        badge:null,
        desc:'Nossas fritas cobertas com molho de cheddar cremoso e bacon bits crocante.',
        ingredients:['Batata Rústica','Molho Cheddar','Bacon Bits','Cebolinha'],
        extras:[{name:'Jalapeño',price:3},{name:'Bacon Extra',price:4},{name:'Cebola Crispy',price:3}],
        price:26, kcal:580, prepTime:'10 min', rating:4.7, reviews:1876, popular:false, isNew:false
      },
      {
        id:'onion-rings', category:'acompanhamento', catLabel:'ACOMPANHAMENTO',
        name:'Onion Rings', tagline:'Empanados na hora, sem perdão.',
        image:'/assets/rosso/batata-frita.jpeg',
        badge:null,
        desc:'Anéis de cebola empanados artesanalmente, servidos com molho aioli da casa.',
        ingredients:['Cebola Doce','Empanado Artesanal','Molho Aioli da Casa'],
        extras:[{name:'Molho BBQ',price:3},{name:'Aioli Extra',price:2}],
        price:22, kcal:420, prepTime:'8 min', rating:4.6, reviews:965, popular:false, isNew:false
      },
      {
        id:'shake-baunilha', category:'bebida', catLabel:'BEBIDA',
        name:'Shake de Baunilha', tagline:'Feito na hora. Cremoso sem limites.',
        image:'/assets/rosso/batata-cheddar.jpeg',
        badge:{label:'MAIS PEDIDO',type:'top'},
        desc:'Milkshake cremoso feito na hora com sorvete artesanal de baunilha madagáscar.',
        ingredients:['Sorvete Baunilha Madagáscar','Leite Integral','Chantilly'],
        extras:[{name:'Calda de Chocolate',price:3},{name:'Granola',price:2}],
        price:22, kcal:460, prepTime:'5 min', rating:4.8, reviews:2108, popular:true, isNew:false
      },
      {
        id:'shake-chocolate', category:'bebida', catLabel:'BEBIDA',
        name:'Shake de Chocolate', tagline:'Intenso. Denso. Memorável.',
        image:'/assets/rosso/batata-cheddar.jpeg',
        badge:null,
        desc:'Milkshake denso de chocolate belga 70% com sorvete artesanal. Intenso e cremoso.',
        ingredients:['Chocolate Belga 70%','Sorvete Artesanal','Leite Integral','Chantilly'],
        extras:[{name:'Nutella',price:5},{name:'Granola',price:2}],
        price:22, kcal:510, prepTime:'5 min', rating:4.7, reviews:1543, popular:false, isNew:false
      },
      {
        id:'limonada', category:'bebida', catLabel:'BEBIDA',
        name:'Limonada da Casa', tagline:'Fresca. Cremosa. Refrescante.',
        image:'/assets/rosso/batata-frita.jpeg',
        badge:null,
        desc:'Limonada suíça feita na hora, cremosa, no ponto certo de doce e azedo.',
        ingredients:['Limão Tahiti','Leite Condensado','Água com Gás','Hortelã'],
        extras:[{name:'Dose de Gim',price:12},{name:'Hortelã Extra',price:2}],
        price:14, kcal:180, prepTime:'4 min', rating:4.7, reviews:2234, popular:false, isNew:false
      },
      {
        id:'brownie', category:'sobremesa', catLabel:'SOBREMESA',
        name:'Brownie Quente', tagline:'Quente, derretendo, com sorvete. Ponto.',
        image:'/assets/rosso/batata-cheddar.jpeg',
        badge:null,
        desc:'Brownie de chocolate belga aquecido, servido com sorvete de creme e calda de caramelo.',
        ingredients:['Chocolate Belga','Sorvete de Creme','Calda de Caramelo','Nozes Trituradas'],
        extras:[{name:'Sorvete Extra',price:6},{name:'Calda de Chocolate',price:3}],
        price:19, kcal:560, prepTime:'6 min', rating:4.8, reviews:876, popular:false, isNew:false
      },
      {
        id:'sundae', category:'sobremesa', catLabel:'SOBREMESA',
        name:'Sundae Rosso', tagline:'Clássico demais para ser ignorado.',
        image:'/assets/rosso/batata-cheddar.jpeg',
        badge:null,
        desc:'Sorvete artesanal com cobertura quente de chocolate, granola crocante e chantilly.',
        ingredients:['Sorvete Artesanal','Cobertura de Chocolate Quente','Granola Crocante','Chantilly'],
        extras:[{name:'Calda de Caramelo',price:3},{name:'Amendoim',price:2}],
        price:16, kcal:420, prepTime:'5 min', rating:4.6, reviews:621, popular:false, isNew:false
      },
    ];"""

html = re.sub(
    r'/\* ── MENU DATA ── \*/\s*const menuData = \[.*?\];',
    '/* ── MENU DATA ── */\n    ' + NEW_MENU_DATA,
    html, flags=re.DOTALL
)

# ═══════════════════════════════════════════════════════════════════════════════
# 4. FIX CARREIRAS PAGE — "ENTRE PARA O AURA" → Rosso
# ═══════════════════════════════════════════════════════════════════════════════
html = html.replace(
    'ENTRE PARA<br>O <span class="text-red">AURA.</span>',
    'TRAMPE NO<br><span class="text-red">ROSSO.</span>'
)
html = html.replace(
    'Se você gosta de operação bem feita, atendimento forte, cozinha viva e ritmo alto, queremos conhecer seu perfil. Preencha sua candidatura, anexe seu currículo e candidate-se para oportunidades no Rosso Burguer.',
    'Se você gosta de ritmo intenso, parrilla viva e time de verdade, o Rosso é o seu lugar. Preencha sua candidatura e faça parte da família Rosso Burguer.'
)
# Fix careers badge still referencing old content
html = html.replace('RH ROSSO BURGUER', 'TRAMPE NO ROSSO')

# ═══════════════════════════════════════════════════════════════════════════════
# 5. FIX DELIVERY PAGE — remove Rappi, Keeta, 99Food; keep iFood + WhatsApp
# ═══════════════════════════════════════════════════════════════════════════════
DELIVERY_PAGE_NEW = '''  <div id="page-delivery" class="spa-page">
    <div class="subpage-hero" style="min-height:40vh;background:linear-gradient(160deg,#0a0a0a 0%,#111 60%,#1a0a0a 100%);display:flex;align-items:center;justify-content:center;text-align:center;padding:120px 24px 60px;">
      <div>
        <span class="eyebrow">DELIVERY</span>
        <h1 class="section-title" style="font-size:clamp(56px,8vw,100px);margin-bottom:16px;">PEÇA ONDE<br><span class="text-red">ESTIVER.</span></h1>
        <p style="color:var(--gray-1);font-size:17px;max-width:480px;margin:0 auto;">Rosso Burguer disponível pelo iFood ou direto pelo WhatsApp. Escolha sua unidade.</p>
      </div>
    </div>

    <section class="section" style="background:var(--surface-1);">
      <div class="container">
        <div class="section-header-center reveal" style="margin-bottom:48px;">
          <span class="eyebrow">PLATAFORMAS</span>
          <h2 class="section-title-xl">COMO PEDIR.</h2>
        </div>

        <div style="display:grid;grid-template-columns:1fr;gap:24px;max-width:800px;margin:0 auto 80px;">
          <!-- iFood -->
          <div class="partner-card reveal" data-brand="ifood" style="background:rgba(15,15,15,0.8);border:1px solid rgba(255,255,255,0.06);padding:40px;display:grid;grid-template-columns:80px 1fr auto;gap:32px;align-items:center;">
            <div style="width:80px;height:80px;background:#EA1D2C;display:flex;align-items:center;justify-content:center;font-weight:900;font-family:var(--font-display);font-size:11px;letter-spacing:0.1em;color:white;text-align:center;">iFOOD</div>
            <div>
              <h3 style="font-family:var(--font-display);font-size:24px;font-weight:900;text-transform:uppercase;color:white;margin-bottom:8px;">iFood</h3>
              <p style="color:var(--gray-1);font-size:14px;line-height:1.6;">Maior cobertura de São Paulo e Jundiaí · Entrega em até 45 min · Rastreamento em tempo real</p>
            </div>
            <a href="#unidades" onclick="showPage('home');setTimeout(()=>document.getElementById('unidades').scrollIntoView({behavior:'smooth'}),100);return false;" class="btn btn--primary" style="white-space:nowrap;">VER LOJAS →</a>
          </div>

          <!-- WhatsApp Direto -->
          <div class="partner-card reveal" data-delay="1" style="background:rgba(15,15,15,0.8);border:1px solid rgba(255,255,255,0.06);padding:40px;display:grid;grid-template-columns:80px 1fr auto;gap:32px;align-items:center;">
            <div style="width:80px;height:80px;background:#25D366;display:flex;align-items:center;justify-content:center;">
              <svg viewBox="0 0 24 24" width="36" height="36" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            </div>
            <div>
              <h3 style="font-family:var(--font-display);font-size:24px;font-weight:900;text-transform:uppercase;color:white;margin-bottom:8px;">WhatsApp Direto</h3>
              <p style="color:var(--gray-1);font-size:14px;line-height:1.6;">Peça diretamente com a nossa equipe · Atendimento personalizado · Resposta rápida</p>
            </div>
            <a href="#unidades" onclick="showPage('home');setTimeout(()=>document.getElementById('unidades').scrollIntoView({behavior:'smooth'}),100);return false;" class="btn btn--outline" style="white-space:nowrap;">VER LOJAS →</a>
          </div>
        </div>

        <!-- How it works -->
        <div class="how-it-works reveal" style="border-top:1px solid var(--border);padding-top:60px;">
          <h2 class="how-title">COMO FUNCIONA.</h2>
          <p class="how-sub">Do pedido ao seu prato, em minutos.</p>
          <div class="steps-grid" style="grid-template-columns:repeat(3,1fr);">
            <div class="step-item">
              <div class="step-num">01</div>
              <h3 class="step-title">Escolha a Unidade</h3>
              <p class="step-body">Clique em "Ver Lojas" e escolha a unidade mais próxima de você.</p>
            </div>
            <div class="step-item">
              <div class="step-num">02</div>
              <h3 class="step-title">Faça o Pedido</h3>
              <p class="step-body">Peça pelo WhatsApp ou acesse nosso iFood direto pela unidade.</p>
            </div>
            <div class="step-item">
              <div class="step-num">03</div>
              <h3 class="step-title">Receba em Casa</h3>
              <p class="step-body">Seu Rosso Burguer preparado na parrilla chega quentinho até você.</p>
            </div>
          </div>
        </div>

      </div>
    </section>
  </div><!-- END DELIVERY -->'''

html = re.sub(
    r'<!-- PAGE: DELIVERY -->.*?<!-- END DELIVERY -->',
    DELIVERY_PAGE_NEW,
    html, flags=re.DOTALL
)

# ═══════════════════════════════════════════════════════════════════════════════
# 6. FIX PAGE-UNIDADES — replace with 5 real Rosso units
# ═══════════════════════════════════════════════════════════════════════════════
UNIDADES_PAGE_NEW = '''  <!-- PAGE: UNIDADES -->
  <div id="page-unidades" class="spa-page">
    <div class="subpage-hero" style="min-height:40vh;background:linear-gradient(160deg,#0a0a0a 0%,#0f0f0f 60%,#1a0a0a 100%);display:flex;align-items:center;justify-content:center;text-align:center;padding:120px 24px 60px;">
      <div>
        <span class="eyebrow">NOSSAS LOJAS</span>
        <h1 class="section-title" style="font-size:clamp(56px,8vw,100px);margin-bottom:16px;">NOS ENCONTRE.</h1>
        <p style="color:var(--gray-1);font-size:17px;max-width:480px;margin:0 auto;">5 unidades em São Paulo e Jundiaí. Peça direto ou pelo iFood.</p>
      </div>
    </div>

    <section class="section" style="background:var(--black);">
      <div class="container">
        <div style="display:grid;grid-template-columns:1fr;gap:20px;margin-bottom:60px;">

          <!-- Unit 1 -->
          <div class="unit-card reveal" data-delay="1" style="display:grid;grid-template-columns:1fr auto;gap:24px;align-items:start;padding:40px;">
            <div class="unit-content" style="position:relative;z-index:1;">
              <div class="unit-status" style="margin-bottom:12px;position:static;"><span class="status-dot status--live"></span><span>DISPONÍVEL</span></div>
              <h3 class="unit-name">SHOPPING ANÁLIA FRANCO</h3>
              <address class="unit-address">Praça de Alimentação – Av. Reg. Feijó, 1739<br>Vila Reg. Feijó, São Paulo – SP · 03342-900</address>
            </div>
            <div class="unit-number" aria-hidden="true" style="position:static;font-size:80px;opacity:0.04;">01</div>
            <div style="display:flex;gap:12px;grid-column:1/-1;padding-top:20px;border-top:1px solid rgba(255,255,255,0.06);">
              <a href="https://wa.me/5511947936611?text=Ol%C3%A1!+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+Rosso+Burguer+An%C3%A1lia+Franco" target="_blank" rel="noopener" class="btn btn--primary" style="font-size:12px;padding:12px 24px;">PEDIR DIRETO →</a>
              <a href="https://www.ifood.com.br/delivery/sao-paulo-sp/rosso-burguer---analia-franco-vila-regente-feijo/c0221e7c-ccf1-4d1e-b66f-cf753365a7a0" target="_blank" rel="noopener" class="btn btn--outline" style="font-size:12px;padding:12px 24px;">IFOOD →</a>
            </div>
          </div>

          <!-- Unit 2 -->
          <div class="unit-card reveal" data-delay="2" style="display:grid;grid-template-columns:1fr auto;gap:24px;align-items:start;padding:40px;">
            <div class="unit-content" style="position:relative;z-index:1;">
              <div class="unit-status" style="margin-bottom:12px;position:static;"><span class="status-dot status--live"></span><span>DISPONÍVEL</span></div>
              <h3 class="unit-name">PARK SHOPPING SÃO CAETANO SUL</h3>
              <address class="unit-address">Praça de Alimentação – Alameda Terracota, 545<br>Cerâmica, São Caetano do Sul – SP · 09531-190</address>
            </div>
            <div class="unit-number" aria-hidden="true" style="position:static;font-size:80px;opacity:0.04;">02</div>
            <div style="display:flex;gap:12px;grid-column:1/-1;padding-top:20px;border-top:1px solid rgba(255,255,255,0.06);">
              <a href="https://wa.me/5511947921707?text=Ol%C3%A1!+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+Rosso+Burguer+S%C3%A3o+Caetano" target="_blank" rel="noopener" class="btn btn--primary" style="font-size:12px;padding:12px 24px;">PEDIR DIRETO →</a>
              <a href="https://www.ifood.com.br/delivery/sao-caetano-do-sul-sp/rosso-burguer---sao-caetano-ceramica/0f8f3a19-8e77-407d-8133-6a48b4295f20" target="_blank" rel="noopener" class="btn btn--outline" style="font-size:12px;padding:12px 24px;">IFOOD →</a>
            </div>
          </div>

          <!-- Unit 3 -->
          <div class="unit-card reveal" data-delay="3" style="display:grid;grid-template-columns:1fr auto;gap:24px;align-items:start;padding:40px;">
            <div class="unit-content" style="position:relative;z-index:1;">
              <div class="unit-status" style="margin-bottom:12px;position:static;"><span class="status-dot status--live"></span><span>DISPONÍVEL</span></div>
              <h3 class="unit-name">ROSSO BURGUER SAPOPEMBA</h3>
              <address class="unit-address">R. Adutora de Rio Claro, 151<br>Vila Primavera, São Paulo – SP · 03374-050</address>
            </div>
            <div class="unit-number" aria-hidden="true" style="position:static;font-size:80px;opacity:0.04;">03</div>
            <div style="display:flex;gap:12px;grid-column:1/-1;padding-top:20px;border-top:1px solid rgba(255,255,255,0.06);">
              <a href="https://wa.me/5511961809916?text=Ol%C3%A1!+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+Rosso+Burguer+Sapopemba" target="_blank" rel="noopener" class="btn btn--primary" style="font-size:12px;padding:12px 24px;">PEDIR DIRETO →</a>
              <a href="https://www.ifood.com.br/delivery/sao-paulo-sp/rosso-burguer-vila-primavera/55527464-4001-4f67-ae9f-597cfc75ca9b" target="_blank" rel="noopener" class="btn btn--outline" style="font-size:12px;padding:12px 24px;">IFOOD →</a>
            </div>
          </div>

          <!-- Unit 4 -->
          <div class="unit-card reveal" data-delay="4" style="display:grid;grid-template-columns:1fr auto;gap:24px;align-items:start;padding:40px;">
            <div class="unit-content" style="position:relative;z-index:1;">
              <div class="unit-status" style="margin-bottom:12px;position:static;"><span class="status-dot status--live"></span><span>DISPONÍVEL</span></div>
              <h3 class="unit-name">JUNDIAÍ SHOPPING</h3>
              <address class="unit-address">Praça de Alimentação – Av. 9 de Julho, 3333<br>Anhangabaú, Jundiaí – SP</address>
            </div>
            <div class="unit-number" aria-hidden="true" style="position:static;font-size:80px;opacity:0.04;">04</div>
            <div style="display:flex;gap:12px;grid-column:1/-1;padding-top:20px;border-top:1px solid rgba(255,255,255,0.06);">
              <a href="https://wa.me/5511947925999?text=Ol%C3%A1!+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+Rosso+Burguer+Jundia%C3%AD" target="_blank" rel="noopener" class="btn btn--primary" style="font-size:12px;padding:12px 24px;">PEDIR DIRETO →</a>
              <a href="https://www.ifood.com.br/delivery/jundiai-sp/rosso-burguer---jundiai-anhangabau/16db2830-8f4f-414c-9554-1cafeb46af8b" target="_blank" rel="noopener" class="btn btn--outline" style="font-size:12px;padding:12px 24px;">IFOOD →</a>
            </div>
          </div>

          <!-- Unit 5 -->
          <div class="unit-card reveal" data-delay="5" style="display:grid;grid-template-columns:1fr auto;gap:24px;align-items:start;padding:40px;">
            <div class="unit-content" style="position:relative;z-index:1;">
              <div class="unit-status" style="margin-bottom:12px;position:static;"><span class="status-dot status--live"></span><span>DISPONÍVEL</span></div>
              <h3 class="unit-name">ROSSO BURGUER VILA PRUDENTE</h3>
              <address class="unit-address">São Paulo – SP</address>
            </div>
            <div class="unit-number" aria-hidden="true" style="position:static;font-size:80px;opacity:0.04;">05</div>
            <div style="display:flex;gap:12px;grid-column:1/-1;padding-top:20px;border-top:1px solid rgba(255,255,255,0.06);">
              <a href="https://wa.me/5511993471000?text=Ol%C3%A1!+Vi+no+site+e+gostaria+de+informa%C3%A7%C3%B5es+sobre+a+Rosso+Burguer+Vila+Prudente" target="_blank" rel="noopener" class="btn btn--primary" style="font-size:12px;padding:12px 24px;">PEDIR DIRETO →</a>
              <a href="https://www.ifood.com.br/delivery/sao-paulo-sp/rosso-burguer---vila-prudente-vila-prudente/d45b7eaa-a1b5-415e-b802-e73f2617e989" target="_blank" rel="noopener" class="btn btn--outline" style="font-size:12px;padding:12px 24px;">IFOOD →</a>
            </div>
          </div>

        </div>
      </div>
    </section>
  </div><!-- END UNIDADES -->'''

html = re.sub(
    r'<!-- PAGE: UNIDADES -->.*?<!-- END UNIDADES -->',
    UNIDADES_PAGE_NEW,
    html, flags=re.DOTALL
)

# ═══════════════════════════════════════════════════════════════════════════════
# 7. FIX STATS BAR — "25+" → "5"
# ═══════════════════════════════════════════════════════════════════════════════
html = html.replace('>25+<', '>5<')
html = html.replace('25+</div>', '5</div>')
html = html.replace(
    '>25+<span',
    '>5<span'
)
# Fix any stat labels referencing old count
html = html.replace('Mais de 25 unidades', '5 unidades')

# ═══════════════════════════════════════════════════════════════════════════════
# 8. FIX FOOTER — phone, hours, tagline
# ═══════════════════════════════════════════════════════════════════════════════
html = html.replace('(11) 99999-9999', 'contato@rossoburguer.com.br')
html = html.replace(
    'O hambúrguer com tradição italiana. Blend artesanal, ingredientes frescos, sem atalhos.',
    '"O Hambúrguer Artesanal com a Tradição Italiana." — Since 2017.'
)
# Remove hours from footer (Rosso hours vary per unit/shopping)
html = re.sub(
    r'<div>\s*<p class="footer-col-title"[^>]*>Horários</p>.*?</div>\s*</div>\s*</div>\s*<div class="footer-bottom">',
    '</div>\n        </div>\n        <div class="footer-bottom">',
    html, flags=re.DOTALL
)

# ═══════════════════════════════════════════════════════════════════════════════
# 9. ROSSO AESTHETIC ENHANCEMENTS — add Italian flag CSS, better color refs
# ═══════════════════════════════════════════════════════════════════════════════
ROSSO_EXTRA_CSS = """
    /* ═══ ROSSO BURGUER IDENTITY ═══ */

    /* Italian flag accent bar */
    .italian-bar {
      display: inline-block;
      height: 3px;
      width: 64px;
      background: linear-gradient(90deg, #009246 33.3%, #ffffff 33.3% 66.6%, #ce2b37 66.6%);
      margin-bottom: 24px;
    }

    /* Rosso green button override */
    .btn--green {
      background: var(--green, #2d6a4f);
      color: white;
      border: none;
    }
    .btn--green:hover {
      background: var(--green-hover, #245c43);
      transform: translateY(-2px);
      box-shadow: 0 8px 32px rgba(45,106,79,0.35);
    }

    /* Unit card action buttons full-width on mobile */
    @media (max-width: 640px) {
      .unit-card .unit-actions { flex-direction: column !important; }
      .unit-card .unit-actions a { justify-content: center; width: 100%; }
    }

    /* Partner card responsive fix */
    @media (max-width: 640px) {
      .partner-card[style*="grid-template-columns:80px"] {
        grid-template-columns: 60px 1fr !important;
        gap: 16px !important;
      }
      .partner-card[style*="grid-template-columns:80px"] a.btn {
        grid-column: 1 / -1;
        justify-content: center;
      }
    }

    /* WhatsApp float — Rosso green */
    .whatsapp-float {
      background: #25D366;
    }
    .whatsapp-float:hover {
      background: #1ebe5d;
      transform: scale(1.08);
    }

    /* Navbar scrolled border → red (was transparent) */
    .navbar.scrolled {
      border-bottom-color: var(--red) !important;
    }

    /* Footer logo image fit */
    .footer-logo img {
      border-radius: 50%;
      border: 1px solid rgba(255,255,255,0.1);
    }
"""

html = html.replace("</style>", ROSSO_EXTRA_CSS + "\n    </style>", 1)

# ═══════════════════════════════════════════════════════════════════════════════
# 10. FIX REMAINING STRAY REFERENCES
# ═══════════════════════════════════════════════════════════════════════════════
# Fix cardápio CTA section — remove Rappi/Keeta/99Food links
html = html.replace(
    'Disponível no iFood, Rappi, Keeta e 99Food.',
    'Disponível no iFood ou diretamente pelo WhatsApp.'
)
html = html.replace(
    'Via iFood, Rappi, Keeta ou 99Food',
    'Via iFood ou WhatsApp Direto'
)
# Fix mobile drawer "PEDIR AGORA" → goes to delivery page (fine as-is)
# Fix any "Vegano da Vila" still in card name
html = html.replace('VEGANO DA VILA', 'ROSSO ESPECIAL')
html = html.replace('Vegano da Vila', 'Rosso Especial')
# Fix editorial image alt
html = html.replace(
    'alt="Rosso Burguer — parrilla à lenha" loading="lazy">',
    'alt="Rosso Burguer — parrilla à lenha" loading="lazy" onerror="this.src=\'/assets/rosso/hero-dois-lanches.jpeg\'">'
)
# Fix history stats bar
html = html.replace(
    '<div class="stat-number">25+</div>',
    '<div class="stat-number">5</div>'
)
html = html.replace(
    '<div class="stat-label">Unidades</div>',
    '<div class="stat-label">Unidades em SP</div>'
)

# ═══════════════════════════════════════════════════════════════════════════════
# 11. FIX HISTORIA PAGE TIMELINE CONTENT
# ═══════════════════════════════════════════════════════════════════════════════
html = html.replace(
    'Dois amigos, uma chapa de aço e uma obsessão com carne boa.',
    'Uma parrilla à lenha, uma receita artesanal e uma obsessão com qualidade.'
)
html = html.replace(
    'Primeiro ponto na Vila Madalena, sem pretensão — só muito amor pelo hambúrguer.',
    'Primeiro ponto em São Paulo. Sem atalhos — só tradição italiana no smash burger.'
)
html = html.replace('Vila Madalena', 'São Paulo')

# Fix the "Pinheiros e Itaim" reference in timeline if still present
html = html.replace('PINHEIROS E ITAIM', 'EXPANSÃO SP')

# ═══════════════════════════════════════════════════════════════════════════════
# WRITE OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════
with open(FILE, "w", encoding="utf-8") as f:
    f.write(html)

lines = html.count('\n') + 1
print(f"Complete fix applied. {len(html):,} chars, {lines:,} lines.")

# Final audit
remaining_aura = [(i+1, l.strip()[:120]) for i,l in enumerate(html.split('\n'))
                  if 'aura' in l.lower() and '//' not in l and 'script' not in l.lower()
                  and 'unsplash' not in l.lower()]
if remaining_aura:
    print(f"\n⚠ {len(remaining_aura)} possible 'aura' references remaining:")
    for ln, text in remaining_aura[:10]:
        print(f"  L{ln}: {text}")
else:
    print("\n✅ Zero 'aura' references remaining.")

broken_imgs = [i+1 for i,l in enumerate(html.split('\n')) if 'unsplash.com//' in l]
if broken_imgs:
    print(f"\n⚠ {len(broken_imgs)} broken double-slash image URLs at lines: {broken_imgs[:5]}")
else:
    print("✅ No broken Unsplash double-slash URLs.")
