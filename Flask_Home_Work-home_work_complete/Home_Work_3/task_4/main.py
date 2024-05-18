# Задание №4
# 📌 Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# 📌 После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.
# 📌 Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.

from flask import Flask, render_template, request, flash, url_for, redirect
from flask_wtf.csrf import CSRFProtect
from .form import RegistrationForm
from .model import User, db

app = Flask(__name__)
app.config['SECRET_KEY'] = b'4a2c04f2949a42d594a6479946a12c957d692bfbbcbce5e2d141713512c21a17'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db.init_app(app)
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        try:
            name = form.username.data
            email = form.email.data
            password = hash(form.password.data)
            user = User(name=name, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            context = {'name': name}
            return render_template('home_page.html',
                                   **context)
        except:
            flash('Такой пользователь уже существует повторите регистрацию',
                  'danger')

            return redirect(url_for('registration'))

    return render_template('registration.html',
                           form=form)


if __name__ == '__main__':
    app.run(debug=True)
