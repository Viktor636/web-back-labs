from flask import Blueprint, redirect, abort, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
    return 'без слеша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слешем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']


# Роут для вывода всех цветов
@lab2.route('/lab2/all_flowers')
def all_flowers():
    flowers_html = ""
    for i, flower in enumerate(flower_list):
        flowers_html += f"<li>{i}. {flower}</li>"
    
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Все цветы</h1>
            <p>Количество: {len(flower_list)}</p>
            <ul>
                {flowers_html}
            </ul>
            <a href="/lab2/clear_flowers">Очистить список</a>
        </body>
    </html>
    '''


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list) or flower_id < 0:
        abort(404)
    else:
        return f'''
        <!doctype html>
        <html>
            <body>
                <h1>Цветок №{flower_id}</h1>
                <p>Название: {flower_list[flower_id]} </p>
                <a href="/lab2/all_flowers">Все цветы</a>
            </body>
        </html>
        '''


@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен: {name}</h1>
    <p>Всего цветов: {len(flower_list)}</p>
    <a href="/lab2/all_flowers">Все цветы</a>
    </body>
</html>
'''


# Роут для очистки списка
@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return '''
    <!doctype html>
    <html>
        <body>
            <h1>Список очищен</h1>
            <a href="/lab2/all_flowers">Все цветы</a>
        </body>
    </html>
    '''


@lab2.route('/lab2/add_flower/')
def add_flower_empty():
    return "вы не задали имя цветка", 400


@lab2.route('/lab2/example')
def example():
    name = 'Виктор Гайдабура'
    group = "ФБИ-31"
    lab = "Лабораторная работа 2 "
    curs = "3 Курс"
    fruits = [
        {'name': 'Яблоки', 'price': 100},
        {'name': 'Груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 96},
        {'name': 'манго', 'price': 312}
    ]
    return render_template('lab2/example.html', name=name, group=group, lab=lab, curs=curs, fruits=fruits)


@lab2.route('/lab2/')
def lab_2():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "0 <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase = phrase)


@lab2.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>')
def calc_single(a):
    return redirect(f'/lab2/calc/{a}/1')


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Калькулятор</h1>
            <p>Числа: {a} и {b}</p>
            <ul>
                <li>{a} + {b} = {a + b}</li>
                <li>{a} - {b} = {a - b}</li>
                <li>{a} * {b} = {a * b}</li>
                <li>{a} / {b} = {a / b if b != 0 else 'деление на ноль!'}</li>
                <li>{a}<sup>{b}</sup> = {a ** b}</li>
            </ul>
        </body>
    </html>
    '''

# Список книг на сервере
books = [
    {'author': 'Фёдор Достоевский', 'title': 'Преступление и наказание', 'genre': 'Роман', 'pages': 671},
    {'author': 'Лев Толстой', 'title': 'Война и мир', 'genre': 'Роман-эпопея', 'pages': 1225},
    {'author': 'Михаил Булгаков', 'title': 'Мастер и Маргарита', 'genre': 'Фантастика', 'pages': 480},
    {'author': 'Антон Чехов', 'title': 'Рассказы', 'genre': 'Рассказы', 'pages': 320},
    {'author': 'Александр Пушкин', 'title': 'Евгений Онегин', 'genre': 'Роман в стихах', 'pages': 240},
    {'author': 'Николай Гоголь', 'title': 'Мёртвые души', 'genre': 'Поэма', 'pages': 352},
    {'author': 'Иван Тургенев', 'title': 'Отцы и дети', 'genre': 'Роман', 'pages': 288},
    {'author': 'Александр Островский', 'title': 'Гроза', 'genre': 'Драма', 'pages': 128},
    {'author': 'Михаил Лермонтов', 'title': 'Герой нашего времени', 'genre': 'Роман', 'pages': 224},
    {'author': 'Иван Гончаров', 'title': 'Обломов', 'genre': 'Роман', 'pages': 640}
]


@lab2.route('/lab2/books')
def show_books():
    return render_template('lab2/books.html', books=books)

# Список фруктов с картинками
fruits = [
    {'name': 'Яблоко', 'image': 'lab2/Summer/apple.jpeg', 'description': 'Сладкий и сочный фрукт'},
    {'name': 'Банан', 'image': 'lab2/Summer/banana.jpeg', 'description': 'Желтый и богатый калием'},
    {'name': 'Апельсин', 'image': 'lab2/Summer/citrus.jpg', 'description': 'Цитрусовый с витамином C'},
    {'name': 'Клубника', 'image': 'lab2/Summer/Klubnika.jpg', 'description': 'Красная ягода с семечками'},
    {'name': 'Виноград', 'image': 'lab2/Summer/Vinograd.jpg', 'description': 'Маленькие сладкие ягоды'},
    {'name': 'Арбуз', 'image': 'lab2/Summer/Arbuz.jpg', 'description': 'Большой и водянистый'},
    {'name': 'Груша', 'image': 'lab2/Summer/Gruza.jpg', 'description': 'Сочная с мягкой текстурой'},
    {'name': 'Персик', 'image': 'lab2/Summer/Persik.jpg', 'description': 'Пушистый и ароматный'},
    {'name': 'Ананас', 'image': 'lab2/Summer/Ananas.jpg', 'description': 'Тропический с колючей кожурой'},
    {'name': 'Манго', 'image': 'lab2/Summer/mango.png', 'description': 'Сладкий тропический фрукт'},
    {'name': 'Киви', 'image': 'lab2/Summer/Qiwu.png', 'description': 'Зеленый с мелкими семенами'},
    {'name': 'Лимон', 'image': 'lab2/Summer/lemon.png', 'description': 'Кислый цитрусовый фрукт'},
    {'name': 'Вишня', 'image': 'lab2/Summer/Vishnya.jpg', 'description': 'Маленькая красная косточковая'},
    {'name': 'Слива', 'image': 'lab2/Summer/Sliva.jpg', 'description': 'Сочная с косточкой внутри'},
    {'name': 'Малина', 'image': 'lab2/Summer/Malina.jpg', 'description': 'Нежная ароматная ягода'},
    {'name': 'Голубика', 'image': 'lab2/Summer/Golobika.jpg', 'description': 'Маленькая синяя ягода'},
    {'name': 'Гранат', 'image': 'lab2/Summer/Granat.jpg', 'description': 'С множеством сочных зерен'},
    {'name': 'Папайя', 'image': 'lab2/Summer/papaya.jpg', 'description': 'Тропический оранжевый фрукт'},
    {'name': 'Кокос', 'image': 'lab2/Summer/cocos.jpg', 'description': 'С твердой скорлупой и водой'},
    {'name': 'Авокадо', 'image': 'lab2/Summer/avokado.jpeg', 'description': 'С маслянистой текстурой'}
]


@lab2.route('/lab2/fruits')
def show_fruits():
    return render_template('lab2/fruits.html', fruits=fruits)