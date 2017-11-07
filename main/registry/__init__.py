from flask import Blueprint

reg = Blueprint('reg', __name__,)

from registry import views
from registry import api
