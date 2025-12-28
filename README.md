# sentiment-analysis-customer-feedback
# Sentiment Analysis System for Customer Feedback

## Overview
This project is a sentiment analysis system designed to analyze customer feedback and classify it into
**Positive**, **Negative**, or **Neutral** sentiments.  
The goal is to help businesses understand customer opinions and improve products or services based on feedback.

The system collects feedback via Google Forms, stores it in Google Sheets, processes the text using NLP
techniques, and visualizes sentiment insights through an interactive Streamlit web application.

---

## Project Workflow
1. Customer feedback is collected using Google Forms  
2. Responses are stored automatically in Google Sheets  
3. Data is fetched into the Python program using Google Sheets API  
4. Text data is cleaned and processed  
5. Sentiment analysis is performed using NLP techniques  
6. Results are visualized using charts  
7. A Streamlit web app displays analysis results interactively  

---

## Tools & Technologies
- Python  
- Pandas  
- NLTK  
- VADER Sentiment  
- Plotly  
- Streamlit  
- Google Sheets API
  
## Features
- Real-time feedback classification
- Google Sheets integration
- Interactive Streamlit UI
- Plotly charts for sentiment trends

---

## Dataset Source
- Feedback data collected using **Google Forms**
- Responses stored in **Google Sheets**
- Data accessed programmatically via Google Sheets API

---

## Project Structure
sentiment-analysis-customer-feedback/
├── sentiment_analysis_app.py
├── requirements.txt
├── .gitignore
├── screenshots/
└── README.md


---

## Installation & Setup

### Step 1: Clone the repository

### Step 2: Install required libraries

---

## Google Sheets API Configuration
This project uses Google Sheets API to fetch feedback data.

Steps:
1. Create a Google Cloud project
2. Enable Google Sheets API
3. Create OAuth client credentials
4. Download the credentials file and rename it to `key.json`
5. Place `key.json` in the project root directory

**Note:**  
The `key.json` file is not included in this repository for security reasons.

---

## Running the Application
streamlit run sentiment_analysis_app.py

---

## Output
- Sentiment classification (Positive / Neutral / Negative)
- Interactive charts and visualizations
- Streamlit-based analysis dashboard

---

## Screenshots
Sample screenshots of the application and sentiment visualizations are included in the `screenshots` folder.

---

## Note
This project was developed as part of self-directed, project-based learning.
