#!/usr/bin/env python

from flask.ext.script import Manager
from flask.ext.script import Server

from app import app

'''
@author: Anant Bhardwaj
@date: Sep 19, 2015
'''

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=8000, threaded=True))

if __name__ == '__main__':
  manager.run()