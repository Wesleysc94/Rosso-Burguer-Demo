import { Instagram, Facebook, Mail } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-dark border-t border-border pt-16 pb-8">
      <div className="max-w-7xl mx-auto px-6">
        {/* Main grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-12 mb-12 pb-12 border-b border-border">

          {/* Brand */}
          <div className="md:col-span-1 flex flex-col gap-5">
            <img
              src="/assets/rosso/logo-oficial.jpeg"
              alt="Rosso Burguer"
              className="w-20 h-20 rounded-full object-cover border border-border"
            />
            <p className="font-oswald font-bold text-white text-xl uppercase tracking-tight leading-snug max-w-[220px]">
              "O Hambúrguer Artesanal com a Tradição Italiana"
            </p>
            <div className="flex gap-3">
              <a
                href="https://www.instagram.com/rossoburguer"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Instagram Rosso Burguer"
                className="w-10 h-10 rounded-full bg-card border border-border flex items-center justify-center hover:bg-green hover:border-green text-white transition-all"
              >
                <Instagram size={18} />
              </a>
              <a
                href="https://www.facebook.com/rossoburguer"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Facebook Rosso Burguer"
                className="w-10 h-10 rounded-full bg-card border border-border flex items-center justify-center hover:bg-green hover:border-green text-white transition-all"
              >
                <Facebook size={18} />
              </a>
            </div>
          </div>

          {/* Links rápidos */}
          <div>
            <h4 className="font-oswald font-bold uppercase tracking-widest text-white mb-5 text-sm">
              Links Rápidos
            </h4>
            <ul className="space-y-3 text-gray text-sm">
              <li>
                <button
                  onClick={() => document.getElementById('unidades')?.scrollIntoView({ behavior: 'smooth' })}
                  className="hover:text-white transition-colors uppercase tracking-widest font-bold text-xs"
                >
                  Lojas
                </button>
              </li>
              <li>
                <a
                  href="https://rossoburguer.com.br"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="hover:text-white transition-colors uppercase tracking-widest font-bold text-xs"
                >
                  Site Oficial
                </a>
              </li>
              <li>
                <a
                  href="https://linktr.ee/RossoBurguerr"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="hover:text-white transition-colors uppercase tracking-widest font-bold text-xs"
                >
                  Linktree
                </a>
              </li>
            </ul>
          </div>

          {/* Contato */}
          <div>
            <h4 className="font-oswald font-bold uppercase tracking-widest text-white mb-5 text-sm">
              Contato
            </h4>
            <ul className="space-y-4 text-gray text-sm">
              <li className="flex items-center gap-3">
                <Mail size={16} className="text-green shrink-0" />
                <a
                  href="mailto:contato@rossoburguer.com.br"
                  className="hover:text-white transition-colors"
                >
                  contato@rossoburguer.com.br
                </a>
              </li>
              <li className="flex items-center gap-3">
                <Mail size={16} className="text-green shrink-0" />
                <a
                  href="mailto:rh@rossoburguer.com.br"
                  className="hover:text-white transition-colors"
                >
                  rh@rossoburguer.com.br
                </a>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom bar */}
        <div className="flex flex-col md:flex-row justify-between items-center gap-3 text-gray text-xs">
          <p>&copy; 2026 Rosso Burguer · Since 2017 · Todos os direitos reservados.</p>
          <p className="text-gray/50">São Paulo &amp; Jundiaí · SP</p>
        </div>
      </div>
    </footer>
  );
}
