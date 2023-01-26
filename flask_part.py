# do not name the file flask.py
# setup an environment:
# sudo apt install python3.10-venv -y
# python3 -m venv env_name
# source new_env/bin/activate
#
# pip3 install flask
# ...
# export FLASK_APP=flask_part.py
# export FLASK_ENV=development

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h2>Welcome to my web app</h2>"
