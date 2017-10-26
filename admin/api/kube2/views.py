from flask import jsonify, url_for, current_app
import json
from api.kube2 import kube2
from . import config
#import pdb; pdb.set_trace()

@kube2.route('/')
def index():
    #import pdb; pdb.set_trace()
    URL = current_app.config['REG_URL']
    print("RegUrl:",URL)
    return "test kube..."

@kube2.route('/node/<int:id>')
def node(id):
    return "The node id is %d." % id
