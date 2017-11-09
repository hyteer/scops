title scops
@echo off
call workon scops
set FLASK_APP=app.py
set FLASK_DEBUG=1
flask run --reload --with-threads -p 8000
CMD
