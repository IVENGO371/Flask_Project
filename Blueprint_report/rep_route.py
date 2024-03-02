from flask import Blueprint, render_template, current_app
from access import *
from sql_provider import SQLProvider
from Work_with_DB import *
import os

blueprint_report = Blueprint('bp_report', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_report.route('/')
@login_required
@group_required
def report_menu():
    sql = provider.get('reports_list_for_menu.sql')
    res = select_dict(current_app.config['db_config'], sql)

    if res is None:
        return render_template('db_error.html')
    elif res != -1:
        for rep in res:
            rep['href_name'] = rep['href_name'].split('; ')[0]

    print("res_1: ", res)

    return render_template('report_menu.html', result=res)


@blueprint_report.route('/report/<proc>')
@login_required
def report(proc):
    if 'create_report' not in current_app.config['access'][session['User_group']]:
        return redirect(url_for('.view_report', proc=proc))

    sql = provider.get(f'proc_desc_{proc}.sql', proc=proc)
    res = select_dict(current_app.config['db_config'], sql)

    if res is None or res == -1:
        return render_template('db_error.html')
    else:
        res = res[0]['href_name'].split('; ')[0]

    return render_template('create_or_view.html', result=res, proc=proc)


@blueprint_report.route('/create-report/<proc>', methods=['GET', 'POST'])
@login_required
@group_required
def create_report(proc):
    sql = provider.get(f'proc_desc_{proc}.sql', proc=proc)
    res = select_dict(current_app.config['db_config'], sql)

    if res is None or res == -1:
        return render_template('db_error.html')
    else:
        ret = [res[0]['href_name'].split('; ')[0], ]

    if request.method == 'GET':
        html = f"input_date.html"
    else:
        html = 'proc_res.html'
        res = call_procedure(current_app.config['db_config'], f'{proc}', (request.form['year'], request.form['month'], 0), (2,))

        if res is None or res == -1:
            html = 'db_error.html'
        else:
            ret.append(res[0])

    return render_template(html, result=ret, month=request.form.get('month'), year=request.form.get('year'), proc=proc)


@blueprint_report.route('/view-report/<proc>', methods=['GET', 'POST'])
@login_required
@group_required
def view_report(proc):
    sql = provider.get(f'proc_desc_{proc}.sql', proc=proc)
    res = select_dict(current_app.config['db_config'], sql)

    if res is None or res == -1:
        return render_template('db_error.html')
    else:
        ret = [res[0]['href_name'].split('; ')[0], ]

    if request.method == 'GET':
        sql = provider.get(f'proc_desc_{proc}.sql', proc=proc)
        ret.append(select_distinct(current_app.config['db_config'], sql))
        if ret[1] is None:
            html = 'db_error.html'
        else:
            html = f"input_date.html"
    else:
        html = 'report_result.html'
        sql = provider.get(f'select_{proc}.sql', month=request.form['month'], year=request.form['year'])
        ret.append(select_tab(current_app.config['db_config'], sql))

        if ret[1] is None or ret[1] == -1:
            html = 'not_exists.html'

    return render_template(html, result=ret, month=request.form.get('month'), year=request.form.get('year'), group_name=session['User_group'], proc=proc)
