from flask import Blueprint

kube2 = Blueprint('kube2', __name__,)

from api.kube2 import views
