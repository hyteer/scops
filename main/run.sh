#!/bin/sh
gunicorn --reload -b 0.0.0.0:8000 app:app
