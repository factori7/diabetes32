from flask import Flask,render_template

app = Flask("my-dengue")

@app.route('/')
def home():
    return render_template('index.html')