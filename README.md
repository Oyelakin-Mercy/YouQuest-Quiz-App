# YouQuest App

## Project Overview

This **YouQuest Quiz App** allows users to select quiz categories, difficulty levels, and question types, then take interactive quizzes fetched live from the Open Trivia Database API.

## Features
• Fetches questions from [Open Trivia DB](https://opentdb.com)  
• Multiple categories, difficulties, and question types  
• Interactive quiz interface with instant scoring  
• Review your answers after submission  
• Restart or take a new quiz anytime  

## Project Structure

youquest/
│
├── app.py                     # Main Flask application
├── requirements.txt            # Python dependencies
│
├── templates/                  # HTML templates
│   ├── index.html              # Home page (category selection)
│   ├── quiz.html               # Quiz question interface
│   ├── results.html            # Result page
│   └── review.html             # Review answers page
│
├── static/                     # Static assets
│   ├── style.css               # Global stylesheet
│   └── images/
│       ├── main_background_1.png
│       └── quiz_background.jpg
│
└── README.md                   # Project documentation

## Installation & Setup

Follow these steps to run YouQuest locally:

### Clone the repository
git clone https://github.com/yourusername/youquest.git
cd youquest

### Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate    *On Windows*
source venv/bin/activate  *On macOS/Linux*

### Install dependencies
pip install -r requirements.txt

### Run the Flask app
python app.py

### Open in your browser

Go to http://127.0.0.1:5000/
and start your quiz!