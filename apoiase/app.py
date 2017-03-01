import json

import requests
from flask import Flask, jsonify
from flask_cors import CORS

import config


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/')
def home():
    response = requests.get('https://apoia.se/api/v1/users/serenata?format=json')
    if response.status_code == 200:
        page = json.loads(response.text)
        users = page.get('supports', {}).get('users', [])
        names = list(map(serializer, users))
        return jsonify(names)


def serializer(users):
    private=users.get('privateSupport')
    if not private:
        return dict(
            name=users.get('_id').get('name')
        )


if __name__ == '__main__':
    app.run()
