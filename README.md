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

Stay one step ahead of crime with Security Plus – the intelligent surveillance system built for modern security needs.

# Running the Flask Backend

Follow these steps to set up and run the Flask backend:

## Prerequisites

- Python (>=3.8)
- pip (latest version recommended)
- Virtual environment (optional but recommended)

## Installation

1. **Clone the Repository**
   
   ```sh
   git clone "https://github.com/Sarthacker/Security-plus.git"
   cd security-plus

2. **Create and Activate Virtual Environment (Optional but Recommended)**
   
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows

3. **Install Dependencies**

   ```sh
   cd backend
   pip install -r requirements.txt

4. **Run the Flask Server**

   ```sh
   python app.py

## Dataset
- The dataset that we used to train our model is the UCF Crime Dataset available on [Kaggle](https://www.kaggle.com/datasets/odins0n/ucf-crime-dataset).
- The Model Weights can be downloaded from [here](https://drive.google.com/file/d/1hJiKJBcu3phWvjucH_zYD22Y_DpZ0-oy).
