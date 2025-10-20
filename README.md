# YouQuest App

## Project Overview

This **YouQuest Quiz App** allows users to select quiz categories, difficulty levels, and question types, then take interactive quizzes fetched live from the Open Trivia Database API.

## Features
• Fetches questions from [Open Trivia DB](https://opentdb.com)  
• Multiple categories, difficulties, and question types  
• Interactive quiz interface with instant scoring  
• Review your answers after submission  
• Restart or take a new quiz anytime  

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
