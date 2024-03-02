from flask import Flask, render_template, url_for, redirect, session
from Blueprint_auth.auth_route import blueprint_auth
from Blueprint_query.query_route import blueprint_query
from Blueprint_basket.basket_route import blueprint_basket
from Blueprint_report.rep_route import blueprint_report
from access import login_required
import json


app = Flask(__name__)
app.secret_key = 'Secret_key'

with open('../db_config.json', encoding='utf-8') as f:
    app.config['db_config'] = json.load(f)

with open('../access.json') as f:
    app.config['access'] = json.load(f)

app.register_blueprint(blueprint_auth, url_prefix='/auth_service')
app.register_blueprint(blueprint_query, url_prefix='/query')
app.register_blueprint(blueprint_basket, url_prefix='/basket')
app.register_blueprint(blueprint_report, url_prefix='/report')


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
    app.run(host='127.0.0.1', port=5000, debug=True)
