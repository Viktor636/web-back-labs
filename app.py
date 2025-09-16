from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404

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
    name = "Гайжабура Виктор Васильевич"
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
    return '''<!doctype html> 
        <html> 
            <head>
                <link rel="stylesheet" href="''' + css_path + '''">
            </head>
            <body> 
                <h1>Дуб</h1>
                <img src="''' + path + '''">
            </body> 
        </html>'''

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