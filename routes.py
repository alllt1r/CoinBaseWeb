import requests
from flask import request, render_template, redirect, url_for
from app import app
import os  # работа с операционной системой (компьютера\сервера)
from forms import SearchForm


@app.route('/', methods=['GET', 'POST'])  # главная страница - mysite.com/
def main_page():
    form = SearchForm()
    # экземпляр формы. То есть создаю форму для пользователя,
    # когда он заходит на главную страницу моего сайта
    if form.validate_on_submit():  # если форма отправляется
        currency_from = request.form['currency_from'].upper()
        currency_to = request.form['currency_to'].upper()
        type = request.form['type'].lower()
        return redirect(url_for('search_weather', from_currency=currency_from, to_currency=currency_to, type=type))
        # перенаправляю пользователя на страницу с отображением погоды для выбранного гоорода
    return render_template('index.html', form=form)


@app.route('/currency', methods=['GET', 'POST'])
def search_weather():
    from_currency = request.args.get('from_currency')
    to_currency = request.args.get('to_currency')
    type = request.args.get('type')
    #response1 = requests.get("https://api.coinbase.com/v2/currencies").json()

    url = f'https://api.coinbase.com/v2/prices/{from_currency}-{to_currency}/{type}'
    response = requests.get(url).json()
    return response.get('data', {}).get('amount'), response.status_code