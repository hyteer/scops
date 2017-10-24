from flask import Flask, jsonify, url_for, redirect
from api import *
from main import app

#app = Flask(__name__)

@app.route('/')
def index():
    return "home..."

@app.route('/staticurl/<filename>')
def static_url(filename):
    return url_for("static",filename=filename)

@app.route('/admin')
def admin():
    return redirect(url_for("static",filename='admin/index.html'))

if __name__=='__main__':
    app.run(debug=True,threaded=True,host='0.0.0.0',port=7000)
