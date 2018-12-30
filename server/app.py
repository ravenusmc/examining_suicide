from flask import Flask, jsonify, request
from flask_cors import CORS

#Importing my files for this project
from data import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#Getting the number of suicides by country
@app.route('/suicides_by_country', methods=['GET', 'POST'])
def route_one():
    data = Data()
    if request.method == 'POST':
        post_data = request.get_json()
        country = post_data.get('country')
        Total = country
        return jsonify(Total)
        # Total = data.suicides_by_country()
    Total = 'TEST'
    return jsonify(Total)

if __name__ == '__main__':
    app.run()
