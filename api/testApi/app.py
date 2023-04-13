from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
    return '<h1>Hello, Welcome to Repurpost Web API!</h1>'


# GET requests will be blocked
@app.route('/suggestTags', methods=['POST'])
@cross_origin()
def suggest_Tags():
    request_data = request.get_json()

    contentTitle = request_data['title']
    contentBody = request_data['body']

    return ['Tag1', 'Tag2', 'Tag3', 'Tag4']
