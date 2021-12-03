from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

# Configuration
DEBUG = True

# Instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# load env variables
NU_DIRECTORY_API_KEY = os.environ.get('NU_DIRECTORY_API_KEY')

# index & health check routes
@app.route('/', methods=['GET'])
def index():
    return '<h1>NU Directory Search API</h1>'

@app.route('/health', methods=['GET'])
def health_check():
    return '<h1>Healthy!</h1>'

@app.route('/search/netid/<netid>', methods=['GET'])
def search_by_netid(netid):
    print(netid)
    url =  f"https://northwestern-prod.apigee.net/directory-search/res/netid/bas/{netid}"
    headers = {'apikey': NU_DIRECTORY_API_KEY }
    res = requests.get(url, headers=headers)
    data = res.json()
    return jsonify(data)

@app.route('/search/email/<email>', methods=['GET'])
def search_by_email(email):
    print(email)
    url =  f"https://northwestern-prod.apigee.net/directory-search/res/mail/bas/{email}"
    headers = {'apikey': NU_DIRECTORY_API_KEY }
    res = requests.get(url, headers=headers)
    data = res.json()
    return jsonify(data)

@app.route('/status/netid/<netid>', methods=['GET'])
def status_netid(netid):
    print(netid)
    url =  f"https://northwestern-prod.apigee.net/netIdStatus/{netid}"
    headers = {'apikey': NU_DIRECTORY_API_KEY }
    res = requests.get(url, headers=headers)
    data = res.json()
    return jsonify(data)


if __name__ == '__main__':
    app.run()

