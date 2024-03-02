from flask import Blueprint, request, render_template, current_app, session, redirect, url_for
from sql_provider import SQLProvider
from Work_with_DB import select_dict
from typing import Optional, Dict
import os


blueprint_auth = Blueprint('bp_auth', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_auth.route('/', methods=['POST', 'GET'])
def start_auth():
    if request.method == 'GET':
        return render_template('auth_form.html')
    else:
        login = request.form.get('login')
        password = request.form.get('password')
        if login:
            user_info = define_user(login, password)

            if user_info:
                if user_info[0]['User_group'] is not None:
                    user_dict = user_info[0]
                    session['User_ID'] = user_dict['User_ID']
                    session['User_group'] = user_dict['User_group']
                else:
                    user_dict = user_info[0]
                    session['User_ID'] = user_dict['User_ID']
                    session['User_group'] = None

                return redirect(url_for('main_menu'))
            else:
                return render_template('auth_form.html', message='Пользователь не найден')

        return render_template('auth_form.html', message='Повторите ввод')


def define_user(login: str, password: str) -> Optional[Dict]:
    sql_internal = provider.get('internal_user.sql', login=login, password=password)
    sql_external = provider.get('external_user.sql', login=login, password=password)

    user_info = None

    for sql_search in [sql_internal, sql_external]:
        _user_info = select_dict(current_app.config['db_config'], sql_search)
        if _user_info:
            user_info = _user_info
            del _user_info
            break
    return user_info
