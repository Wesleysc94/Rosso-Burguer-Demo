import { Instagram, Facebook, MapPin, Phone, Mail } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-dark border-t border-border pt-20 pb-10">
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-16">
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-10 h-10 bg-red rounded-full flex items-center justify-center text-white font-oswald font-bold text-xl tracking-tighter">
                AB
              </div>
              <span className="text-2xl font-oswald font-black tracking-tight text-white uppercase">
                Aura Burger
              </span>
            </div>
            <p className="text-gray max-w-md mb-8">
              O hambúrguer com alma paulistana. Nascido na Vila Madalena, feito para quem exige o melhor da cidade.
            </p>
            <div className="flex gap-4">
              <a href="#" className="w-12 h-12 rounded-full bg-card border border-border flex items-center justify-center hover:bg-orange hover:border-orange text-white transition-all">
                <Instagram size={20} />
              </a>
              <a href="#" className="w-12 h-12 rounded-full bg-card border border-border flex items-center justify-center hover:bg-orange hover:border-orange text-white transition-all">
                <Facebook size={20} />
              </a>
            </div>
          </div>

          <div>
            <h4 className="font-oswald font-bold uppercase tracking-widest text-white mb-6">Contato</h4>
            <ul className="space-y-4 text-gray">
              <li className="flex items-start gap-3">
                <MapPin size={20} className="text-orange shrink-0 mt-1" />
                <span>Rua Fradique Coutinho, 1234<br/>Vila Madalena, São Paulo - SP</span>
              </li>
              <li className="flex items-center gap-3">
                <Phone size={20} className="text-orange shrink-0" />
                <span>(11) 99999-9999</span>
              </li>
              <li className="flex items-center gap-3">
                <Mail size={20} className="text-orange shrink-0" />
                <span>contato@auraburger.com.br</span>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="font-oswald font-bold uppercase tracking-widest text-white mb-6">Horários</h4>
            <ul className="space-y-4 text-gray">
              <li className="flex justify-between border-b border-border pb-2">
                <span>Segunda</span>
                <span className="text-red font-bold">Fechado</span>
              </li>
              <li className="flex justify-between border-b border-border pb-2">
                <span>Ter - Qui</span>
                <span>18h - 23h</span>
              </li>
              <li className="flex justify-between border-b border-border pb-2">
                <span>Sex - Sáb</span>
                <span>18h - 01h</span>
              </li>
              <li className="flex justify-between border-b border-border pb-2">
                <span>Domingo</span>
                <span>17h - 23h</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-border pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-gray text-sm">
            &copy; {new Date().getFullYear()} Aura Burger SP. Todos os direitos reservados.
          </p>
          <div className="flex gap-6 text-sm text-gray">
            <a href="#" className="hover:text-white transition-colors">Termos de Uso</a>
            <a href="#" className="hover:text-white transition-colors">Privacidade</a>
          </div>
        </div>
      </div>
    </footer>
  );
}
