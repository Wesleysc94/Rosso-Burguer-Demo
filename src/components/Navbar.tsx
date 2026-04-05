'use client';
import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Menu as MenuIcon, X } from 'lucide-react';

const scrollTo = (id: string) => {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
};

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setIsScrolled(window.scrollY > 60);
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  return (
    <>
      <header
        className={`fixed top-0 w-full z-50 transition-all duration-300 border-b ${
          isScrolled
            ? 'bg-black/92 backdrop-blur-md border-border py-3'
            : 'bg-transparent border-transparent py-5'
        }`}
      >
        <div className="max-w-7xl mx-auto px-6 flex justify-between items-center">
          {/* Logo */}
          <button
            onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
            className="flex items-center gap-3 group"
            aria-label="Rosso Burguer — início"
          >
            <img
              src="/assets/rosso/logo-oficial.jpeg"
              alt="Rosso Burguer"
              className="w-12 h-12 rounded-full object-cover group-hover:scale-105 transition-transform duration-300 border border-border"
            />
            <span className="hidden sm:block text-2xl font-oswald font-bold tracking-tight text-white uppercase">
              Rosso Burguer
            </span>
          </button>

          {/* Desktop nav */}
          <nav className="hidden md:flex items-center gap-2">
            <button
              onClick={() => scrollTo('unidades')}
              className="px-5 py-2.5 text-sm font-bold uppercase tracking-widest text-white bg-green hover:bg-green-hover transition-colors"
            >
              Lojas
            </button>
            <a
              href="mailto:rh@rossoburguer.com.br"
              className="px-5 py-2.5 text-sm font-bold uppercase tracking-widest text-black bg-white hover:bg-gray/20 hover:text-white border border-white transition-colors"
            >
              Trampe no Rosso
            </a>
            <a
              href="mailto:contato@rossoburguer.com.br"
              className="px-5 py-2.5 text-sm font-bold uppercase tracking-widest text-white bg-red hover:bg-red/80 transition-colors"
            >
              Fale Conosco
            </a>
          </nav>

          {/* Mobile hamburger */}
          <button
            className="md:hidden text-white p-1"
            onClick={() => setMobileOpen(!mobileOpen)}
            aria-label="Menu"
          >
            {mobileOpen ? <X size={30} /> : <MenuIcon size={30} />}
          </button>
        </div>
      </header>

      {/* Mobile menu */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, y: '-100%' }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: '-100%' }}
            transition={{ type: 'tween', duration: 0.25 }}
            className="fixed inset-0 z-40 bg-dark flex flex-col items-center justify-center gap-6 md:hidden"
          >
            {/* Logo in mobile menu */}
            <img
              src="/assets/rosso/logo-oficial.jpeg"
              alt="Rosso Burguer"
              className="w-20 h-20 rounded-full object-cover border-2 border-green mb-4"
            />

            <button
              onClick={() => { scrollTo('unidades'); setMobileOpen(false); }}
              className="w-64 py-4 text-xl font-oswald font-bold uppercase tracking-widest text-white bg-green text-center"
            >
              Lojas
            </button>
            <a
              href="mailto:rh@rossoburguer.com.br"
              onClick={() => setMobileOpen(false)}
              className="w-64 py-4 text-xl font-oswald font-bold uppercase tracking-widest text-black bg-white text-center"
            >
              Trampe no Rosso
            </a>
            <a
              href="mailto:contato@rossoburguer.com.br"
              onClick={() => setMobileOpen(false)}
              className="w-64 py-4 text-xl font-oswald font-bold uppercase tracking-widest text-white bg-red text-center"
            >
              Fale Conosco
            </a>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
