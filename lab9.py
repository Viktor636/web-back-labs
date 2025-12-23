from flask import Blueprint, render_template, jsonify, request, session
import random

lab9 = Blueprint('lab9', __name__)

# Подарки
GIFTS = [
    {"id": 1, "message": "С Новым Годом! Желаю счастья, здоровья и успехов!", "image": "gift1.png"},
    {"id": 2, "message": "Пусть все мечты сбудутся в новом году!", "image": "gift2.png"},
    {"id": 3, "message": "Желаю радости, улыбок и тепла в доме!", "image": "gift3.png"},
    {"id": 4, "message": "Пусть новый год принесет много хороших новостей!", "image": "gift4.png"},
    {"id": 5, "message": "Желаю процветания и финансового благополучия!", "image": "gift5.png"},
    {"id": 6, "message": "Пусть каждый день будет наполнен счастьем!", "image": "gift6.png"},
    {"id": 7, "message": "Желаю крепкого здоровья вам и вашим близким!", "image": "gift7.png"},
    {"id": 8, "message": "Пусть удача всегда будет на вашей стороне!", "image": "gift8.png"},
    {"id": 9, "message": "Желаю любви, гармонии и семейного уюта!", "image": "gift9.png"},
    {"id": 10, "message": "С новым годом! Пусть все плохое останется в прошлом!", "image": "gift10.png"}
]

@lab9.route('/lab9/')
def main():
    # Инициализируем сессию
    if 'opened_boxes' not in session:
        session['opened_boxes'] = []
    if 'opened_count' not in session:
        session['opened_count'] = 0
    
    # Считаем оставшиеся
    remaining = 3 - session['opened_count']
    if remaining < 0:
        remaining = 0
    
    return render_template('lab9/index.html',
                         opened_count=session['opened_count'],
                         remaining=remaining)

@lab9.route('/lab9/open', methods=['POST'])
def open_gift():
    # Проверяем лимит
    if session.get('opened_count', 0) >= 3:
        return jsonify({
            "success": False,
            "message": "Вы уже открыли 3 коробки! Больше нельзя."
        })
    
    # Выбираем случайный подарок
    available_gifts = [g for g in GIFTS if g['id'] not in session.get('opened_gifts', [])]
    
    if not available_gifts:
        # Все подарки открыты, берем любой
        gift = random.choice(GIFTS)
    else:
        gift = random.choice(available_gifts)
    
    # Обновляем сессию
    if 'opened_gifts' not in session:
        session['opened_gifts'] = []
    
    session['opened_gifts'].append(gift['id'])
    session['opened_count'] = session.get('opened_count', 0) + 1
    
    # Считаем оставшиеся
    remaining = 3 - session['opened_count']
    if remaining < 0:
        remaining = 0
    
    return jsonify({
        "success": True,
        "gift": gift,
        "opened_count": session['opened_count'],
        "remaining": remaining
    })

@lab9.route('/lab9/reset')
def reset():
    # Просто очищаем сессию
    session['opened_boxes'] = []
    session['opened_gifts'] = []
    session['opened_count'] = 0
    return jsonify({"success": True})