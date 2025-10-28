from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('/lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены')
    x1 = int(x1)
    x2 = int(x2)

    if x2 == 0:
        return render_template('lab4/div.html', error='На ноль делить нельзя!')
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')


@lab4.route('/lab4/sum', methods = ['POST'])
def sum():
    x1 = request.form.get('x1', '0')  # По умолчанию 0 если пустое
    x2 = request.form.get('x2', '0')  # По умолчанию 0 если пустое
    
    x1 = int(x1) if x1 != '' else 0
    x2 = int(x2) if x2 != '' else 0
    
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/mult-form')
def mult_form():
    return render_template('lab4/mult-form.html')


@lab4.route('/lab4/mult', methods = ['POST'])
def mult():
    x1 = request.form.get('x1', '1')  # По умолчанию 1 если пустое
    x2 = request.form.get('x2', '1')  # По умолчанию 1 если пустое
    
    x1 = int(x1) if x1 != '' else 1
    x2 = int(x2) if x2 != '' else 1
    
    result = x1 * x2
    return render_template('lab4/mult.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')


@lab4.route('/lab4/sub', methods = ['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены')
    
    x1 = int(x1)
    x2 = int(x2)
    
    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/pow-form')
def pow_form():
    return render_template('lab4/pow-form.html')


@lab4.route('/lab4/pow', methods = ['POST'])
def power():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/pow.html', error='Оба поля должны быть заполнены')
    
    x1 = int(x1)
    x2 = int(x2)
    
    # Проверка на оба нуля
    if x1 == 0 and x2 == 0:
        return render_template('lab4/pow.html', error='Оба числа не могут быть равны нулю!')
    
    result = x1 ** x2
    return render_template('lab4/pow.html', x1=x1, x2=x2, result=result)


tree_count = 0
max_trees = 10  # Максимальное количество деревьев

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count, max_trees=max_trees)
    
    operation = request.form.get('operation')

    if operation == 'cut':
        # Проверка, чтобы счетчик не ушел в отрицательную область
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        # Проверка, чтобы не превысить максимальное количество
        if tree_count < max_trees:
            tree_count += 1

    return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Александр Петров', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Боб Иванов', 'gender': 'male'},
    {'login': 'viktor', 'password': '1919', 'name': 'Виктор Гайдабура', 'gender': 'male'},
    {'login': 'jack', 'password': '132', 'name': 'Жаклин Смит', 'gender': 'female'},
    {'login': 'anna', 'password': '777', 'name': 'Анна Сидорова', 'gender': 'female'},
]

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            user_found = None
            for user in users:
                if user['login'] == session['login']:
                    user_found = user
                    break
            name = user_found['name'] if user_found else session['login']
        else:
            authorized = False
            name = ''
        return render_template('lab4/login.html', authorized=authorized, name=name)
    
    login = request.form.get('login')
    password = request.form.get('password')
    
    # Проверка на пустые значения
    errors = []
    if not login:
        errors.append('Не введён логин')
    if not password:
        errors.append('Не введён пароль')
    
    if errors:
        return render_template('lab4/login.html', errors=errors, login=login, authorized=False)
    
    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, login=login, authorized=False)


@lab4.route('/lab4/logout', methods = ['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/fridge', methods = ['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template('lab4/fridge.html')
    
    temperature = request.form.get('temperature')
    
    if not temperature:
        return render_template('lab4/fridge.html', error='Ошибка: не задана температура')
    
    try:
        temp = int(temperature)
    except ValueError:
        return render_template('lab4/fridge.html', error='Ошибка: температура должна быть числом')
    
    if temp < -12:
        return render_template('lab4/fridge.html', error='Не удалось установить температуру — слишком низкое значение')
    elif temp > -1:
        return render_template('lab4/fridge.html', error='Не удалось установить температуру — слишком высокое значение')
    
    snowflakes = ''
    if -12 <= temp <= -9:
        snowflakes = '❄️❄️❄️'
    elif -8 <= temp <= -5:
        snowflakes = '❄️❄️'
    elif -4 <= temp <= -1:
        snowflakes = '❄️'
    
    return render_template('lab4/fridge.html', temperature=temp, snowflakes=snowflakes)


@lab4.route('/lab4/grain-order', methods = ['GET', 'POST'])
def grain_order():
    if request.method == 'GET':
        return render_template('lab4/grain-order.html')
    
    grain_type = request.form.get('grain_type')
    weight = request.form.get('weight')
    
    # Цены за тонну
    prices = {
        'barley': 12000,
        'oats': 8500,
        'wheat': 9000,
        'rye': 15000
    }
    
    # Названия зерна
    grain_names = {
        'barley': 'ячмень',
        'oats': 'овёс',
        'wheat': 'пшеница',
        'rye': 'рожь'
    }
    
    # Проверки
    if not weight:
        return render_template('lab4/grain-order.html', error='Ошибка: не указан вес')
    
    try:
        weight = float(weight)
    except ValueError:
        return render_template('lab4/grain-order.html', error='Ошибка: вес должен быть числом')
    
    if weight <= 0:
        return render_template('lab4/grain-order.html', error='Ошибка: вес должен быть положительным числом')
    
    if weight > 100:
        return render_template('lab4/grain-order.html', error='Извините, такого объёма сейчас нет в наличии')
    
    # Расчет стоимости
    price_per_ton = prices[grain_type]
    total = weight * price_per_ton
    
    # Скидка за большой объем
    discount = 0
    if weight > 10:
        discount = total * 0.1
        total -= discount
    
    grain_name = grain_names[grain_type]
    
    return render_template('lab4/grain-order.html', 
                         success=True,
                         grain_name=grain_name,
                         weight=weight,
                         total=total,
                         discount=discount,
                         has_discount=weight > 10)