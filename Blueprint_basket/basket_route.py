from flask import Blueprint, session, current_app, request, render_template, redirect, url_for
from sql_provider import SQLProvider
from Work_with_DB import select_dict
import os
import datetime
from access import *


blueprint_basket = Blueprint('bp_basket', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_basket.route('/', methods=['GET', 'POST'])
@login_required
@group_required
def basket_index():
    db_config = current_app.config['db_config']

    if 'basket' not in session:
        session['basket'] = {}

    if request.method == 'GET':
        _sql = provider.get('all_items.sql')
        items = select_dict(db_config, _sql)
        basket_items = session.get('basket', {})

        return render_template('basket_order_list.html', items=items, basket=basket_items)
    else:
        vac_id = request.form.get('vac_id')
        vac_id_del = request.form.get('vac_id_del')
        _sql = provider.get('added_item.sql', vac_id=vac_id)
        item = select_dict(db_config, _sql)

        add_and_delete(item, vac_id, vac_id_del)

    return redirect(url_for('bp_basket.basket_index'))


def add_and_delete(item, vac_id, vac_id_del):
    if item != -1 and item is not None:
        session['basket'][vac_id] = {}
        session['basket'][vac_id]['Candidate_ID'] = item[0]['c_ID']
        session['basket'][vac_id]['Candidate_FIO'] = item[0]['c_FIO']
        session['basket'][vac_id]['Vacancy_ID'] = item[0]['v_ID']
        session['basket'][vac_id]['Job_title'] = item[0]['jt']

    if vac_id_del is not None:
        del (session['basket'])[vac_id_del]

    session.permanent = True


@blueprint_basket.route('/save_order', methods=['GET', 'POST'])
@login_required
@group_required
def save_order():
    current_basket = session.get('basket', {})
    sql = provider.get('select_inter_id.sql')
    inter_date = (datetime.date.today() + datetime.timedelta(31)).strftime("%Y-%m-01")

    if current_basket:
        session['basket'] = {}
        for key in current_basket.keys():
            max_id = select_dict(current_app.config['db_config'], sql)[0]['max_id']
            sql_1 = provider.get('insert_interview.sql', inter_id=max_id+1, date=inter_date)
            select_dict(current_app.config['db_config'], sql_1)

            emp_id = 1 if current_basket[key]['Job_title'] == 'Программист' else 2
            sql_2 = provider.get('insert_interview_info.sql',
                         inter_id=max_id+1,
                         emp_id=emp_id,
                         cand_id=current_basket[key]['Candidate_ID'],
                         vac_id=key)
            select_dict(current_app.config['db_config'], sql_2)

        return render_template('order_created.html')
    else:
        return render_template('empty_order.html')
