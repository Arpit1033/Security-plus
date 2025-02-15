import "./../styles/LiveFootage.css";

function LiveFootage() {
    const handleClick = () => {
        alert("Crime Class: Explosion detected!");
    };

    return (
        <section className="live-footage">
            <h3>Live CCTV Footage</h3>
            <div className="video-container">
                <img src="/assets/image 4.png" alt="CCTV Footage" />
                <p className="prediction">Prediction Result</p>
                <button className="btn btn-danger" onClick={handleClick}>
                    Predicted Crime Class: Explosions
                </button>
                <section>hi</section>
            </div>
        
        </section>
    );
}

export default LiveFootage;
