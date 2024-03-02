from flask import session, render_template, current_app, request, redirect, url_for
from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'User_ID' in session:
            return func(*args, **kwargs)
        return redirect(url_for('bp_auth.start_auth'))
    return wrapper


def group_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        endpoint_app = request.endpoint.split('.')[-1]
        config = current_app.config['access']
        if 'User_group' in session:
            user_group = session['User_group']
            if user_group in config and endpoint_app in config[user_group]:
                return func(*args, **kwargs)
            else:
                return render_template('forbidden.html')
        return func(*args, **kwargs)

    return wrapper
