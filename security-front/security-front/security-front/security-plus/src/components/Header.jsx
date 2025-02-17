import "./../styles/Header.css";

function Header() {
    return (
        <div className="header-container">
            <div className="cctv-column">
            <img src="/assets/cctv 1.png" className="cctv-image left-top" alt="CCTV 1" />
            <img src="/assets/cctv 2.png" className="cctv-image right-top" alt="CCTV 2" />
            </div>
            
            <section className="heading-container">
                <p className="sub-heading">Welcome to</p>
                <h1 className="main-heading">SECURITY+</h1>
            </section>

            <div className="cctv-column">
                <img src="/assets/cctv 3.png" className="cctv-image left-bottom" alt="CCTV 3" />
                <img src="/assets/cctv 4.png" className="cctv-image right-bottom" alt="CCTV 4" />
            </div>
        </div>
    );
}

export default Header;

