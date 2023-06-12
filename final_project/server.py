from translator import english_to_french, french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    a = english_to_french(textToTranslate) 
    return a 

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    b = french_to_english(textToTranslate) 
    return b

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
