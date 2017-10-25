from flask import Flask
from registry import reg
from kube import kube

app = Flask(__name__)

app.register_blueprint(reg, url_prefix='/api/reg')
app.register_blueprint(kube, url_prefix='/kube')

if __name__ == '__main__':
    app.run(debug=True,threaded=True)
