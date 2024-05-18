# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route('/news/')
def news():
    _news = [
        {
            'title': 'Роботы начали думать как люди',
            'description': 'Это не возможно)',
            'data_published': '10.05.2150',
        },
        {
            'title': 'Люди преземлились на Марс',
            'description': 'Там воды не оказалось',
            'data_published': '15.12.2149',
        },
        {
            'title': 'Нейросети стали умнее',
            'description': 'Но людей они не заменят',
            'data_published': '9.10.2149',
        },

    ]

    context = {
        'news': _news,
        'title': 'Новости ИТ'
    }
    return render_template('news.html',
                           **context)


if __name__ == '__main__':
    app.run(debug=True)
