import { motion } from 'motion/react';

export default function Sobre() {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="w-full bg-black"
    >
      {/* Hero Sobre */}
      <section className="relative h-[60vh] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 bg-black">
          <img
            src="https://images.unsplash.com/photo-1586816001966-79b736744398?auto=format&fit=crop&q=80&w=2000"
            alt="Aura Burger Chapa"
            className="w-full h-full object-cover opacity-30 grayscale"
            referrerPolicy="no-referrer"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black to-transparent" />
        </div>
        <div className="relative z-10 text-center px-6">
          <h1 className="text-6xl md:text-8xl font-oswald font-black uppercase tracking-tighter text-white mb-4">
            Nossa <span className="text-red">História</span>
          </h1>
          <p className="text-xl text-gray max-w-2xl mx-auto font-light">
            Da garagem na Zona Oeste para o coração da Vila Madalena.
          </p>
        </div>
      </section>

      {/* Content */}
      <section className="py-24 max-w-4xl mx-auto px-6">
        <div className="prose prose-invert prose-lg max-w-none">
          <h2 className="text-4xl font-oswald font-black uppercase tracking-tight text-white mb-8">
            A Obsessão pela Perfeição
          </h2>
          <p className="text-gray leading-relaxed mb-6">
            O Aura Burger nasceu em 2018, numa garagem apertada na Zona Oeste de São Paulo. Não tínhamos investidores, não tínhamos uma agência de marketing. Tínhamos apenas uma chapa de aço carbono, uma receita de blend de carnes que levou meses para ser aprimorada, e uma obsessão doentia por fazer o melhor hambúrguer possível.
          </p>
          <p className="text-gray leading-relaxed mb-12">
            Nossa filosofia sempre foi clara: menos é mais. Enquanto o mercado inventava hambúrgueres com 10 andares e ingredientes bizarros, nós focamos no básico bem feito. O pão tem que ser macio e selado na manteiga. A carne tem que ter a crosta da reação de Maillard. O queijo tem que derreter perfeitamente.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 my-16">
            <img 
              src="https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&q=80&w=800" 
              alt="Preparação" 
              className="w-full aspect-[4/5] object-cover border border-border"
              referrerPolicy="no-referrer"
            />
            <img 
              src="https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&q=80&w=800" 
              alt="Restaurante" 
              className="w-full aspect-[4/5] object-cover border border-border mt-0 md:mt-12"
              referrerPolicy="no-referrer"
            />
          </div>

          <h2 className="text-4xl font-oswald font-black uppercase tracking-tight text-white mb-8">
            A Alma Paulistana
          </h2>
          <p className="text-gray leading-relaxed mb-6">
            São Paulo é uma cidade que não perdoa mediocridade. Aqui, as pessoas sabem o que é comer bem. O Aura Burger é um reflexo dessa cidade: intenso, sem frescura, autêntico e que entrega o que promete.
          </p>
          <p className="text-gray leading-relaxed">
            Hoje, na Vila Madalena, continuamos moendo nossa carne diariamente, recebendo pães frescos todas as manhãs e preparando nossa maionese verde com a mesma receita daquela garagem em 2018. A aura continua a mesma.
          </p>
        </div>
      </section>
    </motion.div>
  );
}
