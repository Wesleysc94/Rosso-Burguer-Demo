import { useState } from 'react';
import { AnimatePresence } from 'motion/react';

// Components
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Menu from './pages/Menu';
import Sobre from './pages/Sobre';
import Contato from './pages/Contato';
import Footer from './components/Footer';

export default function App() {
  const [currentPage, setCurrentPage] = useState('home');

  return (
    <div className="min-h-screen bg-black text-white font-sans selection:bg-orange selection:text-white">
      <Navbar currentPage={currentPage} setCurrentPage={setCurrentPage} />
      
      <main className="pt-20">
        <AnimatePresence mode="wait">
          {currentPage === 'home' && <Home key="home" setCurrentPage={setCurrentPage} />}
          {currentPage === 'menu' && <Menu key="menu" />}
          {currentPage === 'sobre' && <Sobre key="sobre" />}
          {currentPage === 'contato' && <Contato key="contato" />}
        </AnimatePresence>
      </main>

      <Footer />
    </div>
  );
}
