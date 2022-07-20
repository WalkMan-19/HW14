import sqlite3


def get_value_from_db(query):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(
            query
        ).fetchall()
    return result


def get_value_by_title(title):
    query = f"""
    SELECT title, country, release_year, description, listed_in
    FROM netflix 
    WHERE title = '{title.capitalize()}'
    ORDER BY release_year DESC
    LIMIT 1
    """
    values = get_value_from_db(query)
    for item in values:
        return dict(item)


def get_value_by_range(from_value, to_value):
    query = f"""
    SELECT title, release_year
    FROM netflix
    WHERE release_year BETWEEN {from_value} AND {to_value}
    LIMIT 100
    """
    values = get_value_from_db(query)
    result = []
    for item in values:
        result.append(dict(item))
    return result


def get_value_by_rating(rating):
    query = f"""
    SELECT title, rating, description
    FROM netflix
    WHERE rating IN {rating}
    """
    values = get_value_from_db(query)
    result = []
    for item in values:
        result.append(dict(item))
    return result


def get_value_by_genre(genre):
    query = f"""
    SELECT title, description
    FROM netflix
    WHERE "listed_in" LIKE '%{genre.capitalize()}%'
    ORDER BY release_year DESC
    LIMIT 10
    """
    values = get_value_from_db(query)
    result = []
    for item in values:
        result.append(dict(item))
    return result


def get_value_by_actor(actor_1, actor_2):
    query = f"""
    SELECT "cast"
    FROM netflix
    WHERE "cast" LIKE '%{actor_1}%' AND "cast" LIKE '%{actor_2}%'
    """
    values = get_value_from_db(query)
    result = []
    names_dict = {}
    for item in values:
        names = set(dict(item).get("cast").split(", ")) - {actor_1, actor_2}

        for name in names:
            names_dict[str(name).strip()] = names_dict.get(str(name).strip(), 0) + 1

    for k, v in names_dict.items():
        if v >= 2:
            result.append(k)
    return result


def get_type(movie_type, release_year, genre):
    query = f"""
    SELECT title, description
    FROM netflix
    WHERE "type" = '{movie_type.capitalize()}'
    AND "release_year" = '{release_year}'
    AND "listed_in" LIKE '%{genre.capitalize()}%'
    """
    result = []
    values = get_value_from_db(query)
    for item in values:
        result.append(dict(item))
    return result

# print(get_type('Movie', 2007, 'Thrillers'))
