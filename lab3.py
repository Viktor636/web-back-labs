from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('/lab3/lab3.html', name=name, name_color=name_color)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле'
    
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле'

    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    # Пусть кофе стоит 120 рублей, чёрный чай - 80 рублей, зелёный - 70 рублей.
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    # Добавка молока удорожает напиток на 30 рублей, а сахара - на 10.
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    # Просто получаем готовые данные
    drink = request.args.get('drink')
    milk = request.args.get('milk') == 'on'
    sugar = request.args.get('sugar') == 'on'
    price = request.args.get('price')  # Уже рассчитана в pay
    card = request.args.get('card')
    name = request.args.get('name')
    
    return render_template('lab3/success.html', 
                         drink=drink,
                         milk=milk,
                         sugar=sugar,
                         price=price,
                         card=card,
                         name=name)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    font_style = request.args.get('font_style')
    font_weight = request.args.get('font_weight')
    
    if color or bg_color or font_size or font_style or font_weight:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if bg_color:
            resp.set_cookie('bg_color', bg_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if font_style:
            resp.set_cookie('font_style', font_style)
        if font_weight:
            resp.set_cookie('font_weight', font_weight)
        return resp
    
    color = request.cookies.get('color')
    bg_color = request.cookies.get('bg_color')
    font_size = request.cookies.get('font_size')
    font_style = request.cookies.get('font_style')
    font_weight = request.cookies.get('font_weight')
    
    resp = make_response(render_template('lab3/settings.html', 
                                       color=color, 
                                       bg_color=bg_color,
                                       font_size=font_size,
                                       font_style=font_style,
                                       font_weight=font_weight))
    return resp


@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    
    # Получаем данные из формы
    fio = request.args.get('fio')
    age = request.args.get('age')
    departure = request.args.get('departure')
    destination = request.args.get('destination')
    date = request.args.get('date')
    shelf = request.args.get('shelf')
    linen = request.args.get('linen')
    baggage = request.args.get('baggage')
    insurance = request.args.get('insurance')
    
    # Проверка на пустые поля
    if not fio:
        errors['fio'] = 'Заполните ФИО пассажира'
    if not age:
        errors['age'] = 'Заполните возраст'
    elif not age.isdigit() or not (1 <= int(age) <= 120):
        errors['age'] = 'Возраст должен быть от 1 до 120 лет'
    if not departure:
        errors['departure'] = 'Заполните пункт выезда'
    if not destination:
        errors['destination'] = 'Заполните пункт назначения'
    if not date:
        errors['date'] = 'Выберите дату поездки'
    if not shelf:
        errors['shelf'] = 'Выберите тип полки'
    
    # Если есть ошибки или форма не заполнена, показываем форму
    if errors or not fio:
        return render_template('lab3/ticket.html', 
                             fio=fio, age=age, departure=departure, 
                             destination=destination, date=date, shelf=shelf,
                             linen=linen, baggage=baggage, insurance=insurance,
                             errors=errors)
    
    # Рассчитываем стоимость
    if int(age) < 18:
        price = 700  # Детский билет
    else:
        price = 1000  # Взрослый билет
    
    # Доплаты
    if shelf in ['нижняя', 'нижняя боковая']:
        price += 100
    if linen == 'on':
        price += 75
    if baggage == 'on':
        price += 250
    if insurance == 'on':
        price += 150
    
    # Генерируем номер билета
    ticket_number = "1"
    
    return render_template('lab3/ticket.html', 
                         fio=fio, age=age, departure=departure, 
                         destination=destination, date=date, shelf=shelf,
                         linen=linen, baggage=baggage, insurance=insurance,
                         price=price, ticket_number=ticket_number)