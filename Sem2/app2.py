from flask import Flask, request, render_template
from Work_with_DB import select_dict
import json


app = Flask(__name__)

with open('../db_config.json') as f:
    app.config['db_config'] = json.load(f)


@app.route('/')
@app.route('/<my_name>')
def hello_name(my_name=None):
    if my_name is None:
        return 'Hello, world!'
    else:
        return f"Hello, {my_name}!"


@app.route('/product', methods=['GET', 'POST'])
def get_product():
    if request.method == 'GET':
        return render_template('input_params.html')
    else:
        category = request.form.get('category')
        price = request.form.get('price')
        _sql = f"""select Product_ID, Category, Price from product
                    where Category='{category}' and Price > {price}"""
        products = select_dict(app.config['db_config'], _sql)

        if products:
            return render_template('dynamic.html', products=products, prod_title='Results')
        else:
            return 'Results not found'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
