from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!'


@app.route('/static')
def static_index():
    return render_template('static.html')


@app.route('/dynamic')
def dynamic_index():
    products = [
        {'prod_name': 'говядина', 'cost': '300 rub/kg'},
        {'prod_name': 'свинина', 'cost': '330 rub/kg'},
        {'prod_name': 'баранина', 'cost': '400 rub/kg'}
    ]
    prod_title = 'Our meat'

    return render_template('Dynamic_1.html', products=products, prod_title=prod_title)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
