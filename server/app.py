from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSON_SORT_KEYS'] = False #Used to not sort json objects by keys (jsonify) - 

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


from route import *


if __name__ == '__main__':
    app.run()