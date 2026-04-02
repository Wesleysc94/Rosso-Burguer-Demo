import { motion } from 'motion/react';
import { MapPin, Phone, Mail, Clock } from 'lucide-react';

export default function Contato() {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="w-full pt-10 pb-32 bg-black bg-grid-lines"
    >
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center mb-20">
          <h1 className="text-6xl md:text-8xl font-oswald font-black uppercase tracking-tighter text-white mb-6">
            Contato
          </h1>
          <div className="w-24 h-2 bg-orange mx-auto mb-8"></div>
          <p className="text-xl text-gray max-w-2xl mx-auto">
            Vem comer com a gente ou manda uma mensagem.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16">
          {/* Info & Map */}
          <div className="space-y-12">
            <div className="bg-card border border-border p-8">
              <h3 className="text-3xl font-oswald font-black uppercase tracking-tight text-white mb-8 border-b border-border pb-4">
                Onde Estamos
              </h3>
              <ul className="space-y-6">
                <li className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-dark border border-border flex items-center justify-center shrink-0 text-orange">
                    <MapPin size={24} />
                  </div>
                  <div>
                    <h4 className="text-xl font-oswald font-bold uppercase text-white mb-1">Endereço</h4>
                    <p className="text-gray">Rua Fradique Coutinho, 1234<br/>Vila Madalena, São Paulo - SP<br/>05416-001</p>
                  </div>
                </li>
                <li className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-dark border border-border flex items-center justify-center shrink-0 text-orange">
                    <Clock size={24} />
                  </div>
                  <div>
                    <h4 className="text-xl font-oswald font-bold uppercase text-white mb-1">Horários</h4>
                    <p className="text-gray">Terça a Quinta: 18h às 23h<br/>Sexta e Sábado: 18h às 01h<br/>Domingo: 17h às 23h</p>
                  </div>
                </li>
                <li className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-dark border border-border flex items-center justify-center shrink-0 text-orange">
                    <Phone size={24} />
                  </div>
                  <div>
                    <h4 className="text-xl font-oswald font-bold uppercase text-white mb-1">Telefone / Delivery</h4>
                    <p className="text-gray">(11) 99999-9999<br/>Disponível no iFood e Keeta</p>
                  </div>
                </li>
              </ul>
            </div>

            <div className="aspect-video bg-dark border border-border relative overflow-hidden group">
              <img 
                src="https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&q=80&w=1000" 
                alt="São Paulo Map" 
                className="w-full h-full object-cover opacity-50 grayscale group-hover:scale-105 transition-transform duration-700"
                referrerPolicy="no-referrer"
              />
              <div className="absolute inset-0 flex items-center justify-center">
                <button className="bg-red text-white px-8 py-4 font-oswald font-bold uppercase tracking-widest hover:bg-orange transition-colors flex items-center gap-3">
                  <MapPin size={20} />
                  Abrir no Google Maps
                </button>
              </div>
            </div>
          </div>

          {/* Form */}
          <div className="bg-card border border-border p-8 md:p-12">
            <h3 className="text-3xl font-oswald font-black uppercase tracking-tight text-white mb-2">
              Mande uma Mensagem
            </h3>
            <p className="text-gray mb-8">Dúvidas, elogios ou reclamações? Fala com a gente.</p>
            
            <form className="space-y-6" onSubmit={(e) => e.preventDefault()}>
              <div>
                <label htmlFor="name" className="block text-sm font-bold uppercase tracking-widest text-gray mb-2">Nome</label>
                <input 
                  type="text" 
                  id="name" 
                  className="w-full bg-dark border border-border px-4 py-3 text-white focus:outline-none focus:border-orange transition-colors"
                  placeholder="Seu nome completo"
                />
              </div>
              <div>
                <label htmlFor="email" className="block text-sm font-bold uppercase tracking-widest text-gray mb-2">E-mail</label>
                <input 
                  type="email" 
                  id="email" 
                  className="w-full bg-dark border border-border px-4 py-3 text-white focus:outline-none focus:border-orange transition-colors"
                  placeholder="seu@email.com"
                />
              </div>
              <div>
                <label htmlFor="subject" className="block text-sm font-bold uppercase tracking-widest text-gray mb-2">Assunto</label>
                <select 
                  id="subject" 
                  className="w-full bg-dark border border-border px-4 py-3 text-white focus:outline-none focus:border-orange transition-colors appearance-none"
                >
                  <option>Dúvida</option>
                  <option>Elogio</option>
                  <option>Reclamação</option>
                  <option>Trabalhe Conosco</option>
                </select>
              </div>
              <div>
                <label htmlFor="message" className="block text-sm font-bold uppercase tracking-widest text-gray mb-2">Mensagem</label>
                <textarea 
                  id="message" 
                  rows={5}
                  className="w-full bg-dark border border-border px-4 py-3 text-white focus:outline-none focus:border-orange transition-colors resize-none"
                  placeholder="Escreva sua mensagem aqui..."
                ></textarea>
              </div>
              <button 
                type="submit"
                className="w-full bg-orange hover:bg-red text-white px-8 py-4 font-oswald font-bold uppercase tracking-widest text-lg transition-colors mt-4"
              >
                Enviar Mensagem
              </button>
            </form>
          </div>
        </div>
      </div>
    </motion.div>
  );
}
