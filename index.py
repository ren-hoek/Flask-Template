from flask import Flask, render_template, request
import json

app = Flask(__name__)

#Needs setting as CSRF_ENABLED=True for flask-wtf. Keep secret_key, secret
app.secret_key = '7923847kajsdhakjdsh'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ixbrl')
def ixbrl():
    return render_template('ixbrl.html')

@app.route('/data')
def data():
    with open('data.json', 'r') as json_file:
        data=json_file.read().replace('\n','').replace(' ','')
    return data

if __name__ == '__main__':
    app.run(debug=True)
