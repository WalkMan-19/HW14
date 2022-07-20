import json

from flask import Flask, request
from utils import get_value_by_title, get_value_by_range, get_value_by_rating, get_value_by_genre

app = Flask(__name__)


@app.route('/movie/<title>')
def movie_title(title):
    result = get_value_by_title(title)
    return json.dumps(result)


@app.route('/movie/<int:from_value>/to/<int:to_value>')
def filer_page(from_value, to_value):
    result = get_value_by_range(from_value, to_value)
    return json.dumps(result)


@app.route('/rating/children')
def children_page():
    result = get_value_by_rating(rating=('G', 'G'))
    return json.dumps(result)


@app.route('/rating/family')
def family_page():
    result = get_value_by_rating(rating=('G', 'PG', 'PG-13'))
    return json.dumps(result)


@app.route('/rating/adult')
def adult_page():
    result = get_value_by_rating(rating=('R', 'NC-17'))
    return json.dumps(result)


@app.route('/genre/<genre>')
def genre_page(genre):
    result = get_value_by_genre(genre)
    return json.dumps(result)


if __name__ == '__main__':
    app.run()
