import importlib

moduleName = input('Enter module name:')
importlib.import_module(moduleName)
#from src.app import app

__author__ = 'jslvtr'

app.run(debug=app.config['DEBUG'], port=4990)
