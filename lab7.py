from flask import Blueprint, render_template, abort, request
lab7 = Blueprint('lab7', __name__)


@lab7.route('/lab7/')
def main():
    return render_template('/lab7/index.html')


films = [
    {
        "title": "Interstellar",
        "title_ru": "Интерстеллар",
        "year": 2014,
        "description": "Когда засуха, пыльные бури и вымирание растений \
            приводят человечество к продовольственному кризису, коллектив \
            исследователей и учёных отправляется сквозь червоточину \
            (которая предположительно соединяет области пространства-времени \
            через большое расстояние) в путешествие, чтобы превзойти прежние \
            ограничения для космических путешествий человека и найти планету \
            с подходящими для человечества условиями."
    },
    {
        "title": "Intouchables",
        "title_ru": "1+1",
        "year": 2011,
        "description": "Аристократ на коляске нанимает в сиделки бывшего \
            заключенного. Искрометная французская комедия с Омаром Си"
    },
    {
        "title": "The Gentlemen",
        "title_ru": "Джентльмены",
        "year": 2019,
        "description": "Гангстеры всех мастей делят наркоферму. Закрученная \
            экшен-комедия Гая Ричи с Мэттью Макконахи и Хью Грантом."
    },
]


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_films1(id):
    if id < 0 or id >= len(films):
        abort(404)
    return films[id]


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_films(id):
    if id < 0 or id >= len(films):
        abort(404)
    del films[id]
    return '', 204


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_films(id):
    if id < 0 or id >= len(films):
        abort(404)
    film = request.get_json()
    films[id] = film
    return films[id]