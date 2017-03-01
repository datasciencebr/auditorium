import json

import requests
from flask import Flask, jsonify, render_template
from flask_cors import CORS

import config


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/')
def home():
    if not config.APOIASE_URL:
        return render_template('no_env_variable.html')
    response = requests.get(config.APOIASE_URL)
    if response.status_code == 200:
        page = json.loads(response.text)
        users = page.get('supports', {}).get('users', [])
        users = filter(filter_private_supporters, users)
        names = list(map(serializer, users))
        return jsonify(names)


def filter_private_supporters(apoiase_users):
    if not apoiase_users.get('privateSupport'):
        return apoiase_users


def serializer(apoiase_users):
    return dict(name=apoiase_users.get('_id').get('name'))


if __name__ == '__main__':
    app.run()
