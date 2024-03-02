from flask import Blueprint, render_template, request, current_app, session
from Work_with_DB import select_dict
from sql_provider import SQLProvider
import os
from access import *

blueprint_query = Blueprint('bp_query', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@login_required
@group_required
@blueprint_query.route('/')
def choose_menu():
    return render_template('choose_menu.html')


@login_required
@group_required
@blueprint_query.route('/request_1', methods=['GET', 'POST'])
def query_index():
    if request.method == 'GET':
        return render_template('Input_params_for_request_1.html')

    jt = request.form.get("jt")
    _sql = provider.get('Request_1.sql', jt=jt)
    result = select_dict(current_app.config['db_config'], _sql)

    if result:
        return render_template('Dynamic_1.html', result=result, title='Информация о данной вакансии')
    else:
        return render_template('Not_found_template.html')


@blueprint_query.route('/request_2', methods=['GET', 'POST'])
@login_required
@group_required
def query_index_1():
    if request.method == 'GET':
        return render_template('Input_params_for_request_2.html')

    jt = request.form.get('jt')
    _sql = provider.get('Request_2.sql', jt=jt)
    results = select_dict(current_app.config['db_config'], _sql)

    if results:
        return render_template('Dynamic_2.html', results=results, title='Информация о сотрудниках отдела')
    else:
        return render_template('Not_found_template.html')


@blueprint_query.route('/request_3', methods=['GET', 'POST'])
@login_required
@group_required
def query_index_2():
    if request.method == 'GET':
        return render_template('Input_params_for_request_3.html')

    jt = request.form.get('jt')
    _sql = provider.get('Request_3.sql', jt=jt)
    results = select_dict(current_app.config['db_config'], _sql)

    if results:
        return render_template('Dynamic_3.html', results=results, title='Информация о собеседованиях')
    else:
        return render_template('Not_found_template.html')


@blueprint_query.route('/request_4', methods=['GET', 'POST'])
@login_required
@group_required
def query_index_3():
    if request.method == 'GET':
        return render_template('Input_params_for_request_3.html')

    jt = request.form.get('jt')
    _sql = provider.get('Request_4.sql', jt=jt)
    results = select_dict(current_app.config['db_config'], _sql)

    if results:
        return render_template('Dynamic_4.html', results=results, title='Информация о всех должностях')
    else:
        return render_template('Not_found_template.html')
