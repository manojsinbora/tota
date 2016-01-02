from flask import Flask
from flask import render_template
from flask.ext.login import LoginManager

'''
@author: Anant Bhardwaj
@date: Sep 19, 2015
'''

##### Create the app #####
app = Flask(__name__)


##### Login Manager #####
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/account/login'


@app.route("/")
def hello():
  return "Hello World!"