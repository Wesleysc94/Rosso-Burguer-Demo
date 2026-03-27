import { motion } from 'motion/react';

const menuCategories = [
  {
    title: 'Smash Burgers',
    description: 'Pão de batata super macio, carne prensada na chapa para aquela crostinha perfeita.',
    items: [
      { name: 'Smash Simples', desc: '1 smash 90g, american cheese, maionese da casa.', price: 'R$ 24' },
      { name: 'Smash Duplo', desc: '2 smashs 90g, duplo american cheese, bacon, maionese.', price: 'R$ 32' },
      { name: 'Smash Salada', desc: '2 smashs 90g, queijo prato, alface, tomate, cebola roxa, picles.', price: 'R$ 34' },
    ]
  },
  {
    title: 'Clássicos Aura',
    description: 'Nossos blends de 160g, altos e suculentos. Ponto da casa: rosado por dentro.',
    items: [
      { name: 'Aura Clássico', desc: 'Pão brioche, blend 160g, queijo prato, alface, tomate, maionese verde.', price: 'R$ 36' },
      { name: 'Cheddar Bacon', desc: 'Pão australiano, blend 160g, creme de cheddar, bacon crocante, cebola caramelizada.', price: 'R$ 42' },
      { name: 'Gorgonzola', desc: 'Pão brioche, blend 160g, creme de gorgonzola, rúcula, mel picante.', price: 'R$ 44' },
      { name: 'Vegano da Vila', desc: 'Pão vegano, burger de falafel, queijo vegano, rúcula, maionese de alho.', price: 'R$ 38' },
    ]
  },
  {
    title: 'Porções',
    description: 'Para compartilhar (ou não).',
    items: [
      { name: 'Fritas Rústicas', desc: 'Batatas rústicas com páprica e alecrim. Acompanha maionese verde.', price: 'R$ 18' },
      { name: 'Fritas Cheddar & Bacon', desc: 'Nossas fritas cobertas com creme de cheddar e farofa de bacon.', price: 'R$ 28' },
      { name: 'Onion Rings', desc: 'Anéis de cebola empanados e super crocantes. Acompanha molho barbecue.', price: 'R$ 22' },
    ]
  },
  {
    title: 'Bebidas & Sobremesas',
    description: 'Para refrescar e adoçar.',
    items: [
      { name: 'Refrigerantes', desc: 'Lata 350ml (Coca-Cola, Guaraná, Sprite).', price: 'R$ 8' },
      { name: 'Cerveja Artesanal', desc: 'IPA ou Pilsen da casa (Long Neck).', price: 'R$ 16' },
      { name: 'Milkshake de Paçoca', desc: 'Sorvete de creme, muita paçoca, chantilly.', price: 'R$ 24' },
      { name: 'Pudim de Leite', desc: 'Receita de vó, sem furinhos, com calda de caramelo escuro.', price: 'R$ 14' },
    ]
  }
];

export default function Menu() {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="w-full pt-10 pb-32 bg-black"
    >
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-20">
          <h1 className="text-6xl md:text-8xl font-oswald font-black uppercase tracking-tighter text-white mb-6">
            Cardápio
          </h1>
          <div className="w-24 h-2 bg-red mx-auto mb-8"></div>
          <p className="text-xl text-gray max-w-2xl mx-auto">
            Sem frescura, apenas ingredientes de altíssima qualidade e execução perfeita.
          </p>
        </div>

        <div className="space-y-24">
          {menuCategories.map((category, idx) => (
            <div key={idx} className="relative">
              <div className="mb-10 border-b border-border pb-6">
                <h2 className="text-4xl md:text-5xl font-oswald font-black uppercase tracking-tight text-orange mb-3">
                  {category.title}
                </h2>
                <p className="text-gray text-lg">{category.description}</p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-10">
                {category.items.map((item, itemIdx) => (
                  <div key={itemIdx} className="group">
                    <div className="flex justify-between items-baseline mb-2">
                      <h3 className="text-2xl font-oswald font-bold uppercase tracking-wide text-white group-hover:text-red transition-colors">
                        {item.name}
                      </h3>
                      <div className="flex-grow border-b border-dashed border-border mx-4 relative top-[-6px]"></div>
                      <span className="text-xl font-oswald font-bold text-orange shrink-0">
                        {item.price}
                      </span>
                    </div>
                    <p className="text-gray text-sm leading-relaxed pr-12">
                      {item.desc}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </motion.div>
  );
}
