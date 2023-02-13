from server import mysql
from server.db import wine_repository


def create_wine(wine):
    print("create wine: wine =", wine)
    all_wines = wine_repository.get_wine(mysql)
    sort = wine['sort']

    for ex_wine in all_wines:
        if ex_wine['sort'] == sort:
            return {'error': 'wine with this sort already exists'}

    wine_repository.post_wine(mysql, wine)
    return None


def show_wine():
    wine = wine_repository.get_wine(mysql)
    print('all wines', wine)
    return wine
