from flask import Flask
import os
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'sqlite')


app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)


@app.route("/")
@app.route("/index")
def index():
    return """<!doctype html>
        <html>
            <head>
                <title>НГТУ, ФБ, Лабораторные работы</title>
            </head>
            <body>
                <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
                <ul>
                    <li><a href="/lab1">Лабораторная работа 1</a></li>
                </ul>
                <ul>
                    <li><a href="/lab2/">Лабораторная работа 2</a></li>
                </ul>
                <ul>
                    <li><a href="/lab3/">Лабораторная работа 3</a></li>
                </ul>
                <ul>
                    <li><a href="/lab4/">Лабораторная работа 4</a></li>
                </ul>
                <ul>
                    <li><a href="/lab5/">Лабораторная работа 5</a></li>
                </ul>
                <ul>
                    <li><a href="/lab6/">Лабораторная работа 6</a></li>
                </ul>
                <ul>
                    <li><a href="/lab7/">Лабораторная работа 7</a></li>
                </ul>
                <footer>
                    Гайдабура Виктор Васильевич, ФБИ-31, 3 курс, 2025
                </footer>
            </body>
        </html>"""


# Задание 6: Коды ответов HTTP
@app.route("/400")
def A():
    return "400 - Неверный запрос", 400


@app.route("/401")
def B():
    return "401 - Неавторизован", 401


@app.route("/402")
def C():
    return "402 - Требуется оплата", 402


@app.route("/403")
def D():
    return "403 - Запрещено", 403


@app.route("/405")
def E():
    return "405 - Метод не разрешен", 405


@app.route("/418")
def F():
    return "418 - Я чайник", 418


# Задание 7: Кастомная страница 404
@app.errorhandler(404)
def not_found(error):
    return '''<!doctype html>
        <html>
            <head>
                <title>404 - Страница не найдена</title>
                <style>
                    body { 
                        font-family: Arial, sans-serif; 
                        text-align: center; 
                        background-color: #f0f0f0;
                        color: #333;
                    }
                    h1 { color: #d32f2f; }
                    img { max-width: 300px; }
                </style>
            </head>
            <body>
                <h1>404 - Страница не найдена</h1>
                <p>К сожалению, запрашиваемая страница не существует.</p>
                <img src="/static/404.png" alt="Страница не найдена">
                <br>
                <a href="/">Вернуться на главную</a>
            </body>
        </html>''', 404


# Задание 8: Ошибка 500
@app.route("/500")
def server_error():
    # Вызовем ошибку делением на ноль
    result = 1 / 0


# Задание 8: Кастомная страница 500
@app.errorhandler(500)
def internal_server_error(error):
    return '''<!doctype html>
        <html>
            <head>
                <title>500 - Ошибка сервера</title>
                <style>
                    body { 
                        font-family: Arial, sans-serif; 
                        text-align: center; 
                        background-color: #fff0f0;
                        color: #733;
                    }
                    h1 { color: #b71c1c; }
                </style>
            </head>
            <body>
                <h1>500 - Внутренняя ошибка сервера</h1>
                <p>Произошла непредвиденная ошибка на сервере.</p>
                <p>Пожалуйста, попробуйте позже или обратитесь к администратору.</p>
                <a href="/">Вернуться на главную</a>
            </body>
        </html>''', 500

