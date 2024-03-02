from flask import Flask, render_template, request
import json
from Blueprint_query.query_route import blueprint_query


app = Flask(__name__)

with open('../db_config.json') as f:
    app.config['db_config'] = json.load(f)

app.register_blueprint(blueprint_query, url_prefix='/query')


@app.route('/')
def main_menu():
    return render_template('internal_user_menu.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
