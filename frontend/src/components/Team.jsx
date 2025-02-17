import "./../styles/Team.css";

function Team() {
    return (
        <section className="team">
            <h3 className="team-title">Team Members</h3>
            <div className="members">
                <div className="member-card">
                    <h4>Sarthak Kumar Singh</h4>
                    <p>AI/ML Developer</p>
                </div>
                <div className="member-card">
                    <h4>Manan Sharma</h4>
                    <p>AI/ML Developer</p>
                </div>
                <div className="member-card">
                    <h4>Devendra Gurnani</h4>
                    <p>Web Developer</p>
                </div>
                <div className="member-card">
                    <h4>Shagun Singh</h4>
                    <p>Web Developer</p>
                </div>
                <div className="member-card">
                    <h4>Aript Dubey</h4>
                    <p>Web Developer</p>
                </div>
            </div>
        </section>
    );
}

export default Team;
