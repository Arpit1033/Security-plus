import Header from "./components/Header";
import About from "./components/About";
import LiveFootage from "./components/LiveFootage";
import TechStack from "./components/TechStack";
import Team from "./components/Team";
import Footer from "./components/Footer";
import "./styles/App.css";

function App() {
    return (
        <div className="App">
            <Header />
            <About />
            <LiveFootage />
            <TechStack />
            <Team />
            <Footer />
        </div>
    );
}

export default App;
