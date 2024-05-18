#  Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
#  При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello my Friend"


@app.route('/square-number', methods=['GET', 'POST'])
def square_number():
    if request.method == 'POST':
        number = request.form.get('number')
        return f'Square number: {number} = {int(number)**2}'
    return render_template('square_number.html')


if __name__ == '__main__':
    app.run(debug=True)
