FROM reg.ci.snsshop.net/scops/base:20171107
COPY main /home/main
CMD gunicorn --reload -b 0.0.0.0:8000 main:app
