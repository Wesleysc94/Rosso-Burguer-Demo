import Navbar from './components/Navbar';
import Home from './pages/Home';
import Footer from './components/Footer';

export default function App() {
  return (
    <div className="min-h-screen bg-black text-white font-sans selection:bg-red selection:text-white">
      <Navbar />
      <main>
        <Home />
      </main>
      <Footer />
    </div>
  );
}
