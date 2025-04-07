# Security Plus

![Demo](demo.gif)

## Overview
Security Plus specializes in AI-powered surveillance technology designed to enhance real-time security. Our state-of-the-art software continuously monitors live video feeds, identifying criminal activities such as theft, violence, or suspicious behavior.

## Features
- *AI-Powered Monitoring*: Uses advanced machine learning algorithms to detect threats and anomalies.
- *Real-Time Analysis*: Continuously analyzes video feeds for security risks.
- *Instant Alerts*: Notifies authorities immediately upon detecting unlawful activities.
- *Proactive Security*: Helps safeguard communities, businesses, and public areas.

## How It Works
1. The system processes live video feeds in real-time.
2. AI algorithms analyze the footage to detect potential threats.
3. If a threat is identified, an alert is sent to the concerned authorities.
4. Authorities can take swift action to prevent or mitigate risks.

## Why Choose Security Plus?
- *Enhanced Crime Prevention*: Stay ahead of threats with proactive security measures.
- *Automated Surveillance*: Reduces the need for manual monitoring.
- *Scalable Solutions*: Suitable for businesses, public spaces, and communities.

Stay one step ahead of crime with Security Plus – the intelligent surveillance system built for modern security needs.

---

# Running the Application with Docker

## Prerequisites
- Docker
- Docker Compose

## Running the Application
1. **Clone the Repository**
   ```sh
   git clone "https://github.com/Sarthacker/Security-plus.git"
   cd security-plus
   ```

2. **Build and Run Containers**
   ```sh
   docker-compose up --build
   ```

3. **Access the Application**
   - Backend: `http://localhost:5000`
   - Frontend: `http://localhost:3000`

4. **Stopping the Application**
   ```sh
   docker-compose down
   ```

---

# Running the Flask Backend (Without Docker)

## Prerequisites
- Python (>=3.8)
- pip (latest version recommended)
- Virtual environment (optional but recommended)

## Installation

1. **Create and Activate Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

2. **Install Dependencies**
   ```sh
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the Flask Server**
   ```sh
   python app.py
   ```

---

# Running the React Frontend (Without Docker)

## Prerequisites
- Node.js (>=14.0)
- npm or yarn

## Installation and Running
1. **Navigate to the Frontend Directory**
   ```sh
   cd frontend
   ```

2. **Install Dependencies**
   ```sh
   npm install  # or yarn install
   ```

3. **Start the React Development Server**
   ```sh
   npm start  # or yarn start
   ```

4. **Access the Application**
   - Frontend: `http://localhost:3000`

---

# Dataset
- The dataset used to train our model is the UCF Crime Dataset available on [Kaggle](https://www.kaggle.com/datasets/mission-ai/crimeucfdataset).
- The Model Weights can be downloaded from [here](https://drive.google.com/file/d/1hJiKJBcu3phWvjucH_zYD22Y_DpZ0-oy).

