# Задание №2
# 📌 Создать базу данных для хранения информации о книгах в библиотеке.
# 📌 База данных должна содержать две таблицы: "Книги" и "Авторы".
# 📌 В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# 📌 В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# 📌 Необходимо создать связь между таблицами "Книги" и "Авторы".
# 📌 Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, render_template

from .model import db, Author, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('base.html')


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-auth")
def add_auth():
    author = {
        '1': ("Лев", "Толслой"),
        '2': ("Метью", "Фаулер"),
        '3': ("Антонио", "Мелле")
    }

    for auth in author.values():
        auth = Author(name=auth[0], surname=auth[1])
        db.session.add(auth)
        db.session.commit()

    print('author_add')


@app.cli.command("add-book")
def add_book():
    book = {
        '1': {
            'Война и Мира': ('1869', 5, 1),
            'Анна Каренина': ('1877', 3, 1),
            'Исповедь': ('1884', 2, 1),
        },
        '2': {
            'Asyncio и конкурентное пограммирование': ('2023', 4, 2),
        },
        '3': {
            'Django': ('2020', 2, 3),
        }
    }

    for book in book.values():
        for title, date in book.items():
            book = Book(title=title,
                        year=date[0],
                        count=date[1],
                        id_auth=date[2])
            db.session.add(book)
            db.session.commit()

    print('book_add')


@app.route("/list-book/")
def list_book():
    books = Book.query.all()

    list_bok = []
    for book in books:
        author = Author.query.filter(Author.id == book.id_auth).all()
        list_bok.append(f'{book.title} {author[0]}')
    context = {'books': list_bok, }
    return render_template('list_book.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
