from flask import Flask, jsonify
from flask_cors import CORS

# Configuration
DEBUG = True

# Instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# index & health check routes
@app.route('/', methods=['GET'])
def index():
    return '<h1>NU Directory Search API</h1>'

@app.route('/health', methods=['GET'])
def health_check():
    return '<h1>Healthy!</h1>'

@app.route('/search/<netid>', methods=['GET'])
def search_by_netid(netid):
    
    return jsonify()

if __name__ == '__main__':
    app.run()

