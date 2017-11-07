from flask import Blueprint

kube = Blueprint('kube', __name__,)

from kube import views
