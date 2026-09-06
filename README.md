# Language Detection System Using NLP

## Student Details

- **Name:** Janhavi Dudhankar
- **Roll No.:** BT240022ET
- **Semester/Branch:** V Semester ETC

## Problem Statement

To develop an NLP-based application that automatically identifies the language of a given text.

## Introduction

Language Detection is an important Natural Language Processing (NLP) task used to identify the language in which a text is written. This project provides a simple web-based application that detects the language of user-provided text.

## Objective

The objective of this project is to develop a system that automatically detects the language of a given text using Natural Language Processing techniques.

## NLP Technique / Method Used

This project uses automatic language identification using the `langdetect` Python library.

The system:
1. Accepts text from the user.
2. Processes the entered text.
3. Detects the language.
4. Displays the detected language and language code.

## Dataset / Source of Data

This project does not require a separate manually prepared dataset. The language detection is performed using the `langdetect` library.

## Software, Tools and Libraries Used

- Python
- Flask
- langdetect
- HTML
- CSS
- GitHub
- Web Browser

## Methodology / Workflow

```text
User enters text
       ↓
Text is sent to Flask application
       ↓
Language detection using langdetect
       ↓
Language code is obtained
       ↓
Language name is identified
## Project Structure
```text
Language-Detection-System-Using-NLP/
│
├── README.md
├── app.py
├── index.html
├── style.css
├── requirements.txt
│
└── source_code/
    └── app.py

## Steps to Execute the Project
1. Install Python
Install Python on the system.
 2. Install Required Libraries
Open the terminal and run:
pip install -r requirements.txt
 3. Run the Flask Application
python app.py

### 4. Open the Application
Open the web browser and access the Flask application.
## Sample Input
Hello, how are you?
## Sample Output
Language: English
Code: en

## Results / Observations
The system successfully detects the language of the given text and displays the detected language along with its language code.
The application can detect multiple languages such as English, Hindi, Marathi, French, Spanish, German, Italian, Portuguese, Russian, Japanese, Korean and Chinese.

## Conclusion
The Language Detection System demonstrates the application of Natural Language Processing for automatic language identification. The project provides a simple and user-friendly interface for detecting the language of input text.
       ↓
Result is displayed to the user
