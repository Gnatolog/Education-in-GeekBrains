# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/cold-steel/')
def cold_steel():
    _items = [
        {
            'title': 'катаны',
            'link_page': '/catana/',
            'path': '../static/image/catana.jpg'
        },
        {
            'title': 'мечи',
            'link_page': '/sword/',
            'path': '../static/image/мечи.jpg'
        },
        {
            'title': 'топоры',
            'link_page': '/axe/',
            'path': '../static/image/топоры.jpeg'
        },
    ]
    context = {
        'items': _items,
    }

    return render_template('cold_steel.html',
                           **context)


@app.route('/catana/')
def catana():
    _items = [
        {
            'title': 'катана 1',
            'path': '../static/image/catana.jpg',
        },
        {
            'title': 'катана 2',
            'path': '../static/image/catana.jpg',
        },
        {
            'title': 'катана 3',
            'path': '../static/image/catana.jpg',
        },
    ]
    context = {
        'items': _items,
        'title': 'Катаны'
    }
    return render_template('catana.html',
                           **context)


@app.route('/sword/')
def sword():
    _items = [
        {
            'title': 'меч 1',
            'path': '../static/image/мечи.jpg',
        },
        {
            'title': 'меч 2',
            'path': '../static/image/мечи.jpg',
        },
        {
            'title': 'меч 3',
            'path': '../static/image/мечи.jpg',
        },
    ]
    context = {
        'items': _items,
        'title': 'Мечи'
    }
    return render_template('sword.html',
                           **context)


@app.route('/axe/')
def axe():
    _items = [
        {
            'title': 'топор 1',
            'path': '../static/image/топоры.jpeg',
        },
        {
            'title': 'топор 2',
            'path': '../static/image/топоры.jpeg',
        },
        {
            'title': 'топор 3',
            'path': '../static/image/топоры.jpeg',
        },
    ]
    context = {
        'items': _items,
        'title': 'Топоры'
    }
    return render_template('sword.html',
                           **context)


if __name__ == '__main__':
    app.run(debug=True)
