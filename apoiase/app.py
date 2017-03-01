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
        users = filter(lambda u: not u.get('privateSupport'), users)
        names = list(map(serializer, users))
        return jsonify(names)


def serializer(apoiase_users):
    return dict(name=apoiase_users.get('_id').get('name'))


if __name__ == '__main__':
    app.run()
