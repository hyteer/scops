from flask import Flask, g
from registry import reg
from kube import kube
from api.kube2 import kube2

app = Flask(__name__)

app.config['REG_URL'] = 'http://10.100.100.130:6001/v2'

app.register_blueprint(reg, url_prefix='/api/reg')
app.register_blueprint(kube2, url_prefix='/api/kube2')
app.register_blueprint(kube, url_prefix='/kube')

@app.route('/')
def index():
    return "home..."

@app.route('/debug')
def debug():
    import pdb; pdb.set_trace()
    return "debug..."

@app.route('/admin')
def admin():
    return '<a href="/admin/">Click me to get to Admin!</a>'

if __name__ == '__main__':
    app.run(port=8000,debug=True,threaded=True)
