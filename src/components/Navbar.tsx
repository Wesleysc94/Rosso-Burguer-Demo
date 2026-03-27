import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Menu as MenuIcon, X } from 'lucide-react';

const navItems = [
  { id: 'home', label: 'Início' },
  { id: 'menu', label: 'Cardápio' },
  { id: 'sobre', label: 'Sobre Nós' },
  { id: 'contato', label: 'Contato' },
];

export default function Navbar({ currentPage, setCurrentPage }: { currentPage: string, setCurrentPage: (page: string) => void }) {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleNav = (id: string) => {
    setCurrentPage(id);
    setMobileMenuOpen(false);
    window.scrollTo(0, 0);
  };

  return (
    <>
      <header
        className={`fixed top-0 w-full z-50 transition-all duration-300 border-b ${
          isScrolled ? 'bg-black/90 backdrop-blur-md border-border py-4' : 'bg-transparent border-transparent py-6'
        }`}
      >
        <div className="max-w-7xl mx-auto px-6 flex justify-between items-center">
          <div 
            className="flex items-center gap-3 cursor-pointer group"
            onClick={() => handleNav('home')}
          >
            <div className="w-12 h-12 bg-red rounded-full flex items-center justify-center text-white font-oswald font-bold text-2xl tracking-tighter group-hover:scale-105 transition-transform">
              AB
            </div>
            <span className="text-3xl font-oswald font-black tracking-tight text-white uppercase">
              Aura Burger
            </span>
          </div>

          {/* Desktop Nav */}
          <nav className="hidden md:flex items-center gap-8">
            {navItems.map((item) => (
              <button
                key={item.id}
                onClick={() => handleNav(item.id)}
                className={`text-sm font-bold uppercase tracking-widest transition-colors ${
                  currentPage === item.id ? 'text-orange' : 'text-gray hover:text-white'
                }`}
              >
                {item.label}
              </button>
            ))}
            <button
              onClick={() => handleNav('menu')}
              className="bg-red hover:bg-orange text-white px-8 py-3 rounded-none font-oswald font-bold uppercase tracking-widest transition-colors text-sm"
            >
              Pedir Agora
            </button>
          </nav>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden text-white"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          >
            {mobileMenuOpen ? <X size={32} /> : <MenuIcon size={32} />}
          </button>
        </div>
      </header>

      {/* Mobile Menu */}
      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, y: '-100%' }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: '-100%' }}
            transition={{ type: 'tween', duration: 0.3 }}
            className="fixed inset-0 z-40 bg-dark pt-32 px-6 md:hidden border-b border-border"
          >
            <div className="flex flex-col gap-8 text-center">
              {navItems.map((item) => (
                <button
                  key={item.id}
                  onClick={() => handleNav(item.id)}
                  className={`text-4xl font-oswald font-black uppercase tracking-tight ${
                    currentPage === item.id ? 'text-orange' : 'text-white'
                  }`}
                >
                  {item.label}
                </button>
              ))}
              <button
                onClick={() => handleNav('menu')}
                className="mt-8 bg-red text-white px-8 py-5 font-oswald font-bold uppercase tracking-widest text-xl"
              >
                Fazer Pedido
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
