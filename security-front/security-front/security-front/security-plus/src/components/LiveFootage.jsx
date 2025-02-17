import { useState, useEffect } from "react";
import "./../styles/LiveFootage.css";

function LiveFootage() {
    const [prediction, setPrediction] = useState("");

    useEffect(() => {
        const eventSource = new EventSource("http://localhost:5000/predict");

        eventSource.onmessage = (event) => {
            setPrediction(event.data);
        };

        return () => {
            eventSource.close();
        };
    }, []);

    return (
        <section className="live-footage">
            <h3>Live CCTV Footage</h3>
            <div className="video-container">
                {/* Live Video Feed */}
                <img src="http://localhost:5000/video_feed" alt="Live CCTV Footage" />
                
                {/* Prediction Result */}
                <p className="prediction">{prediction}</p>
                
                {/* Alert Button */}
                {/* <button className="btn btn-danger" onClick={() => alert(`Crime Class: ${prediction}`)}>
                    Predicted Crime Class: {prediction}
                </button> */}
            </div>
        </section>
    );
}

export default LiveFootage;
