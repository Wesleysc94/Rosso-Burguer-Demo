import { motion } from 'motion/react';
import { ChevronRight } from 'lucide-react';

export default function Home({ setCurrentPage }: { setCurrentPage: (page: string) => void }) {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="w-full"
    >
      {/* Hero Section */}
      <section className="relative min-h-[90vh] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 bg-black">
          <img
            src="https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&q=80&w=2000"
            alt="Aura Burger Hero"
            className="w-full h-full object-cover opacity-40"
            referrerPolicy="no-referrer"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black via-black/50 to-transparent" />
          <div className="absolute inset-0 bg-gradient-to-r from-black via-black/30 to-transparent" />
        </div>

        <div className="relative z-10 w-full max-w-7xl mx-auto px-6 pt-20">
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="max-w-3xl"
          >
            <div className="inline-block border border-border bg-dark/50 backdrop-blur-sm px-4 py-2 mb-6">
              <span className="text-orange font-bold tracking-widest uppercase text-sm">
                Vila Madalena, SP
              </span>
            </div>
            <h1 className="text-6xl md:text-8xl lg:text-9xl font-oswald font-black text-white leading-[0.9] tracking-tighter mb-8 uppercase">
              O Hambúrguer <br />
              <span className="text-stroke-orange text-transparent">Com Alma</span> <br />
              Paulistana
            </h1>
            <p className="text-xl md:text-2xl text-gray mb-10 max-w-2xl font-light">
              Blend artesanal, ingredientes frescos e a energia caótica de São Paulo em cada mordida. 
              Esqueça o fast-food, sinta o sabor da nossa cidade.
            </p>
            <div className="flex flex-col sm:flex-row gap-6">
              <button
                onClick={() => setCurrentPage('menu')}
                className="bg-red hover:bg-orange text-white px-10 py-5 font-oswald font-bold uppercase tracking-widest text-lg transition-colors flex items-center justify-center gap-3 group"
              >
                Ver Cardápio <ChevronRight className="group-hover:translate-x-1 transition-transform" />
              </button>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Marquee */}
      <div className="bg-orange py-4 overflow-hidden border-y border-border flex items-center">
        <div className="marquee-container flex whitespace-nowrap">
          <div className="animate-marquee flex items-center">
            {[...Array(10)].map((_, i) => (
              <span key={i} className="text-black font-oswald font-black uppercase text-3xl tracking-widest mx-8 flex items-center gap-8">
                AURA BURGER <span className="w-3 h-3 bg-black rounded-full"></span>
              </span>
            ))}
          </div>
          <div className="animate-marquee flex items-center" aria-hidden="true">
            {[...Array(10)].map((_, i) => (
              <span key={i} className="text-black font-oswald font-black uppercase text-3xl tracking-widest mx-8 flex items-center gap-8">
                AURA BURGER <span className="w-3 h-3 bg-black rounded-full"></span>
              </span>
            ))}
          </div>
        </div>
      </div>

      {/* Featured Section */}
      <section className="py-32 bg-black bg-grid-lines">
        <div className="max-w-7xl mx-auto px-6">
          <div className="flex flex-col md:flex-row justify-between items-end mb-16 gap-6">
            <div>
              <h2 className="text-5xl md:text-7xl font-oswald font-black uppercase tracking-tighter text-white mb-4">
                Os Favoritos <br/><span className="text-red">da Casa</span>
              </h2>
              <p className="text-gray text-lg max-w-md">
                Aqueles que fizeram nossa história. Se é sua primeira vez, comece por aqui.
              </p>
            </div>
            <button
              onClick={() => setCurrentPage('menu')}
              className="text-white border-b-2 border-orange pb-1 font-oswald font-bold uppercase tracking-widest hover:text-orange transition-colors"
            >
              Ver Menu Completo
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Featured Item 1 */}
            <div className="group relative bg-card border border-border overflow-hidden">
              <div className="aspect-[4/3] overflow-hidden">
                <img 
                  src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&q=80&w=1000" 
                  alt="Aura Clássico" 
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-80 group-hover:opacity-100"
                  referrerPolicy="no-referrer"
                />
              </div>
              <div className="p-8 relative z-10 bg-gradient-to-t from-card via-card to-transparent -mt-20 pt-24">
                <div className="flex justify-between items-start mb-4">
                  <h3 className="text-3xl font-oswald font-black uppercase tracking-tight text-white">Aura Clássico</h3>
                  <span className="text-2xl font-oswald font-bold text-orange">R$ 36</span>
                </div>
                <p className="text-gray mb-6">
                  Pão brioche artesanal, blend 160g de costela, queijo prato derretido, alface americana, tomate e nossa maionese verde secreta.
                </p>
              </div>
            </div>

            {/* Featured Item 2 */}
            <div className="group relative bg-card border border-border overflow-hidden">
              <div className="aspect-[4/3] overflow-hidden">
                <img 
                  src="https://images.unsplash.com/photo-1594212691516-436f8f6c582f?auto=format&fit=crop&q=80&w=1000" 
                  alt="Duplo Cheddar Bacon" 
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-80 group-hover:opacity-100"
                  referrerPolicy="no-referrer"
                />
              </div>
              <div className="p-8 relative z-10 bg-gradient-to-t from-card via-card to-transparent -mt-20 pt-24">
                <div className="flex justify-between items-start mb-4">
                  <h3 className="text-3xl font-oswald font-black uppercase tracking-tight text-white">Duplo Cheddar</h3>
                  <span className="text-2xl font-oswald font-bold text-orange">R$ 48</span>
                </div>
                <p className="text-gray mb-6">
                  Pão australiano, dois blends 160g, muito cheddar cremoso, fatias de bacon crocante e cebola caramelizada.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </motion.div>
  );
}
