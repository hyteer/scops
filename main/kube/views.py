from flask import jsonify, url_for, current_app
import json
from kube import kube
from . import config

@kube.route('/')
def index():
    #import pdb; pdb.set_trace()
    URL = current_app.config['REG_URL']
    print("RegUrl:",URL)
    return "test k8s."
@kube.route('/node/<int:id>')
def node(id):
    return "The node id is %d." % id
