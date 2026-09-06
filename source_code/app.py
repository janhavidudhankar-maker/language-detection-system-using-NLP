from flask import Flask, request, jsonify, send_from_directory
from langdetect import detect, DetectorFactory

app = Flask(name)

Same result every time

DetectorFactory.seed = 0

@app.route("/")
def home():
return send_from_directory(".", "index.html")

@app.route("/detect", methods=["POST"])
def detect_language():
data = request.get_json()
text = data.get("text", "").strip()

if not text:  
    return jsonify({"error": "Please enter some text."})  

try:  
    language = detect(text)  

    language_names = {  
        "en": "English",  
        "hi": "Hindi",  
        "mr": "Marathi",  
        "fr": "French",  
        "es": "Spanish",  
        "de": "German",  
        "it": "Italian",  
        "pt": "Portuguese",  
        "ru": "Russian",  
        "ja": "Japanese",  
        "ko": "Korean",  
        "zh-cn": "Chinese"  
    }  

    result = language_names.get(language, language)  

    return jsonify({  
        "language": result,  
        "code": language  
    })  

except Exception:  
    return jsonify({"error": "Language could not be detected."})

if name == "main":
app.run(debug=True)
Ye code hai app.py ka
