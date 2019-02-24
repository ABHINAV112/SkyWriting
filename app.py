from flask import Flask,render_template,request
from main import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/AR')
def AR():
    text1 = main()
    return render_template("AR.html",text =text1)

@app.route('/text')
def text():
    a = main()
    return render_template("text.html",test=a)

if(__name__=="__main__"):
    app.run(debug=True)