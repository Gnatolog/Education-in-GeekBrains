#  Создать страницу, на которой будет форма для ввода имени
# и электронной почты
#  При отправке которой будет создан cookie файл с данными
# пользователя
#  Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
#  На странице приветствия должна быть кнопка "Выйти"
#  При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, request, render_template, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route('/form-cookie', methods=['GET', 'POST'])
def form_cookie():
    if request.method == 'POST' and request.values:
        context = {
            'name': request.values.get('name'),
            'email': request.values.get('email')
        }
        response = make_response(render_template('login-user.html',
                                                 **context))
        response.headers['new_head'] = 'User'
        response.set_cookie('username', context['name'])
        response.set_cookie('email', context['email'])
        return response

    # очищаем печеньки
    response = make_response(render_template('form-cookie.html'))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
