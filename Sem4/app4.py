from flask import Flask, render_template, session
from access import login_required
from Blueprint_auth.auth_route import blueprint_auth
from Blueprint_query.query_route import blueprint_query
import json


app = Flask(__name__)
app.secret_key = 'Secret_key'

with open('../db_config.json') as f:
    app.config['db_config'] = json.load(f)

with open('../access.json') as f:
    app.config['access'] = json.load(f)

app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(blueprint_query, url_prefix='/query')


@app.route('/')
@login_required
def main_menu():
    if session.get('User_group', None):
        return render_template('internal_user_menu.html')
    return render_template('external_user_menu.html')


@app.route('/exit')
@login_required
def exit_func():
    session.clear()
    return render_template('log_out.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
