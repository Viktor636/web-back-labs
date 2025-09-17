from flask import Flask, url_for, request, redirect, abort
import datetime
app = Flask(__name__)

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
                    <li><a href="/lab1">Первая лабораторная</a></li>
                </ul>
                <footer>
                    Гайдабура Виктор Васильевич, ФБИ-31, 3 курс, 2025
                </footer>
            </body>
        </html>"""

@app.route("/lab1")
def lab1():
    return """<!doctype html>
        <html>
            <head>
                <title>Лабораторная 1</title>
            </head>
            <body>
                <p>Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</p>
                <a href="/">Корень сайта</a>
                
                <h2>Список роутов</h2> 
                <!-- Задание 10 БЫЛО СДЕЛАНО В САМОМ НАЧАЛЕ-->
                <ul>
                    <li><a href="/lab1/web">Web</a></li>
                    <li><a href="/lab1/author">Author</a></li>
                    <li><a href="/lab1/image">Image</a></li>
                    <li><a href="/lab1/counter">Counter</a></li>
                    <li><a href="/lab1/info">Info</a></li>
                </ul>
            </body>
        </html>"""

@app.route("/lab1/web")
def web():
    return """<!doctype html> 
        <html> 
            <body> 
                <h1>web-сервер на flask</h1>
                <a href="/lab1/author">author</a> 
                <br><a href="/lab1/image">image</a>
                <br><a href="/lab1/counter">counter</a>
            </body> 
        </html>"""#, 200, {
            #'X-Server': 'sample',
            #'Content-Type': 'text/plain; charset=utf-8'
           #}

@app.route("/lab1/author")
def author():
    name = "Гайдабура Виктор Васильевич"
    group = "ФБИ-31"
    faculty = "ФБ"

    return """<!doctype html> 
        <html> 
            <body> 
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body> 
        </html>"""

@app.route("/lab1/image")
def image():
    path = url_for("static", filename="DYB.jpg")
    css_path = url_for("static", filename="lab1.css")
    
    # Создаем response объект
    return '''<!doctype html> 
        <html> 
            <head>
                <link rel="stylesheet" href="''' + css_path + '''">
            </head>
            <body> 
                <h1>Дуб</h1>
                <img src="''' + path + '''">
            </body> 
        </html>''', {
    
    
            'Content-Language': 'ru', 
            'X-My-Custom-Header': 'HelloFromFlask',
            'X-Student-Name': 'Victor'}
    
count = 0

@app.route("/lab1/counter")
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr

    return '''<!doctype html> 
        <html> 
            <body> 
                Сколько раз вы суда заходили: ''' + str(count) + '''
                <hr>
                Дата и время: ''' + str(time) + '''<br>
                Запрошенный адрес: ''' + url + '''<br>
                Ваш IP-адрес: ''' + client_ip + '''<br>
            </body> 
        </html>'''

# Задание 2: Очистка счётчика
@app.route("/lab1/clear_counter")
def clear_counter():
    global count
    count = 0
    return '''<!doctype html> 
        <html> 
            <body> 
                Счётчик очищен!
                <br><a href="/lab1/counter">Перейти к счётчику</a>
                <br><a href="/lab1/web">web</a>
            </body> 
        </html>'''

@app.route("/lab1/info")
def info():
    return redirect('/lab1/author')

@app.route("/lab1/created")
def created():
    return '''<!doctype html> 
        <html> 
            <body> 
                <h1>Создано успешно</h1>
                <div><i>что-то создано...</i></div>
            </body> 
        </html>''', 201

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

@app.route('/lab2/a')
def a():
    return 'без слеша'

@app.route('/lab2/a/')
def a2():
    return 'со слешем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    else:
        return "цветок: " + flower_id[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''