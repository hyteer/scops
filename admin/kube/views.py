from flask import jsonify, url_for
import json
from kube import kube

@kube.route('/')
def index():
    return "test k8s."
@kube.route('/node/<int:id>')
def node(id):
    return "The node id is %d." % id
