'use client';
import { motion } from 'motion/react';
import { MapPin, MessageCircle, UtensilsCrossed } from 'lucide-react';

/* ─── Data ─────────────────────────────────────────────────────────────────── */

const TICKER_ITEMS = [
  'HAMBÚRGUER ARTESANAL COM TRADIÇÃO ITALIANA',
  'FEITO NA PARRILLA À LENHA',
  '5 UNIDADES EM SP E JUNDIAÍ',
  'SINCE 2017 · BENVENUTI',
  'PEÇA DIRETO OU PELO IFOOD',
];

const UNITS = [
  {
    name: 'Shopping Anália Franco',
    address: 'Praça de Alimentação – Av. Reg. Feijó, 1739\nVila Reg. Feijó, São Paulo – SP, 03342-900',
    whatsapp: 'https://wa.me/5511947936611?text=Olá!+Gostaria+de+informações+sobre+a+Rosso+Burguer+Anália+Franco',
    ifood: 'https://www.ifood.com.br/delivery/sao-paulo-sp/rosso-burguer---analia-franco-vila-regente-feijo/c0221e7c-ccf1-4d1e-b66f-cf753365a7a0',
  },
  {
    name: 'Park Shopping São Caetano Sul',
    address: 'Praça de Alimentação – Alameda Terracota, 545\nCerâmica, São Caetano do Sul – SP, 09531-190',
    whatsapp: 'https://wa.me/5511947921707?text=Olá!+Gostaria+de+informações+sobre+a+Rosso+Burguer+São+Caetano',
    ifood: 'https://www.ifood.com.br/delivery/sao-caetano-do-sul-sp/rosso-burguer---sao-caetano-ceramica/0f8f3a19-8e77-407d-8133-6a48b4295f20',
  },
  {
    name: 'Rosso Burguer Sapopemba',
    address: 'R. Adutora de Rio Claro, 151\nVila Primavera, São Paulo – SP, 03374-050',
    whatsapp: 'https://wa.me/5511961809916?text=Olá!+Gostaria+de+informações+sobre+a+Rosso+Burguer+Sapopemba',
    ifood: 'https://www.ifood.com.br/delivery/sao-paulo-sp/rosso-burguer-vila-primavera/55527464-4001-4f67-ae9f-597cfc75ca9b',
  },
  {
    name: 'Jundiaí Shopping',
    address: 'Praça de Alimentação – Av. 9 de Julho, 3333\nAnhangabaú, Jundiaí – SP',
    whatsapp: 'https://wa.me/5511947925999?text=Olá!+Gostaria+de+informações+sobre+a+Rosso+Burguer+Jundiaí',
    ifood: 'https://www.ifood.com.br/delivery/jundiai-sp/rosso-burguer---jundiai-anhangabau/16db2830-8f4f-414c-9554-1cafeb46af8b',
  },
  {
    name: 'Rosso Burguer Vila Prudente',
    address: 'São Paulo – SP',
    whatsapp: 'https://wa.me/5511993471000?text=Olá!+Vi+no+site+e+gostaria+de+informações+sobre+a+Rosso+Burguer+Vila+Prudente',
    ifood: 'https://www.ifood.com.br/delivery/sao-paulo-sp/rosso-burguer---vila-prudente-vila-prudente/d45b7eaa-a1b5-415e-b802-e73f2617e989',
  },
];

const PHOTOS = [
  { src: '/assets/rosso/lanche-queijo.jpeg', label: 'Smash Clássico' },
  { src: '/assets/rosso/lanche-02.jpeg',    label: 'Rosso Especial' },
  { src: '/assets/rosso/lanche-01.jpeg',    label: 'Black Skull' },
  { src: '/assets/rosso/batata-frita.jpeg', label: 'Fritas na Parrilla' },
  { src: '/assets/rosso/batata-cheddar.jpeg', label: 'Fritas Cheddar' },
];

/* ─── Ticker strip (memoised to avoid re-renders) ─────────────────────────── */
function Ticker() {
  const repeated = [...TICKER_ITEMS, ...TICKER_ITEMS];
  return (
    <div className="bg-green py-4 overflow-hidden border-y border-border flex items-center" aria-hidden="true">
      <div className="marquee-track whitespace-nowrap flex">
        {repeated.map((item, i) => (
          <span
            key={i}
            className="text-white font-oswald font-bold uppercase text-2xl md:text-3xl tracking-widest mx-8 flex items-center gap-8"
          >
            {item}
            <span className="w-2.5 h-2.5 bg-white/50 rounded-full shrink-0" />
          </span>
        ))}
      </div>
    </div>
  );
}

/* ─── Unit card ────────────────────────────────────────────────────────────── */
type UnitCardProps = { unit: { name: string; address: string; whatsapp: string; ifood: string }; index: number; key?: string | number };
function UnitCard({ unit, index }: UnitCardProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 32 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ duration: 0.5, delay: index * 0.08 }}
      className="bg-card border border-border p-8 flex flex-col gap-6"
    >
      {/* Name */}
      <div className="border-b border-border pb-4">
        <h3 className="text-2xl md:text-3xl font-oswald font-bold text-white leading-tight">
          {unit.name.toUpperCase()}
        </h3>
      </div>

      {/* Address */}
      <div className="flex items-start gap-3 text-gray text-sm leading-relaxed">
        <MapPin size={18} className="text-green shrink-0 mt-0.5" />
        <span className="whitespace-pre-line">{unit.address}</span>
      </div>

      {/* CTAs */}
      <div className="flex flex-col gap-3 mt-auto">
        <a
          href={unit.whatsapp}
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center justify-center gap-2.5 bg-green hover:bg-green-hover text-white py-3.5 font-oswald font-bold uppercase tracking-widest text-sm transition-colors active:scale-[0.98]"
        >
          <MessageCircle size={18} />
          Pedir Direto
        </a>
        <a
          href={unit.ifood}
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center justify-center gap-2.5 border border-border hover:border-white/30 text-white py-3.5 font-oswald font-bold uppercase tracking-widest text-sm transition-colors active:scale-[0.98]"
        >
          <UtensilsCrossed size={18} />
          iFood
        </a>
      </div>
    </motion.div>
  );
}

/* ─── Home ─────────────────────────────────────────────────────────────────── */
export default function Home() {
  return (
    <div className="w-full">

      {/* ── Hero ────────────────────────────────────────────────────────────── */}
      <section className="relative min-h-[100dvh] flex items-end md:items-center overflow-hidden">
        {/* Background image */}
        <div className="absolute inset-0">
          <img
            src="/assets/rosso/hero-dois-lanches.jpeg"
            alt="Rosso Burguer — dois lanches na parrilla"
            className="w-full h-full object-cover opacity-50"
          />
          {/* Gradient — dark at bottom + left for text legibility */}
          <div className="absolute inset-0 bg-gradient-to-t from-black via-black/60 to-black/10" />
          <div className="absolute inset-0 bg-gradient-to-r from-black/90 via-black/40 to-transparent" />
        </div>

        {/* Content — left-aligned (taste-skill: anti-center bias) */}
        <div className="relative z-10 w-full max-w-7xl mx-auto px-6 pb-24 pt-32 md:pt-0">
          <motion.div
            initial={{ opacity: 0, y: 48 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.9, ease: [0.16, 1, 0.3, 1] }}
            className="max-w-2xl"
          >
            {/* Italian flag bar */}
            <div className="italian-bar h-1 w-20 mb-6" />

            <div className="inline-flex items-center gap-2 border border-border bg-black/50 backdrop-blur-sm px-4 py-2 mb-6">
              <img
                src="/assets/rosso/logo-oficial.jpeg"
                alt=""
                className="w-5 h-5 rounded-full object-cover"
              />
              <span className="text-green font-bold tracking-widest uppercase text-xs">
                Since 2017 · São Paulo &amp; Jundiaí
              </span>
            </div>

            <h1 className="text-5xl sm:text-7xl md:text-8xl font-oswald font-bold text-white leading-[0.92] tracking-tighter mb-6 uppercase">
              O Hambúrguer<br />
              Artesanal<br />
              <span className="text-stroke-red">Com a Tradição</span><br />
              <span className="text-red">Italiana.</span>
            </h1>

            <p className="text-lg md:text-xl text-gray mb-10 max-w-lg font-light leading-relaxed">
              Feito na parrilla à lenha. Sem atalhos.
            </p>

            <div className="flex flex-col sm:flex-row gap-4">
              <button
                onClick={() => document.getElementById('unidades')?.scrollIntoView({ behavior: 'smooth' })}
                className="bg-green hover:bg-green-hover text-white px-10 py-4 font-oswald font-bold uppercase tracking-widest text-base transition-colors active:scale-[0.98]"
              >
                Ver Lojas
              </button>
              <a
                href="https://www.instagram.com/rossoburguer"
                target="_blank"
                rel="noopener noreferrer"
                className="border border-border hover:border-white/30 text-white px-10 py-4 font-oswald font-bold uppercase tracking-widest text-base transition-colors text-center"
              >
                @rossoburguer
              </a>
            </div>
          </motion.div>
        </div>

        {/* Scroll cue */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.4, duration: 0.6 }}
          className="absolute bottom-8 right-8 hidden md:flex flex-col items-center gap-2"
        >
          <div className="w-px h-16 bg-gradient-to-b from-transparent to-green" />
          <span className="text-[10px] text-gray uppercase tracking-widest rotate-90 origin-center translate-y-4">Scroll</span>
        </motion.div>
      </section>

      {/* ── Ticker ──────────────────────────────────────────────────────────── */}
      <Ticker />

      {/* ── Gallery strip ───────────────────────────────────────────────────── */}
      <section className="py-20 bg-dark border-b border-border overflow-hidden">
        <div className="max-w-7xl mx-auto px-6 mb-12">
          <motion.h2
            initial={{ opacity: 0, x: -24 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="text-4xl md:text-6xl font-oswald font-bold text-white"
          >
            Feito na <span className="text-red">Parrilla</span>
          </motion.h2>
          <p className="text-gray mt-3 text-base max-w-md">
            Blend artesanal, ingredientes frescos e muito respeito pelo processo.
          </p>
        </div>

        {/* Horizontal scroll gallery */}
        <div className="flex gap-4 px-6 overflow-x-auto hide-scrollbar">
          {PHOTOS.map((photo, i) => (
            <motion.div
              key={photo.src}
              initial={{ opacity: 0, scale: 0.95 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: i * 0.07 }}
              className="shrink-0 group relative"
            >
              <div className="w-64 md:w-80 aspect-[3/4] overflow-hidden border border-border">
                <img
                  src={photo.src}
                  alt={photo.label}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-80 group-hover:opacity-100"
                />
              </div>
              <p className="mt-3 text-xs font-bold uppercase tracking-widest text-gray group-hover:text-white transition-colors">
                {photo.label}
              </p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* ── Units — "Faça Seu Pedido" ────────────────────────────────────────── */}
      <section id="unidades" className="py-28 bg-black bg-grid-lines">
        <div className="max-w-7xl mx-auto px-6">
          <div className="mb-16">
            <motion.div
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <div className="italian-bar h-1 w-16 mb-6" />
              <h2 className="text-5xl md:text-7xl font-oswald font-bold text-white mb-4">
                Faça Seu <span className="text-green">Pedido</span>
              </h2>
              <p className="text-gray text-lg max-w-lg">
                5 unidades para você. Peça direto pelo WhatsApp ou pelo iFood.
              </p>
            </motion.div>
          </div>

          {/* 5-unit grid — 2 cols then remaining centered */}
          <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
            {UNITS.map((unit, i) => (
              <UnitCard key={unit.name} unit={unit} index={i} />
            ))}
          </div>
        </div>
      </section>

      {/* ── Nossa História ───────────────────────────────────────────────────── */}
      <section className="py-28 bg-dark border-t border-border">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-center">
            {/* Text */}
            <motion.div
              initial={{ opacity: 0, x: -32 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.7 }}
            >
              <div className="italian-bar h-1 w-16 mb-6" />
              <h2 className="text-5xl md:text-6xl font-oswald font-bold text-white mb-10 leading-tight">
                Nossa <span className="text-red">História</span>
              </h2>

              {/* Timeline */}
              <div className="space-y-8 relative before:absolute before:left-2 before:top-3 before:bottom-3 before:w-px before:bg-border">
                {[
                  { year: '2017', text: 'Nascemos da paixão pela culinária italiana e pelo hambúrguer artesanal. A Rosso Burguer abriu suas portas com uma missão: trazer a tradição da parrilla à lenha para o smash burger paulistano.' },
                  { year: '2019', text: 'Expansão para o segundo endereço. A tradição que começou como uma ideia virou referência nos shoppings de São Paulo.' },
                  { year: '2022', text: 'Cruzamos fronteiras e chegamos a Jundiaí. A Rosso Burguer agora é orgulho de dois estados.' },
                  { year: 'Hoje', text: 'Com 5 unidades entre São Paulo e Jundiaí, seguimos o mesmo princípio: blend artesanal, ingredientes frescos e muito respeito pelo processo.' },
                ].map(({ year, text }) => (
                  <div key={year} className="pl-8 relative">
                    <div className="absolute left-0 top-1.5 w-4 h-4 rounded-full bg-green border-2 border-dark shrink-0" />
                    <span className="text-green font-oswald font-bold text-sm uppercase tracking-widest block mb-1">
                      {year}
                    </span>
                    <p className="text-gray leading-relaxed text-sm md:text-base">{text}</p>
                  </div>
                ))}
              </div>
            </motion.div>

            {/* Image composition */}
            <motion.div
              initial={{ opacity: 0, x: 32 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.7, delay: 0.15 }}
              className="relative"
            >
              {/* Main image */}
              <div className="aspect-[4/5] border border-border overflow-hidden">
                <img
                  src="/assets/rosso/hero-dois-lanches.jpeg"
                  alt="Rosso Burguer — lanches artesanais"
                  className="w-full h-full object-cover opacity-85"
                />
              </div>
              {/* Floating badge */}
              <div className="absolute -bottom-6 -left-6 bg-red px-6 py-4 border border-red">
                <p className="font-oswald font-bold text-white text-3xl leading-none">SINCE</p>
                <p className="font-oswald font-bold text-white text-5xl leading-none">2017</p>
              </div>
              {/* Accent logo */}
              <div className="absolute -top-6 -right-6 hidden lg:block">
                <img
                  src="/assets/rosso/logo-oficial.jpeg"
                  alt="Rosso Burguer"
                  className="w-20 h-20 rounded-full object-cover border-2 border-green"
                />
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* ── Final CTA banner ─────────────────────────────────────────────────── */}
      <section className="py-20 bg-red border-t border-red/50">
        <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-8">
          <div>
            <h2 className="text-4xl md:text-5xl font-oswald font-bold text-white leading-tight">
              Benvenuti.<br />
              <span className="text-white/70 text-2xl font-normal normal-case tracking-normal">
                Escolha a unidade mais próxima de você.
              </span>
            </h2>
          </div>
          <button
            onClick={() => document.getElementById('unidades')?.scrollIntoView({ behavior: 'smooth' })}
            className="shrink-0 bg-white hover:bg-gray/10 text-red px-12 py-5 font-oswald font-bold uppercase tracking-widest text-lg transition-colors active:scale-[0.98]"
          >
            Ver Lojas
          </button>
        </div>
      </section>
    </div>
  );
}
